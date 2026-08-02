#!/usr/bin/env python3
"""Audit one-point background fragility of the first side-four reopenings.

Finite affine theorem only. The witnesses are relative-coordinate schema
completions; this checker does not certify that either completion occurs in a
globally legal construction state.
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
DELETIONS = ("02", "20")
BASE_RESPONSES: dict[str, Perm] = {
    "3012": (3, 0, 1, 2),
    "3210": (3, 2, 1, 0),
}
REOPENING_RESPONSES: dict[str, Perm] = {
    "2031": (2, 0, 3, 1),
    "2310": (2, 3, 1, 0),
    "3201": (3, 2, 0, 1),
}


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def normalize_line(p: Point, q: Point) -> Line:
    require(p != q, "line needs distinct points")
    x1, y1 = p
    x2, y2 = q
    a, b, c = y1 - y2, x2 - x1, x1 * y2 - x2 * y1
    divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
    require(divisor > 0, "zero line")
    a, b, c = a // divisor, b // divisor, c // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(point: tuple[Fraction, Fraction] | Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def secant_lines(permutation: Perm) -> tuple[Line, ...]:
    return tuple(
        sorted(
            {
                normalize_line(p, q)
                for p, q in combinations(response_points(permutation), 2)
            }
        )
    )


def intersect(first: Line, second: Line) -> tuple[Fraction, Fraction] | None:
    a, b, c = first
    d, e, f = second
    determinant = a * e - d * b
    if determinant == 0:
        return None
    return (
        Fraction(b * f - e * c, determinant),
        Fraction(c * d - f * a, determinant),
    )


def collinear(first: Point, second: Point, third: Point) -> bool:
    return on_line(third, normalize_line(first, second))


def triple_count(points: Iterable[Point]) -> int:
    sequence = tuple(points)
    return sum(
        1
        for first, second, third in combinations(sequence, 3)
        if collinear(first, second, third)
    )


def intrinsic_score(permutation: Perm) -> int:
    return triple_count(response_points(permutation))


def singleton_complete_score(permutation: Perm, background: Point) -> int:
    require(background not in response_points(permutation), "background overlaps response")
    return triple_count((*response_points(permutation), background))


def rational_common_secant_points() -> tuple[tuple[Fraction, Fraction], ...]:
    line_families = {
        name: secant_lines(permutation)
        for name, permutation in REOPENING_RESPONSES.items()
    }
    first, second, third = tuple(REOPENING_RESPONSES)
    points: set[tuple[Fraction, Fraction]] = set()
    for first_line in line_families[first]:
        for second_line in line_families[second]:
            point = intersect(first_line, second_line)
            if point is None:
                continue
            if any(on_line(point, line) for line in line_families[third]):
                points.add(point)
    return tuple(sorted(points))


def encode_fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def encode_point(point: tuple[Fraction, Fraction] | Point) -> list[str]:
    return [encode_fraction(Fraction(point[0])), encode_fraction(Fraction(point[1]))]


def compile_manifest() -> dict[str, object]:
    common = rational_common_secant_points()
    integer_witnesses = tuple(
        (int(x), int(y))
        for x, y in common
        if x.denominator == 1 and y.denominator == 1
    )
    require(integer_witnesses == ((-1, 4), (4, -1)), "integer witness census")

    reopening_rows = []
    for name, permutation in REOPENING_RESPONSES.items():
        lines = secant_lines(permutation)
        require(len(lines) == 6, f"{name}: six distinct secants")
        require(intrinsic_score(permutation) == 0, f"{name}: intrinsic zero")
        reopening_rows.append(
            {
                "response": name,
                "points": [list(point) for point in response_points(permutation)],
                "secant_lines": [list(line) for line in lines],
            }
        )

    witness_rows = []
    for witness in integer_witnesses:
        response_scores = {
            name: {
                "intrinsic": intrinsic_score(permutation),
                "complete_with_singleton": singleton_complete_score(permutation, witness),
            }
            for name, permutation in {**BASE_RESPONSES, **REOPENING_RESPONSES}.items()
        }
        require(
            all(
                response_scores[name]["complete_with_singleton"] == 1
                for name in REOPENING_RESPONSES
            ),
            "all reopenings spoiled",
        )
        require(response_scores["3012"]["complete_with_singleton"] == 2, "3012 score")
        require(response_scores["3210"]["complete_with_singleton"] == 10, "3210 score")
        witness_rows.append(
            {
                "point": list(witness),
                "unit_padding_required": True,
                "response_scores": response_scores,
            }
        )

    return {
        "schema": "exact-recurrent-first-host-reopening-singleton-fragility/v1",
        "scope": {
            "host_id": HOST_ID,
            "deletions": list(DELETIONS),
            "base_responses": list(BASE_RESPONSES),
            "reopening_responses": list(REOPENING_RESPONSES),
            "background_size": 1,
            "coordinate_status": "relative affine schema completion",
        },
        "rational_common_secant_points": [encode_point(point) for point in common],
        "integer_common_secant_witnesses": [list(point) for point in integer_witnesses],
        "reopening_rows": reopening_rows,
        "witness_rows": witness_rows,
        "aggregate": {
            "reopening_responses": 3,
            "secants_per_reopening_response": 6,
            "rational_common_secant_points": 5,
            "integer_common_secant_witnesses": 2,
            "internal_4x4_integer_witnesses": 0,
            "minimum_coordinate_padding": 1,
            "reopening_responses_spoiled_per_integer_witness": 3,
        },
        "honesty": {
            "finite_affine_secant_classification_complete": 1,
            "integer_singleton_witness_classification_complete": 1,
            "witness_globally_realizable": 0,
            "deletion_causes_populated": 0,
            "legal_reopening_proved": 0,
            "recurrent_child_rows_populated": 0,
            "strict_lyapunov_certificate_proved": 0,
            "all_n_proved_by_checker": 0,
        },
    }


def validate(manifest: dict[str, object]) -> None:
    require(manifest == compile_manifest(), "manifest differs from exact compiler")
    honesty = manifest.get("honesty")
    require(isinstance(honesty, dict), "honesty object")
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")
    require(honesty.get("witness_globally_realizable") == 0, "realizability honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(integer_common_secant_witnesses=1),
        lambda item: item["aggregate"].update(internal_4x4_integer_witnesses=1),
        lambda item: item["integer_common_secant_witnesses"].pop(),
        lambda item: item["rational_common_secant_points"].pop(),
        lambda item: item["reopening_rows"][0]["secant_lines"].pop(),
        lambda item: item["reopening_rows"][0].update(response="9999"),
        lambda item: item["witness_rows"][0]["response_scores"]["2031"].update(
            complete_with_singleton=0
        ),
        lambda item: item["witness_rows"][0]["response_scores"]["3012"].update(
            complete_with_singleton=1
        ),
        lambda item: item["honesty"].update(witness_globally_realizable=1),
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

    print(
        json.dumps(
            {
                "checker": "exact-recurrent-first-host-reopening-singleton-fragility",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
