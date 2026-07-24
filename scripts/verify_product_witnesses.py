#!/usr/bin/env python3
"""Verify explicit finite no-three witnesses found by product searches.

These are exact finite certificates at side lengths 6, 8, and 9. They do not
imply an infinite product-closure theorem.
"""
from __future__ import annotations

from itertools import combinations

Point = tuple[int, int]
Permutation = tuple[int, ...]
PermutationPair = tuple[Permutation, Permutation]

EXAMPLES: tuple[PermutationPair, ...] = (
    (
        (3, 0, 5, 2, 4, 1),
        (4, 1, 3, 0, 5, 2),
    ),
    (
        (2, 3, 1, 0, 7, 6, 4, 5),
        (4, 5, 7, 6, 1, 0, 2, 3),
    ),
    (
        (3, 6, 1, 8, 0, 2, 5, 7, 4),
        (4, 1, 3, 6, 8, 0, 7, 2, 5),
    ),
)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def verify_pair(pair: PermutationPair) -> None:
    side = len(pair[0])
    assert len(pair[1]) == side
    assert sorted(pair[0]) == list(range(side))
    assert sorted(pair[1]) == list(range(side))
    assert all(pair[0][x] != pair[1][x] for x in range(side))

    points = [
        (x, pair[layer][x])
        for layer in (0, 1)
        for x in range(side)
    ]
    for triple in combinations(points, 3):
        assert determinant(*triple) != 0, (side, triple)


def main() -> None:
    for pair in EXAMPLES:
        verify_pair(pair)
        print(f"n={len(pair[0])}: verified {2 * len(pair[0])} no-three points")


if __name__ == "__main__":
    main()
