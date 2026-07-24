#!/usr/bin/env python3
"""Verify the AC1c anchor-link matching bound."""

from __future__ import annotations

from itertools import combinations


def greedy_matching(
    size: int, edges: tuple[tuple[int, int], ...]
) -> list[tuple[int, int]]:
    remaining = set(edges)
    matching: list[tuple[int, int]] = []
    while remaining:
        edge = min(remaining)
        matching.append(edge)
        endpoints = set(edge)
        remaining = {
            other for other in remaining if endpoints.isdisjoint(other)
        }
    return matching


def verify(max_size: int = 6) -> None:
    for size in range(max_size + 1):
        possible = tuple(combinations(range(size), 2))
        for mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if mask & (1 << index)
            )
            degrees = [
                sum(vertex in edge for edge in edges) for vertex in range(size)
            ]
            maximum_degree = max(degrees, default=0)
            matching = greedy_matching(size, edges)
            used = [vertex for edge in matching for vertex in edge]
            assert len(used) == len(set(used))
            if edges:
                assert len(matching) * (2 * maximum_degree - 1) >= len(edges)


def main() -> None:
    verify()
    print("anchor-link extraction: verified through six link vertices")


if __name__ == "__main__":
    main()
