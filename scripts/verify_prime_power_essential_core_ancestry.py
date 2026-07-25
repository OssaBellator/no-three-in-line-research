#!/usr/bin/env python3
"""Finite and arithmetic checks for CMR429--CMR432."""

from __future__ import annotations

from itertools import permutations
from math import comb


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


def verify_essential_sets_are_matchings() -> None:
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
            left = [source for source, _ in essential]
            right = [row for _, row in essential]
            assert len(left) == len(set(left))
            assert len(right) == len(set(right))
            assert len(essential) <= side


def verify_monotone_first_essential_layers() -> None:
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
            for deleted in edges - essential:
                smaller = edges - {deleted}
                later_states = perfect_matchings(side, smaller)
                if not later_states:
                    continue
                later_essential = set.intersection(
                    *(set(state) for state in later_states)
                )
                assert essential <= later_essential
                assert len(later_essential) <= side


def verify_certificate_and_link_counts() -> None:
    for side in range(1, 200):
        ranks = range(1, min(3, side) + 1)
        certificates = sum(comb(side, rank) for rank in ranks)
        links = sum(rank * comb(side, rank) for rank in ranks)
        per_edge = sum(comb(side - 1, rank - 1) for rank in ranks)

        assert links == side * per_edge
        assert certificates < side**3 + side
        assert links < 3 * side**3

        for new_essential in range(side + 1):
            incoming = new_essential * per_edge
            assert incoming <= links


def verify_ledger_bounds() -> None:
    for side in range(2, 100):
        deletions = side * (side - 1)
        certificates = sum(comb(side, rank) for rank in range(1, 4))
        links = sum(rank * comb(side, rank) for rank in range(1, 4))

        assert deletions + certificates < side**3 + side**2 + side
        assert links < 3 * side**3


def main() -> None:
    verify_essential_sets_are_matchings()
    verify_monotone_first_essential_layers()
    verify_certificate_and_link_counts()
    verify_ledger_bounds()
    print(
        "verified essential-core ancestry: essential matching structure, "
        "monotone first-essentiality layers, rank-three subset counts, and "
        "polynomial node/link width"
    )


if __name__ == "__main__":
    main()
