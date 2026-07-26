#!/usr/bin/env python3
"""Checks for CMR934--CMR941."""

from itertools import combinations
import random


def feasible(states, host):
    return {state for state in states if set(state) <= set(host)}


def face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def host_with(universe_size, state, probability, rng):
    host = set(state)
    for edge in range(universe_size):
        if edge not in host and rng.random() < probability:
            host.add(edge)
    return frozenset(host)


def sampled_family(states, rng):
    return set(rng.sample(states, rng.randint(1, min(100, len(states)))))


def check_expansion():
    rng = random.Random(934)
    checked = 0
    for size in range(1, 14):
        for rank in range(size + 1):
            states = [frozenset(item) for item in combinations(range(size), rank)]
            for _ in range(120):
                ambient = sampled_family(states, rng)
                potential = {state: rng.randint(0, 30) for state in ambient}
                small = host_with(size, rng.choice(tuple(ambient)), 0.25, rng)
                large = set(small)
                for edge in range(size):
                    if edge not in large and rng.random() < 0.6:
                        large.add(edge)
                large = frozenset(large)
                small_family = feasible(ambient, small)
                large_family = feasible(ambient, large)
                small_face, small_value = face(small_family, potential)
                large_face, large_value = face(large_family, potential)
                assert large_value <= small_value
                if large_value == small_value:
                    assert small_face <= large_face
                    added = set(large) - set(small)
                    assert frozenset(set(large) - added) == small
                checked += 1
    return checked


def check_intersections():
    rng = random.Random(937)
    checked = 0
    for size in range(1, 14):
        for rank in range(size + 1):
            states = [frozenset(item) for item in combinations(range(size), rank)]
            for _ in range(140):
                ambient = sampled_family(states, rng)
                potential = {state: rng.randint(0, 30) for state in ambient}
                first = host_with(size, rng.choice(tuple(ambient)), 0.5, rng)
                second = host_with(size, rng.choice(tuple(ambient)), 0.5, rng)
                first_family = feasible(ambient, first)
                second_family = feasible(ambient, second)
                first_face, first_value = face(first_family, potential)
                _second_face, second_value = face(second_family, potential)
                if second_value < first_value:
                    continue
                middle = frozenset(set(first) & set(second))
                middle_family = feasible(ambient, middle)
                survivors = first_face & middle_family
                if survivors:
                    middle_face, middle_value = face(middle_family, potential)
                    assert middle_value == first_value == second_value
                    assert middle_face == survivors
                    added = set(second) - set(first)
                    assert frozenset(set(second) - added) == middle
                else:
                    old = min(first_face, key=lambda state: tuple(sorted(state)))
                    assert set(old) & (set(first) - set(second))
                checked += 1
    return checked


def check_depth_and_recurrence():
    rng = random.Random(939)
    depth_cases = 0
    for size in range(1, 250):
        for rank in range(size + 1):
            for _ in range(5):
                survivor = set(rng.sample(range(size), rank))
                deleted = set(range(size)) - survivor
                assert len(deleted) <= size - rank
                depth_cases += 1
    recurrence_cases = 0
    for universe in range(1, 1000):
        for threshold in range(2, 50):
            assert (threshold - 1) * universe < threshold * universe
            recurrence_cases += 1
    return depth_cases, recurrence_cases


def main():
    depth, recurrence = check_depth_and_recurrence()
    print(
        "verified minimum expansion rollback:",
        check_expansion(),
        "expansions,",
        check_intersections(),
        "intersection transitions,",
        depth,
        "depth cases, and",
        recurrence,
        "recurrence cases",
    )


if __name__ == "__main__":
    main()
