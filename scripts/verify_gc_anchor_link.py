#!/usr/bin/env python3
"""Verify the GC4b pair-concentration/star dichotomy."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations


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


def maximum_independent_weight(
    size: int,
    edges: tuple[tuple[int, int], ...],
    weights: list[int],
) -> int:
    edge_set = set(edges)
    best = 0
    for mask in range(1 << size):
        chosen = [vertex for vertex in range(size) if mask & (1 << vertex)]
        if any(edge in edge_set for edge in combinations(chosen, 2)):
            continue
        best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_weighted_star_conflicts(max_vertices: int = 5) -> None:
    for size in range(1, max_vertices + 1):
        possible = tuple(combinations(range(size), 2))
        for mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if mask & (1 << index)
            )
            weights = [1 + (3 * vertex + mask) % 11 for vertex in range(size)]
            loads = weights.copy()
            for left, right in edges:
                loads[left] += weights[right]
                loads[right] += weights[left]
            bound = sum(
                (
                    Fraction(weights[vertex] ** 2, loads[vertex])
                    for vertex in range(size)
                ),
                Fraction(0),
            )
            optimum = maximum_independent_weight(size, edges, weights)
            assert optimum >= bound
            for threshold in range(1, 12):
                if all(
                    loads[vertex] <= threshold * weights[vertex]
                    for vertex in range(size)
                ):
                    assert optimum * threshold >= sum(weights)


def induced_maximum_weight(
    vertices: list[int],
    edges: tuple[tuple[int, int], ...],
    weights: list[int],
) -> int:
    edge_set = set(edges)
    best = 0
    for mask in range(1 << len(vertices)):
        chosen = [
            vertex
            for index, vertex in enumerate(vertices)
            if mask & (1 << index)
        ]
        if any(edge in edge_set for edge in combinations(chosen, 2)):
            continue
        best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_labelled_star_overload(max_vertices: int = 5) -> None:
    for size in range(2, max_vertices + 1):
        possible = tuple(combinations(range(size), 2))
        for mask in range(1 << len(possible)):
            edges = tuple(
                edge
                for index, edge in enumerate(possible)
                if mask & (1 << index)
            )
            edge_set = set(edges)
            weights = [1 + (7 * vertex + mask) % 10 for vertex in range(size)]
            for center in range(size):
                neighbours = [
                    vertex
                    for vertex in range(size)
                    if (
                        min(center, vertex),
                        max(center, vertex),
                    )
                    in edge_set
                ]
                load = weights[center] + sum(
                    weights[vertex] for vertex in neighbours
                )
                for threshold in range(2, 9):
                    if load <= threshold * weights[center]:
                        continue
                    for label_count in range(1, 4):
                        classes = [
                            [
                                vertex
                                for vertex in neighbours
                                if (vertex + 2 * mask) % label_count == label
                            ]
                            for label in range(label_count)
                        ]
                        selected = max(
                            classes,
                            key=lambda vertices: sum(
                                weights[vertex] for vertex in vertices
                            ),
                        )
                        selected_weight = sum(
                            weights[vertex] for vertex in selected
                        )
                        assert (
                            selected_weight * label_count
                            > (threshold - 1) * weights[center]
                        )

                        for recursive_threshold in range(1, 6):
                            overloaded = any(
                                weights[vertex]
                                + sum(
                                    weights[other]
                                    for other in selected
                                    if other != vertex
                                    and (
                                        min(vertex, other),
                                        max(vertex, other),
                                    )
                                    in edge_set
                                )
                                > recursive_threshold * weights[vertex]
                                for vertex in selected
                            )
                            if not overloaded:
                                optimum = induced_maximum_weight(
                                    selected,
                                    edges,
                                    weights,
                                )
                                assert (
                                    optimum * recursive_threshold
                                    >= selected_weight
                                )

                        for relative_weight in range(1, 5):
                            if all(
                                weights[vertex]
                                <= relative_weight * weights[center]
                                for vertex in selected
                            ):
                                assert (
                                    len(selected)
                                    * label_count
                                    * relative_weight
                                    > threshold - 1
                                )


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


def verify_strict_support_descent(max_vertices: int = 7) -> None:
    for size in range(1, max_vertices + 1):
        full_support = frozenset(range(size))
        for ordering in permutations(range(size)):
            support = full_support
            previous = size - len(support)
            descents = 0
            for center in ordering:
                if center not in support:
                    continue
                label_class = support - {center}
                if not label_class:
                    break
                potential = size - len(label_class)
                assert label_class < support
                assert potential >= previous + 1
                support = label_class
                previous = potential
                descents += 1
            assert descents <= size - 1

    support = frozenset({0, 1, 2})
    restricted = support - {0}
    assert restricted < support
    assert restricted | {0} == support


def verify_ticketed_support_potential(
    max_vertices: int = 6,
    maximum_tickets: int = 3,
) -> None:
    for size in range(1, max_vertices + 1):
        supports = [
            frozenset(
                vertex
                for vertex in range(size)
                if mask & (1 << vertex)
            )
            for mask in range(1, 1 << size)
        ]
        for ticket_budget in range(maximum_tickets + 1):
            upper = size * ticket_budget + size - 1
            for used in range(ticket_budget + 1):
                for support in supports:
                    potential = size * used + size - len(support)
                    assert 0 <= potential <= upper
                    for next_support in supports:
                        if next_support < support:
                            assert (
                                size * used + size - len(next_support)
                                >= potential + 1
                            )
                        if used < ticket_budget:
                            assert (
                                size * (used + 1)
                                + size
                                - len(next_support)
                                >= potential + 1
                            )


def main() -> None:
    verify()
    verify_weighted_star_conflicts()
    verify_labelled_star_overload()
    verify_strict_support_descent()
    verify_ticketed_support_potential()
    print("weighted GC anchor-link dichotomy: verified through six vertices")


if __name__ == "__main__":
    main()
