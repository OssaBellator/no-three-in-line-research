#!/usr/bin/env python3
"""Finite checks for CMR1790--CMR1797."""

from __future__ import annotations

from itertools import combinations, permutations
from random import Random


Edge = tuple[int, int]
Matching = frozenset[Edge]


def host_matchings(side: int, allowed: set[Edge]) -> list[Matching]:
    return [
        frozenset((left, permutation[left]) for left in range(side))
        for permutation in permutations(range(side))
        if all((left, permutation[left]) in allowed for left in range(side))
    ]


def main() -> None:
    random = Random(1790)
    systems = 0
    contracted_matching_checks = 0
    pair_bounds = 0
    triple_bounds = 0
    integer_checks = 0

    for side in range(3, 7):
        all_edges = {
            (left, right)
            for left in range(side)
            for right in range(side)
        }

        for _ in range(100):
            # Retain the identity matching to guarantee a nonempty response host.
            allowed = {(index, index) for index in range(side)}
            allowed |= {
                edge
                for edge in all_edges
                if random.random() < 0.65
            }
            matchings = host_matchings(side, allowed)
            assert matchings

            pair_score: dict[frozenset[Edge], int] = {}
            triple_score: dict[frozenset[Edge], int] = {}
            for matching in matchings:
                for pair in combinations(sorted(matching), 2):
                    pair_score.setdefault(frozenset(pair), random.randint(0, 9))
                for triple in combinations(sorted(matching), 3):
                    triple_score.setdefault(frozenset(triple), random.randint(0, 7))

            edges = sorted(set().union(*matchings))
            containing_edge = {
                edge: [matching for matching in matchings if edge in matching]
                for edge in edges
            }
            compatible_pairs = list(pair_score)
            containing_pair = {
                pair: [matching for matching in matchings if pair <= matching]
                for pair in compatible_pairs
            }

            exact_pair = max(
                sum(
                    pair_score[frozenset(pair)]
                    for pair in combinations(sorted(matching), 2)
                )
                for matching in matchings
            )

            inner_pair: dict[Edge, int] = {}
            for edge in edges:
                inner_pair[edge] = max(
                    sum(
                        pair_score.get(frozenset((edge, other)), 0)
                        for other in matching
                        if other != edge
                    )
                    for matching in containing_edge[edge]
                )
                contracted_matching_checks += len(containing_edge[edge])

            outer_pair_numerator = max(
                sum(inner_pair[edge] for edge in matching)
                for matching in matchings
            )
            assert 2 * exact_pair <= outer_pair_numerator
            pair_bounds += 1

            exact_triple = max(
                sum(
                    triple_score[frozenset(triple)]
                    for triple in combinations(sorted(matching), 3)
                )
                for matching in matchings
            )

            inner_triple: dict[tuple[Edge, Edge], int] = {}
            for pair in compatible_pairs:
                first, second = tuple(pair)
                value = max(
                    sum(
                        triple_score.get(frozenset((first, second, third)), 0)
                        for third in matching
                        if third not in pair
                    )
                    for matching in containing_pair[pair]
                )
                inner_triple[(first, second)] = value
                inner_triple[(second, first)] = value
                contracted_matching_checks += len(containing_pair[pair])

            middle_triple: dict[Edge, int] = {}
            for edge in edges:
                middle_triple[edge] = max(
                    sum(
                        inner_triple.get((edge, other), 0)
                        for other in matching
                        if other != edge
                    )
                    for matching in containing_edge[edge]
                )

            outer_triple_numerator = max(
                sum(middle_triple[edge] for edge in matching)
                for matching in matchings
            )
            assert 6 * exact_triple <= outer_triple_numerator
            triple_bounds += 1

            destroyed_load = exact_pair + exact_triple + 1
            if 3 * outer_pair_numerator + outer_triple_numerator < 6 * destroyed_load:
                assert exact_pair + exact_triple < destroyed_load
            integer_checks += 1
            systems += 1

    print(
        "verified nested assignment line-energy certificates: "
        f"{systems} random response hosts, "
        f"{contracted_matching_checks} contracted-matching checks, "
        f"{pair_bounds} rank-two bounds, "
        f"{triple_bounds} rank-three bounds and "
        f"{integer_checks} strict integer implications"
    )


if __name__ == "__main__":
    main()
