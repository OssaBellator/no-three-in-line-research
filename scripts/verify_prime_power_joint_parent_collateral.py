#!/usr/bin/env python3
"""Exact arithmetic checks for CMR157--CMR161."""

from __future__ import annotations

from fractions import Fraction


def verify_cross_bounds() -> None:
    for p in (5, 7, 13, 17, 29):
        for k in range(2, 7):
            n = p**k
            for s in range(1, k):
                m = p**s
                t = n // m

                cross_two = m * (2 * n - 2 * t) * (t - 1)
                assert cross_two < 2 * n**2

                cross_three = m * (t - 1) ** 2
                assert cross_three < Fraction(n**2, p)


def verify_order_optimization() -> None:
    for first in range(101):
        for second in range(101):
            optimized = min(72 * first + 700 * second, 700 * first + 72 * second)
            assert 2 * optimized <= 772 * (first + second)


def verify_scale_sum() -> None:
    for p in (13, 17, 29):
        for k in range(2, 12):
            direct = sum(
                386
                * Fraction(12 * s + p + 1, 1)
                + Fraction(386, 3 * p)
                + 50400 * Fraction(2 * p + 1, p)
                for s in range(1, k)
            )
            closed = (
                386
                * (
                    6 * k * (k - 1)
                    + Fraction((3 * p * (p + 1) + 1) * (k - 1), 3 * p)
                )
                + 50400 * Fraction((2 * p + 1) * (k - 1), p)
            )
            assert direct == closed


def verify_degree_three_scale_boundary() -> None:
    for k in range(2, 8):
        # p=5: exactly the bottom t=5 scale is excluded.
        covered = [s for s in range(1, k) if 5 ** (k - s) >= 13]
        assert covered == list(range(1, max(1, k - 1)))

        # Every nontrivial block is covered for p>=13.
        for p in (13, 17, 29):
            assert all(p ** (k - s) >= 13 for s in range(1, k))


def main() -> None:
    verify_cross_bounds()
    verify_order_optimization()
    verify_scale_sum()
    verify_degree_three_scale_boundary()
    print(
        "verified joint parent collateral: cross bounds, 386 order constant, "
        "scale sum, and t>=13 boundary"
    )


if __name__ == "__main__":
    main()
