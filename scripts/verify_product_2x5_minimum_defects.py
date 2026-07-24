#!/usr/bin/env python3
"""Exact minimum-defect census for every unmodified 2 x 5 product host."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_product_hybrid_repair import (
    FactorPair,
    Point,
    determinant,
    valid_factor_pairs,
)
from verify_product_two_factor import product_host

ORIENTATIONS = ("cc", "cf", "fc", "ff")
EXPECTED = {
    "cc": Counter({7: 12, 8: 12, 9: 8}),
    "cf": Counter({2: 4, 3: 12, 4: 8, 5: 4, 6: 4}),
    "fc": Counter({2: 4, 3: 12, 4: 8, 5: 4, 6: 4}),
    "ff": Counter({2: 8, 3: 4, 4: 12, 5: 8}),
}


def unique_layer_unordered_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    for first, second in valid_factor_pairs(n):
        key = tuple(sorted((first, second)))
        if key in seen:
            continue
        seen.add(key)
        result.append((first, second))
    return tuple(result)


def minimum_defects(host: tuple[Point, ...]) -> tuple[int, int, int]:
    """Return minimum triple count, model multiplicity, and search nodes."""
    side = len(host) // 4
    rows = tuple(
        tuple(y for x, y in host if x == row)
        for row in range(side)
    )
    remaining = [[0] * side for _ in range(side + 1)]
    for row in range(side - 1, -1, -1):
        remaining[row] = remaining[row + 1].copy()
        for y in rows[row]:
            remaining[row][y] += 1

    edge_index = {edge: index for index, edge in enumerate(host)}
    prior_pair_masks: dict[Point, tuple[int, ...]] = {}
    for point in host:
        prior = tuple(edge for edge in host if edge[0] < point[0])
        prior_pair_masks[point] = tuple(
            (1 << edge_index[first]) | (1 << edge_index[second])
            for first, second in combinations(prior, 2)
            if determinant(first, second, point) == 0
        )

    column_degree = [0] * side
    selected_mask = 0
    best = 10**9
    best_count = 0
    nodes = 0

    def search(row: int, defects: int) -> None:
        nonlocal selected_mask, best, best_count, nodes
        nodes += 1
        if defects > best:
            return
        if row == side:
            if column_degree == [2] * side:
                if defects < best:
                    best = defects
                    best_count = 1
                elif defects == best:
                    best_count += 1
            return

        for selected_columns in combinations(rows[row], 2):
            if any(column_degree[y] == 2 for y in selected_columns):
                continue
            new_points = (
                (row, selected_columns[0]),
                (row, selected_columns[1]),
            )
            increment = sum(
                selected_mask & pair_mask == pair_mask
                for point in new_points
                for pair_mask in prior_pair_masks[point]
            )
            if defects + increment > best:
                continue

            for y in selected_columns:
                column_degree[y] += 1
            feasible = all(
                column_degree[y] <= 2
                and column_degree[y] + remaining[row + 1][y] >= 2
                for y in range(side)
            )
            if feasible:
                added_mask = (
                    (1 << edge_index[new_points[0]])
                    | (1 << edge_index[new_points[1]])
                )
                selected_mask |= added_mask
                search(row + 1, defects + increment)
                selected_mask ^= added_mask
            for y in selected_columns:
                column_degree[y] -= 1

    search(0, 0)
    return best, best_count, nodes


def main() -> None:
    outer = unique_layer_unordered_pairs(2)
    inner = unique_layer_unordered_pairs(5)
    assert len(outer) == 1
    assert len(inner) == 32

    distributions = {orientation: Counter() for orientation in ORIENTATIONS}
    total_nodes = {orientation: 0 for orientation in ORIENTATIONS}
    for factor in inner:
        for orientation in ORIENTATIONS:
            host = product_host(outer[0], factor, orientation)
            minimum, _, nodes = minimum_defects(host)
            distributions[orientation][minimum] += 1
            total_nodes[orientation] += nodes

    assert distributions == EXPECTED
    assert all(
        minimum >= 2
        for values in distributions.values()
        for minimum in values
    )

    for orientation in ORIENTATIONS:
        print(
            f"2x5 {orientation}: minimum-defect host distribution="
            f"{dict(sorted(distributions[orientation].items()))}, "
            f"search_nodes={total_nodes[orientation]}"
        )
    print(
        "all 128 ordered factor-pair instances are covered by "
        "layer-swap invariance"
    )


if __name__ == "__main__":
    main()
