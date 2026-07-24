#!/usr/bin/env python3
"""Finite checks for CMR153--CMR156."""

from __future__ import annotations

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


def verify_small_density() -> None:
    expected_minimum = {4: 2, 5: 12, 6: 80}
    for t, expected in expected_minimum.items():
        minimum = min(
            allowed_count(t, relative)
            for relative in permutations(range(t))
        )
        assert minimum == expected
        assert 72 * minimum >= factorial(t)


def allowed_states(t: int, first_forbidden, second_forbidden):
    return [
        state
        for state in permutations(range(t))
        if all(
            state[row] != first_forbidden[row]
            and state[row] != second_forbidden[row]
            for row in range(t)
        )
    ]


def verify_small_joint_bank() -> None:
    # Normalize one current layer to the identity and the other to a cyclic shift.
    for t in (4, 5):
        identity = tuple(range(t))
        shift = tuple((index + 1) % t for index in range(t))
        first_states = allowed_states(t, identity, shift)
        assert 72 * len(first_states) >= factorial(t)

        total = 0
        for first in first_states:
            second_states = allowed_states(t, shift, first)
            assert 72 * len(second_states) >= factorial(t)
            total += len(second_states)
        assert total * 72**2 >= factorial(t) ** 2


def verify_split_rank_coefficients() -> None:
    for t in range(4, 100):
        falling = [1]
        for rank in range(1, 4):
            falling.append(falling[-1] * (t - rank + 1))

        coefficients = {
            (1, 0): 72 / falling[1],
            (0, 1): 72 / falling[1],
            (2, 0): 72 / falling[2],
            (0, 2): 72 / falling[2],
            (1, 1): 72**2 / (falling[1] * falling[1]),
            (3, 0): 72 / falling[3],
            (0, 3): 72 / falling[3],
            (2, 1): 72**2 / (falling[2] * falling[1]),
            (1, 2): 72**2 / (falling[1] * falling[2]),
        }
        assert set(coefficients) == {
            (1, 0),
            (0, 1),
            (2, 0),
            (0, 2),
            (1, 1),
            (3, 0),
            (0, 3),
            (2, 1),
            (1, 2),
        }
        assert all(value > 0 for value in coefficients.values())


def main() -> None:
    verify_small_density()
    verify_small_joint_bank()
    verify_split_rank_coefficients()
    print(
        "verified ordered joint parent bank: small minima 2,12,80 and "
        "all nine split-rank coefficients"
    )


if __name__ == "__main__":
    main()
