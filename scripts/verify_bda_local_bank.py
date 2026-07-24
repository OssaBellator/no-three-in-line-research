#!/usr/bin/env python3
"""Verify the bounded local permutation bank used in BDA2a."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import factorial


def falling(n: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= n - offset
    return result


def allowed_states(t: int) -> list[tuple[int, ...]]:
    """Avoid the current diagonal and a cyclic other-layer matching."""
    return [
        state
        for state in permutations(range(t))
        if all(state[row] not in (row, (row + 1) % t) for row in range(t))
    ]


def verify(t: int = 8) -> None:
    assert t >= 7
    states = allowed_states(t)
    assert len(states) * 128 >= factorial(t)

    event_counts: dict[int, Counter[tuple[tuple[int, int], ...]]] = {
        rank: Counter() for rank in (1, 2, 3)
    }
    for state in states:
        edges = tuple((row, state[row]) for row in range(t))
        assert all(column not in (row, (row + 1) % t) for row, column in edges)
        for rank in (1, 2, 3):
            event_counts[rank].update(combinations(edges, rank))

    for rank, counts in event_counts.items():
        for occurrences in counts.values():
            assert occurrences * falling(t, rank) <= 128 * len(states)


def main() -> None:
    verify(7)
    verify(8)
    print("BDA2a local permutation bank: verified for t=7,8")


if __name__ == "__main__":
    main()
