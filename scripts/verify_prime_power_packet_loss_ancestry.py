#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR422--CMR425."""

from __future__ import annotations

from itertools import combinations, permutations


def matching(vector: tuple[int, ...]) -> set[tuple[int, int]]:
    return {(source, row) for source, row in enumerate(vector)}


def perfect_matchings(
    side: int, edges: set[tuple[int, int]]
) -> list[set[tuple[int, int]]]:
    return [
        matching(vector)
        for vector in permutations(range(side))
        if matching(vector) <= edges
    ]


def verify_small_host_dichotomy() -> None:
    """Every realized certificate has a deletable edge or is fully essential."""

    for side in (2, 3):
        universe = [
            (source, row)
            for source in range(side)
            for row in range(side)
        ]
        for mask in range(1 << len(universe)):
            edges = {
                edge
                for index, edge in enumerate(universe)
                if mask & (1 << index)
            }
            states = perfect_matchings(side, edges)
            if not states:
                continue

            essential = set.intersection(*(set(state) for state in states))
            for state in states:
                certificate = set(state)
                nonessential = certificate - essential
                if nonessential:
                    edge = next(iter(nonessential))
                    assert perfect_matchings(side, edges - {edge})
                else:
                    assert certificate <= essential


def verify_entering_leaving_equality() -> None:
    for side in range(2, 8):
        states = list(permutations(range(side)))
        sample = states[: min(200, len(states))]
        for old_vector in sample:
            old = matching(old_vector)
            for new_vector in sample:
                new = matching(new_vector)
                entering = new - old
                leaving = old - new
                assert len(entering) == len(leaving)
                if old != new:
                    assert len(entering) >= 2
                    assert len(leaving) >= 2


def verify_recreation_support() -> None:
    universe = set(range(8))
    triples = [set(choice) for choice in combinations(universe, 3)]
    states = [
        {value for value in universe if mask & (1 << value)}
        for mask in range(1 << len(universe))
    ]

    for old in states:
        absent_conflicts = [triple for triple in triples if not triple <= old]
        for new in states:
            entering = new - old
            recreated = [
                triple for triple in absent_conflicts if triple <= new
            ]
            assert all(triple & entering for triple in recreated)


def verify_deletion_and_batch_bounds() -> None:
    for side in range(2, 50):
        deletion_cap = side * (side - 1)
        assert side * side - side == deletion_cap

        for packets in range(1, 12):
            for deletions in (0, 1, min(3, deletion_cap), deletion_cap):
                for forced in range(10):
                    lossy_batches = deletions + forced
                    losses = packets * lossy_batches
                    installations = packets + losses

                    assert lossy_batches <= deletions + forced
                    assert losses <= packets * (deletions + forced)
                    assert installations <= packets * (
                        1 + deletions + forced
                    )
                    assert installations <= packets * (
                        1 + deletion_cap + forced
                    )

                for width in range(8):
                    forced = width * deletions
                    installations = packets * (
                        1 + deletions + forced
                    )
                    assert installations == packets * (
                        1 + (1 + width) * deletions
                    )
                    assert installations <= packets * (
                        1 + (1 + width) * deletion_cap
                    )


def main() -> None:
    verify_small_host_dichotomy()
    verify_entering_leaving_equality()
    verify_recreation_support()
    verify_deletion_and_batch_bounds()
    print(
        "verified packet-loss ancestry: entering/leaving orientation, "
        "deletion-or-essential dichotomy, finite deletion budget, lossy-batch "
        "accounting, and conditional ancestry-width closure"
    )


if __name__ == "__main__":
    main()
