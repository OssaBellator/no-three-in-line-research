#!/usr/bin/env python3
"""Exact arithmetic checks for CMR176--CMR180."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def derangement_number(t: int) -> int:
    values = [1, 0]
    for size in range(2, t + 1):
        values.append((size - 1) * (values[-1] + values[-2]))
    return values[t]


def verify_density_and_atoms(max_t: int) -> None:
    for t in range(5, max_t + 1):
        count = derangement_number(t)
        assert 30 * count >= 11 * factorial(t)
        assert count % (t - 1) == 0

        rank_one_probability = Fraction(count // (t - 1), count)
        assert rank_one_probability == Fraction(1, t - 1)
        assert rank_one_probability <= Fraction(5, 4 * t)

        for rank in (2, 3):
            trivial_numerator = factorial(t - rank)
            probability_bound = Fraction(trivial_numerator, count)
            falling = factorial(t) // factorial(t - rank)
            assert probability_bound <= Fraction(30, 11 * falling)


def verify_reciprocal_sum() -> None:
    for p in (5, 13, 17, 29):
        for k in range(2, 15):
            direct = sum(
                Fraction(5, 4) * (12 * s + p - 1)
                + Fraction(30, 11) * (2 + Fraction(1, 3 * p))
                + Fraction(25, 8)
                + Fraction(75, 22 * p)
                for s in range(1, k)
            )
            closed = (k - 1) * (
                Fraction(5, 4) * (6 * k + p - 1)
                + Fraction(30, 11) * (2 + Fraction(1, 3 * p))
                + Fraction(25, 8)
                + Fraction(75, 22 * p)
            )
            assert direct == closed


def verify_prime_seven_sum() -> None:
    for k in range(2, 15):
        direct = sum(
            Fraction(135 * s, 7) + Fraction(2015, 168)
            for s in range(1, k)
        )
        closed = Fraction((1620 * k + 2015) * (k - 1), 168)
        assert direct == closed


def main() -> None:
    verify_density_and_atoms(200)
    verify_reciprocal_sum()
    verify_prime_seven_sum()
    print(
        "verified sharp derangement cylinders: density 11/30, exact rank one, "
        "reciprocal and prime-seven scale sums"
    )


if __name__ == "__main__":
    main()
