#!/usr/bin/env python3
"""Exhaustive finite checks for CMR477--CMR481."""

from __future__ import annotations

from collections import defaultdict, deque
from itertools import product
from math import ceil


Arc = tuple[int, int]


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


def adjacency(side: int, arcs: set[Arc]) -> list[set[int]]:
    result = [set() for _ in range(side)]
    for source, target in arcs:
        result[source].add(target)
    return result


def shortest_path(
    graph: list[set[int]],
    start: int,
    target: int,
) -> list[int] | None:
    queue: deque[int] = deque([start])
    previous: dict[int, int | None] = {start: None}

    while queue:
        source = queue.popleft()
        if source == target:
            break
        for vertex in sorted(graph[source]):
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


def all_simple_paths(
    side: int,
    arcs: set[Arc],
    start: int,
    target: int,
) -> list[tuple[int, ...]]:
    graph = adjacency(side, arcs)
    paths: list[tuple[int, ...]] = []

    def search(source: int, path: list[int], seen: set[int]) -> None:
        if source == target:
            paths.append(tuple(path))
            return
        for vertex in sorted(graph[source]):
            if vertex not in seen:
                search(vertex, path + [vertex], seen | {vertex})

    search(start, [start], {start})
    return paths


def path_edges(path: tuple[int, ...] | list[int]) -> frozenset[Arc]:
    return frozenset(zip(path, path[1:]))


def cyclic_boundary_witnesses(
    side: int,
    arcs: set[Arc],
    colours: tuple[int, ...],
) -> tuple[list[Arc], list[tuple[Arc, frozenset[Arc], frozenset[int]]]]:
    graph = adjacency(side, arcs)
    boundary: list[Arc] = []
    witnesses: list[tuple[Arc, frozenset[Arc], frozenset[int]]] = []

    for source, target in sorted(arcs):
        if colours[source] == colours[target]:
            continue
        path = shortest_path(graph, target, source)
        if path is None:
            continue
        cycle_sequence = [source] + path
        cycle_edges = path_edges(cycle_sequence)
        cycle_vertices = frozenset(cycle_sequence[:-1])
        boundary.append((source, target))
        witnesses.append(((source, target), cycle_edges, cycle_vertices))

    return boundary, witnesses


def unit_edge_flow_and_cut(
    side: int,
    arcs: set[Arc],
    start: int,
    target: int,
) -> tuple[int, frozenset[Arc]]:
    capacity: defaultdict[Arc, int] = defaultdict(int)
    neighbours = [set() for _ in range(side)]
    for source, vertex in arcs:
        capacity[(source, vertex)] = 1
        neighbours[source].add(vertex)
        neighbours[vertex].add(source)

    flow: defaultdict[Arc, int] = defaultdict(int)
    value = 0

    while True:
        queue: deque[int] = deque([start])
        previous: dict[int, int | None] = {start: None}
        while queue and target not in previous:
            source = queue.popleft()
            for vertex in sorted(neighbours[source]):
                residual = capacity[(source, vertex)] - flow[(source, vertex)]
                if residual > 0 and vertex not in previous:
                    previous[vertex] = source
                    queue.append(vertex)

        if target not in previous:
            break

        current = target
        while current != start:
            parent = previous[current]
            assert parent is not None
            flow[(parent, current)] += 1
            flow[(current, parent)] -= 1
            current = parent
        value += 1

    reachable = {start}
    stack = [start]
    while stack:
        source = stack.pop()
        for vertex in neighbours[source]:
            residual = capacity[(source, vertex)] - flow[(source, vertex)]
            if residual > 0 and vertex not in reachable:
                reachable.add(vertex)
                stack.append(vertex)

    cut = frozenset(
        (source, target_vertex)
        for source, target_vertex in arcs
        if source in reachable and target_vertex not in reachable
    )
    assert len(cut) == value
    return value, cut


def verify_instance(
    side: int,
    arcs: set[Arc],
    colours: tuple[int, ...],
) -> None:
    boundary, witnesses = cyclic_boundary_witnesses(side, arcs, colours)
    boundary_set = set(boundary)

    # CMR477: labelled vertex congestion produces a boundary arc supporting
    # many distinct underlying cycles.
    for vertex in range(side):
        labelled = [
            witness
            for witness in witnesses
            if vertex in witness[2]
        ]
        delta = len(labelled)
        if delta == 0:
            continue

        distinct_cycles = {cycle_edges for _arc, cycle_edges, _vertices in labelled}
        cycle_count = len(distinct_cycles)
        assert cycle_count >= ceil(delta / side)

        support = {arc: 0 for arc in boundary}
        for cycle_edges in distinct_cycles:
            boundary_edges = [arc for arc in cycle_edges if arc in boundary_set]
            assert len(boundary_edges) >= 2
            for arc in boundary_edges:
                support[arc] += 1

        maximum_support = max(support.values())
        assert maximum_support >= ceil(2 * cycle_count / len(boundary))
        assert maximum_support >= ceil(2 * delta / (side * len(boundary)))

    # CMR478--CMR480: cycle/path bijection, directed edge Menger, and cut
    # concentration for every cyclic colour-boundary arc.
    for arc in boundary:
        source, target = arc
        reduced = arcs - {arc}
        return_paths = all_simple_paths(side, reduced, target, source)
        assert return_paths

        cycle_edges = {
            frozenset({arc}) | path_edges(path)
            for path in return_paths
        }
        assert len(cycle_edges) == len(return_paths)
        for cycle in cycle_edges:
            assert arc in cycle
            assert any(colours[u] != colours[v] for u, v in cycle)

        flow_value, cut = unit_edge_flow_and_cut(
            side,
            reduced,
            target,
            source,
        )
        assert flow_value >= 1
        assert len(cut) == flow_value
        for path in return_paths:
            assert path_edges(path).intersection(cut)

        incidence: defaultdict[Arc, int] = defaultdict(int)
        for path in return_paths:
            edges = path_edges(path)
            for cut_edge in cut:
                if cut_edge in edges:
                    incidence[cut_edge] += 1
        assert max(incidence.values()) >= ceil(len(return_paths) / len(cut))

        # Every threshold q is covered by the same max-flow/min-cut witness.
        for threshold in range(1, flow_value + 3):
            if flow_value >= threshold:
                continue
            assert len(cut) < threshold
            assert max(incidence.values()) >= ceil(
                len(return_paths) / (threshold - 1)
            )


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
        "verified mixed-cycle concentration endpoint: vertex-to-boundary "
        "incidence, exact return-path bijection, directed edge Menger fan/cut, "
        "and second-edge concentration through side four"
    )


if __name__ == "__main__":
    main()
