#!/usr/bin/env python3
"""Verify stationary resampling on two disjoint complete matchings."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations

State = tuple[tuple[int, ...], tuple[int, ...]]


def states(n: int) -> list[State]:
    result: list[State] = []
    for first in permutations(range(n)):
        for second in permutations(range(n)):
            if all(first[row] != second[row] for row in range(n)):
                result.append((first, second))
    return result


def swap_images(permutation: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    output = list(permutation)
    output[left], output[right] = output[right], output[left]
    return tuple(output)


def forward_targets(state: State) -> list[State]:
    first, second = state
    assert first[0] == 0
    bad_one = first.index(second[0])
    bad_two = second.index(0)
    allowed = [
        row
        for row in range(1, len(first))
        if row not in {bad_one, bad_two}
    ]
    if bad_one == bad_two:
        allowed.remove(min(allowed))
    return [(swap_images(first, 0, row), second) for row in allowed]


def verify(n: int) -> None:
    omega = states(n)
    state_set = set(omega)
    flawed = {state for state in omega if state[0][0] == 0}
    scale = n - 3
    reverse: dict[State, list[State]] = {
        state: [] for state in omega if state not in flawed
    }

    for source in flawed:
        targets = forward_targets(source)
        assert len(targets) == scale
        assert len(set(targets)) == scale
        for target in targets:
            assert target in state_set
            assert target not in flawed
            first_old, second = source
            first_new, second_new = target
            assert second_new == second
            old_edges = {(row, first_old[row]) for row in range(n)}
            new_edges = {(row, first_new[row]) for row in range(n)}
            assert len(old_edges ^ new_edges) == 4
            assert all(first_new[row] != second[row] for row in range(n))
            reverse[target].append(source)

    assert all(len(predecessors) <= 1 for predecessors in reverse.values())

    incoming = {state: Fraction(0) for state in omega}
    for source in flawed:
        for target in forward_targets(source):
            incoming[target] += Fraction(1, scale)
    for source, predecessors in reverse.items():
        for target in predecessors:
            incoming[target] += Fraction(1, scale)
        incoming[source] += Fraction(scale - len(predecessors), scale)
    assert all(total == 1 for total in incoming.values())


def main() -> None:
    for n in (4, 5):
        verify(n)
    print("complete two-layer resampling: verified for N=4,5")


if __name__ == "__main__":
    main()
