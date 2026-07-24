#!/usr/bin/env python3
"""Verify the GC4b pair-concentration/star dichotomy."""

from __future__ import annotations

from itertools import combinations


def maximal_matching(
    edges: tuple[tuple[int, int], ...]
) -> list[tuple[int, int]]:
    remaining = set(edges)
    chosen: list[tuple[int, int]] = []
    while remaining:
        edge = min(remaining)
        chosen.append(edge)
        endpoints = set(edge)
        remaining = {
            other for other in remaining if endpoints.isdisjoint(other)
        }
    return chosen


def verify(max_vertices: int = 6) -> None:
    for size in range(max_vertices + 1):
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
            delta = max(degrees, default=0)
            matching = maximal_matching(edges)
            flattened = [vertex for edge in matching for vertex in edge]
            assert len(flattened) == len(set(flattened))
            if edges:
                assert len(matching) * (2 * delta - 1) >= len(edges)


def main() -> None:
    verify()
    print("GC anchor-link dichotomy: verified through six link vertices")


if __name__ == "__main__":
    main()
