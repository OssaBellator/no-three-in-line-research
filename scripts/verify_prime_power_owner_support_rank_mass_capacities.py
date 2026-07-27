#!/usr/bin/env python3
"""Finite checks for CMR1718--CMR1725."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb
from random import Random


Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


def matching_number(side: int, edges: set[Edge]) -> int:
    adjacency: list[list[int]] = [[] for _ in range(side)]
    for left, right in edges:
        adjacency[left].append(right)

    dynamic: dict[int, int] = {0: 0}
    for left in range(side):
        updated = dict(dynamic)
        for mask, value in dynamic.items():
            for right in adjacency[left]:
                if mask & (1 << right):
                    continue
                new_mask = mask | (1 << right)
                updated[new_mask] = max(updated.get(new_mask, -1), value + 1)
        dynamic = updated
    return max(dynamic.values(), default=0)


def owner(item: Prescription) -> Edge:
    return min(item)


def main() -> None:
    random = Random(1718)
    systems = 0
    responsewise_checks = 0
    expectation_checks = 0
    conditional_checks = 0
    weighted_checks = 0
    cover_checks = 0

    for side in range(2, 8):
        all_responses = list(permutations(range(side)))
        for _ in range(100):
            sample_size = random.randint(1, min(24, len(all_responses)))
            responses = random.sample(all_responses, sample_size)
            weights = [random.randint(1, 30) for _ in responses]
            denominator = sum(weights)
            response_law = [
                (response, Fraction(weight, denominator))
                for response, weight in zip(responses, weights)
            ]

            owner_support = {
                (left, right)
                for left in range(side)
                for right in range(side)
                if random.random() < 0.3
            }
            support_matching_number = matching_number(side, owner_support)

            prescription_probability: dict[Prescription, Fraction] = {}
            for response, probability in response_law:
                for rank in range(1, min(3, side) + 1):
                    for sources in combinations(range(side), rank):
                        item = tuple((source, response[source]) for source in sources)
                        prescription_probability[item] = (
                            prescription_probability.get(item, Fraction(0, 1))
                            + probability
                        )

            for response, _ in response_law:
                response_edges = {(left, response[left]) for left in range(side)}
                owner_count = len(response_edges.intersection(owner_support))
                for rank in range(1, min(3, side) + 1):
                    realised = 0
                    for sources in combinations(range(side), rank):
                        item = tuple((source, response[source]) for source in sources)
                        if owner(item) in owner_support:
                            realised += 1
                    assert realised <= owner_count * comb(side - 1, rank - 1)
                    responsewise_checks += 1

            for rank in range(1, min(3, side) + 1):
                owned_mass = sum(
                    probability
                    for item, probability in prescription_probability.items()
                    if len(item) == rank and owner(item) in owner_support
                )
                assert owned_mass <= (
                    support_matching_number * comb(side - 1, rank - 1)
                )
                expectation_checks += 1

            for edge in owner_support:
                edge_probability = sum(
                    probability
                    for response, probability in response_law
                    if response[edge[0]] == edge[1]
                )
                if edge_probability == 0:
                    continue
                for rank in range(1, min(3, side) + 1):
                    mass = sum(
                        probability
                        for item, probability in prescription_probability.items()
                        if len(item) == rank and owner(item) == edge
                    )
                    assert mass <= edge_probability * comb(side - 1, rank - 1)
                    conditional_checks += 1

            rank_weights = {
                rank: random.randint(0, 7)
                for rank in range(1, min(3, side) + 1)
            }
            weighted_mass = sum(
                rank_weights[len(item)] * probability
                for item, probability in prescription_probability.items()
                if owner(item) in owner_support
            )
            weighted_bound = support_matching_number * sum(
                rank_weights[rank] * comb(side - 1, rank - 1)
                for rank in rank_weights
            )
            assert weighted_mass <= weighted_bound
            weighted_checks += 1

            source_cover = {
                left for left in range(side) if random.random() < 0.35
            }
            target_cover = {
                right for right in range(side) if random.random() < 0.35
            }
            covered_edges = {
                edge
                for edge in owner_support
                if edge[0] in source_cover or edge[1] in target_cover
            }
            assert matching_number(side, covered_edges) <= (
                len(source_cover) + len(target_cover)
            )
            cover_checks += 1
            systems += 1

    print(
        "verified owner-support rank-mass capacities: "
        f"{systems} rational response systems, "
        f"{responsewise_checks} response-wise bounds, "
        f"{expectation_checks} matching-number capacities, "
        f"{conditional_checks} fixed-owner conditional bounds, "
        f"{weighted_checks} weighted capacities and "
        f"{cover_checks} source/target cover checks"
    )


if __name__ == "__main__":
    main()
