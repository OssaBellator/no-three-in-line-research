#!/usr/bin/env python3
"""Finite checks for CMR770--CMR776."""

from itertools import combinations, permutations
import random


def edges(perm):
    return {(source, perm[source]) for source in range(len(perm))}


def perfect_matchings(side, host):
    return [
        edges(perm)
        for perm in permutations(range(side))
        if edges(perm) <= host
    ]


def contract_host(host, pair):
    used_left = {source for source, _ in pair}
    used_right = {target for _, target in pair}
    left = sorted({source for source, _ in host} - used_left)
    right = sorted({target for _, target in host} - used_right)
    left_index = {value: index for index, value in enumerate(left)}
    right_index = {value: index for index, value in enumerate(right)}
    residual = {
        (left_index[source], right_index[target])
        for source, target in host
        if source in left_index and target in right_index
    }
    return len(left), residual


def check_active_pair(side, host, pair):
    matchings = perfect_matchings(side, host)
    containing = [matching for matching in matchings if pair <= matching]
    if not containing:
        return False

    essential = set.intersection(*matchings)
    if not pair <= essential:
        nonessential = next(edge for edge in pair if edge not in essential)
        reduced = set(host)
        reduced.remove(nonessential)
        reduced_matchings = perfect_matchings(side, reduced)
        assert reduced_matchings
        assert all(not pair <= matching for matching in reduced_matchings)
    else:
        residual_side, residual = contract_host(host, pair)
        residual_matchings = perfect_matchings(residual_side, residual)
        assert len(matchings) == len(residual_matchings)
        assert all(pair <= matching for matching in matchings)
    return True


def exhaustive_small():
    checked = 0
    for side in range(1, 4):
        universe = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        for mask in range(1 << len(universe)):
            host = {
                universe[index]
                for index in range(len(universe))
                if (mask >> index) & 1
            }
            if not perfect_matchings(side, host):
                continue
            compatible_pairs = [
                set(pair)
                for pair in combinations(host, 2)
                if len({source for source, _ in pair}) == 2
                and len({target for _, target in pair}) == 2
            ]
            for pair in compatible_pairs:
                if check_active_pair(side, host, pair):
                    checked += 1
    return checked


def sampled_side_four():
    rng = random.Random(776)
    side = 4
    universe = [
        (source, target)
        for source in range(side)
        for target in range(side)
    ]
    checked = 0
    for _ in range(10000):
        host = {edge for edge in universe if rng.random() < 0.55}
        matchings = perfect_matchings(side, host)
        if not matchings:
            continue
        matching = rng.choice(matchings)
        pair = set(rng.sample(sorted(matching), 2))
        assert check_active_pair(side, host, pair)
        checked += 1
    return checked


def recurrence_arithmetic():
    checked = 0
    for occurrences in range(1, 10000):
        largest_type = (occurrences + 5) // 6
        assert largest_type * 6 >= occurrences
        for threshold in range(2, 20):
            if occurrences > 6 * (threshold - 1):
                assert largest_type >= threshold
            checked += 1
    return checked


def main():
    print(
        "verified recurrent labelled target pairs:",
        exhaustive_small(),
        "exhaustive active pairs,",
        sampled_side_four(),
        "sampled side-four pairs, and",
        recurrence_arithmetic(),
        "recurrence cases",
    )


if __name__ == "__main__":
    main()
