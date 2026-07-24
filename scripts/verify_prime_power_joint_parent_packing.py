#!/usr/bin/env python3
"""Exact checks for CMR169--CMR171."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_scale_occupancy_identity() -> None:
    for block_count in range(1, 9):
        for labels in product(range(block_count), repeat=3):
            occupied = len(set(labels))
            destroyed_counts = [
                int(block in labels) for block in range(block_count)
            ]
            assert sum(destroyed_counts) == occupied
            assert 1 <= occupied <= 3


def verify_reciprocal_division() -> None:
    for p in (5, 13, 17, 29):
        for k in range(2, 20):
            all_scale = (
                4
                * (
                    6 * k * (k - 1)
                    + Fraction((3 * p * (p + 1) + 1) * (k - 1), 3 * p)
                )
                + 16 * Fraction((2 * p + 1) * (k - 1), p)
            )
            frozen = (
                4
                * (
                    6 * k
                    + p
                    + 1
                    + Fraction(1, 3 * p)
                )
                + 16 * (2 + Fraction(1, p))
            )
            assert all_scale / (k - 1) == frozen


def verify_prime_seven_division() -> None:
    for k in range(2, 20):
        all_scale = Fraction((216 * k + 360) * (k - 1), 7)
        frozen = Fraction(216 * k + 360, 7)
        assert all_scale / (k - 1) == frozen


def main() -> None:
    verify_scale_occupancy_identity()
    verify_reciprocal_division()
    verify_prime_seven_division()
    print(
        "verified joint parent packing: exact 1--3 block multiplicity and "
        "reciprocal/prime-seven frozen endpoints"
    )


if __name__ == "__main__":
    main()
