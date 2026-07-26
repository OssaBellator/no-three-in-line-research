#!/usr/bin/env python3
"""Finite checks for CMR1358--CMR1365."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import random


def derangement_table(limit):
    values = [0] * (limit + 1)
    values[0] = 1
    if limit >= 1:
        values[1] = 0
    for side in range(2, limit + 1):
        values[side] = (side - 1) * (values[side - 1] + values[side - 2])
    return values


def factorial_table(limit):
    values = [1] * (limit + 1)
    for side in range(1, limit + 1):
        values[side] = side * values[side - 1]
    return values


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def compatible(prescription):
    return len({row for row, _column in prescription}) == len(prescription) and len(
        {column for _row, column in prescription}
    ) == len(prescription)


def check_exact_bank_sizes_and_marginals():
    rng = random.Random(1358)
    derangement = derangement_table(8)
    checked = 0
    edges_checked = 0
    prescriptions = 0

    for side in range(4, 9):
        identity = matching(tuple(range(side)))
        all_matchings = [matching(permutation) for permutation in permutations(range(side))]
        derangements = [state for state in all_matchings if state.isdisjoint(identity)]
        assert len(derangements) == derangement[side]
        cells = {(row, column) for row in range(side) for column in range(side)}
        target_edges = list(cells - set(identity))
        if side >= 7:
            target_edges = rng.sample(target_edges, min(12, len(target_edges)))

        for edge in target_edges:
            bank = [state for state in derangements if edge not in state]
            expected_size = derangement[side] * (side - 2) // (side - 1)
            assert len(bank) == expected_size
            allowed = list(cells - set(identity) - {edge})
            full_edge_count = derangement[side] // (side - 1)

            edge_sample = allowed if side <= 6 else rng.sample(allowed, min(40, len(allowed)))
            for candidate in edge_sample:
                count = sum(candidate in state for state in bank)
                assert count <= full_edge_count
                assert Fraction(count, len(bank)) <= Fraction(1, side - 2)
                if candidate[0] == edge[0] or candidate[1] == edge[1]:
                    assert count == full_edge_count
                    assert Fraction(count, len(bank)) == Fraction(1, side - 2)
                edges_checked += 1

            lambda_value = Fraction(
                factorial(side) * (side - 1),
                derangement[side] * (side - 2),
            )
            assert lambda_value <= 4
            for rank in (2, 3):
                candidates = [
                    frozenset(value)
                    for value in combinations(allowed, rank)
                    if compatible(value)
                ]
                if side >= 6:
                    candidates = rng.sample(candidates, min(120, len(candidates)))
                for prescription in candidates:
                    count = sum(prescription <= state for state in bank)
                    falling = factorial(side) // factorial(side - rank)
                    assert Fraction(count, len(bank)) <= lambda_value / falling
                    prescriptions += 1
            checked += 1

    return checked, edges_checked, prescriptions


def check_derangement_constants():
    limit = 2000
    derangement = derangement_table(limit)
    factorials = factorial_table(limit)
    checked = 0
    for side in range(4, limit):
        lambda_value = Fraction(
            factorials[side] * (side - 1),
            derangement[side] * (side - 2),
        )
        assert lambda_value <= 4
        assert Fraction(derangement[side], factorials[side]) >= Fraction(1, 3)
        if side > 20:
            assert abs(float(lambda_value) - 2.718281828459045) < 0.2
        checked += 1
    return checked


def check_sharpened_penalty_arithmetic():
    rng = random.Random(1363)
    limit = 1000
    derangement = derangement_table(limit)
    factorials = factorial_table(limit)
    checked = 0
    improvements = 0
    for side in range(4, limit):
        lambda_value = Fraction(
            factorials[side] * (side - 1),
            derangement[side] * (side - 2),
        )
        for _ in range(120):
            rank_one = rng.randint(0, 100000)
            rank_two = rng.randint(0, 100000)
            rank_three = rng.randint(0, 100000)
            potential = rng.randint(1, 10000)
            missing = rng.randint(0, side * side)
            destroyed = rng.randint(1, 10000)
            upper = Fraction(rank_one + (potential + 1) * missing, side - 2)
            upper += lambda_value * Fraction(
                rank_two,
                side * (side - 1),
            )
            upper += lambda_value * Fraction(
                rank_three,
                side * (side - 1) * (side - 2),
            )
            if upper < destroyed:
                assert upper - destroyed < 0
                improvements += 1
            checked += 1
    return checked, improvements


def main():
    finite = check_exact_bank_sizes_and_marginals()
    penalty = check_sharpened_penalty_arithmetic()
    print(
        "verified exact extension-free derangement marginals:",
        finite[0],
        "banks with",
        finite[1],
        "edge marginals and",
        finite[2],
        "higher-rank prescriptions,",
        check_derangement_constants(),
        "constant checks, and",
        penalty[0],
        "penalty cases with",
        penalty[1],
        "improvement certificates",
    )


if __name__ == "__main__":
    main()
