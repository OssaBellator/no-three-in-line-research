#!/usr/bin/env python3
"""Finite checks for CMR1822--CMR1829."""

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
    random = Random(1822)
    systems = 0
    response_checks = 0
    strict_checks = 0

    for side in range(3, 7):
        all_edges = {
            (left, right)
            for left in range(side)
            for right in range(side)
        }

        for _ in range(100):
            allowed = {(index, index) for index in range(side)}
            allowed |= {
                edge
                for edge in all_edges
                if random.random() < 0.65
            }
            matchings = host_matchings(side, allowed)
            assert matchings

            edges = sorted(set().union(*matchings))
            containing_edge = {
                edge: [matching for matching in matchings if edge in matching]
                for edge in edges
            }

            compatible_pairs: set[frozenset[Edge]] = set()
            compatible_triples: set[frozenset[Edge]] = set()
            for matching in matchings:
                compatible_pairs.update(
                    frozenset(pair)
                    for pair in combinations(sorted(matching), 2)
                )
                compatible_triples.update(
                    frozenset(triple)
                    for triple in combinations(sorted(matching), 3)
                )

            containing_pair = {
                pair: [matching for matching in matchings if pair <= matching]
                for pair in compatible_pairs
            }

            return_score = {edge: random.randint(0, 5) for edge in edges}
            selector_score = {edge: random.randint(0, 4) for edge in edges}
            rank_one_score = {edge: random.randint(0, 7) for edge in edges}
            selector_cap = random.randint(0, 5)
            pair_score = {
                pair: random.randint(0, 8)
                for pair in compatible_pairs
            }
            triple_score = {
                triple: random.randint(0, 6)
                for triple in compatible_triples
            }

            inner_pair = {
                edge: max(
                    sum(
                        pair_score.get(frozenset((edge, other)), 0)
                        for other in matching
                        if other != edge
                    )
                    for matching in containing_edge[edge]
                )
                for edge in edges
            }

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

            middle_triple = {
                edge: max(
                    sum(
                        inner_triple.get((edge, other), 0)
                        for other in matching
                        if other != edge
                    )
                    for matching in containing_edge[edge]
                )
                for edge in edges
            }

            cleared_outer_score = {
                edge: (
                    6
                    * (
                        return_score[edge]
                        + selector_cap * selector_score[edge]
                        + rank_one_score[edge]
                    )
                    + 3 * inner_pair[edge]
                    + middle_triple[edge]
                )
                for edge in edges
            }

            outer_objective = max(
                sum(cleared_outer_score[edge] for edge in matching)
                for matching in matchings
            )

            for matching in matchings:
                exact_score = sum(
                    return_score[edge]
                    + selector_cap * selector_score[edge]
                    + rank_one_score[edge]
                    for edge in matching
                )
                exact_score += sum(
                    pair_score[frozenset(pair)]
                    for pair in combinations(sorted(matching), 2)
                )
                exact_score += sum(
                    triple_score[frozenset(triple)]
                    for triple in combinations(sorted(matching), 3)
                )

                matching_outer_score = sum(
                    cleared_outer_score[edge]
                    for edge in matching
                )
                assert 6 * exact_score <= matching_outer_score
                assert matching_outer_score <= outer_objective
                response_checks += 1

            destroyed_load = outer_objective // 6 + 1
            assert outer_objective < 6 * destroyed_load
            for matching in matchings:
                exact_score = sum(
                    return_score[edge]
                    + selector_cap * selector_score[edge]
                    + rank_one_score[edge]
                    for edge in matching
                )
                exact_score += sum(
                    pair_score[frozenset(pair)]
                    for pair in combinations(sorted(matching), 2)
                )
                exact_score += sum(
                    triple_score[frozenset(triple)]
                    for triple in combinations(sorted(matching), 3)
                )
                assert exact_score < destroyed_load

            strict_checks += 1
            systems += 1

    print(
        "verified unified outer assignment response scores: "
        f"{systems} random hosts, "
        f"{response_checks} complete response checks and "
        f"{strict_checks} strict integer outer certificates"
    )


if __name__ == "__main__":
    main()
