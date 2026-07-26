#!/usr/bin/env python3
"""Finite checks for CMR1150--CMR1157."""

from itertools import combinations, permutations
import random


def all_matchings(side):
    return [
        frozenset((left, permutation[left]) for left in range(side))
        for permutation in permutations(range(side))
    ]


def matching_family(host, matchings):
    host = set(host)
    return {matching for matching in matchings if set(matching) <= host}


def hall_witnesses(side, host):
    adjacency = {left: set() for left in range(side)}
    for left, right in host:
        adjacency[left].add(right)
    result = []
    for size in range(1, side + 1):
        for source in combinations(range(side), size):
            neighbours = set().union(*(adjacency[left] for left in source))
            if len(neighbours) < size:
                result.append((frozenset(source), frozenset(neighbours)))
    return result


def minimal_blocker(host, blocker, matchings):
    if matching_family(set(host) - set(blocker), matchings):
        return False
    return all(
        matching_family(set(host) - (set(blocker) - {edge}), matchings)
        for edge in blocker
    )


def verify_case(side, host, blocker, matchings):
    residual = set(host) - set(blocker)
    witnesses = hall_witnesses(side, residual)
    assert witnesses
    private_matchings = []
    for source, neighbours in witnesses:
        outside = set(range(side)) - set(neighbours)
        cut = {
            (left, right)
            for left in source
            for right in outside
            if (left, right) in host
        }
        assert cut == set(blocker)
        assert len(source) - len(neighbours) == 1
    for edge in blocker:
        restored_host = residual | {edge}
        family = matching_family(restored_host, matchings)
        assert family
        assert all(edge in matching for matching in family)
        witness = min(family, key=lambda matching: tuple(sorted(matching)))
        assert set(witness) & set(blocker) == {edge}
        private_matchings.append(witness)
    assert len(private_matchings) == len(set(private_matchings))
    return len(witnesses), len(private_matchings)


def check_exhaustive_small_hosts():
    checked = 0
    witness_count = 0
    private_count = 0
    for side in range(1, 4):
        universe = [(left, right) for left in range(side) for right in range(side)]
        matchings = all_matchings(side)
        for host_mask in range(1 << len(universe)):
            host = {
                universe[index]
                for index in range(len(universe))
                if host_mask & (1 << index)
            }
            if not matching_family(host, matchings):
                continue
            host_edges = tuple(host)
            for blocker_mask in range(1, 1 << len(host_edges)):
                blocker = {
                    host_edges[index]
                    for index in range(len(host_edges))
                    if blocker_mask & (1 << index)
                }
                if not minimal_blocker(host, blocker, matchings):
                    continue
                witnesses, private = verify_case(side, host, blocker, matchings)
                witness_count += witnesses
                private_count += private
                checked += 1
    return checked, witness_count, private_count


def check_sampled_larger_hosts():
    rng = random.Random(1150)
    checked = 0
    for side in (4, 5):
        universe = {(left, right) for left in range(side) for right in range(side)}
        matchings = all_matchings(side)
        for _ in range(10000):
            host = set(rng.sample(tuple(universe), rng.randint(side, len(universe))))
            if not matching_family(host, matchings):
                continue
            # Construct a blocker, then greedily minimize it.
            blocker = set(rng.sample(tuple(host), rng.randint(1, len(host))))
            if matching_family(host - blocker, matchings):
                continue
            for edge in list(blocker):
                trial = blocker - {edge}
                if not matching_family(host - trial, matchings):
                    blocker = trial
            assert blocker and minimal_blocker(host, blocker, matchings)
            verify_case(side, host, blocker, matchings)
            checked += 1
    return checked


def check_wall_tree_arithmetic():
    checked = 0
    for side in range(1, 1000):
        assert side >= 0
        assert 2 * side + 1 >= 1
        assert sum(value * value for value in range(1, side + 1)) >= side * side
        checked += 1
    return checked


def main():
    exhaustive = check_exhaustive_small_hosts()
    print(
        "verified minimal blocker unit walls:",
        exhaustive[0],
        "exhaustive minimal covers with",
        exhaustive[1],
        "Hall witnesses and",
        exhaustive[2],
        "private matchings,",
        check_sampled_larger_hosts(),
        "sampled larger covers, and",
        check_wall_tree_arithmetic(),
        "wall-tree bounds",
    )


if __name__ == "__main__":
    main()
