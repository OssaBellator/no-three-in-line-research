#!/usr/bin/env python3
"""Finite checks for corrected CMR727--CMR733 unit Hall walls."""

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


def maximum_matching_size(side, host):
    best = 0
    for size in range(1, side + 1):
        for sources in combinations(range(side), size):
            for targets in permutations(range(side), size):
                candidate = set(zip(sources, targets))
                if candidate <= host:
                    best = size
    return best


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


def minimal_hall_witness(side, host):
    witnesses = list(hall_witnesses(side, host))
    minimal = []
    for sources, targets in witnesses:
        if not any(
            other_sources < sources
            for other_sources, _ in witnesses
        ):
            minimal.append((sources, targets))
    return min(
        minimal,
        key=lambda item: tuple(sorted(item[0])),
    )


def check_case(side, host, old_matching, essential_edge):
    matchings = perfect_matchings(side, host)
    assert matchings
    assert all(
        essential_edge in edges(permutation)
        for permutation in matchings
    )

    source_endpoint, target_endpoint = essential_edge
    reduced = set(host)
    reduced.discard(essential_edge)
    assert not perfect_matchings(side, reduced)
    assert maximum_matching_size(side, reduced) == side - 1

    witnesses = list(hall_witnesses(side, reduced))
    assert witnesses
    for sources, targets in witnesses:
        assert len(sources) - len(targets) == 1
        assert source_endpoint in sources
        assert target_endpoint not in targets
        neighbours_in_host = {
            target
            for source, target in host
            if source in sources
        }
        assert neighbours_in_host == targets | {target_endpoint}

        missing = {
            (source, target)
            for source, target in old_matching
            if source in sources and target not in targets
        }
        assert missing
        assert missing <= (old_matching - host)

    sources, targets = minimal_hall_witness(side, reduced)
    for source in sources:
        neighbours_without_source = {
            target
            for left, target in reduced
            if left in sources - {source}
        }
        assert neighbours_without_source == targets

    if len(sources) == 1:
        assert sources == {source_endpoint}
        assert not targets
    else:
        for target in targets:
            degree_from_wall = sum(
                1
                for source in sources
                if (source, target) in reduced
            )
            assert degree_from_wall >= 2


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


def main():
    exhaustive = exhaustive_small()
    sampled = sampled_side_four()
    print(
        "verified essential-return unit Hall walls:",
        exhaustive,
        "exhaustive cases and",
        sampled,
        "sampled side-four cases",
    )


if __name__ == "__main__":
    main()
