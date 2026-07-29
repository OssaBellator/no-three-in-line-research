#!/usr/bin/env python3
"""Verify sharp background-cardinality realisability for hard-core exchange chambers.

The explicit hard-core exchange functional has a sharp finite boundary: no empty
or one-point survivor background can select Q4, while two outside-grid points on
the Q1 triple line select Q4 strictly. This proves scalar chamber realisability
only, not labelled semantics, and permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from typing import Any

import check_prime_power_hard_core_exchange_normal_form as normal

Point = tuple[int, int]
Line = tuple[int, int, int]

GRID = {(x, y) for x in range(4) for y in range(4)}
K_MINUS: Line = (1, -1, -1)
K_PLUS: Line = (1, 1, -3)
K_30: Line = (3, 1, -3)
K_03: Line = (1, 3, -9)
RELEVANT_LINES = (K_MINUS, K_PLUS, K_30, K_03)
LINE_WEIGHTS = {K_MINUS: 3, K_PLUS: -5, K_30: 1, K_03: 1}
EXPECTED_MANIFEST_SHA256 = "2b4d743fc4e98d39d63c2c7415ec33639692f8bd7b484dcb630ddb2aefd8896c"


class HardCoreRealisabilityError(ValueError):
    """Raised when the exact chamber-realisability boundary is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreRealisabilityError(message)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def pair_count(point: Point, background: tuple[Point, ...]) -> int:
    return sum(normal.collinear(point, first, second) for first, second in combinations(background, 2))


def cross_difference(background: tuple[Point, ...]) -> int:
    return (
        pair_count((3, 2), background)
        - pair_count((3, 0), background)
        - pair_count((1, 2), background)
        + pair_count((1, 0), background)
    )


def line_counts(background: tuple[Point, ...]) -> dict[Line, int]:
    return {line: sum(on_line(point, line) for point in background) for line in RELEVANT_LINES}


def delta(background: tuple[Point, ...]) -> int:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid the response grid")
    counts = line_counts(background)
    return cross_difference(background) + sum(LINE_WEIGHTS[line] * counts[line] for line in RELEVANT_LINES) - 3


def intersection(first: Line, second: Line) -> tuple[int, int, int] | None:
    a1, b1, c1 = first
    a2, b2, c2 = second
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return None
    x_numerator = b1 * c2 - b2 * c1
    y_numerator = c1 * a2 - c2 * a1
    if determinant < 0:
        determinant = -determinant
        x_numerator = -x_numerator
        y_numerator = -y_numerator
    return x_numerator, y_numerator, determinant


def exact_manifest() -> dict[str, Any]:
    intersections = []
    for first, second in combinations(RELEVANT_LINES, 2):
        raw = intersection(first, second)
        require(raw is not None, "relevant lines must be nonparallel")
        x_num, y_num, denominator = raw
        record = {
            "first": list(first),
            "second": list(second),
            "x_numerator": x_num,
            "y_numerator": y_num,
            "denominator": denominator,
            "integer_point": None,
            "inside_response_grid": 0,
        }
        if x_num % denominator == 0 and y_num % denominator == 0:
            point = (x_num // denominator, y_num // denominator)
            record["integer_point"] = list(point)
            record["inside_response_grid"] = int(point in GRID)
        intersections.append(record)

    zero_background: tuple[Point, ...] = ()
    tie_background: tuple[Point, ...] = ((-1, -2),)
    q4_background: tuple[Point, ...] = ((-1, -2), (4, 3))

    payload: dict[str, Any] = {
        "version": 1,
        "relevant_lines": [
            {"line": list(line), "weight": LINE_WEIGHTS[line]}
            for line in RELEVANT_LINES
        ],
        "pairwise_line_intersections": intersections,
        "witnesses": {
            "strict_Q1": {"background": [], "delta": delta(zero_background)},
            "tie_Q1": {"background": [list(point) for point in tie_background], "delta": delta(tie_background)},
            "strict_Q4": {"background": [list(point) for point in q4_background], "delta": delta(q4_background)},
        },
        "claims": {
            "zero_background_delta": delta(zero_background),
            "one_point_max_delta": 0,
            "minimum_background_points_for_Q4": 2,
            "strict_Q4_witness_delta": delta(q4_background),
            "both_scalar_halfspaces_realisable": 1,
            "all_n_proved_by_checker": 0,
        },
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, int]:
    require(isinstance(manifest, dict), "manifest must be an object")
    expected = exact_manifest()
    require(manifest == expected, "canonical realisability manifest mismatch")
    require(
        expected["claims"]
        == {
            "zero_background_delta": -3,
            "one_point_max_delta": 0,
            "minimum_background_points_for_Q4": 2,
            "strict_Q4_witness_delta": 5,
            "both_scalar_halfspaces_realisable": 1,
            "all_n_proved_by_checker": 0,
        },
        "realisability claims drift",
    )
    require(
        all(record["inside_response_grid"] == 1 for record in expected["pairwise_line_intersections"]),
        "every integer relevant-line intersection must lie in the forbidden response grid",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256, "built-in manifest digest drift")
    return dict(expected["claims"])


def verify_one_point_boundary() -> dict[str, int]:
    checked = 0
    distribution: dict[int, int] = {}
    for x in range(-12, 13):
        for y in range(-12, 13):
            point = (x, y)
            if point in GRID:
                continue
            value = delta((point,))
            require(value <= 0, f"one-point background selected Q4: {point}")
            distribution[value] = distribution.get(value, 0) + 1
            checked += 1
    require(max(distribution) == 0, "one-point maximum delta must be zero")
    require(delta(((-1, -2),)) == 0, "tie witness drift")
    return {"one_point_cases": checked, "one_point_distinct_deltas": len(distribution)}


def verify_two_point_box() -> dict[str, int]:
    points = [
        (x, y)
        for x in range(-3, 7)
        for y in range(-3, 7)
        if (x, y) not in GRID
    ]
    values: list[int] = []
    q4_cases = 0
    for first, second in combinations(points, 2):
        value = delta((first, second))
        values.append(value)
        q4_cases += int(value > 0)
    require(q4_cases > 0, "bounded two-point box must realise Q4")
    require(delta(((-1, -2), (4, 3))) == 5, "strict Q4 witness drift")
    return {
        "two_point_cases": len(values),
        "two_point_Q4_cases": q4_cases,
        "two_point_min_delta": min(values),
        "two_point_max_delta": max(values),
    }


def mutation_tests() -> int:
    manifest = exact_manifest()
    validate_manifest(manifest)
    mutations: list[dict[str, Any]] = []

    def add(mutator: Any) -> None:
        candidate = copy.deepcopy(manifest)
        mutator(candidate)
        mutations.append(candidate)

    add(lambda data: data.update(version=2))
    add(lambda data: data.update(manifest_sha256="0" * 64))
    add(lambda data: data["claims"].update(minimum_background_points_for_Q4=1))
    add(lambda data: data["claims"].update(strict_Q4_witness_delta=4))
    add(lambda data: data["relevant_lines"][0].update(weight=2))
    add(lambda data: data["pairwise_line_intersections"][0].update(inside_response_grid=0))
    add(lambda data: data["witnesses"]["tie_Q1"].update(delta=1))
    add(lambda data: data["witnesses"]["strict_Q4"]["background"].pop())

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreRealisabilityError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    one = verify_one_point_boundary()
    two = verify_two_point_box()
    rejected = mutation_tests()
    print(json.dumps({
        **claims,
        **one,
        **two,
        "rejected_mutations": rejected,
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
