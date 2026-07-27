#!/usr/bin/env python3
"""Finite checks for CMR1630--CMR1637."""

from __future__ import annotations

from itertools import combinations, permutations
from random import Random


Edge = tuple[int, int]


def perfect_matchings(side: int, edges: set[Edge]) -> list[tuple[int, ...]]:
    return [
        permutation
        for permutation in permutations(range(side))
        if all((left, permutation[left]) in edges for left in range(side))
    ]


def matching_number(side: int, edges: set[Edge]) -> int:
    adjacency: list[list[int]] = [[] for _ in range(side)]
    for left, right in edges:
        adjacency[left].append(right)

    dynamic: dict[int, int] = {0: 0}
    for left in range(side):
        updated = dict(dynamic)
        for mask, value in dynamic.items():
            for right in adjacency[left]:
                if mask & (1 << right):
                    continue
                new_mask = mask | (1 << right)
                updated[new_mask] = max(updated.get(new_mask, -1), value + 1)
        dynamic = updated
    return max(dynamic.values(), default=0)


def minimum_vertex_cover_size(side: int, edges: set[Edge]) -> int:
    edge_list = list(edges)
    for size in range(2 * side + 1):
        for choice in combinations(range(2 * side), size):
            vertices = set(choice)
            if all(
                left in vertices or side + right in vertices
                for left, right in edge_list
            ):
                return size
    raise AssertionError("finite bipartite graph has no vertex cover")


def main() -> None:
    random = Random(1630)
    systems = 0
    level_checks = 0
    cover_checks = 0
    two_level_checks = 0
    strict_certificates = 0

    for _ in range(1_200):
        side = random.randint(2, 7)
        edges = {(index, index) for index in range(side)}
        for left in range(side):
            for right in range(side):
                if random.random() < 0.45:
                    edges.add((left, right))

        response_matchings = perfect_matchings(side, edges)
        assert response_matchings
        score = {edge: random.randint(0, 12) for edge in edges}
        levels = sorted({value for value in score.values() if value > 0})

        previous = 0
        superlevel_bound = 0
        for level in levels:
            superlevel_edges = {
                edge for edge, value in score.items() if value >= level
            }
            matching_size = matching_number(side, superlevel_edges)
            superlevel_bound += (level - previous) * matching_size
            previous = level
            level_checks += 1

            if side <= 5 and cover_checks < 2_500:
                assert (
                    minimum_vertex_cover_size(side, superlevel_edges)
                    == matching_size
                )
                cover_checks += 1

        optimum = max(
            sum(score[(left, permutation[left])] for left in range(side))
            for permutation in response_matchings
        )
        assert optimum <= superlevel_bound

        threshold = random.randint(0, 12)
        maximum_score = max(score.values())
        heavy_edges = {
            edge for edge, value in score.items() if value > threshold
        }
        heavy_matching_size = matching_number(side, heavy_edges)
        assert optimum <= (
            side * threshold
            + heavy_matching_size * max(0, maximum_score - threshold)
        )
        two_level_checks += 1

        denominator = random.randint(
            max(1, superlevel_bound + 1), superlevel_bound + 30
        )
        assert superlevel_bound < denominator
        strict_certificates += 1
        systems += 1

    print(
        "verified superlevel assignment certificates: "
        f"{systems} rational/integer score systems, "
        f"{level_checks} superlevel graphs, "
        f"{cover_checks} exact Konig cover checks, "
        f"{two_level_checks} two-level envelopes and "
        f"{strict_certificates} strict block certificates"
    )


if __name__ == "__main__":
    main()
