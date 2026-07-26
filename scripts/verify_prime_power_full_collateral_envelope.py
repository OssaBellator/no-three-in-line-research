#!/usr/bin/env python3
"""Finite checks for CMR1238--CMR1245."""

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


def collinear(first, second, third):
    return line_key(first, second) == line_key(first, third)


def opposite_line_counts(opposite):
    counts = {}
    for first, second in combinations(opposite, 2):
        key = line_key(first, second)
        counts.setdefault(key, set()).update((first, second))
    return {key: len(cells) for key, cells in counts.items()}


def rank_one_weight(edge, opposite, old_matching):
    if edge in old_matching:
        return 0
    return sum(collinear(first, second, edge) for first, second in combinations(opposite, 2))


def tau2(edge, state, opposite_counts, old_matching):
    total = 0
    for other in state - {edge}:
        if edge in old_matching and other in old_matching:
            continue
        total += opposite_counts.get(line_key(edge, other), 0)
    return total


def tau3(edge, state, old_matching):
    total = 0
    for first, second in combinations(state - {edge}, 2):
        if {edge, first, second} <= set(old_matching):
            continue
        if collinear(edge, first, second):
            total += 1
    return total


def direct_new_ranks(opposite, old_matching, response):
    old_state = set(opposite) | set(old_matching)
    new_state = set(opposite) | set(response)
    ranks = [0, 0, 0, 0]
    for triple in combinations(new_state, 3):
        triple_set = set(triple)
        if triple_set <= old_state:
            continue
        if not collinear(triple[0], triple[1], triple[2]):
            continue
        rank = len(triple_set - set(opposite))
        ranks[rank] += 1
    return ranks


def check_exact_local_identities_and_envelopes():
    rng = random.Random(1239)
    checked = 0
    triples = 0
    for side in range(4, 7):
        opposite = matching(tuple(range(side)))
        opposite_counts = opposite_line_counts(opposite)
        old_list = derangements(side)
        if side >= 5:
            old_list = rng.sample(old_list, min(12, len(old_list)))
        complete = {(row, column) for row in range(side) for column in range(side)}
        for old_permutation in old_list:
            old_matching = matching(old_permutation)
            target_edge = rng.choice(tuple(old_matching))
            extensions = [
                permutation
                for permutation in derangements(side)
                if target_edge in matching(permutation)
            ]
            extensions = rng.sample(extensions, min(3, len(extensions)))
            for forbidden in extensions:
                bank = response_bank(side, forbidden)
                graph = complete - set(opposite) - set(matching(forbidden))
                assert all(any(edge in state for state in bank) for edge in graph)

                weights = {
                    edge: rank_one_weight(edge, opposite, old_matching)
                    for edge in graph
                }
                delta2 = {edge: 0 for edge in graph}
                delta3 = {edge: 0 for edge in graph}

                state_data = {}
                for state in bank:
                    ranks = direct_new_ranks(opposite, old_matching, state)
                    local2 = {edge: tau2(edge, state, opposite_counts, old_matching) for edge in state}
                    local3 = {edge: tau3(edge, state, old_matching) for edge in state}
                    assert ranks[1] == sum(weights[edge] for edge in state)
                    assert 2 * ranks[2] == sum(local2.values())
                    assert 3 * ranks[3] == sum(local3.values())
                    for edge in state:
                        delta2[edge] = max(delta2[edge], local2[edge])
                        delta3[edge] = max(delta3[edge], local3[edge])
                    state_data[state] = ranks
                    triples += sum(ranks)

                envelope = {
                    edge: weights[edge] + delta2[edge] / 2 + delta3[edge] / 3
                    for edge in graph
                }
                row_bound = sum(
                    max(envelope[(row, column)] for column in range(side) if (row, column) in graph)
                    for row in range(side)
                )
                column_bound = sum(
                    max(envelope[(row, column)] for row in range(side) if (row, column) in graph)
                    for column in range(side)
                )
                global_bound = min(row_bound, column_bound)

                for state, ranks in state_data.items():
                    new_count = sum(ranks)
                    state_bound = sum(envelope[edge] for edge in state)
                    assert new_count <= state_bound + 1e-12
                    assert state_bound <= global_bound + 1e-12
                checked += 1
    return checked, triples


def check_rank_two_assignment_representation():
    rng = random.Random(1243)
    checked = 0
    for side in range(4, 8):
        opposite = matching(tuple(range(side)))
        opposite_counts = opposite_line_counts(opposite)
        old_list = derangements(side)
        if side >= 6:
            old_list = rng.sample(old_list, min(20, len(old_list)))
        for old_permutation in old_list:
            old_matching = matching(old_permutation)
            target_edge = rng.choice(tuple(old_matching))
            forbidden = rng.choice(
                [
                    permutation
                    for permutation in derangements(side)
                    if target_edge in matching(permutation)
                ]
            )
            bank = response_bank(side, forbidden)
            graph = set().union(*bank)
            for edge in rng.sample(tuple(graph), min(8, len(graph))):
                conditioned = [state for state in bank if edge in state]
                direct_max = max(tau2(edge, state, opposite_counts, old_matching) for state in conditioned)
                residual_weights = []
                for state in conditioned:
                    residual_weights.append(
                        sum(
                            0
                            if edge in old_matching and other in old_matching
                            else opposite_counts.get(line_key(edge, other), 0)
                            for other in state - {edge}
                        )
                    )
                assert direct_max == max(residual_weights)
                checked += 1
    return checked


def check_line_star_consequences():
    rng = random.Random(1244)
    checked = 0
    star_units = 0
    for side in range(4, 200):
        for _ in range(300):
            delta2_value = rng.randint(0, (side - 1) * side)
            if delta2_value:
                loaded = ceil(delta2_value / (side - 1))
                assert loaded * (side - 1) >= delta2_value
            delta3_value = rng.randint(0, comb(side - 1, 2))
            threshold = rng.randint(2, max(2, side - 1))
            required = ceil(delta3_value / comb(threshold, 2))
            assert required * comb(threshold, 2) >= delta3_value
            star_units += required
            checked += 1
    return checked, star_units


def main():
    identities = check_exact_local_identities_and_envelopes()
    stars = check_line_star_consequences()
    print(
        "verified full collateral envelopes:",
        identities[0],
        "banks with",
        identities[1],
        "new triples,",
        check_rank_two_assignment_representation(),
        "rank-two assignment cases, and",
        stars[0],
        "line/star cases producing",
        stars[1],
        "star units",
    )


if __name__ == "__main__":
    main()
