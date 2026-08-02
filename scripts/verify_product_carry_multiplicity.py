#!/usr/bin/env python3
"""Finite checks for fixed-area and mixed-radix carry multiplicity.

For every saturated no-three permutation pair of side at most five, this script
counts ordered triples at each signed determinant level and checks the proved
bound 4*n*(2*n-1). In the ordinary mixed-radix product, determinant level
D=n*kappa is exactly the fine carry level kappa.
"""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def no_three(points: tuple[Point, ...]) -> bool:
    length = len(points)
    for first in range(length):
        for second in range(first + 1, length):
            for third in range(second + 1, length):
                if determinant(points[first], points[second], points[third]) == 0:
                    return False
    return True


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    all_permutations = tuple(permutations(range(n)))
    for first in all_permutations:
        for second in all_permutations:
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = tuple(
                (x, layer[x])
                for layer in (first, second)
                for x in range(n)
            )
            if no_three(points):
                result.append((first, second))
    return tuple(result)


def signed_area_histogram(pair: FactorPair) -> Counter[int]:
    n = len(pair[0])
    points = tuple(
        (x, pair[layer][x])
        for layer in (0, 1)
        for x in range(n)
    )
    histogram: Counter[int] = Counter()
    for first in points:
        for second in points:
            if second == first:
                continue
            for third in points:
                if third == first or third == second:
                    continue
                histogram[determinant(first, second, third)] += 1
    return histogram


def check_side(n: int) -> None:
    bound = 4 * n * (2 * n - 1)
    maximum = 0
    maximizing_level = 0
    for pair in valid_factor_pairs(n):
        histogram = signed_area_histogram(pair)
        assert histogram[0] == 0
        for level, count in histogram.items():
            if level == 0:
                continue
            assert count <= bound, (n, pair, level, count, bound)
            if count > maximum:
                maximum = count
                maximizing_level = level
    print(
        f"n={n}: factor_pairs={len(valid_factor_pairs(n))}, "
        f"largest_ordered_level={maximum} at determinant {maximizing_level}, "
        f"proved_bound={bound}"
    )


def main() -> None:
    for n in range(2, 6):
        check_side(n)


if __name__ == "__main__":
    main()
