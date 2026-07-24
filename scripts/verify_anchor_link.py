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


def greedy_edge_colouring(
    edges: tuple[tuple[int, int], ...]
) -> list[list[tuple[int, int]]]:
    colours: list[list[tuple[int, int]]] = []
    for edge in edges:
        endpoints = set(edge)
        for colour in colours:
            if all(endpoints.isdisjoint(other) for other in colour):
                colour.append(edge)
                break
        else:
            colours.append([edge])
    return colours


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

            colours = greedy_edge_colouring(edges)
            assert len(colours) <= max(0, 2 * maximum_degree - 1)
            assert sorted(edge for colour in colours for edge in colour) == list(
                edges
            )
            assert all(
                len({vertex for edge in colour for vertex in edge})
                == 2 * len(colour)
                for colour in colours
            )

            weights = {
                edge: 1 + (7 * index + 3 * mask) % 11
                for index, edge in enumerate(edges)
            }
            total_weight = sum(weights.values())
            heaviest = max(
                (
                    sum(weights[edge] for edge in colour)
                    for colour in colours
                ),
                default=0,
            )
            if edges:
                assert heaviest * (2 * maximum_degree - 1) >= total_weight


def main() -> None:
    verify()
    print("weighted anchor-link extraction: verified through six link vertices")


if __name__ == "__main__":
    main()
