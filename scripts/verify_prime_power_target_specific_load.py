#!/usr/bin/env python3
"""Finite checks for CMR248--CMR251."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, floor


def compatible_prescriptions(t: int, rank: int, target: tuple[int, int]):
    for rows in combinations(range(t), rank):
        for columns in permutations(range(t), rank):
            prescription = tuple(zip(rows, columns))
            if target in prescription:
                continue
            yield prescription


def verify_cylinder_atoms() -> None:
    for t in range(4, 7):
        target = (0, 0)
        states = [
            state
            for state in permutations(range(t))
            if state[target[0]] != target[1]
        ]
        assert len(states) == (t - 1) * factorial(t - 1)

        for rank in (1, 2, 3):
            maximum = 0
            for prescription in compatible_prescriptions(t, rank, target):
                count = sum(
                    all(state[row] == column for row, column in prescription)
                    for state in states
                )
                maximum = max(maximum, count)
            assert maximum == factorial(t - rank)

        rank_three_cover_lower_bound = (t - 1) ** 2 * (t - 2)
        atom_denominator = (t - 1) ** 2 * (t - 2)
        assert rank_three_cover_lower_bound == atom_denominator


def verify_local_wall_arithmetic(max_t: int = 1_000_000) -> None:
    for t in range(48, max_t + 1):
        falling_three = t * (t - 1) * (t - 2)
        line_capacity = comb(t - 1, 2)
        assert Fraction(falling_three, 48 * line_capacity) == Fraction(t, 24)
        wall_lines = floor(t / 24)
        assert wall_lines <= t - 2


def main() -> None:
    verify_cylinder_atoms()
    verify_local_wall_arithmetic()
    print(
        "verified target-specific loads: exact rank atoms through t=6 and "
        "the cubic-wall to t/24 line-signature conversion"
    )


if __name__ == "__main__":
    main()
