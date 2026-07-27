#!/usr/bin/env python3
"""Exact finite checks for CMR1702--CMR1709."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb
from random import Random


Edge = tuple[int, int]
Prescription = tuple[Edge, ...]


def main() -> None:
    random = Random(1702)
    systems = 0
    rank_checks = 0
    forced_mass_checks = 0
    capacity_checks = 0

    for _ in range(2_000):
        side = random.randint(2, 7)
        edges = {(index, index) for index in range(side)}
        for left in range(side):
            for right in range(side):
                if random.random() < 0.45:
                    edges.add((left, right))

        response_matchings = [
            permutation
            for permutation in permutations(range(side))
            if all((left, permutation[left]) in edges for left in range(side))
        ]
        assert response_matchings
        response_weights = [
            random.randint(1, 20) for _ in response_matchings
        ]
        denominator = sum(response_weights)

        for rank in range(0, min(3, side) + 1):
            numerator: Counter[Prescription] = Counter()
            for response, weight in zip(
                response_matchings, response_weights
            ):
                for sources in combinations(range(side), rank):
                    prescription = tuple(
                        (left, response[left]) for left in sources
                    )
                    numerator[prescription] += weight

            assert sum(numerator.values()) == denominator * comb(side, rank)
            rank_checks += 1

            forced = sum(
                1 for value in numerator.values() if value == denominator
            )
            nonforced_mass = sum(
                value for value in numerator.values() if value < denominator
            )
            assert nonforced_mass == denominator * (
                comb(side, rank) - forced
            )
            forced_mass_checks += 1

            items = list(numerator.items())
            random.shuffle(items)
            selected = items[: random.randint(0, len(items))]
            exact_selected_mass = sum(
                value for _, value in selected if value < denominator
            )
            selected_nonforced_count = sum(
                1 for _, value in selected if value < denominator
            )
            pointwise_numerator_cap = max(
                [value for value in numerator.values() if value < denominator]
                or [0]
            )
            combined_capacity = min(
                selected_nonforced_count * pointwise_numerator_cap,
                denominator * (comb(side, rank) - forced),
            )
            assert exact_selected_mass <= combined_capacity
            capacity_checks += 1

        systems += 1

    print(
        "verified prescription rank-mass conservation: "
        f"{systems} rational response laws, "
        f"{rank_checks} exact rank identities, "
        f"{forced_mass_checks} forced/nonforced decompositions and "
        f"{capacity_checks} combined pointwise/mass capacities"
    )


if __name__ == "__main__":
    main()
