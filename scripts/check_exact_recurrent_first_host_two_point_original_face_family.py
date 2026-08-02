#!/usr/bin/env python3
"""Compile the exact two-point original-face family for the first residual host.

This is an affine schema-completion theorem. It does not prove that the
background pairs occur in the installed global construction.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
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
TARGET_PAIR_VECTOR = (0, 0, 1, 1, 1)
TARGET_SCORE_VECTOR = (1, 4, 1, 1, 1)


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


def intrinsic_vector() -> tuple[int, ...]:
    return tuple(triple_count(response_points(RESPONSES[name])) for name in NAMES)


def response_union() -> tuple[Point, ...]:
    return tuple(sorted({point for permutation in RESPONSES.values() for point in response_points(permutation)}))


def response_secant_lines() -> tuple[Line, ...]:
    return tuple(sorted({
        normalize_line(first, second)
        for permutation in RESPONSES.values()
        for first, second in combinations(response_points(permutation), 2)
    }))


def pair_vector(line: Line) -> tuple[int, ...]:
    return tuple(
        sum(on_line(point, line) for point in response_points(RESPONSES[name]))
        for name in NAMES
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
    require(background[0] != background[1], "distinct background points")
    result = []
    for name in NAMES:
        response = response_points(RESPONSES[name])
        require(not set(background) & set(response), "background overlaps response")
        result.append(triple_count((*background, *response)) - triple_count(background))
    return tuple(result)


def union_pair_lines(union: tuple[Point, ...]) -> tuple[Line, ...]:
    return tuple(sorted({normalize_line(first, second) for first, second in combinations(union, 2)}))


def integer_base_and_direction(line: Line) -> tuple[Point, Point]:
    a, b, c = line
    base = None
    for x in range(-20, 21):
        for y in range(-20, 21):
            if a * x + b * y + c == 0:
                base = (x, y)
                break
        if base is not None:
            break
    require(base is not None, f"no integer base for {line}")
    direction = (b, -a)
    divisor = math.gcd(abs(direction[0]), abs(direction[1]))
    direction = (direction[0] // divisor, direction[1] // divisor)
    return base, direction


def generic_integer_witnesses(
    line: Line,
    secants: tuple[Line, ...],
    union: tuple[Point, ...],
) -> tuple[Point, Point]:
    require(line not in secants, "critical line must not be a response secant")
    base, direction = integer_base_and_direction(line)
    candidates = []
    for parameter in range(-100, 101):
        point = (
            base[0] + parameter * direction[0],
            base[1] + parameter * direction[1],
        )
        if point in union:
            continue
        if any(on_line(point, secant) for secant in secants):
            continue
        candidates.append(point)
        if len(candidates) == 2:
            break
    require(len(candidates) == 2, f"missing generic witnesses for {line}")
    return candidates[0], candidates[1]


def compile_manifest() -> dict[str, object]:
    union = response_union()
    secants = response_secant_lines()
    require(len(union) == 11, "response-union census")
    require(len(secants) == 20, "secant census")
    intrinsic = intrinsic_vector()
    require(intrinsic == (1, 4, 0, 0, 0), "intrinsic vector")

    critical_lines = [
        line
        for line in union_pair_lines(union)
        if pair_vector(line) == TARGET_PAIR_VECTOR
    ]
    require(critical_lines == [(1, 1, -4), (1, 1, -2)], "critical pair lines")

    rows = []
    for line in critical_lines:
        witnesses = generic_integer_witnesses(line, secants, union)
        increments = [singleton_increment(point, secants) for point in witnesses]
        require(increments == [(0, 0, 0, 0, 0), (0, 0, 0, 0, 0)], "generic singleton increments")
        observed = direct_score_vector(witnesses)
        require(observed == TARGET_SCORE_VECTOR, "critical score vector")
        rows.append({
            "line": list(line),
            "equation": f"x+y={-line[2]}",
            "response_union_points": [list(point) for point in union if on_line(point, line)],
            "pair_through_response_vector": dict(zip(NAMES, TARGET_PAIR_VECTOR)),
            "generic_integer_witnesses": [list(point) for point in witnesses],
            "generic_singleton_increment_vectors": [list(value) for value in increments],
            "complete_score_vector": dict(zip(NAMES, observed)),
            "minimizer_face": ["3012", "2031", "2310", "3201"],
        })

    require(all(line not in secants for line in critical_lines), "nonsecant critical lines")

    return {
        "schema": "exact-recurrent-first-host-two-point-original-face-family/v1",
        "scope": {
            "host_id": HOST_ID,
            "background_size": 2,
            "coordinate_status": "relative affine schema completion",
            "responses": list(NAMES),
        },
        "intrinsic_score_vector": dict(zip(NAMES, intrinsic)),
        "target_pair_through_response_vector": dict(zip(NAMES, TARGET_PAIR_VECTOR)),
        "critical_lines": rows,
        "aggregate": {
            "response_union_points": len(union),
            "response_secant_lines": len(secants),
            "critical_pair_lines": len(critical_lines),
            "critical_line_equations": ["x+y=4", "x+y=2"],
            "generic_complete_score_vector": dict(zip(NAMES, TARGET_SCORE_VECTOR)),
            "generic_minimum_score": 1,
            "generic_minimizer_face_size": 4,
            "infinite_integer_background_pairs_per_critical_line": 1,
        },
        "proof": {
            "finite_pair_line_classification": (
                "enumerate every line through two response-union points and retain "
                "pair vector (0,0,1,1,1)"
            ),
            "genericity": (
                "each retained primitive integer line is not a response secant, "
                "so deleting its finite response-union and secant-intersection set "
                "leaves infinitely many integer points"
            ),
            "score_identity": (
                "intrinsic (1,4,0,0,0) plus zero singleton increments plus "
                "pair vector (0,0,1,1,1)"
            ),
        },
        "honesty": {
            "critical_pair_line_classification_complete": 1,
            "infinite_affine_schema_completion_family_proved": 1,
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
    require(honesty.get("physical_background_realizability_proved") == 0, "physical honesty")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(critical_pair_lines=1),
        lambda item: item["aggregate"].update(generic_minimum_score=0),
        lambda item: item["critical_lines"].pop(),
        lambda item: item["critical_lines"][0].update(line=[1, 1, -3]),
        lambda item: item["critical_lines"][0]["complete_score_vector"].update({"3012": 0}),
        lambda item: item["critical_lines"][0].update(minimizer_face=["2031"]),
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
        "checker": "exact-recurrent-first-host-two-point-original-face-family",
        **manifest["aggregate"],
        "mutation_corruptions_rejected": mutation_audit(manifest),
        **manifest["honesty"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
