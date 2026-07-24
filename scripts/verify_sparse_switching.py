#!/usr/bin/env python3
"""Verify the exact four-cycle switching ratio in small hosts."""

from __future__ import annotations

from itertools import permutations
from fractions import Fraction


Matching = tuple[int, ...]


def perfect_matchings(adjacency: tuple[frozenset[int], ...]) -> list[Matching]:
    return [
        state
        for state in permutations(range(len(adjacency)))
        if all(state[row] in adjacency[row] for row in range(len(adjacency)))
    ]


def switch_targets(
    adjacency: tuple[frozenset[int], ...],
    matching: Matching,
    edge: tuple[int, int],
) -> list[Matching]:
    row, column = edge
    assert matching[row] == column
    targets: list[Matching] = []
    for other in range(len(adjacency)):
        if other == row:
            continue
        other_column = matching[other]
        if column not in adjacency[other] or other_column not in adjacency[row]:
            continue
        output = list(matching)
        output[row], output[other] = output[other], output[row]
        targets.append(tuple(output))
    return targets


def verify_complete(max_n: int = 7) -> None:
    for n in range(2, max_n + 1):
        adjacency = tuple(frozenset(range(n)) for _ in range(n))
        states = perfect_matchings(adjacency)
        edge = (0, 0)
        containing = [state for state in states if state[0] == 0]
        avoiding = [state for state in states if state[0] != 0]
        reverse = {state: 0 for state in avoiding}
        for state in containing:
            targets = switch_targets(adjacency, state, edge)
            assert len(targets) == n - 1
            for target in targets:
                reverse[target] += 1
        assert set(reverse.values()) == {1}
        assert Fraction(len(containing), len(states)) == Fraction(1, n)


def verify_cycle_obstruction(n: int = 6) -> None:
    adjacency = tuple(
        frozenset((row, (row - 1) % n))
        for row in range(n)
    )
    states = perfect_matchings(adjacency)
    assert len(states) == 2
    edge = (0, 0)
    containing = [state for state in states if state[0] == 0]
    assert len(containing) == 1
    assert switch_targets(adjacency, containing[0], edge) == []
    assert Fraction(len(containing), len(states)) == Fraction(1, 2)


def verify() -> None:
    verify_complete()
    verify_cycle_obstruction()


def main() -> None:
    verify()
    print("sparse four-cycle switching ratio: verified through K_7,7")


if __name__ == "__main__":
    main()
