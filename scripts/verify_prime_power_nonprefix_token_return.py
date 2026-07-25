#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR403--CMR405."""

from __future__ import annotations

from itertools import permutations


def matching(vector: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(source, row) for source, row in enumerate(vector)}


def verify_host_churn() -> None:
    for side in range(3, 8):
        universe = {(x, y) for x in range(side) for y in range(side)}
        states = list(permutations(range(side)))
        sample = states[: min(60, len(states))]
        for old_vector in sample:
            old = matching(old_vector)
            for new_vector in sample:
                new = matching(new_vector)
                fixed = {(x, (x + 1) % side) for x in range(side)} - old - new
                before = universe - old - fixed
                after = universe - new - fixed
                returned = after - before
                assert returned <= old - new

                for modulus in range(1, side + 1):
                    for column_residue in range(modulus):
                        for row_residue in range(modulus):
                            token = {
                                (x, y)
                                for x, y in universe
                                if x % modulus == column_residue
                                and y % modulus == row_residue
                            }
                            source_count = sum(
                                x % modulus == column_residue for x in range(side)
                            )
                            assert len(returned & token) <= source_count


def verify_schedule_arithmetic() -> None:
    for p, h in ((3, 6), (5, 5), (7, 4), (11, 3)):
        side = p**h
        for depth in range(1, h):
            width = side // (p**depth)
            initial = width**2
            for one_layer in (0, 1, 3, 10):
                for joint in (0, 1, 2, 7):
                    prefix = 2 * depth * width
                    nonprefix = (one_layer + 2 * joint) * width
                    displayed = initial + (
                        2 * depth + one_layer + 2 * joint
                    ) * width
                    assert initial + prefix + nonprefix == displayed

                    if 3 * depth >= 2 * h:
                        assert initial**3 <= side**2
                        assert width**3 <= side


def main() -> None:
    verify_host_churn()
    verify_schedule_arithmetic()
    print(
        "verified non-prefix token return: host-churn inclusion, one/joint "
        "reset capacity, and combined deep schedule coefficients"
    )


if __name__ == "__main__":
    main()
