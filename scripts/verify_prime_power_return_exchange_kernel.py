#!/usr/bin/env python3
"""Finite checks for CMR1574--CMR1581."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from random import Random


Edge = tuple[int, int]
State = tuple[int, ...]


def alternating_cycle_lengths(old: State, new: State) -> dict[int, int]:
    side = len(old)
    inverse_old = {old[source]: source for source in range(side)}
    transition = [inverse_old[new[source]] for source in range(side)]
    lengths: dict[int, int] = {}
    seen: set[int] = set()

    for source in range(side):
        if source in seen:
            continue
        cycle: list[int] = []
        current = source
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = transition[current]
        length = len(cycle)
        for member in cycle:
            lengths[member] = length

    return lengths


def verify_transition(old: State, new: State) -> tuple[int, int, int]:
    side = len(old)
    old_edges = {(source, old[source]) for source in range(side)}
    new_edges = {(source, new[source]) for source in range(side)}
    leaving = old_edges - new_edges
    entering = new_edges - old_edges

    source_pair = {
        (source, old[source]): (source, new[source])
        for source in range(side)
        if old[source] != new[source]
    }
    target_pair = {
        (old_source, target): (new_source, target)
        for target in range(side)
        for old_source in range(side)
        for new_source in range(side)
        if old[old_source] == target
        and new[new_source] == target
        and old_source != new_source
    }

    assert set(source_pair) == leaving
    assert set(source_pair.values()) == entering
    assert len(source_pair) == len(set(source_pair.values()))
    assert set(target_pair) == leaving
    assert set(target_pair.values()) == entering
    assert len(target_pair) == len(set(target_pair.values()))

    cycle_lengths = alternating_cycle_lengths(old, new)
    exact_transport: dict[tuple[Edge, tuple[int, int]], int] = defaultdict(int)
    owner_degrees: dict[tuple[Edge, tuple[int, int]], int] = defaultdict(int)
    recreated = 0

    for triple in combinations(sorted(new_edges), 3):
        credit = set(triple)
        if credit <= old_edges:
            continue

        entering_support = sorted(credit & entering)
        assert entering_support
        owner = max(entering_support)
        predecessor = (owner[0], old[owner[0]])
        assert source_pair[predecessor] == owner

        coarse_class = (
            len(credit & old_edges),
            cycle_lengths[owner[0]],
        )
        exact_transport[(predecessor, coarse_class)] += 1
        owner_degrees[(owner, coarse_class)] += 1
        recreated += 1

    transported_totals: dict[tuple[int, int], int] = defaultdict(int)
    owner_totals: dict[tuple[int, int], int] = defaultdict(int)
    for (_edge, coarse_class), count in exact_transport.items():
        transported_totals[coarse_class] += count
    for (_edge, coarse_class), count in owner_degrees.items():
        owner_totals[coarse_class] += count

    assert transported_totals == owner_totals
    for (predecessor, coarse_class), count in exact_transport.items():
        assert count == owner_degrees[
            (source_pair[predecessor], coarse_class)
        ]

    return len(leaving), recreated, len(exact_transport)


def main() -> None:
    systems = 0
    leaving_edges = 0
    recreated_credits = 0
    kernel_entries = 0

    for side in range(3, 6):
        states = list(permutations(range(side)))
        for old in states:
            for new in states:
                counts = verify_transition(old, new)
                leaving_edges += counts[0]
                recreated_credits += counts[1]
                kernel_entries += counts[2]
                systems += 1

    rng = Random(1574)
    for side in range(6, 11):
        for _ in range(2_000):
            old_list = list(range(side))
            new_list = list(range(side))
            rng.shuffle(old_list)
            rng.shuffle(new_list)
            counts = verify_transition(tuple(old_list), tuple(new_list))
            leaving_edges += counts[0]
            recreated_credits += counts[1]
            kernel_entries += counts[2]
            systems += 1

    print(
        "verified returned-edge exchange kernels: "
        f"{systems} matching transitions, "
        f"{leaving_edges} leaving edges, "
        f"{recreated_credits} recreated triple credits, and "
        f"{kernel_entries} nonzero transported class entries"
    )


if __name__ == "__main__":
    main()
