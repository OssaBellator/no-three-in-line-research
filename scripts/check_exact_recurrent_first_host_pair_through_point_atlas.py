#!/usr/bin/env python3
"""Classify first-host pair-through-response-point contribution vectors exactly."""
from __future__ import annotations

import argparse
import copy
import json
import math
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

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


class AuditError(RuntimeError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AuditError(message)


def response_points(permutation: Perm) -> tuple[Point, ...]:
    return tuple((row, permutation[row]) for row in range(4))


def response_union() -> tuple[Point, ...]:
    return tuple(
        sorted(
            {
                point
                for permutation in RESPONSES.values()
                for point in response_points(permutation)
            }
        )
    )


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


def union_incidence(line: Line, union: tuple[Point, ...]) -> tuple[Point, ...]:
    return tuple(point for point in union if on_line(point, line))


def contribution_vector(points: tuple[Point, ...]) -> tuple[int, ...]:
    return tuple(
        sum(point in response_points(permutation) for point in points)
        for permutation in RESPONSES.values()
    )


def union_lines(union: tuple[Point, ...]) -> dict[Line, tuple[Point, ...]]:
    result = {}
    for first, second in combinations(union, 2):
        line = normalize_line(first, second)
        result[line] = union_incidence(line, union)
    return result


def nearest_pair_on_line(line: Line, union: tuple[Point, ...]) -> tuple[Point, Point]:
    forbidden = set(union)
    candidates = [
        (x, y)
        for x in range(-30, 31)
        for y in range(-30, 31)
        if (x, y) not in forbidden and on_line((x, y), line)
    ]
    require(len(candidates) >= 2, f"integer witnesses missing for {line}")
    return min(
        combinations(candidates, 2),
        key=lambda pair: (
            max(abs(coordinate) for point in pair for coordinate in point),
            sum(abs(coordinate) for point in pair for coordinate in point),
            pair,
        ),
    )


def nearest_zero_pair(union: tuple[Point, ...]) -> tuple[Point, Point]:
    forbidden = set(union)
    candidates = [
        (x, y)
        for x in range(-8, 9)
        for y in range(-8, 9)
        if (x, y) not in forbidden
    ]
    valid = [
        (first, second)
        for first, second in combinations(candidates, 2)
        if not union_incidence(normalize_line(first, second), union)
    ]
    require(valid, "zero-contribution witness missing")
    return min(
        valid,
        key=lambda pair: (
            max(abs(coordinate) for point in pair for coordinate in point),
            sum(abs(coordinate) for point in pair for coordinate in point),
            pair,
        ),
    )


def nearest_single_point_pair(
    target: Point,
    union: tuple[Point, ...],
) -> tuple[Point, Point]:
    forbidden = set(union)
    candidates = [
        (x, y)
        for x in range(-12, 13)
        for y in range(-12, 13)
        if (x, y) not in forbidden
    ]
    valid = [
        (first, second)
        for first, second in combinations(candidates, 2)
        if union_incidence(normalize_line(first, second), union) == (target,)
    ]
    require(valid, f"single-point witness missing for {target}")
    return min(
        valid,
        key=lambda pair: (
            max(abs(coordinate) for point in pair for coordinate in point),
            sum(abs(coordinate) for point in pair for coordinate in point),
            pair,
        ),
    )


def compile_manifest() -> dict[str, object]:
    union = response_union()
    require(len(union) == 11, "response union size")
    lines = union_lines(union)
    require(len(lines) == 36, "union line census")
    line_size_census = Counter(len(points) for points in lines.values())
    require(line_size_census == Counter({2: 28, 3: 7, 4: 1}), "line-size census")

    grouped: dict[tuple[int, ...], list[dict[str, object]]] = defaultdict(list)

    zero_pair = nearest_zero_pair(union)
    grouped[(0, 0, 0, 0, 0)].append(
        {
            "kind": "zero",
            "pair": zero_pair,
            "line": normalize_line(*zero_pair),
        }
    )

    single_vectors = set()
    for point in union:
        vector = contribution_vector((point,))
        single_vectors.add(vector)
        pair = nearest_single_point_pair(point, union)
        grouped[vector].append(
            {
                "kind": "single",
                "point": point,
                "pair": pair,
                "line": normalize_line(*pair),
            }
        )
    require(len(single_vectors) == 11, "single-point membership vectors")

    for line, points in sorted(lines.items()):
        pair = nearest_pair_on_line(line, union)
        grouped[contribution_vector(points)].append(
            {
                "kind": "multiple",
                "points": points,
                "pair": pair,
                "line": line,
            }
        )

    require(len(grouped) == 39, "contribution class census")

    checked_witnesses = 0
    classes = []
    for vector in sorted(grouped):
        realizers = grouped[vector]
        for realizer in realizers:
            pair = realizer["pair"]
            require(not set(pair) & set(union), "witness overlaps response union")
            observed = contribution_vector(
                union_incidence(normalize_line(*pair), union)
            )
            require(observed == vector, "witness vector mismatch")
            checked_witnesses += 1
        classes.append(
            {
                "vector": list(vector),
                "total": sum(vector),
                "source_kind_census": dict(
                    sorted(Counter(item["kind"] for item in realizers).items())
                ),
                "representative_background_pair": [
                    list(point) for point in realizers[0]["pair"]
                ],
            }
        )
    require(checked_witnesses == 48, "witness census")

    total_census = Counter(item["total"] for item in classes)
    maxima = {
        name: max(item["vector"][index] for item in classes)
        for index, name in enumerate(RESPONSES)
    }
    require(
        maxima == {"3012": 3, "3210": 4, "2031": 2, "2310": 2, "3201": 2},
        "response maxima",
    )
    require(
        total_census
        == Counter({0: 1, 1: 4, 2: 8, 3: 12, 4: 8, 5: 4, 6: 1, 10: 1}),
        "total census",
    )

    return {
        "schema": "exact-recurrent-first-host-pair-through-point-atlas/v1",
        "scope": {
            "host_id": HOST_ID,
            "responses": list(RESPONSES),
            "background": "two distinct integer points disjoint from response union",
            "quantity": "pair-through-response-point contribution only",
        },
        "response_union_membership": [
            [
                point[0],
                point[1],
                *contribution_vector((point,)),
            ]
            for point in union
        ],
        "contribution_classes": classes,
        "aggregate": {
            "response_union_points": 11,
            "distinct_lines_through_union_pairs": 36,
            "union_line_size_census": {
                str(key): value for key, value in sorted(line_size_census.items())
            },
            "distinct_single_point_membership_vectors": 11,
            "pair_through_point_contribution_classes": 39,
            "stored_integer_witness_pairs": checked_witnesses,
            "total_contribution_census": {
                str(key): value for key, value in sorted(total_census.items())
            },
            "maximum_contribution_by_response": maxima,
        },
        "honesty": {
            "pair_through_point_vector_classification_complete": 1,
            "full_two_point_score_signature_classification_complete": 0,
            "physical_two_point_background_coverage_proved": 0,
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
    require(
        honesty.get("full_two_point_score_signature_classification_complete") == 0,
        "two-point honesty",
    )
    require(honesty.get("all_n_proved_by_checker") == 0, "all-n honesty")


def mutation_audit(manifest: dict[str, object]) -> int:
    mutations = [
        lambda item: item["aggregate"].update(response_union_points=10),
        lambda item: item["aggregate"].update(distinct_lines_through_union_pairs=35),
        lambda item: item["aggregate"].update(pair_through_point_contribution_classes=38),
        lambda item: item["aggregate"].update(stored_integer_witness_pairs=47),
        lambda item: item["aggregate"]["union_line_size_census"].update({"2": 27}),
        lambda item: item["aggregate"]["maximum_contribution_by_response"].update({"3210": 3}),
        lambda item: item["response_union_membership"].pop(),
        lambda item: item["contribution_classes"].pop(),
        lambda item: item["contribution_classes"][0]["vector"].__setitem__(0, 99),
        lambda item: item["contribution_classes"][0]["source_kind_census"].update({"zero": 2}),
        lambda item: item["honesty"].update(full_two_point_score_signature_classification_complete=1),
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
                "checker": "exact-recurrent-first-host-pair-through-point-atlas",
                **manifest["aggregate"],
                "mutation_corruptions_rejected": mutation_audit(manifest),
                **manifest["honesty"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
