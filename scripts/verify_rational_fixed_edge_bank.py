#!/usr/bin/env python3
"""Verify RI5a--RI5b fixed-edge I6 bank probabilities."""

from __future__ import annotations

from itertools import permutations, product
from math import factorial


State = tuple[tuple[int, ...], tuple[int, ...]]


def falling(value: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def states(blocks: int, order: int) -> tuple[State, ...]:
    return tuple(
        (permutation, shifts)
        for permutation in permutations(range(blocks))
        for shifts in product(range(order), repeat=blocks)
    )


def current_blocks_survive(
    state: State,
    selected: tuple[int, ...],
) -> bool:
    permutation, shifts = state
    return all(
        permutation[index] == index and shifts[index] == 0
        for index in selected
    )


def prescription_survives(
    state: State,
    sources: tuple[int, ...],
    targets: tuple[int, ...],
    shifts: tuple[int, ...],
) -> bool:
    permutation, state_shifts = state
    return all(
        permutation[source] == target
        and state_shifts[source] == shift
        for source, target, shift in zip(sources, targets, shifts)
    )


def verify_probabilities(maximum_blocks: int = 4, maximum_order: int = 5) -> None:
    for blocks in range(1, maximum_blocks + 1):
        for order in range(1, maximum_order + 1):
            bank = states(blocks, order)
            total = factorial(blocks) * order**blocks
            assert len(bank) == total

            for source in range(blocks):
                surviving = sum(
                    current_blocks_survive(state, (source,))
                    for state in bank
                )
                assert surviving * blocks * order == total

            for first in range(blocks):
                for second in range(first + 1, blocks):
                    surviving = sum(
                        current_blocks_survive(
                            state,
                            (first, second),
                        )
                        for state in bank
                    )
                    assert (
                        surviving
                        * falling(blocks, 2)
                        * order**2
                        == total
                    )

            for rank in range(1, blocks + 1):
                sources = tuple(range(rank))
                targets = tuple(reversed(range(rank)))
                prescribed_shifts = tuple(
                    index % order for index in range(rank)
                )
                surviving = sum(
                    prescription_survives(
                        state,
                        sources,
                        targets,
                        prescribed_shifts,
                    )
                    for state in bank
                )
                assert (
                    surviving
                    * falling(blocks, rank)
                    * order**rank
                    == total
                )


def verify_paid_neutralization(
    maximum_blocks: int = 4,
    maximum_order: int = 5,
) -> None:
    for blocks in range(1, maximum_blocks + 1):
        for order in range(1, maximum_order + 1):
            bank = states(blocks, order)
            orbit_types = [
                ((source,), 2 * source + 1)
                for source in range(blocks)
            ]
            orbit_types.extend(
                (
                    (first, second),
                    3 * first + 5 * second + 1,
                )
                for first in range(blocks)
                for second in range(first + 1, blocks)
            )
            total_weight = sum(weight for _, weight in orbit_types)
            destroyed = [
                sum(
                    weight
                    for selected, weight in orbit_types
                    if not current_blocks_survive(state, selected)
                )
                for state in bank
            ]
            assert (
                sum(destroyed) * blocks * order
                >= len(bank) * (blocks * order - 1) * total_weight
            )
            assert max(destroyed) * blocks * order >= (
                (blocks * order - 1) * total_weight
            )


def main() -> None:
    verify_probabilities()
    verify_paid_neutralization()
    print("rational fixed-edge I6 bank: verified")


if __name__ == "__main__":
    main()
