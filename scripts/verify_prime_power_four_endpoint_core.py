#!/usr/bin/env python3
"""Exact finite checks for CMR139--CMR142."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from fractions import Fraction


def partial_off_diagonal_matchings(t: int):
    yield {}
    for rank in range(1, t + 1):
        for rows in combinations(range(t), rank):
            for columns in permutations(range(t), rank):
                if any(row == column for row, column in zip(rows, columns)):
                    continue
                yield dict(zip(rows, columns))


def allowed_states(t: int, opposite: dict[int, int]):
    return [
        state
        for state in permutations(range(t))
        if all(
            state[row] != row
            and (row not in opposite or state[row] != opposite[row])
            for row in range(t)
        )
    ]


def maximum_atom(states, rank: int) -> Fraction:
    t = len(states[0])
    maximum = 0
    for rows in combinations(range(t), rank):
        for columns in permutations(range(t), rank):
            count = sum(
                all(state[row] == column for row, column in zip(rows, columns))
                for state in states
            )
            maximum = max(maximum, count)
    return Fraction(maximum, len(states))


def verify_four_board_profile() -> None:
    count = 0
    state_histogram: Counter[int] = Counter()
    maximum_atoms = [Fraction(0), Fraction(0), Fraction(0)]

    for opposite in partial_off_diagonal_matchings(4):
        states = allowed_states(4, opposite)
        assert len(states) >= 2
        count += 1
        state_histogram[len(states)] += 1

        for rank in (1, 2, 3):
            atom = maximum_atom(states, rank)
            maximum_atoms[rank - 1] = max(maximum_atoms[rank - 1], atom)

    assert count == 108
    assert dict(sorted(state_histogram.items())) == {
        2: 6,
        3: 32,
        4: 45,
        5: 12,
        6: 12,
        9: 1,
    }
    assert maximum_atoms == [Fraction(3, 4), Fraction(2, 3), Fraction(1, 2)]


def verify_cycle_balance() -> None:
    # A concrete abstract triple-set cycle. The identity checked here is purely
    # set-theoretic and is the exact calculation used in CMR142.
    cycle = [
        frozenset({0, 1, 2}),
        frozenset({1, 2, 3, 4}),
        frozenset({2, 4, 5}),
        frozenset({0, 2, 5}),
    ]
    cycle.append(cycle[0])

    created: Counter[int] = Counter()
    removed: Counter[int] = Counter()
    total_created = 0
    total_removed = 0

    for before, after in zip(cycle, cycle[1:]):
        new = after - before
        old = before - after
        total_created += len(new)
        total_removed += len(old)
        created.update(new)
        removed.update(old)

    assert created == removed
    assert total_created == total_removed


def main() -> None:
    verify_four_board_profile()
    verify_cycle_balance()
    print(
        "verified four-endpoint core: 108 boards, state counts "
        "{2:6,3:32,4:45,5:12,6:12,9:1}, atoms 3/4,2/3,1/2"
    )


if __name__ == "__main__":
    main()
