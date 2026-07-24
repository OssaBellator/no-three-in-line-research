#!/usr/bin/env python3
"""Exact finite checks for CMR138--CMR144."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations


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


def verify_two_layer_reoccupation() -> None:
    old_zero = (0, 1, 2, 3)
    old_one = (1, 0, 3, 2)
    new_zero = (2, 3, 0, 1)
    new_one = (0, 1, 2, 3)

    assert all(
        new_zero[column] != old_zero[column]
        and new_zero[column] != old_one[column]
        for column in range(4)
    )
    assert all(
        new_one[column] != old_one[column]
        and new_one[column] != new_zero[column]
        for column in range(4)
    )

    # Every old layer-zero geometric cell is reoccupied by the new second layer.
    assert all(new_one[column] == old_zero[column] for column in range(4))


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (
        c[0] - a[0]
    ) * (b[1] - a[1])


def triple_set(layer_zero: tuple[int, ...], layer_one: tuple[int, ...]):
    points = [
        (column, layer_zero[column], 0) for column in range(len(layer_zero))
    ] + [
        (column, layer_one[column], 1) for column in range(len(layer_one))
    ]
    triples = set()
    for indices in combinations(range(len(points)), 3):
        selected = tuple(points[index] for index in indices)
        if collinear(
            (selected[0][0], selected[0][1]),
            (selected[1][0], selected[1][1]),
            (selected[2][0], selected[2][1]),
        ):
            triples.add(selected)
    return frozenset(triples)


def complete_layer_moves(
    layer_zero: tuple[int, ...], layer_one: tuple[int, ...]
):
    n = len(layer_zero)
    assert n == 4
    results = []
    for moved_layer in (0, 1):
        current = layer_zero if moved_layer == 0 else layer_one
        opposite = layer_one if moved_layer == 0 else layer_zero
        for replacement in permutations(current):
            if not all(
                replacement[column] != current[column]
                and replacement[column] != opposite[column]
                for column in range(n)
            ):
                continue
            if moved_layer == 0:
                results.append((replacement, layer_one))
            else:
                results.append((layer_zero, replacement))
    return results


def verify_exact_trap() -> None:
    state_a = ((0, 1, 3, 2), (2, 3, 0, 1))
    state_b = ((1, 0, 2, 3), (2, 3, 0, 1))
    state_c = ((0, 1, 3, 2), (2, 3, 1, 0))

    triples_a = triple_set(*state_a)
    triples_b = triple_set(*state_b)
    triples_c = triple_set(*state_c)

    assert len(triples_a) == 1
    assert len(triples_b) == 1
    assert len(triples_c) == 0

    assert state_b in complete_layer_moves(*state_a)
    assert state_a in complete_layer_moves(*state_b)

    outgoing_a = sorted(
        len(triple_set(*state)) for state in complete_layer_moves(*state_a)
    )
    outgoing_b = sorted(
        len(triple_set(*state)) for state in complete_layer_moves(*state_b)
    )
    assert outgoing_a == [1, 4, 4, 4]
    assert outgoing_b == [1, 4, 4, 4]

    expected_a = frozenset(
        {((1, 1, 0), (0, 2, 1), (2, 0, 1))}
    )
    expected_b = frozenset(
        {((2, 2, 0), (1, 3, 1), (3, 1, 1))}
    )
    assert triples_a == expected_a
    assert triples_b == expected_b


def verify_cycle_balance() -> None:
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
    verify_two_layer_reoccupation()
    verify_exact_trap()
    verify_cycle_balance()
    print(
        "verified four-endpoint core: two-layer reoccupation, 108 boards, "
        "atoms 3/4,2/3,1/2, and the exact N=4 potential-one two-cycle"
    )


if __name__ == "__main__":
    main()
