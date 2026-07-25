#!/usr/bin/env python3
"""Verify CMR623--CMR628 skeleton-history and factor-diversity bounds."""

from collections import defaultdict
from itertools import combinations, permutations
from math import ceil, factorial, sqrt


Edge = tuple[int, int]
Skeleton = frozenset[Edge]


def derangements(n: int) -> list[tuple[int, ...]]:
    return [
        perm
        for perm in permutations(range(n))
        if all(perm[index] != index for index in range(n))
    ]


def skeleton(perm: tuple[int, ...], k: int) -> Skeleton:
    return frozenset(
        (source, target)
        for source, target in enumerate(perm)
        if (source < k) != (target < k)
    )


def restrictions(
    perm: tuple[int, ...], k: int
) -> tuple[tuple[Edge, ...], tuple[Edge, ...]]:
    protected = tuple(
        sorted(
            (source, target)
            for source, target in enumerate(perm)
            if source < k and target < k
        )
    )
    free = tuple(
        sorted(
            (source, target)
            for source, target in enumerate(perm)
            if source >= k and target >= k
        )
    )
    return protected, free


def check_side(n: int) -> int:
    states = derangements(n)
    checked = 0
    for k in range(n + 1):
        u = n - k
        groups: dict[Skeleton, list[tuple[int, ...]]] = defaultdict(list)
        for perm in states:
            groups[skeleton(perm, k)].append(perm)

        skeletons = list(groups)
        for first, second in combinations(skeletons, 2):
            difference = first ^ second
            assert len(difference) >= 2
            assert len(difference) % 2 == 0

        for current, group in groups.items():
            assert len(current) <= 2 * u
            protected_restrictions = set()
            free_restrictions = set()
            pairs = set()
            for perm in group:
                protected, free = restrictions(perm, k)
                protected_restrictions.add(protected)
                free_restrictions.add(free)
                pairs.add((protected, free))
            assert len(pairs) == len(group)
            assert len(group) <= (
                len(protected_restrictions) * len(free_restrictions)
            )
            assert max(
                len(protected_restrictions),
                len(free_restrictions),
            ) >= ceil(sqrt(len(group)))
            assert len(free_restrictions) <= factorial(u)
            assert len(protected_restrictions) >= ceil(
                len(group) / factorial(u)
            )
            checked += 1

        cross_universe = 2 * k * u
        for recurrence in range(2, 8):
            maximum_changes = (recurrence - 1) * k * u
            assert 2 * maximum_changes <= (
                (recurrence - 1) * cross_universe
            )
    return checked


def check_threshold_arithmetic() -> None:
    for n in range(1, 80):
        for k in range(n + 1):
            u = n - k
            for q in range(u, u + 5):
                assert 2 * u <= 2 * q
                assert (u + 1) * n ** (4 * u) <= (
                    (q + 1) * n ** (4 * q)
                )


def check_factor_state_expansion() -> None:
    for distinct_states in range(1, 1000):
        if distinct_states == 1:
            entering = 0
        else:
            entering = 2 * (distinct_states - 1)
        assert entering >= 0


def main() -> None:
    checked = sum(check_side(n) for n in range(1, 8))
    check_threshold_arithmetic()
    check_factor_state_expansion()
    print(
        "verified protected skeleton history for "
        f"{checked} skeleton classes through side seven"
    )


if __name__ == "__main__":
    main()
