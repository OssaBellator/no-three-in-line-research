#!/usr/bin/env python3
"""Verify all-rank cylinders in complete and derangement blocks."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

EdgeSet = tuple[tuple[int, int], ...]


def partial_matchings(size: int):
    for rank in range(size + 1):
        for rows in combinations(range(size), rank):
            for columns in combinations(range(size), rank):
                for ordered_columns in permutations(columns):
                    yield tuple(zip(rows, ordered_columns))


def contains(state: tuple[int, ...], prescribed: EdgeSet) -> bool:
    return all(state[row] == column for row, column in prescribed)


def verify_block(size: int) -> None:
    states = list(permutations(range(size)))
    residual = [
        state
        for state in states
        if all(state[row] != row for row in range(size))
    ]
    assert len(residual) * 3 >= factorial(size)

    for prescribed in partial_matchings(size):
        rank = len(prescribed)
        first_count = sum(contains(state, prescribed) for state in states)
        assert Fraction(first_count, len(states)) == Fraction(
            factorial(size - rank), factorial(size)
        )
        assert Fraction(first_count, len(states)) <= Fraction(3, size) ** rank

        if any(row == column for row, column in prescribed):
            residual_count = 0
        else:
            residual_count = sum(
                contains(state, prescribed) for state in residual
            )
        observed = Fraction(residual_count, len(residual))
        assert observed <= Fraction(9, size) ** rank
        if rank == 1 and residual_count:
            assert observed == Fraction(1, size - 1)


def main() -> None:
    for size in range(2, 7):
        verify_block(size)
    print("sparse block-host spread: verified through block size six")


if __name__ == "__main__":
    main()
