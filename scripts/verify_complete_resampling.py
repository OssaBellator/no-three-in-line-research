#!/usr/bin/env python3
"""Exhaustively verify the complete-host SRR1a switching kernel."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from math import factorial


def falling(n: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= n - offset
    return result


def switched(matching: tuple[int, ...], fixed_row: int, other: int) -> tuple[int, ...]:
    result = list(matching)
    result[fixed_row], result[other] = result[other], result[fixed_row]
    return tuple(result)


def contains_identity_edges(matching: tuple[int, ...], start: int, size: int) -> bool:
    return all(matching[row] == row for row in range(start, start + size))


def verify_stationarity(n: int) -> None:
    states = list(permutations(range(n)))
    incoming = {state: 0 for state in states}
    for state in states:
        for other in range(1, n):
            output = switched(state, 0, other)
            incoming[output] += 1
            assert switched(output, 0, other) == state
            assert len(set(state) ^ set(output)) == 0
    assert set(incoming.values()) == {n - 1}


def verify_removal_and_support(n: int) -> None:
    for state in permutations(range(n)):
        if state[0] != 0:
            continue
        for other in range(1, n):
            output = switched(state, 0, other)
            assert output[0] != 0
            old_edges = {(row, state[row]) for row in range(n)}
            new_edges = {(row, output[row]) for row in range(n)}
            assert len(old_edges ^ new_edges) == 4


def verify_remote_formula(n: int) -> None:
    states = list(permutations(range(n)))
    for k in range(1, min(3, n - 1) + 1):
        conditioned = [
            state for state in states if contains_identity_edges(state, 0, k)
        ]
        assert len(conditioned) == factorial(n - k)
        for s in range(1, min(3, n - k) + 1):
            successes = 0
            trials = len(conditioned) * (n - 1)
            for state in conditioned:
                for other in range(1, n):
                    output = switched(state, 0, other)
                    successes += contains_identity_edges(output, k, s)
            observed = Fraction(successes, trials)
            expected = Fraction(n - 1 - s, n - 1) * Fraction(
                1, falling(n - k, s)
            )
            assert observed == expected


def verify_positive_correlation() -> None:
    states = list(permutations(range(2)))
    first = sum(state[0] == 0 for state in states)
    second = sum(state[1] == 1 for state in states)
    both = sum(state[0] == 0 and state[1] == 1 for state in states)
    assert Fraction(both, len(states)) > Fraction(first, len(states)) * Fraction(
        second, len(states)
    )


def verify_balanced_switching_kernel(n: int) -> None:
    states = list(permutations(range(n)))
    flawed = {state for state in states if state[0] == 0}
    scale = n - 1
    rows: dict[
        tuple[int, ...], dict[tuple[int, ...], Fraction]
    ] = {state: {} for state in states}

    reverse_neighbours: dict[tuple[int, ...], list[tuple[int, ...]]] = {
        state: [] for state in states if state not in flawed
    }
    for state in flawed:
        neighbours = [switched(state, 0, other) for other in range(1, n)]
        assert len(neighbours) == scale
        assert all(output not in flawed for output in neighbours)
        for output in neighbours:
            rows[state][output] = rows[state].get(output, Fraction(0)) + Fraction(
                1, scale
            )
            reverse_neighbours[output].append(state)

    for state, neighbours in reverse_neighbours.items():
        assert len(neighbours) <= scale
        for output in neighbours:
            rows[state][output] = rows[state].get(output, Fraction(0)) + Fraction(
                1, scale
            )
        rows[state][state] = rows[state].get(state, Fraction(0)) + Fraction(
            scale - len(neighbours), scale
        )

    assert all(sum(row.values()) == 1 for row in rows.values())
    incoming = {state: Fraction(0) for state in states}
    for row in rows.values():
        for output, probability in row.items():
            incoming[output] += probability
    assert all(total == 1 for total in incoming.values())
    assert all(
        probability == rows[output].get(state, Fraction(0))
        for state, row in rows.items()
        for output, probability in row.items()
    )


def verify(max_n: int = 7) -> None:
    for n in range(2, max_n + 1):
        verify_stationarity(n)
        verify_removal_and_support(n)
        verify_remote_formula(n)
        verify_balanced_switching_kernel(n)
    verify_positive_correlation()


def main() -> None:
    verify()
    print("complete-host stationary resampling oracle: verified through N=7")


if __name__ == "__main__":
    main()
