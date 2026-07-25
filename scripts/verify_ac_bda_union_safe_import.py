#!/usr/bin/env python3
"""Finite checks for AC3fz--AC3gb."""

from __future__ import annotations

from fractions import Fraction
from math import comb


def core_count(envelope_roles: int) -> int:
    return 18 * envelope_roles**3 + 5 * envelope_roles**2


def main() -> None:
    clean_counts = tuple(comb(12 + rank - 1, rank) for rank in (1, 2, 3))
    missing_counts = tuple(comb(36 + rank - 1, rank) for rank in (1, 2, 3))
    assert clean_counts == (12, 78, 364)
    assert missing_counts == (36, 666, 8436)

    assert core_count(21) == 168903
    assert core_count(53) == 2693831

    assert Fraction(1, 32) / 3 == Fraction(1, 96)
    assert Fraction(1, 64) / 3 == Fraction(1, 192)

    print("AC union-safe BDA import verification passed")
    print(f"  clean role multisets: {clean_counts}")
    print(f"  missing-support role multisets: {missing_counts}")
    print(f"  clean core dictionary: {core_count(21)}")
    print(f"  missing core dictionary: {core_count(53)}")
    print("  unchanged rank-return constants: 1/96, 1/192")


if __name__ == "__main__":
    main()
