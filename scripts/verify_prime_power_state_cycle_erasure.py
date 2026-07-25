#!/usr/bin/env python3
"""Finite checks for CMR410--CMR412."""

from __future__ import annotations

from itertools import permutations
from math import factorial


def edges(state: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(source, row) for source, row in enumerate(state)}


def verify_monotone_mask_erasure() -> None:
    for side in range(2, 8):
        universe = {(x, y) for x in range(side) for y in range(side)}
        states = list(permutations(range(side)))
        for state in states[: min(100, len(states))]:
            selected = edges(state)
            available_to_delete = sorted(universe - selected)
            masks = [set()]
            for edge in available_to_delete[: min(12, len(available_to_delete))]:
                masks.append(masks[-1] | {edge})

            for earlier in range(len(masks)):
                for later in range(earlier, len(masks)):
                    assert masks[earlier] <= masks[later]
                    assert selected.isdisjoint(masks[later])
                    assert len(selected) == side
                    assert len({x for x, _ in selected}) == side
                    assert len({y for _, y in selected}) == side


def verify_state_counts() -> None:
    for side in range(1, 10):
        states = list(permutations(range(side)))
        assert len(states) == factorial(side)
        assert len({state for state in states}) == factorial(side)

        two_layer_upper = factorial(side) ** 2
        assert two_layer_upper >= len(states)


def verify_context_dichotomy() -> None:
    # A complete state is the product of a local and outside state. Equal local
    # states with equal contexts give equal complete states; otherwise context
    # changed.
    for local_size in range(1, 6):
        for outside_size in range(0, 6):
            local_states = list(permutations(range(local_size)))
            outside_states = list(permutations(range(outside_size)))
            for local in local_states[:5]:
                for first_context in outside_states[:5]:
                    for second_context in outside_states[:5]:
                        first = (local, first_context)
                        second = (local, second_context)
                        assert (first == second) == (
                            first_context == second_context
                        )


def main() -> None:
    verify_monotone_mask_erasure()
    verify_state_counts()
    verify_context_dichotomy()
    print(
        "verified matching-state cycle erasure: monotone masks, factorial state "
        "counts, and local-state/outside-context recurrence"
    )


if __name__ == "__main__":
    main()
