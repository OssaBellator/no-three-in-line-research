#!/usr/bin/env python3
"""Verify exact cactus messages on two-cycle binary phase flowers."""

from __future__ import annotations

from itertools import product

Pattern = tuple[int, int]


def edge_satisfied(left: int, right: int, forbidden: Pattern) -> bool:
    return (left, right) != forbidden


def two_edge_cycle_message(
    first: Pattern, second: Pattern
) -> frozenset[int]:
    return frozenset(
        center
        for center in range(2)
        if any(
            edge_satisfied(center, leaf, first)
            and edge_satisfied(leaf, center, second)
            for leaf in range(2)
        )
    )


def solve_flower(
    cycles: tuple[tuple[Pattern, Pattern], ...]
) -> tuple[int, tuple[int, ...]] | None:
    messages = [
        two_edge_cycle_message(first, second) for first, second in cycles
    ]
    allowed_center = set(range(2))
    for message in messages:
        allowed_center.intersection_update(message)
    if not allowed_center:
        return None

    center = min(allowed_center)
    leaves = tuple(
        next(
            leaf
            for leaf in range(2)
            if edge_satisfied(center, leaf, first)
            and edge_satisfied(leaf, center, second)
        )
        for first, second in cycles
    )
    return center, leaves


def brute_force(
    cycles: tuple[tuple[Pattern, Pattern], ...]
) -> tuple[int, tuple[int, ...]] | None:
    for labels in product(range(2), repeat=len(cycles) + 1):
        center = labels[0]
        leaves = labels[1:]
        if all(
            edge_satisfied(center, leaf, first)
            and edge_satisfied(leaf, center, second)
            for leaf, (first, second) in zip(leaves, cycles)
        ):
            return center, tuple(leaves)
    return None


def verify() -> None:
    patterns = tuple(product(range(2), repeat=2))
    cycle_types = tuple(product(patterns, repeat=2))
    saw_saturation = False
    for first_cycle, second_cycle in product(cycle_types, repeat=2):
        cycles = (first_cycle, second_cycle)
        solved = solve_flower(cycles)
        brute = brute_force(cycles)
        assert (solved is None) == (brute is None)
        if solved is None:
            messages = [
                two_edge_cycle_message(*cycle) for cycle in cycles
            ]
            assert not set.intersection(*(set(message) for message in messages))
            saw_saturation = True
        else:
            center, leaves = solved
            assert all(
                edge_satisfied(center, leaf, first)
                and edge_satisfied(leaf, center, second)
                for leaf, (first, second) in zip(leaves, cycles)
            )
    assert saw_saturation


def main() -> None:
    verify()
    print("binary phase-cactus messages: verified on all two-cycle flowers")


if __name__ == "__main__":
    main()
