#!/usr/bin/env python3
"""Verify the spread rematching bank used for rectangle secant stars."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import factorial

Cell = tuple[int, int]
Permutation = tuple[int, ...]


def allowed_permutations(size: int) -> tuple[Permutation, ...]:
    # Representative maximum-degree-two forbidden system: the original
    # diagonal together with the occupancy permutation of the opposite layer.
    forbidden = {
        (row, row) for row in range(size)
    } | {
        (row, (row + 1) % size) for row in range(size)
    }
    assert all(sum(cell[0] == row for cell in forbidden) == 2 for row in range(size))
    assert all(
        sum(cell[1] == column for cell in forbidden) == 2
        for column in range(size)
    )
    return tuple(
        permutation
        for permutation in permutations(range(size))
        if all((row, permutation[row]) not in forbidden for row in range(size))
    )


def verify_cylinder_bounds(size: int, allowed: tuple[Permutation, ...]) -> None:
    assert len(allowed) >= factorial(size) // 128

    counts = {rank: Counter() for rank in (1, 2, 3)}
    for permutation in allowed:
        cells = tuple((row, permutation[row]) for row in range(size))
        for rank in (1, 2, 3):
            for partial in combinations(cells, rank):
                counts[rank][frozenset(partial)] += 1

    for rank, counter in counts.items():
        falling = 1
        for offset in range(rank):
            falling *= size - offset
        for partial, count in counter.items():
            rows = {row for row, _ in partial}
            columns = {column for _, column in partial}
            assert len(rows) == len(columns) == rank
            assert count * falling <= 128 * len(allowed)


def verify_layer_rematching(size: int, allowed: tuple[Permutation, ...]) -> None:
    original_layer = {(row, row) for row in range(size)}
    opposite_layer = {(row, (row + 1) % size) for row in range(size)}

    for permutation in allowed:
        replacement = {(row, permutation[row]) for row in range(size)}
        assert len(replacement) == size
        assert {row for row, _ in replacement} == set(range(size))
        assert {column for _, column in replacement} == set(range(size))
        assert replacement.isdisjoint(original_layer)
        assert replacement.isdisjoint(opposite_layer)
        combined = replacement | opposite_layer
        assert all(sum(row == value for row, _ in combined) == 2 for value in range(size))
        assert all(
            sum(column == value for _, column in combined) == 2
            for value in range(size)
        )


def main() -> None:
    for size in (7, 8):
        allowed = allowed_permutations(size)
        verify_cylinder_bounds(size, allowed)
        verify_layer_rematching(size, allowed)
        print(
            f"t={size}: allowed matchings={len(allowed)}, "
            f"lower bound={factorial(size) // 128}"
        )

    print("rectangle secant-star rematching bank checks passed")


if __name__ == "__main__":
    main()
