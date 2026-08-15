#!/usr/bin/env python3
"""Classify strict original-response reversals on the two critical pair lines.

The theorem is complete on x+y=2 and x+y=4. It does not classify pair lines
with other pair-through-response vectors and does not prove physical realization.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]
Line = tuple[int, int, int]
Perm = tuple[int, ...]

HOST_ID = "s4-75b04c45c1c8eac2"
RESPONSES: dict[str, Perm] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}
NAMES = tuple(RESPONSES)
CRITICAL_LINES: tuple[Line, ...] = ((1, 1, -2), (1, 1, -4))
PAIR_VECTOR = (0, 0, 1, 1, 1)
STRICT_SCORE_VECTOR = (1, 4, 2, 2, 2)


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def normalize_line(first: Point, second: Point) -> Line:
    require(first != second, "line requires distinct points")
    x1, y1 = first
    x2, y2 = second
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "zero line")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if on_line(third, normalize_line(first, second))
    )


def response_union() -> tuple[Point, ...]:
    return tuple(sorted({point for permutation in RESPONSES.values() for point in response_points(permutation)}))


def response_secants() -> tuple[Line, ...]:
    return tuple(sorted({
        normalize_line(first, second)
        for permutation in RESPONSES.values()
        for first, second in combinations(response_points(permutation), 2)
    }))


def line_intersection(first: Line, second: Line) -> tuple[Fraction, Fraction] | None:
    a, b, c = first
    d, e, f = second
    determinant = a * e - b * d
    if determinant == 0:
        return None
    return (
        Fraction(b * f - c * e, determinant),
        Fraction(c * d - a * f, determinant),
    )


def singleton_increment(point: Point, secants: tuple[Line, ...]) -> tuple[int, ...]:
    result = []
    for name in NAMES:
        points = response_points(RESPONSES[name])
        value = 0
        for line in secants:
            occupancy = sum(on_line(response_point, line) for response_point in points)
            if occupancy >= 2 and on_line(point, line):
                value += math.comb(occupancy, 2)
        result.append(value)
    return tuple(result)


def direct_score_vector(background: tuple[Point, Point]) -> tuple[int, ...]:
    result = []
    for name in NAMES:
        response = response_points(RESPONSES[name])
        require(not set(background) & set(response), "background overlaps response")
        result.append(triple_count((*background, *response)) - triple_count(background))
    return tuple(result)


def exceptional_integer_points(
    critical_line: Line,
    secants: tuple[Line, ...],
    forbidden: tuple[Point, ...],
) -> tuple[Point, ...]:
    points = set()
    for secant in secants:
        intersection = line_intersection(critical_line, secant)
        if intersection is None:
            continue
        x, y = intersection
        if x.denominator == 1 and y.denominator == 1:
            point = (int(x), int(y))
            if point not in forbidden:
                points.add(point)
    return tuple(sorted(points))


def minimizer_face(scores: tuple[int, ...]) -> tuple[str, ...]:
    minimum = min(scores)
    return tuple(name for name, value in zip(NAMES, scores) if value == minimum)


def compile_manifest() -> dict[str, object]:
    union = response_union()
    secants = response_secants()
    require(len(union) == 11, "response-union census")
    require(len(secants) == 20, "secant census")
    require(all(line not in secants for line in CRITICAL_LINES), "critical nonsecants")

    expected_points = {
        (1, 1, -2): ((-3, 5), (-1, 3), (3, -1), (5, -3)),
        (1, 1, -4): ((-2, 6), (0, 4), (4, 0), (6, -2)),
    }
    expected_strict = {
        (1, 1, -2): (
            ((-3, 5), (5, -3)),
            ((-1, 3), (5, -3)),
        ),
        (1, 1, -4): (
            ((-2, 6), (4, 0)),
            ((-2, 6), (6, -2)),
        ),
    }

    rows = []
    all_strict = []
    for line in CRITICAL_LINES:
        points = exceptional_integer_points(line, secants, union)
        require(points == expected_points[line], f"exceptional points {line}")
        point_rows = [
            {
                "point": list(point),
                "singleton_increment_vector": dict(zip(NAMES, singleton_increment(point, secants))),
            }
            for point in points
        ]
        strict_pairs = []
        pair_audit = []
        for first, second in combinations(points, 2):
            scores = direct_score_vector((first, second))
            face = minimizer_face(scores)
            pair_audit.append({
                "background": [list(first), list(second)],
                "complete_score_vector": dict(zip(NAMES, scores)),
                "minimizer_face": list(face),
            })
            if face == ("3012",):
                strict_pairs.append((first, second))
                require(scores == STRICT_SCORE_VECTOR, "strict score vector")
        require(tuple(strict_pairs) == expected_strict[line], f"strict pairs {line}")
        all_strict.extend(strict_pairs)
        rows.append({
            "line": list(line),
            "equation": f"x+y={-line[2]}",
            "pair_through_response_vector": dict(zip(NAMES, PAIR_VECTOR)),
            "exceptional_integer_points": point_rows,
            "exceptional_pair_audit": pair_audit,
            "strict_reversal_pairs": [
                {
                    "background": [list(first), list(second)],
                    "coordinate_radius": max(abs(value) for point in (first, second) for value in point),
                    "complete_score_vector": dict(zip(NAMES, STRICT_SCORE_VECTOR)),
                    "minimizer_face": ["3012"],
                }
                for first, second in strict_pairs
            ],
        })

    radius_census: dict[str, int] = {}
    for first, second in all_strict:
        radius = max(abs(value) for point in (first, second) for value in point)
        radius_census[str(radius)] = radius_census.get(str(radius), 0) + 1
    require(radius_census == {"5": 2, "6": 2}, "radius census")

    return {
        "schema": "exact-recurrent-first-host-critical-line-strict-reversal/v1",
        "scope": {
            "host_id": HOST_ID,
            "coverage": "all integer two-point backgrounds on x+y=2 or x+y=4",
            "responses": list(NAMES),
        },
        "critical_lines": rows,
        "aggregate": {
            "critical_lines": 2,
            "exceptional_integer_points_per_line": 4,
            "exceptional_pairs_audited_per_line": 6,
            "strict_reversal_pairs": 4,
            "strict_score_vector": dict(zip(NAMES, STRICT_SCORE_VECTOR)),
            "strict_reversal_radius_census": radius_census,
            "minimum_strict_reversal_radius": 5,
            "maximum_strict_reversal_radius_on_critical_lines": 6,
        },
        "proof": {
            "generic_points": (
                "outside the four integer secant intersections on each critical line, "
                "the singleton increment is zero, so 3012 only ties the reopening face"
            ),
            "strict_candidates": (
                "a strict reversal must use two exceptional points; all six pairs on "
                "each line are enumerated by direct triple counting"
            ),
        },
        "honesty": {
            "critical_line_strict_reversal_classification_complete": 1,
            "all_pair_lines_strict_reversal_classification_complete": 0,
            "physical_background_realizability_proved": 0,
            "deletion_causes_populated": 0,
            "legal_operations_populated": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    honesty = manifest.get("honesty")
    require(isinstance(honesty, dict), "honesty object")
    require(honesty.get("all_pair_lines_strict_reversal_classification_complete") == 0, "scope honesty")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(strict_reversal_pairs=3),
        lambda item: item["aggregate"]["strict_reversal_radius_census"].update({"5": 1}),
        lambda item: item["critical_lines"].pop(),
        lambda item: item["critical_lines"][0]["exceptional_integer_points"].pop(),
        lambda item: item["critical_lines"][0]["strict_reversal_pairs"].pop(),
        lambda item: item["critical_lines"][0]["strict_reversal_pairs"][0]["complete_score_vector"].update({"3012": 2}),
        lambda item: item["honesty"].update(all_pair_lines_strict_reversal_classification_complete=1),
        lambda item: item["honesty"].update(physical_background_realizability_proved=1),
        lambda item: item["honesty"].update(all_n_proved_by_checker=1),
    ]
    rejected = 0
    for mutate in mutations:
        candidate = copy.deepcopy(manifest)
        mutate(candidate)
        try:
            validate(candidate)
        except (AuditError, KeyError, TypeError, ValueError):
            rejected += 1
    require(rejected == len(mutations), "mutation audit")
    return rejected


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    arguments = parser.parse_args()
    manifest = compile_manifest()
    if arguments.write:
        arguments.write.parent.mkdir(parents=True, exist_ok=True)
        arguments.write.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    if arguments.check:
        observed = json.loads(arguments.check.read_text(encoding="utf-8"))
        validate(observed)
    print(json.dumps({
        "checker": "exact-recurrent-first-host-critical-line-strict-reversal",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
