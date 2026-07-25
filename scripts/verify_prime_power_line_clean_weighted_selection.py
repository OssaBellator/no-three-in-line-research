#!/usr/bin/env python3
"""Finite checks for CMR502--CMR506."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


Edge = tuple[int, int]


def derangements(side: int) -> list[tuple[int, ...]]:
    return [
        vector
        for vector in permutations(range(side))
        if all(vector[index] != index for index in range(side))
    ]


def verify_derangement_marginals() -> None:
    for side in range(2, 7):
        states = derangements(side)
        edges = [
            (left, right)
            for left in range(side)
            for right in range(side)
            if left != right
        ]

        for left, right in edges:
            count = sum(vector[left] == right for vector in states)
            assert Fraction(count, len(states)) == Fraction(1, side - 1)

        if side <= 4:
            masks = range(1 << len(edges))
        else:
            masks = [
                0,
                1,
                (1 << len(edges)) - 1,
                sum(
                    1 << index
                    for index, (left, right) in enumerate(edges)
                    if (left + right) % 3 == 0
                ),
            ]

        for mask in masks:
            unavailable = {
                edge
                for index, edge in enumerate(edges)
                if mask & (1 << index)
            }
            total = 0
            for vector in states:
                total += sum(
                    (left, vector[left]) in unavailable
                    for left in range(side)
                )
            average = Fraction(total, len(states))
            assert average == Fraction(len(unavailable), side - 1)


def verify_weighted_selection() -> None:
    # The weighted selection lemma is an averaging statement.  Exhaust arbitrary
    # small nonnegative integer collateral and restoration profiles.
    for state_count in range(1, 6):
        for collateral in product(range(3), repeat=state_count):
            for restoration in product(range(4), repeat=state_count):
                for threshold in range(1, 5):
                    average = Fraction(sum(collateral), state_count) + Fraction(
                        sum(restoration), state_count * threshold
                    )
                    values = [
                        Fraction(collateral[index], 1)
                        + Fraction(restoration[index], threshold)
                        for index in range(state_count)
                    ]
                    assert min(values) <= average
                    if average < 1:
                        index = min(range(state_count), key=values.__getitem__)
                        assert collateral[index] == 0
                        assert restoration[index] < threshold


def verify_tunable_arithmetic() -> None:
    for denominator in range(1, 20):
        for collateral_numerator in range(0, 31):
            collateral_term = Fraction(collateral_numerator, 30)
            for unavailable_numerator in range(0, 31):
                unavailable_term = Fraction(unavailable_numerator, denominator)
                if collateral_term + unavailable_term < 1:
                    continue
                for alpha_numerator in range(1, 10):
                    alpha = Fraction(alpha_numerator, 10)
                    assert (
                        collateral_term >= 1 - alpha
                        or unavailable_term >= alpha
                    )


def verify_incidence_dichotomy() -> None:
    universe = range(5)
    subsets = [
        set(choice)
        for size in range(6)
        for choice in combinations(universe, size)
    ]

    for family_indices in product(range(len(subsets)), repeat=3):
        family = [subsets[index] for index in family_indices]
        incidence = sum(len(edge_set) for edge_set in family)
        union = set().union(*family)

        for threshold in range(2, 5):
            multiplicity = {
                edge: sum(edge in edge_set for edge_set in family)
                for edge in union
            }
            concentrated = any(
                value >= threshold for value in multiplicity.values()
            )
            if not concentrated:
                assert (threshold - 1) * len(union) >= incidence


def main() -> None:
    verify_derangement_marginals()
    verify_weighted_selection()
    verify_tunable_arithmetic()
    verify_incidence_dichotomy()
    print(
        "verified CMR502--CMR506: exact derangement restoration marginals, "
        "weighted cheap-clean selection, tunable collateral/depletion arithmetic, "
        "and unavailable-edge concentration versus dispersion"
    )


if __name__ == "__main__":
    main()
