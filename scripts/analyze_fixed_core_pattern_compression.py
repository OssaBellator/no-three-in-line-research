#!/usr/bin/env python3
"""Evaluate PP3cr pattern compression against the opposite matching layer."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_full_width_two_block_bank import no_three, patch_states
from analyze_matching_first_reservoirs import alternating_decomposition, load_cases

Point = tuple[int, int]
Candidate = tuple[Point, int, str]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def candidate_cells(n: int, pool: tuple[Point, ...]) -> tuple[Candidate, ...]:
    a, b = n + 1, n + 2
    out: list[Candidate] = []
    for owner, (x, y) in enumerate(pool):
        out.extend(
            (
                ((x, a), owner, "M0"),
                ((x, b), owner, "M1"),
                ((a, y), owner, "F0"),
                ((b, y), owner, "F1"),
            )
        )
    return tuple(out)


def line_meets_fixed_pair(point: Point, fixed: tuple[Point, ...]) -> bool:
    return any(
        determinant(first, second, point) == 0
        for first, second in combinations(fixed, 2)
    )


def line_meets_fixed_anchor(
    first: Point, second: Point, fixed: tuple[Point, ...]
) -> bool:
    return any(determinant(anchor, first, second) == 0 for anchor in fixed)


def pattern_counts(
    n: int, pool: tuple[Point, ...], fixed: tuple[Point, ...]
) -> tuple[int, int, int]:
    candidates = candidate_cells(n, pool)
    blocked_cells = {
        point for point, _, _ in candidates if line_meets_fixed_pair(point, fixed)
    }

    same_edge_pairs: set[tuple[Point, Point]] = set()
    ordinary_pairs: set[tuple[Point, Point]] = set()
    for left, right in combinations(candidates, 2):
        left_point, left_owner, left_role = left
        right_point, right_owner, right_role = right
        if left_owner == right_owner:
            if left_role[0] == right_role[0]:
                continue
            target = same_edge_pairs
        else:
            target = ordinary_pairs
        if line_meets_fixed_anchor(left_point, right_point, fixed):
            target.add((min(left_point, right_point), max(left_point, right_point)))

    return len(blocked_cells), len(same_edge_pairs), len(ordinary_pairs)


def analyze_orientation(
    n: int,
    pool_index: int,
    pool: tuple[Point, ...],
    fixed: tuple[Point, ...],
) -> dict[str, Any]:
    r = len(pool)
    cell_count, same_edge_count, ordinary_count = pattern_counts(n, pool, fixed)
    total_states = 0
    locally_clean_states = 0
    globally_clean_states = 0

    for selected in combinations(range(r), 4):
        selected_set = set(selected)
        deleted = tuple(pool[index] for index in selected)
        retained_pool = tuple(
            point for index, point in enumerate(pool) if index not in selected_set
        )
        for patch in patch_states(deleted, n):
            total_states += 1
            local_clean = no_three(retained_pool + patch)
            locally_clean_states += local_clean
            if local_clean and no_three(fixed + retained_pool + patch):
                globally_clean_states += 1

    delta = Fraction(locally_clean_states, total_states)
    loss = (
        Fraction(2 * cell_count, r)
        + Fraction(same_edge_count, r)
        + Fraction(4 * ordinary_count, r * (r - 1))
    )
    lower_bound = max(Fraction(), delta - loss)

    return {
        "pool_layer": pool_index,
        "edge_count": r,
        "blocked_cell_patterns_C": cell_count,
        "same_edge_anchor_patterns_H": same_edge_count,
        "ordinary_anchor_patterns_A": ordinary_count,
        "local_clean_state_count": locally_clean_states,
        "local_clean_density_delta": fraction_text(delta),
        "pp3cr_pattern_loss": fraction_text(loss),
        "pp3cr_global_clean_density_lower_bound": fraction_text(lower_bound),
        "exact_global_clean_state_count": globally_clean_states,
        "total_full_states": total_states,
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
