#!/usr/bin/env python3
"""Finite checks for CMR727--CMR733."""

from itertools import combinations, permutations
import random


def edges(permutation):
    return {(index, permutation[index]) for index in range(len(permutation))}


def perfect_matchings(side, host):
    return [
        permutation
        for permutation in permutations(range(side))
        if edges(permutation) <= host
    ]


def hall_witnesses(side, host):
    for size in range(1, side + 1):
        for source_tuple in combinations(range(side), size):
            sources = set(source_tuple)
            targets = {
                target
                for source, target in host
                if source in sources
            }
            if len(targets) < len(sources):
                yield sources, targets


def check_case(side, host, old_matching, essential_edge):
    matchings = perfect_matchings(side, host)
    assert matchings
    assert all(
        essential_edge in edges(permutation)
        for permutation in matchings
    )
    reduced = set(host)
    reduced.discard(essential_edge)
    assert not perfect_matchings(side, reduced)
    witnesses = list(hall_witnesses(side, reduced))
    assert witnesses
    for sources, targets in witnesses:
        deficiency = len(sources) - len(targets)
        batch = {
            (source, target)
            for source, target in old_matching
            if source in sources and target not in targets
        }
        assert len(batch) >= deficiency
        assert batch <= (old_matching - host)
        assert len({source for source, _ in batch}) == len(batch)
        assert len({target for _, target in batch}) == len(batch)


def exhaustive_small():
    checked = 0
    for side in range(1, 4):
        universe = [
            (source, target)
            for source in range(side)
            for target in range(side)
        ]
        all_permutations = list(permutations(range(side)))
        for old_permutation in all_permutations:
            old_matching = edges(old_permutation)
            for mask in range(1 << len(universe)):
                host = {
                    universe[index]
                    for index in range(len(universe))
                    if (mask >> index) & 1
                }
                matchings = perfect_matchings(side, host)
                if not matchings:
                    continue
                common = set.intersection(
                    *(edges(permutation) for permutation in matchings)
                )
                for essential_edge in common - old_matching:
                    check_case(
                        side,
                        host,
                        old_matching,
                        essential_edge,
                    )
                    checked += 1
    return checked


def sampled_side_four():
    rng = random.Random(20260726)
    side = 4
    universe = [
        (source, target)
        for source in range(side)
        for target in range(side)
    ]
    all_permutations = list(permutations(range(side)))
    checked = 0
    for _ in range(5000):
        old_matching = edges(rng.choice(all_permutations))
        host = {edge for edge in universe if rng.random() < 0.5}
        matchings = perfect_matchings(side, host)
        if not matchings:
            continue
        common = set.intersection(
            *(edges(permutation) for permutation in matchings)
        )
        candidates = list(common - old_matching)
        if not candidates:
            continue
        essential_edge = rng.choice(candidates)
        check_case(side, host, old_matching, essential_edge)
        checked += 1
    return checked


def arithmetic_checks():
    checked = 0
    for matching_size in range(1, 100):
        for deficiency_threshold in range(1, matching_size + 1):
            for recurrence_threshold in range(2, 10):
                bound = (
                    (recurrence_threshold - 1)
                    * matching_size
                    // deficiency_threshold
                )
                assert bound * deficiency_threshold <= (
                    recurrence_threshold - 1
                ) * matching_size
                checked += 1
    return checked


def main():
    exhaustive = exhaustive_small()
    sampled = sampled_side_four()
    arithmetic = arithmetic_checks()
    print(
        "verified essential-return Hall batches:",
        exhaustive,
        "exhaustive cases,",
        sampled,
        "sampled side-four cases, and",
        arithmetic,
        "incidence bounds",
    )


if __name__ == "__main__":
    main()
