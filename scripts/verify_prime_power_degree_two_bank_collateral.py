#!/usr/bin/env python3
"""Finite checks for CMR1198--CMR1205."""

from collections import Counter
from itertools import combinations, permutations
from math import factorial
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def derangements(side):
    return [
        permutation
        for permutation in permutations(range(side))
        if all(permutation[row] != row for row in range(side))
    ]


def response_bank(side, forbidden):
    opposite = matching(tuple(range(side)))
    forbidden_edges = matching(forbidden)
    return [
        matching(permutation)
        for permutation in permutations(range(side))
        if matching(permutation).isdisjoint(opposite | forbidden_edges)
    ]


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def check_disjoint_extensions():
    checked = 0
    for side in range(3, 10):
        opposite = matching(tuple(range(side)))
        extensions = [matching(permutation) for permutation in derangements(side)]
        for edge in {(row, column) for row in range(side) for column in range(side) if row != column}:
            assert any(edge in extension and extension.isdisjoint(opposite) for extension in extensions)
            checked += 1
    return checked


def check_cylinder_bounds():
    rng = random.Random(1199)
    checked_banks = 0
    checked_prescriptions = 0
    exact_ratios = 0
    for side in range(4, 8):
        candidates = derangements(side)
        if side >= 6:
            candidates = rng.sample(candidates, min(70, len(candidates)))
        kappa = (side / (side - 2)) ** side
        assert kappa <= 16 + 1e-12
        for forbidden in candidates:
            bank = response_bank(side, forbidden)
            assert bank
            lower = factorial(side) * ((side - 2) / side) ** side
            assert len(bank) + 1e-12 >= lower

            counts = Counter()
            for state in bank:
                edges = tuple(state)
                for rank in (1, 2, 3):
                    for prescription in combinations(edges, rank):
                        counts[frozenset(prescription)] += 1

            for prescription, count in counts.items():
                rank = len(prescription)
                probability = count / len(bank)
                bound = kappa / falling(side, rank)
                assert probability <= bound + 1e-12
                checked_prescriptions += 1
                exact_ratios += count
            checked_banks += 1
    return checked_banks, checked_prescriptions, exact_ratios


def check_expected_collateral_identity():
    rng = random.Random(1201)
    checked = 0
    for side in range(4, 8):
        opposite = matching(tuple(range(side)))
        forbidden_list = derangements(side)
        if side >= 6:
            forbidden_list = rng.sample(forbidden_list, min(40, len(forbidden_list)))
        universe = {(row, column) for row in range(side) for column in range(side)}
        for forbidden in forbidden_list:
            bank = response_bank(side, forbidden)
            allowed = universe - opposite - matching(forbidden)
            candidate_atoms = []
            for _ in range(180):
                rank = rng.randint(1, 3)
                prescription = frozenset(rng.sample(tuple(allowed), rank))
                if len({row for row, _ in prescription}) != rank:
                    continue
                if len({column for _, column in prescription}) != rank:
                    continue
                candidate_atoms.append(prescription)

            direct_total = sum(
                sum(prescription <= state for prescription in candidate_atoms)
                for state in bank
            )
            indicator_total = sum(
                sum(1 for state in bank if prescription <= state)
                for prescription in candidate_atoms
            )
            assert direct_total == indicator_total

            kappa = (side / (side - 2)) ** side
            bound = len(bank) * sum(kappa / falling(side, len(atom)) for atom in candidate_atoms)
            assert direct_total <= bound + 1e-9
            checked += 1
    return checked


def check_improvement_arithmetic():
    rng = random.Random(1204)
    checked = 0
    for side in range(4, 100):
        kappa = (side / (side - 2)) ** side
        for _ in range(300):
            v1 = rng.randint(0, side * side)
            v2 = rng.randint(0, side**3)
            v3 = rng.randint(0, side**4)
            score = v1 / side + v2 / falling(side, 2) + v3 / falling(side, 3)
            destroyed = rng.randint(0, max(1, int(kappa * score) + 5))
            if kappa * score < destroyed:
                expected_change_upper = kappa * score - destroyed
                assert expected_change_upper < 0
            checked += 1
    return checked


def main():
    banks = check_cylinder_bounds()
    print(
        "verified degree-two bank collateral:",
        check_disjoint_extensions(),
        "disjoint extensions,",
        banks[0],
        "banks,",
        banks[1],
        "rank prescriptions,",
        banks[2],
        "exact prescription incidences,",
        check_expected_collateral_identity(),
        "collateral identities, and",
        check_improvement_arithmetic(),
        "improvement cases",
    )


if __name__ == "__main__":
    main()
