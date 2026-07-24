#!/usr/bin/env python3
"""Verify the labelled forward/reverse switching-ratio inequality."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify(max_side: int = 3, max_multiplicity: int = 2) -> None:
    for left_size in range(1, max_side + 1):
        for right_size in range(1, max_side + 1):
            slots = left_size * right_size
            for entries in product(range(max_multiplicity + 1), repeat=slots):
                matrix = tuple(
                    entries[row * right_size : (row + 1) * right_size]
                    for row in range(left_size)
                )
                forward = [sum(row) for row in matrix]
                if min(forward) == 0:
                    continue
                reverse = [
                    sum(matrix[row][column] for row in range(left_size))
                    for column in range(right_size)
                ]
                minimum_forward = min(forward)
                maximum_reverse = max(reverse)
                description_count = sum(forward)

                assert minimum_forward * left_size <= description_count
                assert description_count <= maximum_reverse * right_size
                observed = Fraction(left_size, left_size + right_size)
                bound = Fraction(
                    maximum_reverse, minimum_forward + maximum_reverse
                )
                assert observed <= bound


def main() -> None:
    verify()
    print("general switching ratio: verified through 3-by-3 labelled graphs")


if __name__ == "__main__":
    main()
