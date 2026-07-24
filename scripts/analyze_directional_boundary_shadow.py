#!/usr/bin/env python3
"""Measure PP3co/PP3cp directional blocker counts against the opposite layer."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

from analyze_full_width_two_block_bank import patch_states
from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    ordered = tuple(points)
    return all(determinant(*triple) != 0 for triple in combinations(ordered, 3))


def blocked(point: Point, fixed: tuple[Point, ...]) -> bool:
    return any(
        determinant(first, second, point) == 0
        for first, second in combinations(fixed, 2)
    )


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def falling_three(value: int) -> int:
    return value * (value - 1) * (value - 2)


def classify_edges(
    n: int, pool: tuple[Point, ...], fixed: tuple[Point, ...]
) -> tuple[list[set[int]], list[set[int]], dict[str, int]]:
    a, b = n + 1, n + 2
    movement_allowed: list[set[int]] = []
    refill_allowed: list[set[int]] = []
    counts = {
        "unusable": 0,
        "movement_forced_first": 0,
        "movement_forced_second": 0,
        "refill_forced_first": 0,
        "refill_forced_second": 0,
    }

    for x, y in pool:
        movement = {
            index
            for index, row in enumerate((a, b))
            if not blocked((x, row), fixed)
        }
        refill = {
            index
            for index, column in enumerate((a, b))
            if not blocked((column, y), fixed)
        }
        movement_allowed.append(movement)
        refill_allowed.append(refill)
        if not movement or not refill:
            counts["unusable"] += 1
            continue
        if movement == {0}:
            counts["movement_forced_first"] += 1
        elif movement == {1}:
            counts["movement_forced_second"] += 1
        if refill == {0}:
            counts["refill_forced_first"] += 1
        elif refill == {1}:
            counts["refill_forced_second"] += 1

    return movement_allowed, refill_allowed, counts


def deletion_feasible(
    selected: tuple[int, ...],
    movement_allowed: list[set[int]],
    refill_allowed: list[set[int]],
) -> bool:
    if any(not movement_allowed[index] or not refill_allowed[index] for index in selected):
        return False
    for allowed in (movement_allowed, refill_allowed):
        forced_first = sum(allowed[index] == {0} for index in selected)
        forced_second = sum(allowed[index] == {1} for index in selected)
        if forced_first > 2 or forced_second > 2:
            return False
    return True


def analyze_orientation(
    n: int,
    pool_index: int,
    pool: tuple[Point, ...],
    fixed: tuple[Point, ...],
) -> dict[str, Any]:
    r = len(pool)
    movement_allowed, refill_allowed, counts = classify_edges(n, pool, fixed)
    total_deletions = 0
    feasible_deletions = 0
    blocker_free_geometries = 0
    opposite_layer_clean_geometries = 0

    for selected in combinations(range(r), 4):
        total_deletions += 1
        if deletion_feasible(selected, movement_allowed, refill_allowed):
            feasible_deletions += 1
        deleted = tuple(pool[index] for index in selected)
        for patch in patch_states(deleted, n):
            if all(not blocked(point, fixed) for point in patch):
                blocker_free_geometries += 1
            if no_three(fixed + patch):
                opposite_layer_clean_geometries += 1

    u = counts["unusable"]
    forced = (
        counts["movement_forced_first"],
        counts["movement_forced_second"],
        counts["refill_forced_first"],
        counts["refill_forced_second"],
    )
    lower_bound = Fraction(1, 1) - Fraction(4 * u, r)
    if r >= 3:
        lower_bound -= Fraction(4 * sum(falling_three(value) for value in forced), falling_three(r))
    lower_bound = max(Fraction(), lower_bound)

    return {
        "pool_layer": pool_index,
        "edge_count": r,
        **counts,
        "total_four_edge_deletions": total_deletions,
        "pp3cp_feasible_fraction_lower_bound": fraction_text(lower_bound),
        "exact_cell_blocker_feasible_deletions": feasible_deletions,
        "exact_cell_blocker_feasible_fraction": fraction_text(
            Fraction(feasible_deletions, total_deletions)
        ),
        "blocker_free_full_geometries": blocker_free_geometries,
        "opposite_layer_clean_full_geometries": opposite_layer_clean_geometries,
        "total_full_geometries": 36 * total_deletions,
    }


def analyze_case(n: int, core: tuple[Point, ...]) -> dict[str, Any]:
    if n < 4:
        return {"source_n": n, "orientations": [], "status": "fewer-than-four-edges"}
    layer_zero, layer_one, cycle_lengths = alternating_decomposition(n, core)
    return {
        "source_n": n,
        "cycle_edge_lengths": list(cycle_lengths),
        "orientations": [
            analyze_orientation(n, 0, layer_zero, layer_one),
            analyze_orientation(n, 1, layer_one, layer_zero),
        ],
        "status": "searched",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = load_cases(args.certificate, args.n)
        result = {"cases": [analyze_case(n, core) for n, core in cases]}
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
