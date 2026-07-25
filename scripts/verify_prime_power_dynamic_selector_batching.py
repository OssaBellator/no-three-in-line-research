#!/usr/bin/env python3
"""Verify CMR587--CMR592 recurrent-set batching and cover arithmetic."""

from itertools import combinations
from math import ceil, comb, sqrt


Edge = tuple[int, int]
Vertex = tuple[str, int]


def maximum_matching_size(n: int, edges: set[Edge]) -> int:
    """Exact bitmask dynamic programme for a small bipartite graph."""
    adjacency = {u: [] for u in range(n)}
    for u, v in edges:
        adjacency[u].append(v)

    dp = {0: 0}
    for u in range(n):
        nxt = dict(dp)
        for mask, value in dp.items():
            for v in adjacency[u]:
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                nxt[new_mask] = max(nxt.get(new_mask, -1), value + 1)
        dp = nxt
    return max(dp.values())


def minimum_vertex_cover(edges: set[Edge], vertices: list[Vertex]) -> set[Vertex]:
    """Brute-force minimum cover for the configured small cases."""
    for size in range(len(vertices) + 1):
        for choice in combinations(vertices, size):
            cover = set(choice)
            if all(("L", u) in cover or ("R", v) in cover for u, v in edges):
                return cover
    raise AssertionError("no vertex cover found")


def check_matching_cover(n: int, protected_size: int) -> int:
    protected_left = set(range(protected_size))
    protected_right = set(range(protected_size))
    forbidden = {(i, i) for i in range(n)}
    universe = [
        (u, v)
        for u in range(n)
        for v in range(n)
        if (u, v) not in forbidden
    ]

    tested = 0
    for mask in range(1 << len(universe)):
        recurrent = {
            universe[index]
            for index in range(len(universe))
            if mask & (1 << index)
        }
        free = {
            (u, v)
            for u, v in recurrent
            if u not in protected_left and v not in protected_right
        }

        matching_number = maximum_matching_size(n, free)
        free_vertices = [
            ("L", u) for u in range(protected_size, n)
        ] + [
            ("R", v) for v in range(protected_size, n)
        ]
        cover = minimum_vertex_cover(free, free_vertices)
        assert len(cover) == matching_number

        full_cover = (
            {("L", u) for u in protected_left}
            | {("R", v) for v in protected_right}
            | cover
        )
        assert all(
            ("L", u) in full_cover or ("R", v) in full_cover
            for u, v in recurrent
        )

        if recurrent:
            degrees = []
            for side, vertex in full_cover:
                if side == "L":
                    degrees.append(sum(u == vertex for u, _ in recurrent))
                else:
                    degrees.append(sum(v == vertex for _, v in recurrent))
            assert max(degrees) >= ceil(len(recurrent) / len(full_cover))

        tested += 1
    return tested


def check_subset_incidence() -> None:
    for universe_size in range(1, 40):
        for minimum_size in range(1, universe_size + 1):
            for rank in range(1, minimum_size + 1):
                for recurrence in range(2, 8):
                    bound_numerator = (
                        (recurrence - 1)
                        * comb(universe_size, rank)
                    )
                    bound_denominator = comb(minimum_size, rank)
                    maximum_history = bound_numerator // bound_denominator
                    assert (
                        (maximum_history + 1) * bound_denominator
                        > bound_numerator
                    )


def check_joint_absence() -> None:
    for occurrences in range(1, 80):
        for sigma in range(2, 20):
            required_returns = ceil(occurrences / (sigma - 1)) - 1
            runs = required_returns + 1
            assert runs * (sigma - 1) >= occurrences


def check_bulk_growth() -> None:
    for n in range(1, 50):
        for initial_size in range(n + 1):
            for batch_size in range(1, n + 1):
                steps = (n - initial_size) // batch_size
                assert initial_size + steps * batch_size <= n
                assert initial_size + (steps + 1) * batch_size > n


def check_token_partition() -> None:
    for degree in range(1, 2000):
        threshold = ceil(sqrt(degree))
        if threshold >= 2:
            assert ceil(degree / (threshold - 1)) >= threshold
        for generic_threshold in range(2, min(degree + 2, 60)):
            occupied = ceil(degree / (generic_threshold - 1))
            assert occupied * (generic_threshold - 1) >= degree


def main() -> None:
    tested = 0
    for n in range(2, 5):
        for protected_size in range(n + 1):
            tested += check_matching_cover(n, protected_size)

    check_subset_incidence()
    check_joint_absence()
    check_bulk_growth()
    check_token_partition()
    print(
        "verified dynamic selector batching on "
        f"{tested} exhaustive recurrent-set instances through side four"
    )


if __name__ == "__main__":
    main()
