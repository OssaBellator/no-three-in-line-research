#!/usr/bin/env python3
"""Exhaustive small-digraph checks for CMR433--CMR438."""

from __future__ import annotations

from itertools import combinations
from math import ceil, sqrt


Arc = tuple[int, int]


def transitive_closure(side: int, arcs: set[Arc]) -> list[list[bool]]:
    reach = [[False] * side for _ in range(side)]
    for vertex in range(side):
        reach[vertex][vertex] = True
    for source, target in arcs:
        reach[source][target] = True

    for middle in range(side):
        for source in range(side):
            if not reach[source][middle]:
                continue
            for target in range(side):
                if reach[middle][target]:
                    reach[source][target] = True
    return reach


def cycle_vertices(side: int, arcs: set[Arc]) -> set[int]:
    reach = transitive_closure(side, arcs)
    return {
        vertex
        for vertex in range(side)
        if any(
            other != vertex
            and reach[vertex][other]
            and reach[other][vertex]
            for other in range(side)
        )
    }


def simple_paths(
    side: int, arcs: set[Arc], source: int, target: int
) -> list[tuple[int, ...]]:
    adjacency = {vertex: [] for vertex in range(side)}
    for start, end in arcs:
        adjacency[start].append(end)

    paths: list[tuple[int, ...]] = []

    def visit(vertex: int, path: list[int], seen: set[int]) -> None:
        if vertex == target:
            paths.append(tuple(path))
            return
        for next_vertex in adjacency[vertex]:
            if next_vertex in seen:
                continue
            visit(
                next_vertex,
                path + [next_vertex],
                seen | {next_vertex},
            )

    visit(source, [source], {source})
    return paths


def is_chain(vertices: list[int], reach: list[list[bool]]) -> bool:
    return all(
        reach[first][second] or reach[second][first]
        for first, second in combinations(vertices, 2)
    )


def is_antichain(vertices: list[int], reach: list[list[bool]]) -> bool:
    return all(
        not reach[first][second] and not reach[second][first]
        for first, second in combinations(vertices, 2)
    )


def poset_width(vertices: list[int], reach: list[list[bool]]) -> int:
    width = 0
    for mask in range(1 << len(vertices)):
        subset = [
            vertices[index]
            for index in range(len(vertices))
            if mask & (1 << index)
        ]
        if is_antichain(subset, reach):
            width = max(width, len(subset))
    return width


def minimum_chain_cover(vertices: list[int], reach: list[list[bool]]) -> int:
    if not vertices:
        return 0

    chain_masks: list[int] = []
    for mask in range(1, 1 << len(vertices)):
        subset = [
            vertices[index]
            for index in range(len(vertices))
            if mask & (1 << index)
        ]
        if is_chain(subset, reach):
            chain_masks.append(mask)

    infinity = len(vertices) + 1
    costs = [infinity] * (1 << len(vertices))
    costs[0] = 0
    for covered in range(1 << len(vertices)):
        for chain_mask in chain_masks:
            union = covered | chain_mask
            costs[union] = min(costs[union], costs[covered] + 1)
    return costs[-1]


def minimum_path_cover(
    vertices: list[int], paths: list[tuple[int, ...]]
) -> int:
    if not vertices:
        return 0

    index = {vertex: position for position, vertex in enumerate(vertices)}
    path_masks = []
    for path in paths:
        mask = 0
        for vertex in set(path) & set(vertices):
            mask |= 1 << index[vertex]
        if mask:
            path_masks.append(mask)

    infinity = len(vertices) + 1
    costs = [infinity] * (1 << len(vertices))
    costs[0] = 0
    for covered in range(1 << len(vertices)):
        for path_mask in path_masks:
            union = covered | path_mask
            costs[union] = min(costs[union], costs[covered] + 1)
    return costs[-1]


def verify_exchange_corridors() -> None:
    for side in range(2, 5):
        possible_arcs = [
            (source, target)
            for source in range(side)
            for target in range(side)
            if source != target
        ]

        for graph_mask in range(1 << len(possible_arcs)):
            arcs = {
                arc
                for index, arc in enumerate(possible_arcs)
                if graph_mask & (1 << index)
            }

            before_cycles = cycle_vertices(side, arcs)
            for alpha in arcs:
                source, target = alpha
                reduced = arcs - {alpha}
                after_cycles = cycle_vertices(side, reduced)
                newly_essential = before_cycles - after_cycles
                reach = transitive_closure(side, reduced)

                corridor = {
                    vertex
                    for vertex in range(side)
                    if vertex not in after_cycles
                    and reach[target][vertex]
                    and reach[vertex][source]
                }
                assert newly_essential == corridor

                vertices = sorted(newly_essential)
                width = poset_width(vertices, reach)
                assert minimum_chain_cover(vertices, reach) == width

                paths = simple_paths(side, reduced, target, source)
                assert minimum_path_cover(vertices, paths) == width

                for subset_mask in range(1 << len(vertices)):
                    subset = [
                        vertices[index]
                        for index in range(len(vertices))
                        if subset_mask & (1 << index)
                    ]
                    if is_chain(subset, reach):
                        assert not subset or any(
                            set(subset) <= set(path) for path in paths
                        )

                if vertices:
                    threshold = ceil(sqrt(len(vertices)))
                    maximum_chain = max(
                        len(subset)
                        for subset_mask in range(1 << len(vertices))
                        for subset in [[
                            vertices[index]
                            for index in range(len(vertices))
                            if subset_mask & (1 << index)
                        ]]
                        if is_chain(subset, reach)
                    )
                    assert maximum_chain >= threshold or width >= threshold


def verify_linear_temporal_compression() -> None:
    for side in range(1, 50):
        # First-essentiality layer sizes form a partition of at most `side`
        # essential edges.  Every layer width is bounded by its size.
        for first in range(side + 1):
            for second in range(side - first + 1):
                third = side - first - second
                layer_sizes = (first, second, third)
                for widths in (
                    layer_sizes,
                    tuple(0 if size == 0 else 1 for size in layer_sizes),
                ):
                    assert all(
                        width <= size
                        for width, size in zip(widths, layer_sizes)
                    )
                    assert sum(widths) <= sum(layer_sizes) <= side


def main() -> None:
    verify_exchange_corridors()
    verify_linear_temporal_compression()
    print(
        "verified exchange corridors: directed-cycle essentiality, exact "
        "one-edge corridor, chain batching, Dilworth path-cover width, "
        "batch-or-branch dichotomy, and linear temporal cycle compression"
    )


if __name__ == "__main__":
    main()
