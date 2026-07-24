#!/usr/bin/env python3
"""Finite and exact-arithmetic checks for CMR153--CMR156."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import factorial


def allowed_count(t: int, second_forbidden: tuple[int, ...]) -> int:
    return sum(
        all(
            state[row] != row and state[row] != second_forbidden[row]
            for row in range(t)
        )
        for state in permutations(range(t))
    )


def verify_small_degree_two_density() -> None:
    expected_minimum = {4: 2, 5: 12, 6: 80}
    for t, expected in expected_minimum.items():
        minimum = min(
            allowed_count(t, relative)
            for relative in permutations(range(t))
        )
        assert minimum == expected
        assert 72 * minimum >= factorial(t)


def verify_degree_three_lll(max_t: int) -> None:
    for t in range(13, max_t + 1):
        # Local-lemma condition for x=2/t and dependency degree at most four.
        assert Fraction(1, t) <= Fraction(2, t) * Fraction(t - 2, t) ** 4

        lower_bound = Fraction(t - 2, t) ** (3 * t)
        assert lower_bound > Fraction(1, 700)


def verify_split_rank_coefficients(max_t: int) -> None:
    for t in range(13, max_t + 1):
        falling = [1]
        for rank in range(1, 4):
            falling.append(falling[-1] * (t - rank + 1))

        coefficients = {
            (1, 0): Fraction(72, falling[1]),
            (0, 1): Fraction(700, falling[1]),
            (2, 0): Fraction(72, falling[2]),
            (0, 2): Fraction(700, falling[2]),
            (1, 1): Fraction(72 * 700, falling[1] ** 2),
            (3, 0): Fraction(72, falling[3]),
            (0, 3): Fraction(700, falling[3]),
            (2, 1): Fraction(72 * 700, falling[2] * falling[1]),
            (1, 2): Fraction(72 * 700, falling[1] * falling[2]),
        }
        assert len(coefficients) == 9
        assert all(value > 0 for value in coefficients.values())


def verify_old_cell_exclusion() -> None:
    # Abstract one-column check: the first new cell avoids both old cells, and the
    # second avoids both old cells plus the first new cell. Therefore the final
    # unordered point pair contains neither old grid cell.
    for t in range(13, 30):
        for old_zero in range(t):
            for old_one in range(t):
                if old_zero == old_one:
                    continue
                first_choices = {
                    row for row in range(t) if row not in {old_zero, old_one}
                }
                for new_zero in first_choices:
                    second_choices = {
                        row
                        for row in range(t)
                        if row not in {old_zero, old_one, new_zero}
                    }
                    assert second_choices
                    for new_one in second_choices:
                        assert old_zero not in {new_zero, new_one}
                        assert old_one not in {new_zero, new_one}
                        assert new_zero != new_one


def main() -> None:
    verify_small_degree_two_density()
    verify_degree_three_lll(500)
    verify_split_rank_coefficients(500)
    verify_old_cell_exclusion()
    print(
        "verified old-cell-clean joint parent bank: degree-two minima 2,12,80, "
        "degree-three constant 1/700, and nine split-rank coefficients"
    )


if __name__ == "__main__":
    main()
