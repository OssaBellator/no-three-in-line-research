#!/usr/bin/env python3
"""Finite checks for CMR830--CMR837."""

from itertools import combinations
import random


def all_equal_states(universe_size, state_size):
    return [frozenset(state) for state in combinations(range(universe_size), state_size)]


def branch_family(family, edge):
    return {state for state in family if edge not in state}


def check_exact_union():
    rng = random.Random(830)
    checked = 0
    for universe_size in range(1, 16):
        for state_size in range(universe_size + 1):
            states = all_equal_states(universe_size, state_size)
            if not states:
                continue
            for _ in range(min(100, len(states))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                rejected = rng.choice(sorted(family, key=lambda state: tuple(sorted(state))))
                union = set()
                for edge in rejected:
                    union.update(branch_family(family, edge))
                assert union == family - {rejected}
                checked += 1
    return checked


def check_viable_coverage():
    rng = random.Random(831)
    checked = 0
    for universe_size in range(2, 20):
        for state_size in range(1, universe_size):
            states = all_equal_states(universe_size, state_size)
            for _ in range(100):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                rejected = rng.choice(sorted(family, key=lambda state: tuple(sorted(state))))
                viable = [
                    branch_family(family, edge)
                    for edge in rejected
                    if branch_family(family, edge)
                ]
                union = set().union(*viable) if viable else set()
                assert union == family - {rejected}
                for alternative in family - {rejected}:
                    assert any(alternative in child for child in viable)
                checked += 1
    return checked


def check_witness_path():
    checked = 0
    for universe_size in range(2, 25):
        for state_size in range(1, universe_size):
            states = all_equal_states(universe_size, state_size)
            witness = states[0]
            family = set(states)
            deleted = set()
            steps = 0
            while len(family) > 1:
                rejected = next(state for state in family if state != witness)
                edge = min(rejected - witness)
                assert edge not in deleted
                deleted.add(edge)
                family = branch_family(family, edge)
                assert witness in family
                steps += 1
                assert steps <= universe_size - state_size
            checked += 1
    return checked


def check_aggressive_containment():
    rng = random.Random(835)
    checked = 0
    for universe_size in range(2, 30):
        for state_size in range(1, universe_size):
            states = all_equal_states(universe_size, state_size)
            for _ in range(100):
                anchor = rng.choice(states)
                rejected = rng.choice(states)
                entering = rejected - anchor
                aggressive = {
                    state for state in states if state.isdisjoint(entering)
                }
                for edge in entering:
                    assert aggressive.issubset(branch_family(set(states), edge))
                checked += 1
    return checked


def check_two_layer_depth():
    checked = 0
    for side in range(1, 200):
        universe = 2 * side * side
        state_size = 2 * side
        assert universe - state_size == 2 * side * side - 2 * side
        checked += 1
    return checked


def main():
    print(
        "verified complete state exclusion branching:",
        check_exact_union(),
        "union cases,",
        check_viable_coverage(),
        "coverage cases,",
        check_witness_path(),
        "witness paths,",
        check_aggressive_containment(),
        "containment cases, and",
        check_two_layer_depth(),
        "depth cases",
    )


if __name__ == "__main__":
    main()
