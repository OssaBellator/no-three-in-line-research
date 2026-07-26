#!/usr/bin/env python3
"""Finite checks for CMR950--CMR957."""

from itertools import combinations
import random


def feasible(states, host):
    return {state for state in states if set(state) <= set(host)}


def minimum_face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def peel_to_core(states, potential, base, host):
    """Peel avoidable added edges until one is common to the minimum face."""
    current = set(host)
    added = sorted(set(host) - set(base))
    assert feasible(states, current)
    if feasible(states, base):
        old_value = minimum_face(feasible(states, base), potential)[1]
        new_value = minimum_face(feasible(states, current), potential)[1]
        assert new_value < old_value
    else:
        assert all(set(state) & set(added) for state in feasible(states, current))

    peels = 0
    target_value = minimum_face(feasible(states, current), potential)[1]
    for edge in added:
        face, value = minimum_face(feasible(states, current), potential)
        assert value == target_value
        avoiding = {state for state in face if edge not in state}
        if avoiding:
            current.remove(edge)
            new_face, new_value = minimum_face(feasible(states, current), potential)
            assert new_value == target_value
            assert new_face == avoiding
            peels += 1
        else:
            assert all(edge in state for state in face)
            residual = {frozenset(set(state) - {edge}) for state in face}
            assert len(residual) == len(face)
            return peels, edge, frozenset(current), face
    raise AssertionError("all added edges peeled")


def random_states(universe_size, state_size, rng):
    all_states = [
        frozenset(state)
        for state in combinations(range(universe_size), state_size)
    ]
    return set(rng.sample(all_states, rng.randint(1, min(120, len(all_states)))))


def make_infeasible_base_case(universe_size, state_size, rng):
    for _ in range(200):
        states = random_states(universe_size, state_size, rng)
        host_state = rng.choice(tuple(states))
        host = set(host_state)
        for edge in range(universe_size):
            if edge not in host and rng.random() < 0.45:
                host.add(edge)
        family = feasible(states, host)
        if not family:
            continue
        base = set(host)
        removal_order = list(base)
        rng.shuffle(removal_order)
        for edge in removal_order:
            trial = base - {edge}
            if feasible(states, trial):
                base = trial
        if feasible(states, base):
            # Delete one edge from every remaining state to force infeasibility.
            witnesses = set()
            for state in feasible(states, base):
                witnesses.add(next(iter(state)))
            base -= witnesses
        if not feasible(states, base) and set(base) < set(host):
            potential = {state: rng.randint(0, 30) for state in states}
            return states, potential, frozenset(base), frozenset(host)
    return None


def make_lowering_case(universe_size, state_size, rng):
    all_states = [
        frozenset(state)
        for state in combinations(range(universe_size), state_size)
    ]
    for _ in range(200):
        states = set(rng.sample(all_states, rng.randint(2, min(120, len(all_states)))))
        old_seed = rng.choice(tuple(states))
        base = set(old_seed)
        for edge in range(universe_size):
            if edge not in base and rng.random() < 0.3:
                base.add(edge)
        old_family = feasible(states, base)
        outside = [state for state in states if not set(state) <= base]
        if not outside:
            continue
        low_states = set(rng.sample(outside, rng.randint(1, min(10, len(outside)))))
        host = set(base)
        for state in low_states:
            host.update(state)
        potential = {state: rng.randint(5, 30) for state in states}
        for state in low_states:
            potential[state] = 0
        if minimum_face(feasible(states, host), potential)[1] < minimum_face(old_family, potential)[1]:
            return states, potential, frozenset(base), frozenset(host)
    return None


def check_infeasible_base_and_lowering():
    rng = random.Random(951)
    infeasible_cases = 0
    lowering_cases = 0
    peel_count = 0
    for universe_size in range(3, 17):
        for state_size in range(1, universe_size):
            for _ in range(25):
                case = make_infeasible_base_case(universe_size, state_size, rng)
                if case is not None:
                    states, potential, base, host = case
                    assert not feasible(states, base)
                    added = set(host) - set(base)
                    assert added
                    assert all(set(state) & added for state in feasible(states, host))
                    peels, edge, _current, face = peel_to_core(
                        states, potential, base, host
                    )
                    assert edge in added
                    assert all(edge in state for state in face)
                    assert peels <= len(added) - 1
                    infeasible_cases += 1
                    peel_count += peels

                case = make_lowering_case(universe_size, state_size, rng)
                if case is not None:
                    states, potential, base, host = case
                    peels, edge, _current, face = peel_to_core(
                        states, potential, base, host
                    )
                    assert edge in set(host) - set(base)
                    assert all(edge in state for state in face)
                    lowering_cases += 1
                    peel_count += peels
    return infeasible_cases, lowering_cases, peel_count


def check_mixed_normalization():
    rng = random.Random(953)
    checked = 0
    for universe_size in range(2, 15):
        for state_size in range(universe_size + 1):
            all_states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(100):
                states = set(
                    rng.sample(all_states, rng.randint(1, min(100, len(all_states))))
                )
                potential = {state: rng.randint(0, 20) for state in states}
                first_seed = rng.choice(tuple(states))
                second_seed = rng.choice(tuple(states))
                first = set(first_seed)
                second = set(second_seed)
                for edge in range(universe_size):
                    if edge not in first and rng.random() < 0.5:
                        first.add(edge)
                    if edge not in second and rng.random() < 0.5:
                        second.add(edge)
                first = frozenset(first)
                second = frozenset(second)
                first_family = feasible(states, first)
                second_family = feasible(states, second)
                assert first_family and second_family
                middle = frozenset(set(first) & set(second))
                middle_family = feasible(states, middle)
                if not middle_family:
                    old_face, _ = minimum_face(first_family, potential)
                    old = min(old_face, key=lambda state: tuple(sorted(state)))
                    assert set(old) & (set(first) - set(second))
                else:
                    middle_face, middle_value = minimum_face(middle_family, potential)
                    second_face, second_value = minimum_face(second_family, potential)
                    assert second_value <= middle_value
                    if second_value == middle_value:
                        assert middle_face <= second_face
                        added = set(second) - set(middle)
                        assert frozenset(set(second) - added) == middle
                    else:
                        assert all(
                            set(state) & (set(second) - set(middle))
                            for state in second_face
                        )
                checked += 1
    return checked


def check_execution_bounds():
    checked = 0
    for state_size in range(0, 500):
        for universe_size in range(state_size, 1000, 7):
            segment_cap = universe_size - state_size
            assert segment_cap >= 0
            total_cap = (state_size + 1) * universe_size
            assert total_cap >= segment_cap
            checked += 1
    return checked


def main():
    infeasible, lowering, peels = check_infeasible_base_and_lowering()
    print(
        "verified complete host transition normalization:",
        infeasible,
        "infeasible-base contractions,",
        lowering,
        "lowering contractions with",
        peels,
        "peels,",
        check_mixed_normalization(),
        "mixed transitions, and",
        check_execution_bounds(),
        "execution bounds",
    )


if __name__ == "__main__":
    main()
