#!/usr/bin/env python3
"""Exhaustive checks for CMR467--CMR471."""

from __future__ import annotations

from itertools import permutations, product

Edge = tuple[int, int]


def sccs(side: int, arcs: set[Edge]) -> list[list[int]]:
    adjacency = [[] for _ in range(side)]
    reverse = [[] for _ in range(side)]
    for source, target in arcs:
        adjacency[source].append(target)
        reverse[target].append(source)

    seen: set[int] = set()
    order: list[int] = []

    def visit(vertex: int) -> None:
        seen.add(vertex)
        for target in adjacency[vertex]:
            if target not in seen:
                visit(target)
        order.append(vertex)

    for vertex in range(side):
        if vertex not in seen:
            visit(vertex)

    assigned: set[int] = set()
    groups: list[list[int]] = []

    def collect(vertex: int, group: list[int]) -> None:
        assigned.add(vertex)
        group.append(vertex)
        for source in reverse[vertex]:
            if source not in assigned:
                collect(source, group)

    for vertex in reversed(order):
        if vertex not in assigned:
            group: list[int] = []
            collect(vertex, group)
            groups.append(group)
    return groups


def cycle_colour_change(
    base: tuple[int, ...],
    other: tuple[int, ...],
    colour: tuple[int, ...],
) -> tuple[bool, bool]:
    inverse = {right: left for left, right in enumerate(base)}
    successor = tuple(inverse[other[left]] for left in range(len(base)))
    seen: set[int] = set()
    mixed = False

    for start in range(len(base)):
        if start in seen or successor[start] == start:
            seen.add(start)
            continue
        cycle: list[int] = []
        vertex = start
        while vertex not in seen:
            seen.add(vertex)
            cycle.append(vertex)
            vertex = successor[vertex]
        values = {colour[vertex] for vertex in cycle}
        mixed = mixed or len(values) > 1

    source_base = {
        left for left in range(len(base)) if colour[left] == 1
    }
    source_other = {
        left
        for left in range(len(base))
        if colour[inverse[other[left]]] == 1
    }
    return mixed, source_base != source_other


def verify_host(side: int, host_mask: int, colour: tuple[int, ...]) -> bool:
    universe = [
        (left, right)
        for left in range(side)
        for right in range(side)
    ]
    host = {
        edge
        for index, edge in enumerate(universe)
        if host_mask & (1 << index)
    }
    states = [
        state
        for state in permutations(range(side))
        if all((left, state[left]) in host for left in range(side))
    ]
    if not states:
        return False

    base = min(states)
    inverse = {right: left for left, right in enumerate(base)}

    # Column-polarized cost and constant matching cost.
    cost = {(left, right): colour[inverse[right]] for left, right in host}
    expected_cost = sum(colour)
    for state in states:
        assert sum(cost[(left, state[left])] for left in range(side)) == expected_cost

    marked_right = {
        base[index] for index in range(side) if colour[index] == 1
    }
    source_splits: dict[frozenset[int], int] = {}
    for state in states:
        source_set = frozenset(
            left for left in range(side) if state[left] in marked_right
        )
        source_splits[source_set] = source_splits.get(source_set, 0) + 1

    # Exact source-split product count.
    for source_set, count in source_splits.items():
        marked_sources = sorted(source_set)
        unmarked_sources = sorted(set(range(side)) - set(source_set))
        marked_targets = sorted(marked_right)
        unmarked_targets = sorted(set(base) - marked_right)

        marked_count = sum(
            all((source, target) in host for source, target in zip(marked_sources, order))
            for order in permutations(marked_targets)
        )
        unmarked_count = sum(
            all((source, target) in host for source, target in zip(unmarked_sources, order))
            for order in permutations(unmarked_targets)
        )
        assert count == marked_count * unmarked_count

    arcs = {
        (left, inverse[right])
        for left, right in host
        if right != base[left]
    }

    has_mixed_cycle = False
    split_changes = False
    for state in states:
        mixed, changed = cycle_colour_change(base, state, colour)
        assert mixed == changed
        has_mixed_cycle = has_mixed_cycle or mixed
        split_changes = split_changes or changed

    assert has_mixed_cycle == (len(source_splits) > 1)
    assert split_changes == (len(source_splits) > 1)

    mixed_component = any(
        len({colour[vertex] for vertex in group}) > 1
        for group in sccs(side, arcs)
    )
    assert mixed_component == has_mixed_cycle

    if not mixed_component:
        assert len(source_splits) == 1
        only_count = next(iter(source_splits.values()))
        assert only_count == len(states)

    return True


def main() -> None:
    checked: dict[int, int] = {}
    for side in (1, 2, 3):
        count = 0
        for host_mask in range(1 << (side * side)):
            for colour in product((0, 1), repeat=side):
                if verify_host(side, host_mask, colour):
                    count += 1
        checked[side] = count

    assert checked == {1: 2, 2: 28, 3: 1976}
    print(
        "verified same-level colour split: right-endpoint polarization, "
        "exact source-set products, mixed-cycle equivalence, and SCC "
        "factorization"
    )


if __name__ == "__main__":
    main()
