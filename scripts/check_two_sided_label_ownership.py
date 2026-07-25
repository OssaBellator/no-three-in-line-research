#!/usr/bin/env python3
"""Exact checker for PP3mq--PP3mt two-sided balanced ownership."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    return parser.parse_args()


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


def ownership_matching(
    acceptable: list[list[bool]], M: int, W: int
) -> tuple[int, list[int | None], list[int]]:
    adjacency: list[list[int]] = []
    for flags in acceptable:
        neighbors: list[int] = []
        for macro, allowed in enumerate(flags):
            if allowed:
                neighbors.extend(macro * W + copy for copy in range(W))
        adjacency.append(neighbors)

    size, left_to_right = maximum_matching(adjacency, M * W)
    ownership = [
        right // W if right != -1 else None
        for right in left_to_right
    ]
    loads = [0] * M
    for macro in ownership:
        if macro is not None:
            loads[macro] += 1
    return size, ownership, loads


def load_instance(
    path: Path,
) -> tuple[int, int, int, int, int, list[list[list[int]]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    T = data.get("T")
    M = data.get("M")
    W = data.get("W")
    r = data.get("r")
    s = data.get("s")

    if not all(
        isinstance(value, int) and not isinstance(value, bool) and value > 0
        for value in (T, M, W)
    ):
        raise ValueError("T, M, and W must be positive integers")
    if T != M * W:
        raise ValueError("instance must satisfy T = M*W")
    if not all(
        isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= T
        for value in (r, s)
    ):
        raise ValueError("r and s must be integers in [0,T]")

    raw_graphs = data.get("graphs")
    if not isinstance(raw_graphs, list) or len(raw_graphs) != M:
        raise ValueError("graphs must contain M matrices")

    graphs: list[list[list[int]]] = []
    for macro, raw_graph in enumerate(raw_graphs):
        if not isinstance(raw_graph, list) or len(raw_graph) != T:
            raise ValueError(f"graph {macro} must have T rows")
        matrix: list[list[int]] = []
        for movement, raw_row in enumerate(raw_graph):
            if (
                not isinstance(raw_row, list)
                or len(raw_row) != T
                or any(value not in (0, 1) for value in raw_row)
            ):
                raise ValueError(
                    f"graph {macro} row {movement} must contain T zero-one entries"
                )
            matrix.append(raw_row)
        graphs.append(matrix)

    return T, M, W, r, s, graphs


def main() -> None:
    args = parse_args()
    T, M, W, r, s, graphs = load_instance(args.input)

    row_nondegrees = [
        [sum(1 - value for value in graphs[macro][movement]) for macro in range(M)]
        for movement in range(T)
    ]
    column_nondegrees = [
        [
            sum(1 - graphs[macro][movement][refill] for movement in range(T))
            for macro in range(M)
        ]
        for refill in range(T)
    ]

    movement_acceptable = [
        [row_nondegrees[movement][macro] <= r for macro in range(M)]
        for movement in range(T)
    ]
    refill_acceptable = [
        [column_nondegrees[refill][macro] <= s for macro in range(M)]
        for refill in range(T)
    ]

    movement_size, movement_ownership, movement_loads = ownership_matching(
        movement_acceptable, M, W
    )
    refill_size, refill_ownership, refill_loads = ownership_matching(
        refill_acceptable, M, W
    )

    local_results: list[dict[str, object]] = []
    all_local = movement_size == T and refill_size == T
    if all_local:
        for macro in range(M):
            movement_labels = [
                label
                for label in range(T)
                if movement_ownership[label] == macro
            ]
            refill_labels = [
                label
                for label in range(T)
                if refill_ownership[label] == macro
            ]
            adjacency = [
                [
                    local_refill
                    for local_refill, refill in enumerate(refill_labels)
                    if graphs[macro][movement][refill]
                ]
                for movement in movement_labels
            ]
            matching_size, _ = maximum_matching(adjacency, len(refill_labels))
            min_row_degree = min(
                (
                    sum(graphs[macro][movement][refill] for refill in refill_labels)
                    for movement in movement_labels
                ),
                default=0,
            )
            min_column_degree = min(
                (
                    sum(graphs[macro][movement][refill] for movement in movement_labels)
                    for refill in refill_labels
                ),
                default=0,
            )
            local_results.append(
                {
                    "macro": macro,
                    "movement_labels": movement_labels,
                    "refill_labels": refill_labels,
                    "matching_size": matching_size,
                    "min_induced_row_degree": min_row_degree,
                    "min_induced_column_degree": min_column_degree,
                }
            )
            all_local = all_local and matching_size == W

    balanced_movement = movement_size == T and movement_loads == [W] * M
    balanced_refill = refill_size == T and refill_loads == [W] * M
    result = {
        "T": T,
        "M": M,
        "W": W,
        "r": r,
        "s": s,
        "r_plus_s": r + s,
        "row_nondegrees": row_nondegrees,
        "column_nondegrees": column_nondegrees,
        "movement_ownership_size": movement_size,
        "movement_ownership": movement_ownership,
        "movement_macro_loads": movement_loads,
        "refill_ownership_size": refill_size,
        "refill_ownership": refill_ownership,
        "refill_macro_loads": refill_loads,
        "local_macro_results": local_results,
        "pp3mq_threshold": r + s <= W,
        "pp3mq_certified": (
            balanced_movement
            and balanced_refill
            and r + s <= W
            and all_local
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
