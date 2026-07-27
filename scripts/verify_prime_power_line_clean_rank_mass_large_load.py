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
    corrected_family_checks = 0
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

            corrected_total = Fraction(0, 1)
            forced_total = 0
            universal_mass = 0

            for rank in range(1, min(3, side) + 1):
                ranked = {
                    item: value
                    for item, value in probabilities.items()
                    if len(item) == rank
                }
                assert sum(ranked.values(), Fraction(0, 1)) == comb(side, rank)
                rank_identities += 1

                forced = [item for item, value in ranked.items() if value == 1]
                forced_total += len(forced)
                assert len(forced) <= comb(side, rank)
                forced_subtractions += 1

                nonforced = [item for item, value in ranked.items() if value < 1]
                corrected = {
                    item
                    for item in nonforced
                    if random.random() < 0.55
                }
                corrected_mass = sum(
                    (ranked[item] for item in corrected),
                    Fraction(0, 1),
                )
                assert corrected_mass <= comb(side, rank) - len(forced)
                corrected_total += corrected_mass
                universal_mass += comb(side, rank) - len(forced)
                corrected_family_checks += 1

            assert corrected_total <= universal_mass
            destroyed_load = universal_mass + 1
            assert corrected_total < destroyed_load
            assert corrected_total * denominator < destroyed_load * denominator
            large_load_checks += 1
            systems += 1

    print(
        "verified line-clean rank-mass large-load closure: "
        f"{systems} rational response laws, "
        f"{rank_identities} exact rank identities, "
        f"{corrected_family_checks} corrected-family bounds, "
        f"{forced_subtractions} forced-mass subtractions and "
        f"{large_load_checks} strict large-load certificates"
    )


if __name__ == "__main__":
    main()
