#!/usr/bin/env python3
"""Exhaustive finite checks for CMR472--CMR476."""

from __future__ import annotations

from collections import defaultdict, deque
from itertools import product
from math import ceil


Arc = tuple[int, int]
Witness = tuple[int, int, frozenset[int], tuple[int, ...]]


def arcs_from_mask(side: int, mask: int) -> set[Arc]:
    positions = [
        (source, target)
        for source in range(side)
        for target in range(side)
        if source != target
    ]
    return {
        arc
        for index, arc in enumerate(positions)
        if mask & (1 << index)
    }


def reachability(
    side: int,
    arcs: set[Arc],
) -> tuple[list[set[int]], list[list[bool]]]:
    adjacency = [set() for _ in range(side)]
    for source, target in arcs:
        adjacency[source].add(target)

    reach = [[False] * side for _ in range(side)]
    for start in range(side):
        stack = [start]
        reach[start][start] = True
        while stack:
            source = stack.pop()
            for target in adjacency[source]:
                if not reach[start][target]:
                    reach[start][target] = True
                    stack.append(target)
    return adjacency, reach


def shortest_path(
    adjacency: list[set[int]],
    start: int,
    target: int,
) -> list[int] | None:
    queue: deque[int] = deque([start])
    previous: dict[int, int | None] = {start: None}

    while queue:
        source = queue.popleft()
        if source == target:
            break
        for vertex in sorted(adjacency[source]):
            if vertex not in previous:
                previous[vertex] = source
                queue.append(vertex)

    if target not in previous:
        return None

    path: list[int] = []
    current: int | None = target
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    return path


def mixed_cycle_exists(
    side: int,
    arcs: set[Arc],
    colours: tuple[int, ...],
    removed: frozenset[int] = frozenset(),
) -> bool:
    kept = {
        (source, target)
        for source, target in arcs
        if source not in removed and target not in removed
    }
    _adjacency, reach = reachability(side, kept)
    return any(
        colours[source] != colours[target] and reach[target][source]
        for source, target in kept
    )


def canonical_witnesses(
    side: int,
    arcs: set[Arc],
    colours: tuple[int, ...],
) -> tuple[list[Arc], list[Witness]]:
    adjacency, reach = reachability(side, arcs)
    boundary: list[Arc] = []
    witnesses: list[Witness] = []

    for source, target in sorted(arcs):
        if colours[source] == colours[target] or not reach[target][source]:
            continue
        path = shortest_path(adjacency, target, source)
        assert path is not None
        sequence = tuple([source] + path)
        vertices = frozenset(sequence[:-1])
        boundary.append((source, target))
        witnesses.append((source, target, vertices, sequence))

    return boundary, witnesses


def greedy_disjoint(witnesses: list[Witness]) -> list[int]:
    remaining = list(range(len(witnesses)))
    selected: list[int] = []

    while remaining:
        index = remaining[0]
        vertices = witnesses[index][2]
        selected.append(index)
        remaining = [
            other
            for other in remaining[1:]
            if vertices.isdisjoint(witnesses[other][2])
        ]
    return selected


def verify_instance(
    side: int,
    arcs: set[Arc],
    colours: tuple[int, ...],
) -> None:
    boundary, witnesses = canonical_witnesses(side, arcs, colours)

    # CMR472: mixed cycles are equivalent to cyclic colour-boundary arcs.
    assert bool(boundary) == mixed_cycle_exists(side, arcs, colours)

    # CMR473: every canonical witness is a simple short mixed cycle.
    for source, target, vertices, sequence in witnesses:
        assert colours[source] != colours[target]
        assert len(vertices) <= side
        assert sequence[0] == sequence[-1] == source
        assert len(vertices) == len(sequence) - 1
        for first, second in zip(sequence, sequence[1:]):
            assert (first, second) in arcs

    # CMR476: deleting tails of cyclic boundary arcs kills all mixed cycles.
    tails = frozenset(source for source, _target in boundary)
    assert len(tails) <= len(boundary)
    assert not mixed_cycle_exists(side, arcs, colours, tails)

    count = len(boundary)
    if count == 0:
        return

    multiplicity: defaultdict[int, int] = defaultdict(int)
    for _source, _target, vertices, _sequence in witnesses:
        for vertex in vertices:
            multiplicity[vertex] += 1

    # CMR474--CMR475 for every nontrivial concentration threshold.
    for delta in range(2, count + 2):
        if max(multiplicity.values()) >= delta:
            continue

        selected = greedy_disjoint(witnesses)
        lower_bound = ceil(count / (side * (delta - 1)))
        assert len(selected) >= lower_bound

        # Simultaneously flip the selected contraction cycles relative to the
        # identity base matching.
        permutation = list(range(side))
        used_vertices: set[int] = set()
        for index in selected:
            sequence = witnesses[index][3]
            cycle_vertices = sequence[:-1]
            assert used_vertices.isdisjoint(cycle_vertices)
            used_vertices.update(cycle_vertices)
            for source, target in zip(sequence, sequence[1:]):
                permutation[source] = target

        assert sorted(permutation) == list(range(side))
        base_split = {
            index
            for index, colour in enumerate(colours)
            if colour == 1
        }
        new_split = {
            source
            for source in range(side)
            if colours[permutation[source]] == 1
        }
        assert len(base_split.symmetric_difference(new_split)) >= 2 * len(selected)


def verify_exhaustive() -> None:
    expected = {1: 2, 2: 16, 3: 512, 4: 65_536}
    observed: dict[int, int] = {}

    for side in range(1, 5):
        instances = 0
        for mask in range(1 << (side * (side - 1))):
            arcs = arcs_from_mask(side, mask)
            for colours in product((0, 1), repeat=side):
                verify_instance(side, arcs, colours)
                instances += 1
        observed[side] = instances

    assert observed == expected


def main() -> None:
    verify_exhaustive()
    print(
        "verified mixed-cycle endpoint: cyclic colour-boundary criterion, "
        "canonical short witnesses, packing versus vertex concentration, "
        "simultaneous flips, and sparse-tail deletion through side four"
    )


if __name__ == "__main__":
    main()
