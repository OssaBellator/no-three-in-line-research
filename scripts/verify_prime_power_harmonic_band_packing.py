#!/usr/bin/env python3
"""Exact checks for CMR398--CMR402."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd


def phi(n: int) -> int:
    return sum(gcd(n, value) == 1 for value in range(1, n + 1))


def unoriented_directions(height: int) -> set[tuple[int, int]]:
    result = set()
    for first in range(-height, height + 1):
        for second in range(-height, height + 1):
            if max(abs(first), abs(second)) != height:
                continue
            if gcd(abs(first), abs(second)) != 1:
                continue
            direction = (first, second)
            opposite = (-first, -second)
            result.add(min(direction, opposite))
    return result


def verify_direction_count() -> None:
    for height in range(1, 100):
        assert len(unoriented_directions(height)) == 4 * phi(height)


def harmonic_band(lower: int) -> Fraction:
    return sum(Fraction(1, value) for value in range(lower, 2 * lower))


def verify_two_band_budget() -> None:
    for lower in range(1, 100):
        current = harmonic_band(lower)
        following = harmonic_band(lower + 1)
        assert following - current == -Fraction(1, 2 * lower * (2 * lower + 1))

    assert harmonic_band(5) == Fraction(1879, 2520)
    assert harmonic_band(5) < Fraction(3, 4)


def primitive_height(first: tuple[int, int], second: tuple[int, int]) -> int:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    common = gcd(abs(dx), abs(dy))
    return max(abs(dx // common), abs(dy // common))


def collinear(points: tuple[tuple[int, int], ...]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def verify_cell_degree_bound() -> None:
    for t in range(5, 10):
        cells = [(x, y) for x in range(t) for y in range(t)]
        for chosen_heights in ({1}, {2}, {1, 2}, {2, 3}):
            degree = {cell: 0 for cell in cells}
            for triple in combinations(cells, 3):
                if len({x for x, _ in triple}) < 3:
                    continue
                if len({y for _, y in triple}) < 3:
                    continue
                if not collinear(triple):
                    continue
                height = primitive_height(triple[0], triple[1])
                if height not in chosen_heights:
                    continue
                for cell in triple:
                    degree[cell] += 1

            exact_bound = sum(
                4
                * phi(height)
                * ((t - 1) // height)
                * (((t - 1) // height) - 1)
                // 2
                for height in chosen_heights
            )
            assert max(degree.values(), default=0) <= exact_bound

            harmonic = sum(Fraction(1, height) for height in chosen_heights)
            crude_bound = 2 * (t - 1) ** 2 * harmonic
            assert max(degree.values(), default=0) <= crude_bound


def main() -> None:
    verify_direction_count()
    verify_two_band_budget()
    verify_cell_degree_bound()
    print(
        "verified harmonic band packing: exact direction counts, decreasing "
        "dyadic weights, two-band budget, and finite cell-degree bounds"
    )


if __name__ == "__main__":
    main()
