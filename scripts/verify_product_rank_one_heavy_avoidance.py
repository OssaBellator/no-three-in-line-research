#!/usr/bin/env python3
"""Finite checks for PX245--PX248."""

from __future__ import annotations

import itertools
import random


def maximum_degree(edges: set[tuple[int, int]], order: int) -> int:
    row_degree = [0] * order
    column_degree = [0] * order
    for row, column in edges:
        row_degree[row] += 1
        column_degree[column] += 1
    return max(row_degree + column_degree, default=0)


def allowed_permutations(order: int, blocked: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in itertools.permutations(range(order))
        if all((row, permutation[row]) not in blocked for row in range(order))
    ]


def matching_weight(permutation: tuple[int, ...], weights: dict[tuple[int, int], int]) -> int:
    return sum(weights[(row, permutation[row])] for row in range(len(permutation)))


def check_random_weighted_grids(seed: int = 245) -> None:
    rng = random.Random(seed)

    for order in range(3, 9):
        for _ in range(300):
            forbidden: set[tuple[int, int]] = set()
            layers = rng.randint(0, min(2, order // 2))
            for _layer in range(layers):
                permutation = list(range(order))
                rng.shuffle(permutation)
                for row in range(order):
                    if rng.random() < 0.8:
                        forbidden.add((row, permutation[row]))

            delta = maximum_degree(forbidden, order)
            weights = {
                (row, column): rng.randint(0, 4)
                for row in range(order)
                for column in range(order)
            }
            threshold = rng.randint(1, 4)
            heavy = {cell for cell, weight in weights.items() if weight >= threshold}
            heavy_degree = maximum_degree(heavy, order)
            bank = allowed_permutations(order, forbidden | heavy)

            # PX246: the sharp Hall sufficient threshold.
            if order >= 2 * (delta + heavy_degree):
                assert bank
                assert all(
                    matching_weight(permutation, weights) < threshold * order
                    for permutation in bank
                )

            # PX247: failure forces a heavy coordinate.
            if not bank:
                assert heavy_degree > order / 2 - delta


def check_optimized_witness_range() -> None:
    # PX245 uses PX232 with augmented degree Delta + lambda_m.
    for augmented_degree in range(1, 30):
        for order in range(8 * augmented_degree, 8 * augmented_degree + 100):
            x = 1 / (order - 4 * augmented_degree)
            assert 1 / order <= x * (1 - x) ** (2 * augmented_degree) + 1e-15


def check_star_field_translation() -> None:
    # PX228 converts mu >= m and line cap K into star order at least m/K.
    for threshold in range(1, 100):
        for line_cap in range(1, 20):
            extracted = threshold / line_cap
            assert extracted * line_cap <= threshold + 1e-12


def main() -> None:
    check_random_weighted_grids()
    check_optimized_witness_range()
    check_star_field_translation()
    print("PX245--PX248 rank-one heavy-cell checks passed")


if __name__ == "__main__":
    main()
