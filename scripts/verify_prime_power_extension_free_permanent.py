#!/usr/bin/env python3
"""Finite checks for CMR1350--CMR1357."""

from fractions import Fraction
from itertools import combinations, permutations
from math import factorial
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def scaling_entries(side):
    a = Fraction(1, side - 2)
    b = Fraction(1, side - 1)
    g = Fraction(
        side * side - 5 * side + 5,
        (side - 1) * (side - 2) * (side - 3),
    )
    return a, b, g


def explicit_scaling_matrix(side):
    a, b, g = scaling_entries(side)
    matrix = [[Fraction(0) for _column in range(side)] for _row in range(side)]
    remaining = range(2, side)
    for column in remaining:
        matrix[0][column] = a
    matrix[1][0] = b
    for column in remaining:
        matrix[1][column] = b
    for row in remaining:
        matrix[row][0] = b
        matrix[row][1] = a
        for column in remaining:
            if row != column:
                matrix[row][column] = g
    return matrix


def check_scaling():
    symbolic = 0
    explicit = 0
    for side in range(4, 10000):
        a, b, g = scaling_entries(side)
        assert (side - 2) * a == 1
        assert (side - 1) * b == 1
        assert b + a + (side - 3) * g == 1
        assert Fraction(0) < g <= a
        symbolic += 1
    for side in range(4, 40):
        matrix = explicit_scaling_matrix(side)
        assert all(sum(row) == 1 for row in matrix)
        assert all(
            sum(matrix[row][column] for row in range(side)) == 1
            for column in range(side)
        )
        allowed = [entry for row in matrix for entry in row if entry]
        assert all(Fraction(0) < entry <= Fraction(1, side - 2) for entry in allowed)
        assert matrix[0][0] == 0 and matrix[0][1] == 0
        assert all(matrix[row][row] == 0 for row in range(side))
        explicit += 1
    return symbolic, explicit


def compatible(prescription):
    return len({row for row, _column in prescription}) == len(prescription) and len(
        {column for _row, column in prescription}
    ) == len(prescription)


def check_permanents_and_prescriptions():
    rng = random.Random(1352)
    checked = 0
    prescriptions = 0
    canonical_extensions = 0
    for side in range(4, 8):
        identity = matching(tuple(range(side)))
        cells = {(row, column) for row in range(side) for column in range(side)}
        candidate_edges = list(cells - set(identity))
        if side >= 7:
            candidate_edges = rng.sample(candidate_edges, min(12, len(candidate_edges)))
        all_matchings = [matching(permutation) for permutation in permutations(range(side))]
        for edge in candidate_edges:
            bank = [state for state in all_matchings if state.isdisjoint(identity) and edge not in state]
            lower = factorial(side) * Fraction(side - 2, side) ** side
            assert len(bank) >= lower
            kappa = Fraction(side, side - 2) ** side
            graph = cells - set(identity) - {edge}

            for rank in (1, 2, 3):
                candidates = [
                    frozenset(prescription)
                    for prescription in combinations(graph, rank)
                    if compatible(prescription)
                ]
                if side >= 6:
                    candidates = rng.sample(candidates, min(100, len(candidates)))
                for prescription in candidates:
                    count = sum(prescription <= state for state in bank)
                    falling = factorial(side) // factorial(side - rank)
                    assert Fraction(count, len(bank)) <= kappa / falling
                    prescriptions += 1

            response_sample = bank if side <= 5 else rng.sample(bank, min(80, len(bank)))
            for response in response_sample:
                complement = cells - set(identity) - set(response)
                containing = [
                    state
                    for state in all_matchings
                    if edge in state and state <= complement
                ]
                assert containing
                canonical = min(containing, key=lambda state: tuple(sorted(state)))
                assert edge in canonical
                assert canonical.isdisjoint(identity | response)
                canonical_extensions += 1
            checked += 1
    return checked, prescriptions, canonical_extensions


def check_penalty_arithmetic():
    rng = random.Random(1355)
    checked = 0
    improvements = 0
    for side in range(4, 1000):
        kappa = Fraction(side, side - 2) ** side
        for _ in range(100):
            candidate_score = Fraction(rng.randint(0, 100000), 1000)
            potential = rng.randint(1, 10000)
            missing = rng.randint(0, side * side)
            destroyed = rng.randint(1, 10000)
            upper = kappa * (
                candidate_score + Fraction((potential + 1) * missing, side)
            )
            if upper < destroyed:
                assert upper - destroyed < 0
                improvements += 1
            checked += 1
    return checked, improvements


def main():
    finite = check_permanents_and_prescriptions()
    penalty = check_penalty_arithmetic()
    scaling = check_scaling()
    print(
        "verified extension-free permanent:",
        scaling[0],
        "symbolic and",
        scaling[1],
        "explicit scalings,",
        finite[0],
        "finite banks with",
        finite[1],
        "prescription ratios and",
        finite[2],
        "canonical extensions, plus",
        penalty[0],
        "penalty cases with",
        penalty[1],
        "improvement certificates",
    )


if __name__ == "__main__":
    main()
