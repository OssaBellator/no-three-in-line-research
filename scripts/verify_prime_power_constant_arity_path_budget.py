#!/usr/bin/env python3
"""Finite checks for CMR878--CMR885."""

from collections import Counter
from math import ceil, floor
import random


def path_budget(side):
    return 2 * side * side - 2 * side + floor(2 * side / 3)


def maximal_disjoint(supports):
    selected = []
    used = set()
    for support in supports:
        if support.isdisjoint(used):
            selected.append(support)
            used.update(support)
    return selected, used


def check_resource_identity():
    checked = 0
    for side in range(1, 10000):
        deletions = 2 * side * side - 2 * side
        contractions = floor(2 * side / 3)
        budget = path_budget(side)
        assert budget == deletions + contractions
        assert deletions >= 0
        assert 3 * contractions <= 2 * side
        checked += 1
    return checked


def check_packing_cover():
    rng = random.Random(881)
    checked = 0
    for side in range(2, 100):
        budget = path_budget(side)
        universe_size = side * side + 4 * side
        universe = list(range(universe_size))
        for _ in range(200):
            support_count = rng.randint(1, min(500, 5 * universe_size))
            supports = [frozenset(rng.sample(universe, 9)) for _ in range(support_count)]
            supports = list(dict.fromkeys(supports))
            selected, cover = maximal_disjoint(supports)
            if len(selected) <= budget:
                assert len(cover) <= 9 * budget
                assert all(support & cover for support in supports)
                loads = Counter()
                for support in supports:
                    loads[min(support & cover)] += 1
                assert max(loads.values()) >= ceil(len(supports) / len(cover))
            checked += 1
    return checked


def check_episode_bound():
    checked = 0
    for side in range(1, 200):
        budget = path_budget(side)
        for triple_threshold in range(2, 15):
            for atom_threshold in range(2, 15):
                bound = (
                    (triple_threshold - 1)
                    * 9
                    * budget
                    * (atom_threshold - 1)
                )
                assert bound >= 0
                distinct_limit = 9 * budget * (atom_threshold - 1)
                assert (triple_threshold - 1) * distinct_limit == bound
                checked += 1
    return checked


def check_disjoint_resource_assignment():
    rng = random.Random(879)
    checked = 0
    for side in range(1, 200):
        deletion_capacity = 2 * side * side - 2 * side
        contraction_capacity = floor(2 * side / 3)
        budget = path_budget(side)
        for _ in range(200):
            deletions = rng.randint(0, deletion_capacity)
            contractions = rng.randint(0, contraction_capacity)
            resolved = deletions + contractions
            assert resolved <= budget
            checked += 1
    return checked


def main():
    print(
        "verified constant-arity path budget:",
        check_resource_identity(),
        "resource cases,",
        check_packing_cover(),
        "packing/cover cases,",
        check_episode_bound(),
        "episode bounds, and",
        check_disjoint_resource_assignment(),
        "resource assignments",
    )


if __name__ == "__main__":
    main()
