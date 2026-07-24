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

            colours = greedy_edge_colouring(edges)
            assert len(colours) <= max(0, 2 * delta - 1)
            assert sorted(edge for colour in colours for edge in colour) == list(
                edges
            )
            assert all(
                len({vertex for edge in colour for vertex in edge})
                == 2 * len(colour)
                for colour in colours
            )

            weights = {
                edge: 1 + (5 * index + 2 * mask) % 13
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
                assert heaviest * (2 * delta - 1) >= total_weight


def main() -> None:
    verify()
    print("weighted GC anchor-link dichotomy: verified through six vertices")


if __name__ == "__main__":
    main()
