#!/usr/bin/env python3
"""Exact arithmetic checks for CMR385--CMR389."""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def phi(n: int) -> int:
    return sum(gcd(n, value) == 1 for value in range(1, n + 1))


def direction_count(height: int) -> int:
    representatives: set[tuple[int, int]] = set()
    for first in range(-height, height + 1):
        for second in range(-height, height + 1):
            if max(abs(first), abs(second)) != height:
                continue
            if gcd(abs(first), abs(second)) != 1:
                continue
            direction = (first, second)
            opposite = (-first, -second)
            representatives.add(min(direction, opposite))
    return len(representatives)


def harmonic_band(lower: int) -> Fraction:
    return sum(Fraction(1, value) for value in range(lower, 2 * lower))


def verify_direction_counts() -> None:
    for height in range(1, 100):
        assert direction_count(height) == 4 * phi(height)


def verify_harmonic_packets() -> None:
    previous = harmonic_band(1)
    for lower in range(2, 10_000):
        current = harmonic_band(lower)
        assert current < previous
        previous = current
        if lower >= 5:
            assert current < Fraction(3, 4)
    assert harmonic_band(5) == Fraction(1879, 2520)


def verify_degree_inequality() -> None:
    for side in range(5, 1000):
        for heights in ({1}, {2}, {1, 2}, {2, 3}, {5, 6, 7, 8, 9}):
            exact_bound = sum(
                4
                * phi(height)
                * ((side - 1) // height)
                * (((side - 1) // height) - 1)
                // 2
                for height in heights
            )
            harmonic_bound = 2 * (side - 1) ** 2 * sum(
                Fraction(1, height) for height in heights
            )
            assert exact_bound <= harmonic_bound


def main() -> None:
    verify_direction_counts()
    verify_harmonic_packets()
    verify_degree_inequality()
    print(
        "verified harmonic band packing: direction counts, decreasing dyadic "
        "weights, two-band capacity, and harmonic degree bounds"
    )


if __name__ == "__main__":
    main()
