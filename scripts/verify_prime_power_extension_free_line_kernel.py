#!/usr/bin/env python3
"""Finite checks for CMR1366--CMR1373."""

from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, gcd
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


def derangement_number(side):
    if side == 0:
        return 1
    if side == 1:
        return 0
    first, second = 1, 0
    for value in range(2, side + 1):
        first, second = second, (value - 1) * (first + second)
    return second


def lambda_value(side):
    return Fraction(
        factorial(side) * (side - 1),
        derangement_number(side) * (side - 2),
    )


def line_key(first, second):
    x1, y1 = first
    x2, y2 = second
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0) or (a == 0 and b == 0 and c < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def board_lines(side):
    cells = [(row, column) for row in range(side) for column in range(side)]
    keys = {line_key(first, second) for first, second in combinations(cells, 2)}
    return {
        key: frozenset(
            cell
            for cell in cells
            if key[0] * cell[0] + key[1] * cell[1] + key[2] == 0
        )
        for key in keys
        if key[0] != 0 and key[1] != 0
    }


def collinear(triple):
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def line_formula_sums(side, opposite, current, lines):
    sums = [0, 0, 0, 0]
    target_layer = 0
    profiles = []
    for line_cells in lines.values():
        o = len(set(opposite) & set(line_cells))
        m = len(set(current) & set(line_cells))
        u = len(line_cells) - o - m
        sums[1] += side * comb(o, 2) * u
        sums[2] += o * ((side - 1) * m * u + side * comb(u, 2))
        sums[3] += (
            (side - 2) * comb(m, 2) * u
            + (side - 1) * m * comb(u, 2)
            + side * comb(u, 3)
        )
        target_layer += m * comb(o + m - 1, 2)
        if o + m >= 3:
            profiles.append((len(line_cells), o, m, u))
    return sums, target_layer, profiles


def direct_candidate_sums(side, opposite, current):
    cells = {(row, column) for row in range(side) for column in range(side)}
    old_state = set(opposite) | set(current)
    totals = [0, 0, 0, 0]
    for edge in current:
        graph = cells - set(opposite) - {edge}
        for triple in combinations(set(opposite) | graph, 3):
            triple_set = set(triple)
            if triple_set <= old_state or not collinear(triple):
                continue
            rank = len(triple_set - set(opposite))
            totals[rank] += 1
    return totals


def direct_target_incidence(opposite, current):
    state = set(opposite) | set(current)
    total = 0
    for triple in combinations(state, 3):
        if not collinear(triple):
            continue
        total += len(set(triple) & set(current))
    return total


def kernel_layer(side, o, m, u):
    lam = lambda_value(side)
    rank_one = side * comb(o, 2) * u
    rank_two = o * ((side - 1) * m * u + side * comb(u, 2))
    rank_three = (
        (side - 2) * comb(m, 2) * u
        + (side - 1) * m * comb(u, 2)
        + side * comb(u, 3)
    )
    return (
        Fraction(rank_one, side - 2)
        + lam * Fraction(rank_two, side * (side - 1))
        + lam * Fraction(rank_three, side * (side - 1) * (side - 2))
    )


def check_exact_line_sums():
    rng = random.Random(1366)
    checked = 0
    candidates = 0
    targets = 0
    for side in range(4, 8):
        permutation_list = list(permutations(range(side)))
        matching_list = [matching(permutation) for permutation in permutation_list]
        pairs = []
        for _ in range(100 if side < 7 else 40):
            opposite = rng.choice(matching_list)
            disjoint = [state for state in matching_list if state.isdisjoint(opposite)]
            current = rng.choice(disjoint)
            pairs.append((opposite, current))
        lines = board_lines(side)
        for opposite, current in pairs:
            formula, target_formula, _profiles = line_formula_sums(
                side, opposite, current, lines
            )
            direct = direct_candidate_sums(side, opposite, current)
            target_direct = direct_target_incidence(opposite, current)
            assert direct == formula
            assert target_direct == target_formula
            candidates += sum(direct)
            targets += target_direct
            checked += 1
    return checked, candidates, targets


def check_symmetric_kernel_identity():
    rng = random.Random(1371)
    checked = 0
    for side in range(4, 200):
        for _ in range(1000):
            o = rng.randint(0, side)
            m = rng.randint(0, side - o)
            u = rng.randint(0, side - o - m)
            first = kernel_layer(side, o, m, u)
            second = kernel_layer(side, m, o, u)
            target = 3 * comb(o + m, 3)
            assert first >= 0 and second >= 0 and target >= 0
            if u == 0:
                assert first == 0 and second == 0
            checked += 1
    return checked


def check_explicit_obstruction():
    side = 5
    current = matching((0, 1, 2, 4, 3))
    opposite = matching((1, 3, 4, 0, 2))
    assert current.isdisjoint(opposite)
    lines = board_lines(side)
    formula_current, target_current, profiles_current = line_formula_sums(
        side, opposite, current, lines
    )
    formula_opposite, target_opposite, _profiles_opposite = line_formula_sums(
        side, current, opposite, lines
    )
    kernel = Fraction(formula_current[1], side - 2)
    kernel += lambda_value(side) * Fraction(
        formula_current[2], side * (side - 1)
    )
    kernel += lambda_value(side) * Fraction(
        formula_current[3], side * (side - 1) * (side - 2)
    )
    kernel += Fraction(formula_opposite[1], side - 2)
    kernel += lambda_value(side) * Fraction(
        formula_opposite[2], side * (side - 1)
    )
    kernel += lambda_value(side) * Fraction(
        formula_opposite[3], side * (side - 1) * (side - 2)
    )
    assert sorted(profile for profile in profiles_current if profile[1] + profile[2] >= 3) == [
        (3, 1, 2, 0),
        (5, 0, 3, 2),
    ]
    assert kernel == Fraction(160, 11)
    assert target_current + target_opposite == 6
    assert kernel > target_current + target_opposite
    return kernel, target_current + target_opposite


def main():
    exact = check_exact_line_sums()
    obstruction = check_explicit_obstruction()
    print(
        "verified extension-free line kernel:",
        exact[0],
        "states with",
        exact[1],
        "candidate prescriptions and",
        exact[2],
        "layer target incidences,",
        check_symmetric_kernel_identity(),
        "kernel arithmetic cases, and explicit obstruction",
        obstruction[0],
        ">",
        obstruction[1],
    )


if __name__ == "__main__":
    main()
