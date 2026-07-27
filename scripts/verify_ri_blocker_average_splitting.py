#!/usr/bin/env python3
"""Finite arithmetic regressions for RI5ak--RI5ao."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import prod


def falling(t: int, s: int) -> int:
    return prod(range(t - s + 1, t + 1))


def check_partition() -> None:
    for occupancies in product(range(9), repeat=4):
        for values in product(range(4), repeat=4):
            nstates = len(values)
            total = Fraction(sum(values), nstates)
            b1 = Fraction(sum(v for t, v in zip(occupancies, values) if t == 1), nstates)
            bsmall = Fraction(sum(v for t, v in zip(occupancies, values) if 2 <= t <= 6), nstates)
            blarge = Fraction(sum(v for t, v in zip(occupancies, values) if t >= 7), nstates)
            bzero = Fraction(sum(v for t, v in zip(occupancies, values) if t == 0), nstates)
            if bzero == 0:
                assert total == b1 + bsmall + blarge
                assert max(b1, bsmall, blarge) >= total / 3


def check_raw_conversions() -> None:
    for n in range(3, 12):
        for d_num in range(1, 8):
            d = Fraction(d_num, 7)
            singleton_raw = (n - 1) * d
            assert singleton_raw / (n - 1) == d

    for t in range(7, 15):
        for s in range(1, 4):
            cap = Fraction(128, falling(t, s))
            for d_num in range(1, 8):
                d = Fraction(d_num, 11)
                raw = Fraction(falling(t, s), 384) * d
                assert raw * cap == d / 3


def check_failed_bank_constants() -> None:
    for g_num in range(1, 10):
        g = Fraction(g_num, 13)
        regime = g / 12
        assert 3 * regime == g / 4
        for t in range(7, 12):
            for s in range(1, 4):
                raw = Fraction(falling(t, s), 384) * regime
                assert raw == Fraction(falling(t, s), 4608) * g


def main() -> None:
    check_partition()
    check_raw_conversions()
    check_failed_bank_constants()
    print("RI blocker-average splitting checks passed")


if __name__ == "__main__":
    main()
