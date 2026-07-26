#!/usr/bin/env python3
"""Finite checks for CMR1142--CMR1149."""

from itertools import combinations, permutations
from math import ceil
import random


def perfect_matching_exists(side, edges):
    adjacency = {left: [] for left in range(side)}
    for left, right in edges:
        adjacency[left].append(right)
    matched_right = {}

    def augment(left, seen):
        for right in adjacency[left]:
            if right in seen:
                continue
            seen.add(right)
            if right not in matched_right or augment(matched_right[right], seen):
                matched_right[right] = left
                return True
        return False

    return all(augment(left, set()) for left in range(side))


def hall_witness(side, edges):
    adjacency = {left: set() for left in range(side)}
    for left, right in edges:
        adjacency[left].add(right)
    for size in range(1, side + 1):
        for subset in combinations(range(side), size):
            neighbours = set().union(*(adjacency[left] for left in subset))
            if len(neighbours) < size:
                return frozenset(subset), frozenset(neighbours)
    return None


def forbidden_from_permutations(side, count, rng):
    forbidden = set()
    for _ in range(count):
        permutation = list(range(side))
        rng.shuffle(permutation)
        forbidden.update((left, permutation[left]) for left in range(side))
    return forbidden


def max_bipartite_degree(edges, side):
    row = [0] * side
    column = [0] * side
    for left, right in edges:
        row[left] += 1
        column[right] += 1
    return max(row + column, default=0)


def check_random_unmatchable_boards():
    rng = random.Random(1142)
    checked = 0
    unmatchable = 0
    for side in range(2, 9):
        complete = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(6000):
            forbidden_count = rng.randint(0, 2)
            forbidden = forbidden_from_permutations(side, forbidden_count, rng)
            allowed = complete - forbidden
            assert perfect_matching_exists(side, allowed)
            blocker = set(rng.sample(tuple(allowed), rng.randint(0, len(allowed))))
            residual = allowed - blocker
            if perfect_matching_exists(side, residual):
                checked += 1
                continue
            witness = hall_witness(side, residual)
            assert witness is not None
            source, neighbours = witness
            outside = set(range(side)) - set(neighbours)
            assert len(neighbours) < len(source)
            cross_allowed = {
                (left, right)
                for left in source
                for right in outside
                if (left, right) in allowed
            }
            assert cross_allowed <= blocker
            x = len(source)
            z = len(outside)
            d0 = max_bipartite_degree(forbidden, side)
            cross = blocker & cross_allowed
            assert len(cross) >= x * max(0, z - d0)
            assert len(cross) >= z * max(0, x - d0)
            degree = max_bipartite_degree(blocker, side)
            assert degree >= max(0, ceil((side + 1) / 2) - d0)
            unmatchable += 1
            checked += 1
    return checked, unmatchable


def check_constructed_hall_walls():
    rng = random.Random(1145)
    checked = 0
    for side in range(2, 80):
        complete = {(left, right) for left in range(side) for right in range(side)}
        for forbidden_count in (0, 1, 2):
            for _ in range(200):
                forbidden = forbidden_from_permutations(side, forbidden_count, rng)
                allowed = complete - forbidden
                x = rng.randint(1, side)
                z = rng.randint(max(1, side + 1 - x), side)
                source = set(rng.sample(range(side), x))
                outside = set(rng.sample(range(side), z))
                blocker = {
                    (left, right)
                    for left in source
                    for right in outside
                    if (left, right) in allowed
                }
                residual = allowed - blocker
                assert not perfect_matching_exists(side, residual)
                d0 = max_bipartite_degree(forbidden, side)
                assert len(blocker) >= x * max(0, z - d0)
                assert len(blocker) >= z * max(0, x - d0)
                degree = max_bipartite_degree(blocker, side)
                assert degree >= max(0, ceil((side + 1) / 2) - d0)
                checked += 1
    return checked


def check_cover_equivalence():
    rng = random.Random(1142)
    checked = 0
    for side in range(1, 8):
        matchings = [
            frozenset((left, permutation[left]) for left in range(side))
            for permutation in permutations(range(side))
        ]
        universe = {(left, right) for left in range(side) for right in range(side)}
        for _ in range(3000):
            blocker = set(rng.sample(tuple(universe), rng.randint(0, len(universe))))
            covers_all = all(set(matching) & blocker for matching in matchings)
            residual_has_matching = any(set(matching).isdisjoint(blocker) for matching in matchings)
            assert covers_all == (not residual_has_matching)
            checked += 1
    return checked


def main():
    random_cases, unmatchable = check_random_unmatchable_boards()
    print(
        "verified terminal blocker Hall walls:",
        check_cover_equivalence(),
        "cover equivalences,",
        random_cases,
        "random boards with",
        unmatchable,
        "Hall walls, and",
        check_constructed_hall_walls(),
        "constructed walls",
    )


if __name__ == "__main__":
    main()
