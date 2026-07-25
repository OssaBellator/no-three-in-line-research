#!/usr/bin/env python3
"""Verify CMR617--CMR622 protected/free skeleton factorisation."""

from collections import defaultdict
from itertools import permutations
from math import comb, factorial


Edge = tuple[int, int]
Skeleton = tuple[tuple[Edge, ...], tuple[Edge, ...]]


def derangements(n: int) -> list[tuple[int, ...]]:
    return [
        perm
        for perm in permutations(range(n))
        if all(perm[index] != index for index in range(n))
    ]


def matching_count(
    sources: tuple[int, ...],
    targets: tuple[int, ...],
) -> int:
    count = 0
    for image in permutations(targets):
        if all(source != target for source, target in zip(sources, image)):
            count += 1
    return count


def skeleton_of(perm: tuple[int, ...], protected_size: int) -> Skeleton:
    protected = set(range(protected_size))
    forward = tuple(
        sorted(
            (source, target)
            for source, target in enumerate(perm)
            if source in protected and target not in protected
        )
    )
    backward = tuple(
        sorted(
            (source, target)
            for source, target in enumerate(perm)
            if source not in protected and target in protected
        )
    )
    return forward, backward


def factor_count(n: int, protected_size: int, skeleton: Skeleton) -> int:
    forward, backward = skeleton
    protected = set(range(protected_size))
    free = set(range(protected_size, n))

    protected_sources_used = {source for source, _ in forward}
    free_targets_used = {target for _, target in forward}
    free_sources_used = {source for source, _ in backward}
    protected_targets_used = {target for _, target in backward}

    protected_sources = tuple(sorted(protected - protected_sources_used))
    protected_targets = tuple(sorted(protected - protected_targets_used))
    free_sources = tuple(sorted(free - free_sources_used))
    free_targets = tuple(sorted(free - free_targets_used))

    return (
        matching_count(protected_sources, protected_targets)
        * matching_count(free_sources, free_targets)
    )


def exact_skeleton_count(k: int, u: int) -> int:
    return sum(
        comb(k, c) ** 2
        * comb(u, c) ** 2
        * factorial(c) ** 2
        for c in range(min(k, u) + 1)
    )


def check_side(n: int) -> int:
    states = derangements(n)
    checked_classes = 0
    for protected_size in range(n + 1):
        free_size = n - protected_size
        groups: dict[Skeleton, list[tuple[int, ...]]] = defaultdict(list)
        for perm in states:
            skeleton = skeleton_of(perm, protected_size)
            forward, backward = skeleton
            assert len(forward) == len(backward)
            assert len(forward) <= min(protected_size, free_size)
            assert len(forward) + len(backward) <= 2 * free_size
            groups[skeleton].append(perm)

        assert sum(len(group) for group in groups.values()) == len(states)
        assert len(groups) <= exact_skeleton_count(protected_size, free_size)
        assert exact_skeleton_count(protected_size, free_size) <= (
            (free_size + 1) * n ** (4 * free_size)
            if n or free_size == 0
            else 1
        )

        for skeleton, group in groups.items():
            assert len(group) == factor_count(n, protected_size, skeleton)
            checked_classes += 1
    return checked_classes


def check_threshold_bounds() -> None:
    for n in range(1, 60):
        for protected_size in range(n + 1):
            free_size = n - protected_size
            exact = exact_skeleton_count(protected_size, free_size)
            assert exact <= (free_size + 1) * n ** (4 * free_size)
            for q in range(free_size, free_size + 5):
                assert 2 * free_size <= 2 * q
                assert exact <= (q + 1) * n ** (4 * q)


def main() -> None:
    checked = sum(check_side(n) for n in range(1, 8))
    check_threshold_bounds()
    print(
        "verified protected-core interface factorisation for "
        f"{checked} skeleton classes through side seven"
    )


if __name__ == "__main__":
    main()
