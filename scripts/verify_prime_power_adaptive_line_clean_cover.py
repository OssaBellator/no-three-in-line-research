#!/usr/bin/env python3
"""Finite checks for CMR507--CMR511."""

from __future__ import annotations

from itertools import combinations, permutations


Edge = tuple[int, int]
Vertex = tuple[str, int]


def all_edges(side: int) -> list[Edge]:
    return [
        (left, right)
        for left in range(side)
        for right in range(side)
    ]


def is_matching(edges: set[Edge] | tuple[Edge, ...]) -> bool:
    left = {edge[0] for edge in edges}
    right = {edge[1] for edge in edges}
    return len(left) == len(edges) and len(right) == len(edges)


def maximum_matching(edges: set[Edge]) -> set[Edge]:
    edge_list = list(edges)
    best: set[Edge] = set()
    for size in range(len(edge_list) + 1):
        for choice in combinations(edge_list, size):
            if is_matching(choice) and size > len(best):
                best = set(choice)
    return best


def minimum_vertex_cover(side: int, edges: set[Edge]) -> set[Vertex]:
    vertices = [
        *(("L", index) for index in range(side)),
        *(("R", index) for index in range(side)),
    ]
    for size in range(len(vertices) + 1):
        for choice in combinations(vertices, size):
            cover = set(choice)
            if all(
                ("L", left) in cover or ("R", right) in cover
                for left, right in edges
            ):
                return cover
    raise AssertionError("finite bipartite graph has no vertex cover")


def extend_partial_matching(side: int, partial: set[Edge]) -> set[Edge]:
    for vector in permutations(range(side)):
        state = {(left, vector[left]) for left in range(side)}
        if partial <= state:
            return state
    raise AssertionError("partial matching in a complete balanced host did not extend")


def partial_matchings(side: int) -> list[set[Edge]]:
    edges = all_edges(side)
    result: list[set[Edge]] = []
    for size in range(side + 1):
        for choice in combinations(edges, size):
            if is_matching(choice):
                result.append(set(choice))
    return result


def unavailable_masks(side: int) -> list[int] | range:
    edge_count = side * side
    if side <= 3:
        return range(1 << edge_count)
    edges = all_edges(side)
    return [
        0,
        (1 << edge_count) - 1,
        *[
            sum(
                1 << index
                for index, (left, right) in enumerate(edges)
                if (left + 2 * right + residue) % side == 0
            )
            for residue in range(side)
        ],
    ]


def verify_instance(side: int, trace: set[Edge], unavailable: set[Edge]) -> None:
    edges = set(all_edges(side))
    trace_left = {left for left, _right in trace}
    trace_right = {right for _left, right in trace}

    compatible_unavailable = {
        edge
        for edge in unavailable
        if edge[0] not in trace_left and edge[1] not in trace_right
    }
    absorbed = maximum_matching(compatible_unavailable)
    forbidden = extend_partial_matching(side, trace | absorbed)

    # CMR507: no unavailable extension edge remains outside the prescribed
    # unavailable trace edges and the maximum absorbed matching.
    assert forbidden & unavailable == (trace & unavailable) | absorbed

    cover = minimum_vertex_cover(side, compatible_unavailable)
    assert len(cover) == len(absorbed)

    remaining = (edges - forbidden) & unavailable
    full_cover = {
        *(("L", left) for left in trace_left),
        *(("R", right) for right in trace_right),
        *cover,
    }
    assert len(full_cover) <= 2 * len(trace) + len(absorbed)
    assert all(
        ("L", left) in full_cover or ("R", right) in full_cover
        for left, right in remaining
    )

    if remaining:
        degree = {vertex: 0 for vertex in full_cover}
        for left, right in remaining:
            if ("L", left) in degree:
                degree[("L", left)] += 1
            if ("R", right) in degree:
                degree[("R", right)] += 1
        assert max(degree.values()) * len(full_cover) >= len(remaining)

        for threshold in range(1, side + 2):
            if len(absorbed) < threshold:
                bound = 2 * len(trace) + threshold - 1
                assert len(full_cover) <= bound
                if bound > 0:
                    assert max(degree.values()) * bound >= len(remaining)


def verify_finite_hosts() -> int:
    checked = 0
    for side in range(1, 5):
        edges = all_edges(side)
        for trace in partial_matchings(side):
            for mask in unavailable_masks(side):
                unavailable = {
                    edge
                    for index, edge in enumerate(edges)
                    if mask & (1 << index)
                }
                verify_instance(side, trace, unavailable)
                checked += 1
    return checked


def main() -> None:
    checked = verify_finite_hosts()
    print(
        f"verified CMR507--CMR511 on {checked} finite instances: maximum "
        "unavailable matching absorption, exact extension identity, Konig cover, "
        "heavy row/column concentration, and threshold arithmetic"
    )


if __name__ == "__main__":
    main()
