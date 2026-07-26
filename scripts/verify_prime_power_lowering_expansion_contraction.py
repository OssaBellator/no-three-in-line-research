#!/usr/bin/env python3
"""Finite checks for CMR942--CMR949."""

from itertools import combinations
import random


def feasible(states, host):
    return {state for state in states if set(state) <= set(host)}


def face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def peel_added_edges(states, potential, old_host, new_host):
    current = set(new_host)
    added = sorted(set(new_host) - set(old_host))
    current_face, new_value = face(feasible(states, current), potential)
    old_value = face(feasible(states, old_host), potential)[1]
    assert new_value < old_value
    assert all(set(state) & set(added) for state in current_face)

    peels = 0
    for edge in added:
        current_face, current_value = face(feasible(states, current), potential)
        assert current_value == new_value
        avoiding = {state for state in current_face if edge not in state}
        if avoiding:
            current.remove(edge)
            peeled_face, peeled_value = face(feasible(states, current), potential)
            assert peeled_value == new_value
            assert peeled_face == avoiding
            peels += 1
        else:
            state_size = len(next(iter(current_face)))
            residual = {frozenset(set(state) - {edge}) for state in current_face}
            assert len(residual) == len(current_face)
            assert all(len(state) == state_size - 1 for state in residual)
            assert peels <= len(added) - 1
            return peels, edge, current_face
    raise AssertionError("all added edges were peeled")


def random_case(all_states, universe_size, rng):
    ambient = set(
        rng.sample(all_states, rng.randint(2, min(len(all_states), 120)))
    )
    for _ in range(200):
        old_seed = rng.choice(tuple(ambient))
        old_host = set(old_seed)
        for edge in range(universe_size):
            if edge not in old_host and rng.random() < 0.35:
                old_host.add(edge)
        old_family = feasible(ambient, old_host)
        outside = [state for state in ambient if not set(state) <= old_host]
        if not outside:
            continue
        low_states = set(
            rng.sample(outside, rng.randint(1, min(len(outside), 12)))
        )
        new_host = set(old_host)
        for state in low_states:
            new_host.update(state)
        potential = {state: rng.randint(5, 30) for state in ambient}
        for state in low_states:
            potential[state] = 0
        if face(feasible(ambient, new_host), potential)[1] < face(old_family, potential)[1]:
            return ambient, potential, frozenset(old_host), frozenset(new_host)
    return None


def check_lowering_expansions():
    rng = random.Random(944)
    checked = 0
    peel_total = 0
    for universe_size in range(3, 17):
        for state_size in range(1, universe_size):
            all_states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(40):
                case = random_case(all_states, universe_size, rng)
                if case is None:
                    continue
                states, potential, old_host, new_host = case
                peels, edge, current_face = peel_added_edges(
                    states, potential, old_host, new_host
                )
                assert edge in set(new_host) - set(old_host)
                assert all(edge in state for state in current_face)
                peel_total += peels
                checked += 1
    return checked, peel_total


def check_budget_arithmetic():
    checked = 0
    for added_size in range(1, 1000):
        for peels in range(added_size):
            assert peels <= added_size - 1
            assert peels + 1 <= added_size
            checked += 1
    return checked


def main():
    cases, peels = check_lowering_expansions()
    print(
        "verified lowering expansion contraction:",
        cases,
        "lowering expansions with",
        peels,
        "minimum-preserving peels, and",
        check_budget_arithmetic(),
        "budget cases",
    )


if __name__ == "__main__":
    main()
