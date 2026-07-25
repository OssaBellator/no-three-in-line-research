#!/usr/bin/env python3
"""Exact checker for PP3mg--PP3mz exceptional-label ownership criteria."""

from __future__ import annotations

import argparse
import json
from collections import deque
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
) -> tuple[int, list[int], list[int]]:
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
    return size, left_to_right, right_to_left


def ownership_graph(
    rows: list[list[Fraction]], threshold: Fraction, M: int, W: int
) -> tuple[list[list[bool]], list[list[int]]]:
    acceptable = [[score <= threshold for score in row] for row in rows]
    adjacency: list[list[int]] = []
    for flags in acceptable:
        neighbors: list[int] = []
        for macro, allowed in enumerate(flags):
            if allowed:
                neighbors.extend(macro * W + copy for copy in range(W))
        adjacency.append(neighbors)
    return acceptable, adjacency


def hall_witness(
    adjacency: list[list[int]],
    left_to_right: list[int],
    right_to_left: list[int],
    W: int,
) -> dict[str, object] | None:
    roots = [left for left, right in enumerate(left_to_right) if right == -1]
    if not roots:
        return None

    reached_left = set(roots)
    reached_right: set[int] = set()
    queue: deque[int] = deque(roots)

    while queue:
        left = queue.popleft()
        matched_right = left_to_right[left]
        for right in adjacency[left]:
            if right == matched_right or right in reached_right:
                continue
            reached_right.add(right)
            matched_left = right_to_left[right]
            if matched_left != -1 and matched_left not in reached_left:
                reached_left.add(matched_left)
                queue.append(matched_left)

    macros = sorted({right // W for right in reached_right})
    capacity = W * len(macros)
    return {
        "movement_labels": sorted(reached_left),
        "acceptable_macros": macros,
        "label_count": len(reached_left),
        "macro_capacity": capacity,
        "deficiency": len(reached_left) - capacity,
    }


def matching_snapshot(
    rows: list[list[Fraction]], threshold: Fraction, M: int, W: int
) -> dict[str, object]:
    acceptable, adjacency = ownership_graph(rows, threshold, M, W)
    T = len(rows)
    size, left_to_right, right_to_left = maximum_matching(adjacency, T)
    ownership = [right // W if right != -1 else None for right in left_to_right]
    loads = [0] * M
    for macro in ownership:
        if macro is not None:
            loads[macro] += 1
    balanced = size == T and loads == [W] * M
    return {
        "acceptable": acceptable,
        "adjacency": adjacency,
        "size": size,
        "left_to_right": left_to_right,
        "right_to_left": right_to_left,
        "ownership": ownership,
        "loads": loads,
        "balanced": balanced,
    }


def ownership_bottleneck(
    rows: list[list[Fraction]], M: int, W: int
) -> tuple[Fraction, dict[str, object]]:
    candidates = sorted({score for row in rows for score in row})
    for threshold in candidates:
        snapshot = matching_snapshot(rows, threshold, M, W)
        if snapshot["balanced"]:
            return threshold, snapshot
    raise RuntimeError("complete score matrix must be matchable at its maximum score")


def main() -> None:
    args = parse_args()
    T, M, W, r, rows, cols = load_instance(args.input)

    fixed = matching_snapshot(rows, r, M, W)
    acceptable = fixed["acceptable"]
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

    capped_sums: list[Fraction] = []
    refill_slacks: list[Fraction] = []
    refill_violations: list[dict[str, object]] = []
    for B in range(T):
        capped = sum(
            (min(Fraction(W), cols[B][i]) for i in range(M)), Fraction()
        )
        slack = sum(
            (max(Fraction(), Fraction(W) - cols[B][i]) for i in range(M)),
            Fraction(),
        )
        capped_sums.append(capped)
        refill_slacks.append(slack)
        if r + capped > T:
            refill_violations.append(
                {
                    "refill_label": B,
                    "capped_sum": fraction_text(capped),
                    "refill_slack": fraction_text(slack),
                    "r_plus_capped_sum": fraction_text(r + capped),
                }
            )

    bottleneck, optimum = ownership_bottleneck(rows, M, W)
    minimum_slack = min(refill_slacks)
    bottleneck_certified = bottleneck <= minimum_slack

    gap_witness = None
    if not bottleneck_certified:
        threshold_snapshot = matching_snapshot(rows, minimum_slack, M, W)
        gap_witness = {
            "minimum_refill_slack": fraction_text(minimum_slack),
            "ownership_hall_witness_at_refill_slack": hall_witness(
                threshold_snapshot["adjacency"],
                threshold_snapshot["left_to_right"],
                threshold_snapshot["right_to_left"],
                W,
            ),
        }

    result = {
        "T": T,
        "M": M,
        "W": W,
        "r": fraction_text(r),
        "acceptable_macro_counts_by_label": good_macro_counts,
        "acceptable_label_counts_by_macro": good_label_counts,
        "ownership_ore_violations": ore_violations,
        "ownership_matching_size": fixed["size"],
        "balanced_ownership_found": fixed["balanced"],
        "ownership_by_movement_label": fixed["ownership"],
        "macro_loads": fixed["loads"],
        "ownership_hall_witness": (
            None
            if fixed["balanced"]
            else hall_witness(
                fixed["adjacency"],
                fixed["left_to_right"],
                fixed["right_to_left"],
                W,
            )
        ),
        "capped_refill_scores": [fraction_text(value) for value in capped_sums],
        "refill_slacks": [fraction_text(value) for value in refill_slacks],
        "refill_score_violations": refill_violations,
        "pp3mk_certified": fixed["balanced"] and not refill_violations,
        "ownership_bottleneck": fraction_text(bottleneck),
        "minimum_refill_slack": fraction_text(minimum_slack),
        "bottleneck_ownership": optimum["ownership"],
        "pp3mx_bottleneck_slack_certified": bottleneck_certified,
        "bottleneck_slack_gap_witness": gap_witness,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
