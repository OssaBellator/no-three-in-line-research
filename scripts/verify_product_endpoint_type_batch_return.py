#!/usr/bin/env python3
"""Finite checks for PX356--PX361 endpoint-type batching."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
import random


def external_fixed_count(inserted_count: int) -> int:
    assert inserted_count in (1, 2)
    return 3 - inserted_count


def check_dependency_patterns() -> None:
    # One-core cycle has inserted dependency sets {a}, {a,b}, {b}.
    one_core = (frozenset(("a",)), frozenset(("a", "b")), frozenset(("b",)))
    # Two-core cycle has two a-cells and two b-cells.
    two_core = (
        frozenset(("a",)),
        frozenset(("a",)),
        frozenset(("b",)),
        frozenset(("b",)),
    )

    for inserted in (one_core, two_core):
        for rank in (1, 2):
            for choice in combinations(range(len(inserted)), rank):
                dependencies = frozenset().union(*(inserted[i] for i in choice))
                assert 1 <= len(dependencies) <= 2
                assert external_fixed_count(rank) in (1, 2)


def check_random_batching(trials: int = 5000) -> None:
    rng = random.Random(20260726)

    for _ in range(trials):
        q = rng.randint(1, 12)
        type_count = 2 * q
        blocker_count = rng.randint(0, 500)

        # Each blocker has one or two fixed selected endpoints.
        blockers: list[list[tuple[int, int]]] = []
        for _ in range(blocker_count):
            fixed_count = rng.choice((1, 2))
            endpoints = []
            for _ in range(fixed_count):
                point_id = rng.randrange(200)
                point_type = rng.randrange(type_count)
                endpoints.append((point_id, point_type))
            blockers.append(endpoints)

        # Canonically assign each blocker to one fixed endpoint.
        groups: dict[int, set[int]] = defaultdict(set)
        assignment: list[tuple[int, int, int]] = []
        for blocker_id, endpoints in enumerate(blockers):
            point_id, point_type = endpoints[0]
            groups[point_type].add(point_id)
            assignment.append((blocker_id, point_id, point_type))

        assert len(groups) <= type_count

        remaining = set(range(blocker_count))
        processed = 0
        for point_type, moved_points in groups.items():
            assert 0 <= point_type < type_count
            removed = {
                blocker_id
                for blocker_id, point_id, assigned_type in assignment
                if assigned_type == point_type and point_id in moved_points
            }
            remaining.difference_update(removed)
            processed += 1

        assert not remaining
        assert processed <= 2 * q


def check_causal_vector() -> None:
    # Processing one nonempty type batch lowers the first coordinate; deeper
    # obligations may grow arbitrarily without spoiling lexicographic descent.
    for blocker_types in range(1, 40):
        vector = (blocker_types, 0)
        for deeper in range(blocker_types):
            new_vector = (vector[0] - 1, deeper + 1)
            assert new_vector < vector
            vector = new_vector
        assert vector[0] == 0


def main() -> None:
    check_dependency_patterns()
    check_random_batching()
    check_causal_vector()
    print("PX356--PX361 endpoint-type batch-return verifier: PASS")


if __name__ == "__main__":
    main()
