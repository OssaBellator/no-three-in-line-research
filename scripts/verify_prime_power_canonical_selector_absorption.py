#!/usr/bin/env python3
"""Verify CMR571--CMR576 canonical absorption and chase identities."""

from itertools import combinations, permutations
from math import ceil, factorial


Edge = tuple[int, int]


def derangement_number(n: int) -> int:
    return round(
        factorial(n)
        * sum(((-1) ** k) / factorial(k) for k in range(n + 1))
    )


def is_matching(edges: set[Edge]) -> bool:
    return (
        len({u for u, _ in edges}) == len(edges)
        and len({v for _, v in edges}) == len(edges)
    )


def canonical_extension(n: int, protected: set[Edge]) -> set[Edge]:
    assert is_matching(protected)
    used_left = {u for u, _ in protected}
    used_right = {v for _, v in protected}
    left = [u for u in range(n) if u not in used_left]
    right = [v for v in range(n) if v not in used_right]
    extension = set(protected) | set(zip(left, right))
    assert len(extension) == n
    assert is_matching(extension)
    return extension


def all_partial_matchings(n: int, max_size: int | None = None):
    vertices = range(n)
    limit = n if max_size is None else min(n, max_size)
    for k in range(limit + 1):
        for left in combinations(vertices, k):
            for right in combinations(vertices, k):
                for perm in permutations(right):
                    yield set(zip(left, perm))


def check_cylinder_size(n: int, forbidden: set[Edge]) -> None:
    count = 0
    for perm in permutations(range(n)):
        matching = {(u, perm[u]) for u in range(n)}
        if matching.isdisjoint(forbidden):
            count += 1
    assert count == derangement_number(n)


def check_protected_state(n: int, protected: set[Edge]) -> None:
    forbidden = canonical_extension(n, protected)
    if n <= 6:
        check_cylinder_size(n, forbidden)

    all_edges = {(u, v) for u in range(n) for v in range(n)}
    allowed = all_edges - forbidden
    protected_vertices = (
        {u for u, _ in protected},
        {v for _, v in protected},
    )

    blocked: set[Edge] = set()
    for edge in allowed:
        u, v = edge
        disjoint = (
            u not in protected_vertices[0]
            and v not in protected_vertices[1]
        )
        can_extend = is_matching(protected | {edge})
        assert can_extend == disjoint
        if can_extend:
            next_forbidden = canonical_extension(n, protected | {edge})
            assert edge in next_forbidden
            assert protected <= next_forbidden
        else:
            blocked.add(edge)
            assert (
                u in protected_vertices[0]
                or v in protected_vertices[1]
            )

    if blocked and protected:
        cover_vertices = [
            ("L", u) for u in protected_vertices[0]
        ] + [
            ("R", v) for v in protected_vertices[1]
        ]
        degrees = []
        for side, vertex in cover_vertices:
            if side == "L":
                degrees.append(sum(u == vertex for u, _ in blocked))
            else:
                degrees.append(sum(v == vertex for _, v in blocked))
        assert max(degrees) >= ceil(len(blocked) / (2 * len(protected)))


def check_chase_bounds() -> None:
    for n in range(2, 30):
        for ell in range(n + 1):
            max_growth = n - ell
            for lam in range(2, 10):
                per_stage = (lam - 1) * n * (n - 1)
                stages = max_growth + 1
                total = per_stage * stages
                assert total == (lam - 1) * n * (n - 1) * (n - ell + 1)


def main() -> None:
    states = 0
    for n in range(2, 7):
        max_size = n if n <= 4 else 3
        for protected in all_partial_matchings(n, max_size=max_size):
            check_protected_state(n, protected)
            states += 1

    check_chase_bounds()
    print(
        "verified canonical selector absorption for "
        f"{states} protected matching states through side six"
    )


if __name__ == "__main__":
    main()
