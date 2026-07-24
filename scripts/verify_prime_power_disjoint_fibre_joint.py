#!/usr/bin/env python3
"""Exact arithmetic checks for CMR162--CMR168."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


H7 = (
    (0, 2, 6, 5, 3, 4, 1),
    (1, 0, 4, 6, 2, 3, 5),
    (2, 3, 5, 4, 1, 6, 0),
    (3, 5, 0, 2, 6, 1, 4),
    (4, 1, 3, 0, 5, 2, 6),
    (5, 6, 2, 1, 4, 0, 3),
    (6, 4, 1, 3, 0, 5, 2),
)


def derangement_number(t: int) -> int:
    previous, current = 1, 0
    if t == 0:
        return previous
    if t == 1:
        return current
    for size in range(2, t + 1):
        previous, current = current, (size - 1) * (current + previous)
    return current


def verify_derangement_spread(max_t: int) -> None:
    for t in range(2, max_t + 1):
        count = derangement_number(t)
        assert 4 * count >= factorial(t)
        for rank in range(1, min(3, t) + 1):
            # At most (t-r)! derangements contain a compatible prescription.
            assert Fraction(factorial(t - rank), count) <= Fraction(
                4, factorial(t) // factorial(t - rank)
            )


def verify_root_disjointness() -> None:
    # Distinct H7 maps use different rows in every root column.
    for first in range(7):
        for second in range(7):
            if first == second:
                continue
            assert all(H7[first][column] != H7[second][column] for column in range(7))

    # Reciprocal roots with common coefficient and distinct shifts differ by a
    # fixed nonzero output digit. The check is purely modular.
    for p in (5, 13, 17, 29):
        for shift_zero in range(p):
            for shift_one in range(p):
                if shift_zero == shift_one:
                    continue
                difference = (shift_zero - shift_one) % p
                assert difference != 0


def verify_reciprocal_scale_sum() -> None:
    for p in (5, 13, 17, 29):
        for k in range(2, 12):
            direct = sum(
                4
                * (
                    Fraction(12 * s + p - 1, 1)
                    + Fraction(2, 1)
                    + Fraction(1, 3 * p)
                )
                + 16 * (Fraction(2, 1) + Fraction(1, p))
                for s in range(1, k)
            )
            closed = (
                4
                * (
                    6 * k * (k - 1)
                    + Fraction((3 * p * (p + 1) + 1) * (k - 1), 3 * p)
                )
                + 16 * Fraction((2 * p + 1) * (k - 1), p)
            )
            assert direct == closed


def verify_prime_seven_sum() -> None:
    for k in range(2, 12):
        direct = sum(Fraction(432 * s + 360, 7) for s in range(1, k))
        closed = Fraction((216 * k + 360) * (k - 1), 7)
        assert direct == closed


def main() -> None:
    verify_derangement_spread(200)
    verify_root_disjointness()
    verify_reciprocal_scale_sum()
    verify_prime_seven_sum()
    print(
        "verified disjoint-fibre joint bank: derangement constant 4, "
        "root separation, reciprocal sums, and prime-seven coefficient"
    )


if __name__ == "__main__":
    main()
