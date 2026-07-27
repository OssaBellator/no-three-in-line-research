#!/usr/bin/env python3
"""Finite checks for CMR1726--CMR1733."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, comb
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
    random = Random(1726)
    systems = 0
    support_bounds = 0
    strict_closures = 0
    weighted_bounds = 0
    finite_support_checks = 0
    overflow_checks = 0

    for side in range(2, 8):
        all_responses = list(permutations(range(side)))
        for _ in range(110):
            sample_size = random.randint(1, min(24, len(all_responses)))
            responses = random.sample(all_responses, sample_size)
            weights = [random.randint(1, 30) for _ in responses]
            denominator = sum(weights)
            response_law = [
                (response, Fraction(weight, denominator))
                for response, weight in zip(responses, weights)
            ]

            support = {
                (left, right)
                for left in range(side)
                for right in range(side)
                if random.random() < 0.24
            }
            mu = matching_number(side, support)

            probabilities: dict[Prescription, Fraction] = {}
            for response, probability in response_law:
                for rank in range(1, min(3, side) + 1):
                    for sources in combinations(range(side), rank):
                        item = tuple((source, response[source]) for source in sources)
                        probabilities[item] = (
                            probabilities.get(item, Fraction(0, 1))
                            + probability
                        )

            multiplicity_caps: dict[int, int] = {}
            rank_weights: dict[int, int] = {}
            exact_expectation = Fraction(0, 1)
            exact_weighted = Fraction(0, 1)
            support_bound = 0
            weighted_bound = 0

            for rank in range(1, min(3, side) + 1):
                owned = [
                    item
                    for item in probabilities
                    if len(item) == rank and owner(item) in support
                ]
                cap = random.randint(0, 5)
                multiplicity_caps[rank] = cap
                rank_weight = random.randint(0, 7)
                rank_weights[rank] = rank_weight
                multiplicity = {
                    item: random.randint(0, cap)
                    for item in owned
                }
                rank_expectation = sum(
                    (
                        multiplicity[item] * probabilities[item]
                        for item in owned
                    ),
                    Fraction(0, 1),
                )
                rank_capacity = mu * cap * comb(side - 1, rank - 1)
                assert rank_expectation <= rank_capacity
                exact_expectation += rank_expectation
                exact_weighted += rank_weight * rank_expectation
                support_bound += rank_capacity
                weighted_bound += rank_weight * rank_capacity
                support_bounds += 1

            assert exact_expectation <= support_bound
            destroyed_load = support_bound + 1
            assert exact_expectation < destroyed_load
            assert exact_expectation * denominator < destroyed_load * denominator
            strict_closures += 1

            assert exact_weighted <= weighted_bound
            weighted_destroyed_load = weighted_bound + 1
            assert exact_weighted < weighted_destroyed_load
            weighted_bounds += 1

            edge_list = list(support)
            finite_support = set(
                random.sample(edge_list, min(len(edge_list), random.randint(0, 2)))
            )
            assert matching_number(side, finite_support) <= len(finite_support)
            if len(finite_support) == 2:
                first, second = tuple(finite_support)
                if first[0] == second[0] or first[1] == second[1]:
                    assert matching_number(side, finite_support) == 1
            finite_support_checks += 1

            if mu > 0 and support_bound > 0:
                failed_destroyed_load = random.randint(1, support_bound)
                threshold = ceil(Fraction(failed_destroyed_load, 3 * mu))
                contributions = [
                    multiplicity_caps[rank] * comb(side - 1, rank - 1)
                    for rank in multiplicity_caps
                ]
                if mu * sum(contributions) >= failed_destroyed_load:
                    assert max(contributions) >= threshold
                    overflow_checks += 1

            systems += 1

    print(
        "verified small owner-support large-load closure: "
        f"{systems} rational response systems, "
        f"{support_bounds} rankwise support capacities, "
        f"{strict_closures} strict closures, "
        f"{weighted_bounds} weighted closures, "
        f"{finite_support_checks} one/two-edge support checks and "
        f"{overflow_checks} multiplicity-overflow localizations"
    )


if __name__ == "__main__":
    main()
