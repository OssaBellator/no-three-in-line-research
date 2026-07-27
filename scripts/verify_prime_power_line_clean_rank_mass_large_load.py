#!/usr/bin/env python3
"""Finite checks for CMR1710--CMR1717."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
from math import comb
from random import Random


Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


def prescription(response: tuple[int, ...], sources: tuple[int, ...]) -> Prescription:
    return tuple((source, response[source]) for source in sources)


def main() -> None:
    random = Random(1710)
    systems = 0
    rank_identities = 0
    multiplicity_bounds = 0
    pointwise_mass_minima = 0
    forced_subtractions = 0
    large_load_checks = 0

    for side in range(2, 8):
        all_responses = list(permutations(range(side)))
        for _ in range(120):
            sample_size = random.randint(1, min(24, len(all_responses)))
            responses = random.sample(all_responses, sample_size)
            weights = [random.randint(1, 30) for _ in responses]
            denominator = sum(weights)

            probabilities: dict[Prescription, Fraction] = {}
            for response, weight in zip(responses, weights):
                response_probability = Fraction(weight, denominator)
                for rank in range(1, min(3, side) + 1):
                    for sources in combinations(range(side), rank):
                        item = prescription(response, sources)
                        probabilities[item] = (
                            probabilities.get(item, Fraction(0, 1))
                            + response_probability
                        )

            exact_expectation = Fraction(0, 1)
            multiplicity_mass_bound = 0

            for rank in range(1, min(3, side) + 1):
                ranked = {
                    item: value
                    for item, value in probabilities.items()
                    if len(item) == rank
                }
                assert sum(ranked.values(), Fraction(0, 1)) == comb(side, rank)
                rank_identities += 1

                forced = [item for item, value in ranked.items() if value == 1]
                assert len(forced) <= comb(side, rank)
                forced_subtractions += 1

                nonforced = [item for item, value in ranked.items() if value < 1]
                multiplicity = {
                    item: random.randint(0, 5)
                    for item in nonforced
                }
                maximum_multiplicity = max(multiplicity.values(), default=0)
                rank_expectation = sum(
                    (
                        multiplicity[item] * ranked[item]
                        for item in nonforced
                    ),
                    Fraction(0, 1),
                )
                rank_mass_bound = (
                    maximum_multiplicity
                    * (comb(side, rank) - len(forced))
                )
                assert rank_expectation <= rank_mass_bound
                multiplicity_bounds += 1

                candidate_count = sum(multiplicity.values())
                probability_cap = max(
                    (ranked[item] for item in nonforced),
                    default=Fraction(0, 1),
                )
                pointwise_bound = candidate_count * probability_cap
                assert rank_expectation <= min(pointwise_bound, rank_mass_bound)
                pointwise_mass_minima += 1

                integer_numerator = sum(
                    multiplicity[item]
                    * int(ranked[item] * denominator)
                    for item in nonforced
                )
                assert integer_numerator == rank_expectation * denominator
                assert integer_numerator <= denominator * rank_mass_bound

                exact_expectation += rank_expectation
                multiplicity_mass_bound += rank_mass_bound

            assert exact_expectation <= multiplicity_mass_bound
            destroyed_load = multiplicity_mass_bound + 1
            assert exact_expectation < destroyed_load
            assert exact_expectation * denominator < destroyed_load * denominator
            large_load_checks += 1
            systems += 1

    print(
        "verified multiplicity-aware line-clean rank mass: "
        f"{systems} rational response laws, "
        f"{rank_identities} exact rank identities, "
        f"{multiplicity_bounds} multiplicity bounds, "
        f"{pointwise_mass_minima} pointwise/mass minima, "
        f"{forced_subtractions} forced-mass subtractions and "
        f"{large_load_checks} strict large-load certificates"
    )


if __name__ == "__main__":
    main()
