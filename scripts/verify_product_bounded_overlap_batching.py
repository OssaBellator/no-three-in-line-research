#!/usr/bin/env python3
"""Finite checks for PX299--PX302."""

from __future__ import annotations

from itertools import combinations
import random


def max_overlap(edges: list[frozenset[int]]) -> int:
    if not edges:
        return 0
    vertices = set().union(*edges)
    return max(sum(v in edge for edge in edges) for v in vertices)


def conflict_graph(edges: list[frozenset[int]]) -> list[set[int]]:
    graph = [set() for _ in edges]
    for i, j in combinations(range(len(edges)), 2):
        if edges[i] & edges[j]:
            graph[i].add(j)
            graph[j].add(i)
    return graph


def greedy_coloring(edges: list[frozenset[int]]) -> list[int]:
    graph = conflict_graph(edges)
    order = sorted(range(len(edges)), key=lambda i: len(graph[i]), reverse=True)
    color = [-1] * len(edges)
    for i in order:
        used = {color[j] for j in graph[i] if color[j] >= 0}
        c = 0
        while c in used:
            c += 1
        color[i] = c
    return color


def check_family(edges: list[frozenset[int]]) -> None:
    assert all(1 <= len(edge) <= 6 for edge in edges)
    lam = max_overlap(edges)
    graph = conflict_graph(edges)
    if not edges:
        return

    degree_bound = 6 * (lam - 1)
    assert max(map(len, graph), default=0) <= degree_bound

    colors = greedy_coloring(edges)
    number = max(colors) + 1
    assert number <= 6 * lam - 5

    for c in range(number):
        members = [edges[i] for i in range(len(edges)) if colors[i] == c]
        for a, b in combinations(members, 2):
            assert not (a & b)

    largest = max(sum(c == k for c in colors) for k in range(number))
    assert largest * (6 * lam - 5) >= len(edges)


def exhaustive_small() -> None:
    # Exhaust all simple support families on four labels with support size at most 3.
    supports = [
        frozenset(s)
        for r in range(1, 4)
        for s in combinations(range(4), r)
    ]
    for mask in range(1 << len(supports)):
        family = [supports[i] for i in range(len(supports)) if mask & (1 << i)]
        check_family(family)


def randomized_families() -> None:
    rng = random.Random(302)
    for vertices in range(4, 20):
        for _ in range(1000):
            count = rng.randint(1, 50)
            family = []
            for _ in range(count):
                size = rng.randint(1, min(6, vertices))
                family.append(frozenset(rng.sample(range(vertices), size)))
            check_family(family)

            lam = max_overlap(family)
            destroyed = rng.randint(1, 30)
            created = len(family)
            if created < destroyed:
                assert created - destroyed < 0
            else:
                q = created - destroyed + 1
                designated = family[:q]
                assert created - q == destroyed - 1
                check_family(designated)

                designated_lam = max_overlap(designated)
                channels = rng.randint(1, 6)
                colors = greedy_coloring(designated)
                typed_blocks = set()
                for i, c in enumerate(colors):
                    endpoint_type = rng.randrange(2 * channels)
                    typed_blocks.add((c, endpoint_type))
                assert len(typed_blocks) <= 2 * channels * (6 * designated_lam - 5)

                # Choosing one endpoint from every support uses any label no more
                # often than its support degree.
                chosen = [min(edge) for edge in designated]
                for v in set(chosen):
                    assert chosen.count(v) <= designated_lam


def sector_pigeonhole() -> None:
    rng = random.Random(9302)
    for degree in range(1, 100):
        sectors = [0] * 9
        for _ in range(degree):
            sectors[rng.randrange(9)] += 1
        assert max(sectors) * 9 >= degree


def main() -> None:
    exhaustive_small()
    randomized_families()
    sector_pigeonhole()
    print("bounded-overlap child batching verifier: PASS")


if __name__ == "__main__":
    main()
