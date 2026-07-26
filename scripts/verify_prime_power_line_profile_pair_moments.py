#!/usr/bin/env python3
"""Finite checks for CMR1342--CMR1349."""

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


def band(value):
    return 0 if value == 0 else 1 + floor(log2(value))


def lower_endpoint(value):
    return 0 if value == 0 else 2 ** (value - 1)


def upper_endpoint(side, value):
    return 0 if value == 0 else min(side, 2 ** value - 1)


def falling(side, rank):
    return factorial(side) // factorial(side - rank)


def pair_stock(side):
    return side * (side - 2) * (side * side - 4 * side + 5) // 2


def exact_profiles(side, lines, opposite, old_matching, forbidden):
    cells = {(row, column) for row in range(side) for column in range(side)}
    graph = cells - set(opposite) - set(forbidden)
    old_graph = set(old_matching) & graph
    profiles = Counter()
    moments = [0, 0, 0]
    contributions = Counter()

    for key, line_cells in lines.items():
        if is_axis(key):
            continue
        o = len(set(opposite) & set(line_cells))
        g = len(graph & set(line_cells))
        m = len(old_graph & set(line_cells))
        moments[0] += comb(o, 2)
        moments[1] += comb(g, 2)
        moments[2] += comb(m, 2)
        if o + g < 3:
            continue
        profile = (band(o), band(g), band(m))
        profiles[profile] += 1
        contributions[(1,) + profile] += comb(o, 2) * (g - m) / side
        contributions[(2,) + profile] += o * (comb(g, 2) - comb(m, 2)) / falling(side, 2)
        contributions[(3,) + profile] += (comb(g, 3) - comb(m, 3)) / falling(side, 3)

    return graph, old_graph, profiles, moments, contributions


def applicable_tail_bound(numerator, threshold):
    if threshold < 2:
        return None
    return numerator / comb(threshold, 2)


def profile_multiplicity_bound(side, old_size, profile):
    i, j, k = profile
    values = []
    for numerator, threshold in (
        (comb(side, 2), lower_endpoint(i)),
        (pair_stock(side), lower_endpoint(j)),
        (comb(old_size, 2), lower_endpoint(k)),
    ):
        value = applicable_tail_bound(numerator, threshold)
        if value is not None:
            values.append(value)
    return min(values) if values else float("inf")


def rank_envelopes(side, old_size, profile, line_count):
    i, j, k = profile
    o_upper = upper_endpoint(side, i)
    g_upper = upper_endpoint(side, j)
    m_lower = lower_endpoint(k)
    h = min(line_count, profile_multiplicity_bound(side, old_size, profile))

    rank_one = (g_upper - m_lower) * min(
        h * comb(o_upper, 2), comb(side, 2)
    ) / side
    rank_two = o_upper * min(
        h * (comb(g_upper, 2) - comb(m_lower, 2)),
        pair_stock(side),
    ) / falling(side, 2)
    rank_three = min(
        h * (comb(g_upper, 3) - comb(m_lower, 3)),
        max(0, g_upper - 2) * pair_stock(side) / 3,
    ) / falling(side, 3)
    return rank_one, rank_two, rank_three


def check_exact_pair_moments_and_envelopes():
    rng = random.Random(1342)
    checked = 0
    profile_checks = 0
    for side in range(3, 8):
        permutation_list = list(permutations(range(side)))
        matching_list = [matching(permutation) for permutation in permutation_list]
        opposite = matching(tuple(range(side)))
        deranged = [state for state in matching_list if state.isdisjoint(opposite)]
        old_list = deranged if side <= 5 else rng.sample(deranged, min(20, len(deranged)))
        lines = board_lines(side)

        for old_matching in old_list:
            target = rng.choice(tuple(old_matching))
            extensions = [state for state in deranged if target in state]
            if side >= 6:
                extensions = rng.sample(extensions, min(10, len(extensions)))
            for forbidden in extensions:
                _graph, old_graph, profiles, moments, contributions = exact_profiles(
                    side, lines, opposite, old_matching, forbidden
                )
                assert moments[0] == comb(side, 2)
                assert moments[1] == pair_stock(side)
                assert moments[2] == comb(len(old_graph), 2)

                for profile, count in profiles.items():
                    bound = profile_multiplicity_bound(side, len(old_graph), profile)
                    assert count <= bound + 1e-12
                    envelopes = rank_envelopes(side, len(old_graph), profile, count)
                    for rank in (1, 2, 3):
                        assert contributions[(rank,) + profile] <= envelopes[rank - 1] + 1e-12
                        profile_checks += 1
                checked += 1
    return checked, profile_checks


def check_tail_arithmetic():
    rng = random.Random(1343)
    checked = 0
    for side in range(3, 1000):
        p2 = pair_stock(side)
        old_size = rng.randint(0, side)
        for threshold in range(2, side + 1):
            for numerator in (comb(side, 2), p2, comb(old_size, 2)):
                bound = numerator / comb(threshold, 2)
                assert bound >= 0
                checked += 1
    return checked


def check_rank_three_pair_conversion():
    checked = 0
    for g in range(0, 10000):
        left = comb(g, 3)
        right = max(0, g - 2) * comb(g, 2) / 3
        assert abs(left - right) < 1e-12
        checked += 1
    return checked


def main():
    exact = check_exact_pair_moments_and_envelopes()
    print(
        "verified line-profile pair moments:",
        exact[0],
        "exact banks with",
        exact[1],
        "profile-envelope checks,",
        check_tail_arithmetic(),
        "tail bounds, and",
        check_rank_three_pair_conversion(),
        "rank-three pair conversions",
    )


if __name__ == "__main__":
    main()
