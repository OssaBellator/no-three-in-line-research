#!/usr/bin/env python3
"""Finite checks for GC2c--GC2f."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations
from math import gcd

Point = tuple[int, int]
Edge = tuple[int, int]


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    r1, c1 = a
    r2, c2 = b
    A = c2 - c1
    B = r1 - r2
    C = A * r1 + B * c1
    common = gcd(gcd(abs(A), abs(B)), abs(C))
    if common:
        A //= common
        B //= common
        C //= common
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def on_line(point: Point, line: tuple[int, int, int]) -> bool:
    r, c = point
    A, B, C = line
    return A * r + B * c == C


def verify_role_injectivity() -> tuple[int, int]:
    systems = 0
    line_checks = 0
    for order in range(2, 7):
        grid = tuple((row, column) for row in range(order) for column in range(order))
        lines = {
            line_key(a, b)
            for a, b in combinations(grid, 2)
            if line_key(a, b)[0] != 0 and line_key(a, b)[1] != 0
        }
        for permutation in permutations(range(order)):
            layer = tuple((row, permutation[row]) for row in range(order))
            for target_index, target in enumerate(layer):
                partners = tuple(point for index, point in enumerate(layer) if index != target_index)
                for role in ("x", "y"):
                    cells = {
                        partner: (
                            (target[0], partner[1])
                            if role == "x"
                            else (partner[0], target[1])
                        )
                        for partner in partners
                    }
                    assert len(set(cells.values())) == len(partners)
                    for line in lines:
                        witnesses = [
                            partner for partner, cell in cells.items() if on_line(cell, line)
                        ]
                        assert len(witnesses) <= 1
                        line_checks += 1
                    systems += 1
    return systems, line_checks


def maximum_weight_matching(
    vertex_count: int,
    weighted_edges: dict[Edge, int],
) -> int:
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for (u, v), weight in weighted_edges.items():
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))

    @lru_cache(maxsize=None)
    def solve(mask: int) -> int:
        if mask == 0:
            return 0
        least_bit = mask & -mask
        vertex = least_bit.bit_length() - 1
        remaining = mask & ~least_bit
        best = solve(remaining)
        for neighbour, weight in adjacency[vertex]:
            neighbour_bit = 1 << neighbour
            if remaining & neighbour_bit:
                best = max(best, weight + solve(remaining & ~neighbour_bit))
        return best

    return solve((1 << vertex_count) - 1)


def verify_graph_router() -> tuple[int, int]:
    graph_checks = 0
    weighted_checks = 0
    for vertex_count in range(2, 7):
        all_edges = tuple(combinations(range(vertex_count), 2))
        for graph_mask in range(1 << len(all_edges)):
            edges = tuple(
                edge for index, edge in enumerate(all_edges) if graph_mask >> index & 1
            )
            if not edges:
                continue
            degrees = [0] * vertex_count
            for u, v in edges:
                degrees[u] += 1
                degrees[v] += 1
            maximum_degree = max(degrees)
            unweighted = {edge: 1 for edge in edges}
            matching_size = maximum_weight_matching(vertex_count, unweighted)

            for delta in range(1, vertex_count):
                if maximum_degree > delta:
                    assert any(degree > delta for degree in degrees)
                else:
                    assert matching_size * (2 * delta - 1) >= len(edges)
                graph_checks += 1

            weight_patterns = (
                {edge: 1 for edge in edges},
                {edge: 1 + (index % 3) for index, edge in enumerate(edges)},
                {edge: 1 + ((edge[0] + 2 * edge[1]) % 4) for edge in edges},
            )
            delta = max(1, maximum_degree)
            for weights in weight_patterns:
                total_weight = sum(weights.values())
                matching_weight = maximum_weight_matching(vertex_count, weights)
                assert matching_weight * (2 * delta - 1) >= total_weight
                weighted_checks += 1
    return graph_checks, weighted_checks


def main() -> None:
    systems, line_checks = verify_role_injectivity()
    graph_checks, weighted_checks = verify_graph_router()
    print("GC2c--GC2f line-blocker router audit passed")
    print(f"  fixed-role systems: {systems:,}")
    print(f"  fixed-role line checks: {line_checks:,}")
    print(f"  star-or-matching graph checks: {graph_checks:,}")
    print(f"  weighted matching checks: {weighted_checks:,}")


if __name__ == "__main__":
    main()
