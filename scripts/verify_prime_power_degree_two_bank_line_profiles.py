#!/usr/bin/env python3
"""Finite checks for CMR1334--CMR1341."""

from collections import Counter
from itertools import combinations, permutations
from math import comb, factorial, floor, gcd, log2
import random


def matching(permutation):
    return frozenset((row, permutation[row]) for row in range(len(permutation)))


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
    }


def is_axis(key):
    return key[0] == 0 or key[1] == 0


def collinear(triple):
    return line_key(triple[0], triple[1]) == line_key(triple[0], triple[2])


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def band(value):
    return 0 if value == 0 else 1 + floor(log2(value))


def direct_new_ranks(opposite, old_matching, response):
    old_state = set(opposite) | set(old_matching)
    new_state = set(opposite) | set(response)
    ranks = [0, 0, 0, 0]
    for triple in combinations(new_state, 3):
        triple_set = set(triple)
        if triple_set <= old_state or not collinear(triple):
            continue
        ranks[len(triple_set - set(opposite))] += 1
    return ranks


def line_profile_counts(side, lines, opposite, old_matching, forbidden):
    cells = {(row, column) for row in range(side) for column in range(side)}
    graph = cells - set(opposite) - set(forbidden)
    old_graph = set(old_matching) & graph
    ranks = [0, 0, 0, 0]
    histogram = Counter()
    band_contribution = Counter()

    for key, line_cells in lines.items():
        o = len(set(opposite) & set(line_cells))
        g = len(graph & set(line_cells))
        m = len(old_graph & set(line_cells))
        if is_axis(key):
            assert o <= 1
            continue
        if o + g < 3:
            continue
        histogram[(o, g, m)] += 1
        values = (
            comb(o, 2) * (g - m),
            o * (comb(g, 2) - comb(m, 2)),
            comb(g, 3) - comb(m, 3),
        )
        for rank, value in enumerate(values, 1):
            ranks[rank] += value
            band_contribution[(rank, band(o), band(g), band(m))] += value / falling(side, rank)
    return graph, ranks, histogram, band_contribution


def check_exact_profiles():
    rng = random.Random(1336)
    checked = 0
    prescriptions = 0
    profiles = 0
    response_occurrences = 0

    for side in range(3, 7):
        permutation_list = list(permutations(range(side)))
        matching_list = [matching(permutation) for permutation in permutation_list]
        opposite = matching(tuple(range(side)))
        deranged = [state for state in matching_list if state.isdisjoint(opposite)]
        old_list = deranged if side <= 5 else rng.sample(deranged, 20)
        lines = board_lines(side)

        for old_matching in old_list:
            target_edge = rng.choice(tuple(old_matching))
            extensions = [state for state in deranged if target_edge in state]
            if side >= 6:
                extensions = rng.sample(extensions, min(12, len(extensions)))
            for forbidden in extensions:
                graph, profile_ranks, histogram, bands = line_profile_counts(
                    side, lines, opposite, old_matching, forbidden
                )
                responses = [state for state in matching_list if state <= graph]
                direct_totals = [0, 0, 0, 0]
                for response in responses:
                    ranks = direct_new_ranks(opposite, old_matching, response)
                    for rank in (1, 2, 3):
                        direct_totals[rank] += ranks[rank]

                # A rank-r prescription has at most (n-r)! completions in the
                # restricted response graph.  Equality is not assumed.
                for rank in (1, 2, 3):
                    assert direct_totals[rank] <= profile_ranks[rank] * factorial(side - rank)

                score = sum(profile_ranks[rank] / falling(side, rank) for rank in (1, 2, 3))
                assert abs(score - sum(bands.values())) < 1e-12
                prescriptions += sum(profile_ranks)
                response_occurrences += sum(direct_totals)
                profiles += len(histogram)
                checked += 1

    return checked, prescriptions, profiles, response_occurrences


def check_axis_and_nonaxis_compatibility():
    checked = 0
    subsets = 0
    for side in range(2, 11):
        for key, cells in board_lines(side).items():
            if is_axis(key):
                checked += 1
                continue
            cells = list(cells)
            assert len({row for row, _column in cells}) == len(cells)
            assert len({column for _row, column in cells}) == len(cells)
            for rank in range(2, min(4, len(cells)) + 1):
                for subset in combinations(cells, rank):
                    assert len({row for row, _column in subset}) == rank
                    assert len({column for _row, column in subset}) == rank
                    subsets += 1
            checked += 1
    return checked, subsets


def check_dyadic_class_counts():
    checked = 0
    for side in range(1, 10000):
        bands = {band(value) for value in range(side + 1)}
        bound = 2 + floor(log2(side))
        assert len(bands) == bound
        assert 3 * len(bands) ** 3 == 3 * bound ** 3
        checked += 1
    return checked


def check_band_concentration():
    rng = random.Random(1340)
    checked = 0
    for class_count in range(1, 100):
        for _ in range(1000):
            values = [rng.random() * 100 for _class in range(class_count)]
            total = sum(values)
            assert max(values) + 1e-12 >= total / class_count
            checked += 1
    return checked


def main():
    exact = check_exact_profiles()
    geometry = check_axis_and_nonaxis_compatibility()
    print(
        "verified line-profile classes:",
        exact[0],
        "banks with",
        exact[1],
        "candidate prescriptions,",
        exact[3],
        "response occurrences and",
        exact[2],
        "exact profiles,",
        geometry[0],
        "line checks over",
        geometry[1],
        "compatible subsets,",
        check_dyadic_class_counts(),
        "dyadic side counts, and",
        check_band_concentration(),
        "band concentration cases",
    )


if __name__ == "__main__":
    main()
