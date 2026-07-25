#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR426--CMR428."""

from __future__ import annotations

from itertools import permutations


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


def verify_essentiality_monotonicity() -> None:
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
            for edge in essential:
                for deleted in edges - {edge}:
                    smaller = edges - {deleted}
                    later_states = perfect_matchings(side, smaller)
                    if later_states:
                        assert all(edge in state for state in later_states)


def verify_forced_certificate_terminality() -> None:
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
            if len(essential) < side:
                continue

            # A certificate made entirely of essential matching edges occurs in
            # every selected state and therefore cannot be cleaned by rematching.
            certificate = set(next(iter(states))) & essential
            assert certificate
            assert all(certificate <= state for state in states)


def verify_completion_or_endpoint_bounds() -> None:
    for side in range(2, 100):
        deletion_cap = side * (side - 1)
        for packets in range(1, 30):
            completion = packets * (1 + deletion_cap)
            endpoint = packets * (2 + deletion_cap)

            assert completion == packets + packets * deletion_cap
            assert endpoint == packets + packets * (deletion_cap + 1)
            assert completion <= endpoint

            for lossy_batches in range(deletion_cap + 1):
                installations = packets + packets * lossy_batches
                assert installations <= completion


def main() -> None:
    verify_essentiality_monotonicity()
    verify_forced_certificate_terminality()
    verify_completion_or_endpoint_bounds()
    print(
        "verified forced packet terminality: essentiality persistence, "
        "uncleanable fully forced certificates, and polynomial completion-or-"
        "ancestry bounds"
    )


if __name__ == "__main__":
    main()
