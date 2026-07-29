#!/usr/bin/env python3
"""Classify every legal two-point hard-core exchange background.

For the side-four hard-core exchange functional, strict Q4 selection with exactly
two outside-grid background points occurs in precisely two geometric families:
both points lie on K_MINUS, or exactly one lies on K_MINUS and the other lies on
K_30 or K_03 while their joining line avoids the two negative cross pivots.
This finite scalar theorem does not establish recurrence or labelled semantics and
permanently reports all_n_proved_by_checker=0.
"""
from __future__ import annotations

import copy
import hashlib
import json
from itertools import combinations
from typing import Any

Point = tuple[int, int]
Line = tuple[int, int, int]

GRID = {(x, y) for x in range(4) for y in range(4)}
K_MINUS: Line = (1, -1, -1)
K_PLUS: Line = (1, 1, -3)
K_30: Line = (3, 1, -3)
K_03: Line = (1, 3, -9)
RELEVANT_LINES = (K_MINUS, K_PLUS, K_30, K_03)
LINE_WEIGHTS = {K_MINUS: 3, K_PLUS: -5, K_30: 1, K_03: 1}

POSITIVE_PIVOTS: tuple[Point, Point] = ((3, 2), (1, 0))
NEGATIVE_PIVOTS: tuple[Point, Point] = ((3, 0), (1, 2))
EXPECTED_MANIFEST_SHA256 = "4ee3f69f653544853c04f0bf4822e839d537a52a41fe4612410604d7bc630f47"


class HardCoreTwoPointError(ValueError):
    """Raised when the exact two-point classification is inconsistent."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise HardCoreTwoPointError(message)


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y + c == 0


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def pair_count(point: Point, background: tuple[Point, ...]) -> int:
    return sum(
        collinear(point, first, second)
        for first, second in combinations(background, 2)
    )


def delta(background: tuple[Point, ...]) -> int:
    require(len(background) == len(set(background)), "background points must be distinct")
    require(not (set(background) & GRID), "background must avoid response grid")
    cross = (
        pair_count((3, 2), background)
        - pair_count((3, 0), background)
        - pair_count((1, 2), background)
        + pair_count((1, 0), background)
    )
    lines = sum(
        LINE_WEIGHTS[line] * sum(on_line(point, line) for point in background)
        for line in RELEVANT_LINES
    )
    return cross + lines - 3


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_digest(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def pair_cross_term(first: Point, second: Point) -> int:
    return (
        int(collinear(POSITIVE_PIVOTS[0], first, second))
        + int(collinear(POSITIVE_PIVOTS[1], first, second))
        - int(collinear(NEGATIVE_PIVOTS[0], first, second))
        - int(collinear(NEGATIVE_PIVOTS[1], first, second))
    )


def point_weight(point: Point) -> int:
    return sum(
        LINE_WEIGHTS[line] * int(on_line(point, line))
        for line in RELEVANT_LINES
    )


def on_negative_pivot_line(first: Point, second: Point) -> bool:
    return any(collinear(pivot, first, second) for pivot in NEGATIVE_PIVOTS)


def predicted_class(first: Point, second: Point) -> str:
    require(first != second, "two-point background requires distinct points")
    require(first not in GRID and second not in GRID, "background must avoid response grid")
    first_minus = on_line(first, K_MINUS)
    second_minus = on_line(second, K_MINUS)
    if first_minus and second_minus:
        return "both_K_minus"
    if first_minus ^ second_minus:
        other = second if first_minus else first
        if on_line(other, K_30) or on_line(other, K_03):
            if on_negative_pivot_line(first, second):
                return "mixed_negative_pivot_tie"
            return "mixed_positive_unit_line"
    return "non_Q4"


def exact_manifest() -> dict[str, Any]:
    witnesses: dict[str, tuple[Point, Point]] = {
        "both_K_minus": ((-1, -2), (4, 3)),
        "mixed_K_minus_K30": ((-2, -3), (-1, 6)),
        "mixed_K_minus_K03": ((-2, -3), (-3, 4)),
        "mixed_negative_pivot_tie_K30": ((2, -3), (4, 3)),
        "mixed_negative_pivot_tie_K03": ((0, -1), (6, 1)),
        "strict_Q1": ((-3, -3), (6, 6)),
    }
    witness_records = {
        name: {
            "background": [list(point) for point in pair],
            "predicted_class": predicted_class(*pair),
            "delta": delta(pair),
            "point_weights": [point_weight(point) for point in pair],
            "pair_cross_term": pair_cross_term(*pair),
        }
        for name, pair in witnesses.items()
    }
    payload: dict[str, Any] = {
        "version": 1,
        "positive_pivots": [list(point) for point in POSITIVE_PIVOTS],
        "negative_pivots": [list(point) for point in NEGATIVE_PIVOTS],
        "classification": {
            "strict_Q4": [
                "both_K_minus",
                "mixed_positive_unit_line",
            ],
            "tie_Q1": ["mixed_negative_pivot_tie"],
            "remaining": "non_Q4",
        },
        "class_deltas": {
            "both_K_minus": 5,
            "mixed_positive_unit_line": 1,
            "mixed_negative_pivot_tie": 0,
        },
        "witnesses": witness_records,
        "claims": {
            "strict_Q4_classes": 2,
            "strict_Q4_delta_values": [1, 5],
            "negative_pivots": 2,
            "all_n_proved_by_checker": 0,
        },
    }
    payload["manifest_sha256"] = canonical_digest(payload)
    return payload


def validate_manifest(manifest: Any) -> dict[str, Any]:
    require(isinstance(manifest, dict), "manifest must be an object")
    expected = exact_manifest()
    require(manifest == expected, "canonical two-point classification manifest mismatch")
    require(
        expected["claims"]
        == {
            "strict_Q4_classes": 2,
            "strict_Q4_delta_values": [1, 5],
            "negative_pivots": 2,
            "all_n_proved_by_checker": 0,
        },
        "classification claims drift",
    )
    require(expected["witnesses"]["both_K_minus"]["delta"] == 5, "K-minus witness drift")
    require(expected["witnesses"]["mixed_K_minus_K30"]["delta"] == 1, "K30 witness drift")
    require(expected["witnesses"]["mixed_K_minus_K03"]["delta"] == 1, "K03 witness drift")
    require(
        expected["witnesses"]["mixed_negative_pivot_tie_K30"]["delta"] == 0,
        "K30 tie witness drift",
    )
    require(
        expected["witnesses"]["mixed_negative_pivot_tie_K03"]["delta"] == 0,
        "K03 tie witness drift",
    )
    if EXPECTED_MANIFEST_SHA256 != "TO_BE_FILLED":
        require(expected["manifest_sha256"] == EXPECTED_MANIFEST_SHA256, "built-in manifest digest drift")
    return copy.deepcopy(expected["claims"])


def verify_bounded_pair_census() -> dict[str, Any]:
    points = [
        (x, y)
        for x in range(-3, 7)
        for y in range(-3, 7)
        if (x, y) not in GRID
    ]
    class_counts: dict[str, int] = {}
    delta_counts: dict[int, int] = {}
    checked = 0
    for first, second in combinations(points, 2):
        background = (first, second)
        value = delta(background)
        category = predicted_class(first, second)
        predicted_Q4 = category in {"both_K_minus", "mixed_positive_unit_line"}
        require(predicted_Q4 == (value > 0), f"classification mismatch: {background}")
        if category == "both_K_minus":
            require(value == 5, "both-K-minus delta must be five")
        elif category == "mixed_positive_unit_line":
            require(value == 1, "mixed positive-line delta must be one")
        elif category == "mixed_negative_pivot_tie":
            require(value == 0, "negative-pivot mixed pair must tie")
        class_counts[category] = class_counts.get(category, 0) + 1
        delta_counts[value] = delta_counts.get(value, 0) + 1
        checked += 1
    require(checked == 3486, "bounded pair count drift")
    require(class_counts.get("both_K_minus") == 15, "bounded both-K-minus count drift")
    require(class_counts.get("mixed_positive_unit_line") == 22, "bounded mixed-Q4 count drift")
    require(class_counts.get("mixed_negative_pivot_tie") == 2, "bounded mixed-tie count drift")
    require(
        sum(count for value, count in delta_counts.items() if value > 0) == 37,
        "bounded Q4 count drift",
    )
    return {
        "bounded_pair_cases": checked,
        "bounded_class_counts": sorted(class_counts.items()),
        "bounded_delta_counts": sorted(delta_counts.items()),
        "bounded_Q4_cases": 37,
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
    add(lambda data: data["positive_pivots"][0].__setitem__(0, 2))
    add(lambda data: data["negative_pivots"].pop())
    add(lambda data: data["classification"]["strict_Q4"].pop())
    add(lambda data: data["class_deltas"].update(both_K_minus=4))
    add(lambda data: data["witnesses"]["mixed_K_minus_K30"].update(delta=0))
    add(lambda data: data["claims"].update(all_n_proved_by_checker=1))

    rejected = 0
    for candidate in mutations:
        try:
            validate_manifest(candidate)
        except HardCoreTwoPointError:
            rejected += 1
    require(rejected == len(mutations), "mutation suite accepted a corruption")
    return rejected


def main() -> None:
    manifest = exact_manifest()
    claims = validate_manifest(manifest)
    census = verify_bounded_pair_census()
    rejected = mutation_tests()
    print(json.dumps({
        **claims,
        **census,
        "rejected_mutations": rejected,
        "manifest_sha256": manifest["manifest_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
