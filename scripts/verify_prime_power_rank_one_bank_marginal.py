#!/usr/bin/env python3
"""Finite checks for CMR1230--CMR1237."""

from itertools import combinations, permutations
from math import ceil, comb, gcd
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


def secant_weights(opposite, old_matching, graph):
    weights = {edge: 0 for edge in graph}
    opposite_pairs = list(combinations(opposite, 2))
    for edge in graph:
        if edge in old_matching:
            continue
        for first, second in opposite_pairs:
            if line_key(first, second) == line_key(first, edge):
                weights[edge] += 1
    return weights


def direct_rank_one_new(opposite, old_matching, response):
    old_state = set(opposite) | set(old_matching)
    count = 0
    for first, second in combinations(opposite, 2):
        key = line_key(first, second)
        for edge in response:
            triple = {first, second, edge}
            if edge not in old_matching and line_key(first, edge) == key:
                assert not triple <= old_state
                count += 1
    return count


def check_rank_one_identity_and_marginals():
    rng = random.Random(1230)
    checked = 0
    rank_one_total = 0
    for side in range(4, 8):
        opposite = matching(tuple(range(side)))
        old_list = derangements(side)
        if side >= 6:
            old_list = rng.sample(old_list, min(24, len(old_list)))
        complete = {(row, column) for row in range(side) for column in range(side)}
        for old_permutation in old_list:
            old_matching = matching(old_permutation)
            target_edge = rng.choice(tuple(old_matching))
            extensions = [
                permutation
                for permutation in derangements(side)
                if target_edge in matching(permutation)
            ]
            extensions = rng.sample(extensions, min(4, len(extensions)))
            for forbidden in extensions:
                bank = response_bank(side, forbidden)
                graph = complete - set(opposite) - set(matching(forbidden))
                weights = secant_weights(opposite, old_matching, graph)

                state_weights = {state: sum(weights[edge] for edge in state) for state in bank}
                for state in bank:
                    direct = direct_rank_one_new(opposite, old_matching, state)
                    assert direct == state_weights[state]
                    rank_one_total += direct

                raw = [rng.random() for _ in bank]
                total_raw = sum(raw)
                probabilities = [value / total_raw for value in raw]
                marginals = {edge: 0.0 for edge in graph}
                for state, probability in zip(bank, probabilities):
                    for edge in state:
                        marginals[edge] += probability

                for row in range(side):
                    assert abs(
                        sum(
                            marginals[(row, column)]
                            for column in range(side)
                            if (row, column) in graph
                        )
                        - 1
                    ) < 1e-10
                for column in range(side):
                    assert abs(
                        sum(
                            marginals[(row, column)]
                            for row in range(side)
                            if (row, column) in graph
                        )
                        - 1
                    ) < 1e-10

                expectation = sum(
                    probability * state_weights[state]
                    for state, probability in zip(bank, probabilities)
                )
                marginal_expectation = sum(weights[edge] * marginals[edge] for edge in graph)
                assert abs(expectation - marginal_expectation) < 1e-10

                row_bound = sum(
                    max(
                        weights[(row, column)]
                        for column in range(side)
                        if (row, column) in graph
                    )
                    for row in range(side)
                )
                column_bound = sum(
                    max(
                        weights[(row, column)]
                        for row in range(side)
                        if (row, column) in graph
                    )
                    for column in range(side)
                )
                maximum_matching_weight = max(state_weights.values())
                assert expectation <= maximum_matching_weight + 1e-10
                assert maximum_matching_weight <= min(row_bound, column_bound)
                assert all(weights[edge] == 0 for edge in graph & set(old_matching))
                checked += 1
    return checked, rank_one_total


def check_heavy_edge_and_star_arithmetic():
    rng = random.Random(1235)
    checked = 0
    star_lines = 0
    for side in range(4, 200):
        for _ in range(300):
            edge_weights = [rng.randint(0, side * side) for _ in range(side * (side - 2))]
            row_bound = sum(
                max(edge_weights[row * (side - 2):(row + 1) * (side - 2)])
                for row in range(side)
            )
            maximum = max(edge_weights)
            assert maximum >= row_bound / side

            threshold = rng.randint(2, max(2, side))
            weight = rng.randint(0, side * side)
            maximum_line_contribution = comb(threshold, 2)
            required = ceil(weight / maximum_line_contribution)
            assert required * maximum_line_contribution >= weight
            star_lines += required
            checked += 1
    return checked, star_lines


def check_refined_expectation_arithmetic():
    rng = random.Random(1233)
    checked = 0
    improvements = 0
    for side in range(4, 200):
        kappa = (side / (side - 2)) ** side
        for _ in range(300):
            rank_one_bound = rng.random() * side * side
            c2 = rng.random() * side * side
            c3 = rng.random() * side * side
            missing = rng.randint(0, side * side)
            potential = rng.randint(0, 1000)
            destroyed = rng.randint(0, 2 * side * side)
            upper = rank_one_bound + kappa * (
                c2 + c3 + (potential + 1) * missing / side
            )
            if upper < destroyed:
                assert upper - destroyed < 0
                improvements += 1
            checked += 1
    return checked, improvements


def main():
    marginals = check_rank_one_identity_and_marginals()
    heavy = check_heavy_edge_and_star_arithmetic()
    refined = check_refined_expectation_arithmetic()
    print(
        "verified corrected rank-one bank marginals:",
        marginals[0],
        "response banks with",
        marginals[1],
        "new rank-one incidences,",
        heavy[0],
        "heavy-edge cases producing",
        heavy[1],
        "star-line units, and",
        refined[0],
        "refined expectation cases with",
        refined[1],
        "improvement certificates",
    )


if __name__ == "__main__":
    main()
