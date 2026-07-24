#!/usr/bin/env python3
"""Verify AC3k--AC3l anchor-realized resource routing."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import ceil


Edge = tuple[int, int]


def greedy_edge_colours(
    edges: tuple[Edge, ...],
) -> tuple[list[list[int]], int]:
    endpoint_degrees: dict[int, int] = {}
    for left, right in edges:
        endpoint_degrees[left] = endpoint_degrees.get(left, 0) + 1
        endpoint_degrees[right] = endpoint_degrees.get(right, 0) + 1
    maximum_degree = max(endpoint_degrees.values(), default=0)

    colours: list[list[int]] = []
    for edge_index, edge in enumerate(edges):
        for colour in colours:
            if all(
                set(edge).isdisjoint(edges[other_index])
                for other_index in colour
            ):
                colour.append(edge_index)
                break
        else:
            colours.append([edge_index])
    return colours, maximum_degree


def greedy_vertex_colours(
    size: int,
    edges: tuple[Edge, ...],
) -> tuple[list[list[int]], int]:
    adjacency = [set() for _ in range(size)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    maximum_degree = max(map(len, adjacency), default=0)

    colours: list[list[int]] = []
    for vertex in range(size):
        for colour in colours:
            if all(other not in adjacency[vertex] for other in colour):
                colour.append(vertex)
                break
        else:
            colours.append([vertex])
    return colours, maximum_degree


def maximum_independent_weight(
    size: int,
    edges: tuple[Edge, ...],
    weights: list[int],
) -> int:
    edge_set = set(edges)
    best = 0
    for mask in range(1 << size):
        chosen = [
            vertex
            for vertex in range(size)
            if mask & (1 << vertex)
        ]
        if any(
            (left, right) in edge_set
            for left, right in combinations(chosen, 2)
        ):
            continue
        best = max(best, sum(weights[vertex] for vertex in chosen))
    return best


def verify_link_and_support_routing(
    maximum_endpoints: int = 6,
) -> None:
    checked = 0
    for endpoint_count in range(2, maximum_endpoints + 1):
        possible_edges = tuple(combinations(range(endpoint_count), 2))
        for mask in range(1, 1 << len(possible_edges)):
            link_edges = tuple(
                edge
                for index, edge in enumerate(possible_edges)
                if mask & (1 << index)
            )
            edge_colours, maximum_pair_codegree = greedy_edge_colours(
                link_edges
            )
            assert len(edge_colours) <= 2 * maximum_pair_codegree - 1
            checked += 1

            for threshold in range(
                maximum_pair_codegree,
                maximum_pair_codegree + 2,
            ):
                assert maximum_pair_codegree <= threshold
                largest_matching = max(edge_colours, key=len)
                minimum_matching_size = ceil(
                    len(link_edges) / (2 * threshold - 1)
                )
                assert len(largest_matching) >= minimum_matching_size

                matching_size = len(largest_matching)
                possible_conflicts = tuple(
                    combinations(range(matching_size), 2)
                )
                for conflict_mask in range(1 << len(possible_conflicts)):
                    conflicts = tuple(
                        edge
                        for index, edge in enumerate(possible_conflicts)
                        if conflict_mask & (1 << index)
                    )
                    support_colours, maximum_support_degree = (
                        greedy_vertex_colours(matching_size, conflicts)
                    )
                    assert (
                        len(support_colours)
                        <= maximum_support_degree + 1
                    )
                    largest_compatible = max(
                        support_colours,
                        key=len,
                    )
                    nested_bound = ceil(
                        minimum_matching_size
                        / (maximum_support_degree + 1)
                    )
                    assert len(largest_compatible) >= nested_bound
    assert checked


def verify_weighted_composition(
    maximum_endpoints: int = 5,
) -> None:
    for endpoint_count in range(2, maximum_endpoints + 1):
        possible_edges = tuple(combinations(range(endpoint_count), 2))
        for mask in range(1, 1 << len(possible_edges)):
            link_edges = tuple(
                edge
                for index, edge in enumerate(possible_edges)
                if mask & (1 << index)
            )
            edge_colours, maximum_pair_codegree = greedy_edge_colours(
                link_edges
            )
            weights = [
                1 + (7 * index + 3 * mask) % 11
                for index in range(len(link_edges))
            ]
            heaviest = max(
                edge_colours,
                key=lambda colour: sum(weights[index] for index in colour),
            )
            heaviest_weight = sum(weights[index] for index in heaviest)
            total_weight = sum(weights)
            assert (
                heaviest_weight * (2 * maximum_pair_codegree - 1)
                >= total_weight
            )

            matching_size = len(heaviest)
            matching_weights = [weights[index] for index in heaviest]
            possible_conflicts = tuple(
                combinations(range(matching_size), 2)
            )
            for conflict_mask in range(1 << len(possible_conflicts)):
                conflicts = tuple(
                    edge
                    for index, edge in enumerate(possible_conflicts)
                    if conflict_mask & (1 << index)
                )
                loads = matching_weights.copy()
                for left, right in conflicts:
                    loads[left] += matching_weights[right]
                    loads[right] += matching_weights[left]
                optimum = maximum_independent_weight(
                    matching_size,
                    conflicts,
                    matching_weights,
                )
                for threshold in range(1, 7):
                    overloaded = any(
                        loads[index] > threshold * matching_weights[index]
                        for index in range(matching_size)
                    )
                    if overloaded:
                        continue
                    assert optimum * threshold >= heaviest_weight
                    assert (
                        Fraction(optimum, 1)
                        >= Fraction(
                            total_weight,
                            (2 * maximum_pair_codegree - 1) * threshold,
                        )
                    )


def verify_capacity_loss(maximum_tokens: int = 24) -> None:
    for token_count in range(1, maximum_tokens + 1):
        for capacity in range(1, 8):
            resource_count = ceil(token_count / capacity)
            assert resource_count * capacity >= token_count
            assert (resource_count - 1) * capacity < token_count


def main() -> None:
    verify_link_and_support_routing()
    verify_weighted_composition()
    verify_capacity_loss()
    print("AC anchor-realized resource routing: verified")


if __name__ == "__main__":
    main()
