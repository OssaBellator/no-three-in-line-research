#!/usr/bin/env python3
"""Exact checker for PP3mg--PP3mk exceptional-label ownership criteria."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def as_fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("booleans are not numeric scores")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, float):
        return Fraction(str(value))
    raise ValueError(f"invalid rational value: {value!r}")


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def load_instance(
    path: Path,
) -> tuple[int, int, int, Fraction, list[list[Fraction]], list[list[Fraction]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    T = data.get("T")
    M = data.get("M")
    W = data.get("W")
    if not all(
        isinstance(value, int) and not isinstance(value, bool) and value > 0
        for value in (T, M, W)
    ):
        raise ValueError("T, M, and W must be positive integers")
    if T != M * W:
        raise ValueError("instance must satisfy T = M*W")

    r = as_fraction(data.get("r"))
    if not 0 <= r <= T:
        raise ValueError("r must lie in [0,T]")

    raw_rows = data.get("row_scores")
    raw_cols = data.get("column_scores")
    if not isinstance(raw_rows, list) or len(raw_rows) != T:
        raise ValueError("row_scores must have T rows")
    if not isinstance(raw_cols, list) or len(raw_cols) != T:
        raise ValueError("column_scores must have T rows")

    rows: list[list[Fraction]] = []
    for index, raw in enumerate(raw_rows):
        if not isinstance(raw, list) or len(raw) != M:
            raise ValueError(f"row_scores[{index}] must have M entries")
        row = [as_fraction(value) for value in raw]
        if any(value < 0 for value in row):
            raise ValueError("row scores must be nonnegative")
        rows.append(row)

    cols: list[list[Fraction]] = []
    for index, raw in enumerate(raw_cols):
        if not isinstance(raw, list) or len(raw) != M:
            raise ValueError(f"column_scores[{index}] must have M entries")
        row = [as_fraction(value) for value in raw]
        if any(value < 0 for value in row):
            raise ValueError("column scores must be nonnegative")
        cols.append(row)

    return T, M, W, r, rows, cols


def maximum_matching(
    adjacency: list[list[int]], right_size: int
) -> tuple[int, list[int]]:
    right_to_left = [-1] * right_size

    def augment(left: int, seen: list[bool]) -> bool:
        for right in adjacency[left]:
            if seen[right]:
                continue
            seen[right] = True
            owner = right_to_left[right]
            if owner == -1 or augment(owner, seen):
                right_to_left[right] = left
                return True
        return False

    size = 0
    for left in range(len(adjacency)):
        if augment(left, [False] * right_size):
            size += 1

    left_to_right = [-1] * len(adjacency)
    for right, left in enumerate(right_to_left):
        if left != -1:
            left_to_right[left] = right
    return size, left_to_right


def main() -> None:
    args = parse_args()
    T, M, W, r, rows, cols = load_instance(args.input)

    acceptable = [[rows[A][i] <= r for i in range(M)] for A in range(T)]
    good_macro_counts = [sum(flags) for flags in acceptable]
    good_label_counts = [sum(acceptable[A][i] for A in range(T)) for i in range(M)]

    ore_violations: list[dict[str, object]] = []
    for A in range(T):
        for i in range(M):
            if acceptable[A][i]:
                continue
            degree_sum = W * good_macro_counts[A] + good_label_counts[i]
            if degree_sum < T:
                ore_violations.append(
                    {
                        "movement_label": A,
                        "macro": i,
                        "degree_sum": degree_sum,
                    }
                )

    adjacency: list[list[int]] = []
    for A in range(T):
        neighbors: list[int] = []
        for i in range(M):
            if acceptable[A][i]:
                neighbors.extend(i * W + copy for copy in range(W))
        adjacency.append(neighbors)

    matching_size, left_to_right = maximum_matching(adjacency, T)
    ownership = [right // W if right != -1 else None for right in left_to_right]
    macro_loads = [0] * M
    for macro in ownership:
        if macro is not None:
            macro_loads[macro] += 1

    capped_sums: list[Fraction] = []
    refill_violations: list[dict[str, object]] = []
    for B in range(T):
        capped = sum(
            (min(Fraction(W), cols[B][i]) for i in range(M)), Fraction()
        )
        capped_sums.append(capped)
        if r + capped > T:
            refill_violations.append(
                {
                    "refill_label": B,
                    "capped_sum": fraction_text(capped),
                    "r_plus_capped_sum": fraction_text(r + capped),
                }
            )

    balanced = matching_size == T and macro_loads == [W] * M
    result = {
        "T": T,
        "M": M,
        "W": W,
        "r": fraction_text(r),
        "acceptable_macro_counts_by_label": good_macro_counts,
        "acceptable_label_counts_by_macro": good_label_counts,
        "ownership_ore_violations": ore_violations,
        "ownership_matching_size": matching_size,
        "balanced_ownership_found": balanced,
        "ownership_by_movement_label": ownership,
        "macro_loads": macro_loads,
        "capped_refill_scores": [fraction_text(value) for value in capped_sums],
        "refill_score_violations": refill_violations,
        "pp3mk_certified": not ore_violations and balanced and not refill_violations,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
