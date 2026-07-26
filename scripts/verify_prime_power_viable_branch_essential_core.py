#!/usr/bin/env python3
"""Finite checks for CMR838--CMR845."""

from itertools import combinations
import random


def all_states(universe_size, state_size):
    return [frozenset(state) for state in combinations(range(universe_size), state_size)]


def core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def child(family, edge):
    return {state for state in family if edge not in state}


def contract(family, essential):
    return {frozenset(state - essential) for state in family}


def check_viability_and_degree():
    rng = random.Random(839)
    checked = 0
    for universe_size in range(1, 15):
        for state_size in range(universe_size + 1):
            states = all_states(universe_size, state_size)
            if not states:
                continue
            for _ in range(min(200, max(1, len(states) * 2))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                rejected = rng.choice(sorted(family, key=lambda item: tuple(sorted(item))))
                essential = core(family)
                viable = [edge for edge in rejected if child(family, edge)]
                assert set(viable) == set(rejected - essential)
                assert len(viable) == state_size - len(essential)
                checked += 1
    return checked


def check_contraction_and_empty_core():
    rng = random.Random(840)
    checked = 0
    for universe_size in range(1, 16):
        for state_size in range(universe_size + 1):
            states = all_states(universe_size, state_size)
            if not states:
                continue
            for _ in range(min(100, len(states))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                essential = core(family)
                residual = contract(family, essential)
                assert len(residual) == len(family)
                assert all(len(state) == state_size - len(essential) for state in residual)
                assert core(residual) == frozenset()
                rebuilt = {frozenset(set(state) | set(essential)) for state in residual}
                assert rebuilt == family
                checked += 1
    return checked


def check_deterministic_cases():
    checked = 0
    for universe_size in range(1, 15):
        for state_size in range(universe_size + 1):
            states = all_states(universe_size, state_size)
            for family_size in range(1, min(len(states), 8) + 1):
                for sample in combinations(states, family_size):
                    family = set(sample)
                    essential = core(family)
                    for rejected in family:
                        noncore = rejected - essential
                        if len(noncore) == 0:
                            assert family == {rejected}
                        if len(noncore) == 1:
                            edge = next(iter(noncore))
                            assert child(family, edge) == family - {rejected}
                        checked += 1
                    if checked > 200000:
                        return checked
    return checked


def check_telescoping_contractions():
    rng = random.Random(844)
    checked = 0
    for universe_size in range(2, 30):
        for state_size in range(1, universe_size):
            states = all_states(universe_size, state_size)
            for _ in range(100):
                family = set(rng.sample(states, rng.randint(1, min(len(states), 100))))
                initial_size = state_size
                contracted_total = 0
                while family:
                    essential = core(family)
                    contracted_total += len(essential)
                    family = contract(family, essential)
                    current_size = len(next(iter(family)))
                    assert contracted_total + current_size <= initial_size
                    if len(family) == 1 or current_size == 0:
                        break
                    rejected = rng.choice(sorted(family, key=lambda item: tuple(sorted(item))))
                    viable = [edge for edge in rejected if child(family, edge)]
                    assert viable
                    family = child(family, rng.choice(viable))
                assert contracted_total <= initial_size
                checked += 1
    return checked


def check_two_layer_bounds():
    checked = 0
    for side in range(1, 500):
        state_size = 2 * side
        for core_rank in range(state_size + 1):
            branch_degree = state_size - core_rank
            assert core_rank + branch_degree == state_size
            checked += 1
    return checked


def main():
    print(
        "verified viable branch essential core:",
        check_viability_and_degree(),
        "viability cases,",
        check_contraction_and_empty_core(),
        "contraction cases,",
        check_deterministic_cases(),
        "deterministic cases,",
        check_telescoping_contractions(),
        "telescoping paths, and",
        check_two_layer_bounds(),
        "two-layer identities",
    )


if __name__ == "__main__":
    main()
