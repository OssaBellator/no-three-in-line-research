#!/usr/bin/env python3
"""Finite checks for CMR926--CMR933."""

from itertools import combinations
import random


def feasible(ambient, host):
    return {state for state in ambient if set(state) <= set(host)}


def minimum_face(family, potential):
    minimum = min(potential[state] for state in family)
    return {state for state in family if potential[state] == minimum}, minimum


def core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def canonical(face):
    return min(face, key=lambda state: tuple(sorted(state)))


def random_ambient(universe_size, state_size, rng):
    states = [
        frozenset(state)
        for state in combinations(range(universe_size), state_size)
    ]
    return set(rng.sample(states, rng.randint(1, min(len(states), 100))))


def random_host_with_state(universe_size, state, rng):
    host = set(state)
    for edge in range(universe_size):
        if edge not in host and rng.random() < 0.5:
            host.add(edge)
    return frozenset(host)


def check_restriction_and_expansion():
    rng = random.Random(926)
    checked = 0
    for universe_size in range(1, 14):
        for state_size in range(universe_size + 1):
            for _ in range(300):
                ambient = random_ambient(universe_size, state_size, rng)
                potential = {state: rng.randint(0, 20) for state in ambient}
                seed = rng.choice(tuple(ambient))
                large = random_host_with_state(universe_size, seed, rng)
                family_large = feasible(ambient, large)
                if not family_large:
                    continue
                survivor = rng.choice(tuple(family_large))
                small = set(survivor)
                for edge in large:
                    if edge not in small and rng.random() < 0.5:
                        small.add(edge)
                small = frozenset(small)
                family_small = feasible(ambient, small)
                face_large, value_large = minimum_face(family_large, potential)
                face_small, value_small = minimum_face(family_small, potential)

                assert value_small >= value_large
                surviving_minima = face_large & family_small
                if surviving_minima:
                    assert value_small == value_large
                    assert face_small == surviving_minima
                else:
                    assert value_small > value_large

                assert value_large <= value_small
                if value_large == value_small:
                    assert face_small <= face_large
                    assert core(face_large) <= core(face_small)

                face_expanded, value_expanded = minimum_face(family_large, potential)
                assert value_expanded <= value_small
                if value_expanded == value_small:
                    assert face_small <= face_expanded
                    assert core(face_expanded) <= core(face_small)
                    for state in face_expanded - face_small:
                        assert set(state) & (set(large) - set(small))
                checked += 1
    return checked


def check_arbitrary_transition_witnesses():
    rng = random.Random(929)
    checked = 0
    for universe_size in range(1, 15):
        for state_size in range(universe_size + 1):
            for _ in range(400):
                ambient = random_ambient(universe_size, state_size, rng)
                potential = {state: rng.randint(0, 30) for state in ambient}
                first_seed = rng.choice(tuple(ambient))
                second_seed = rng.choice(tuple(ambient))
                first_host = random_host_with_state(universe_size, first_seed, rng)
                second_host = random_host_with_state(universe_size, second_seed, rng)
                first_family = feasible(ambient, first_host)
                second_family = feasible(ambient, second_host)
                if not first_family or not second_family:
                    continue
                first_face, first_value = minimum_face(first_family, potential)
                second_face, second_value = minimum_face(second_family, potential)
                first_canonical = canonical(first_face)
                second_canonical = canonical(second_face)
                if second_value >= first_value and second_canonical != first_canonical:
                    lost = set(first_host) - set(second_host)
                    added = set(second_host) - set(first_host)
                    old_lost = not set(first_canonical) <= set(second_host)
                    new_added = not set(second_canonical) <= set(first_host)
                    assert old_lost or (second_value == first_value and new_added)
                    if old_lost:
                        assert set(first_canonical) & lost
                    if not old_lost:
                        assert set(second_canonical) & added
                checked += 1
    return checked


def check_core_support():
    rng = random.Random(931)
    checked = 0
    for universe_size in range(1, 15):
        for state_size in range(universe_size + 1):
            for _ in range(300):
                ambient = random_ambient(universe_size, state_size, rng)
                potential = {state: rng.randint(0, 10) for state in ambient}
                seed = rng.choice(tuple(ambient))
                small = random_host_with_state(universe_size, seed, rng)
                large = set(small)
                for edge in range(universe_size):
                    if edge not in large and rng.random() < 0.7:
                        large.add(edge)
                large = frozenset(large)
                family_small = feasible(ambient, small)
                family_large = feasible(ambient, large)
                face_small, value_small = minimum_face(family_small, potential)
                face_large, value_large = minimum_face(family_large, potential)
                if value_small != value_large:
                    continue
                core_small = core(face_small)
                core_large = core(face_large)
                assert core_large <= core_small
                for edge in core_small - core_large:
                    witnesses = [
                        state
                        for state in face_large - face_small
                        if edge not in state
                    ]
                    assert witnesses
                    assert all(set(state) & (set(large) - set(small)) for state in witnesses)
                checked += 1
    return checked


def check_recurrence_arithmetic():
    checked = 0
    for universe_size in range(1, 1000):
        for threshold in range(2, 40):
            maximum = (threshold - 1) * universe_size
            assert maximum < threshold * universe_size
            checked += 1
    return checked


def main():
    print(
        "verified minimum-face owner transition:",
        check_restriction_and_expansion(),
        "nested-host cases,",
        check_arbitrary_transition_witnesses(),
        "arbitrary transitions,",
        check_core_support(),
        "core-support cases, and",
        check_recurrence_arithmetic(),
        "recurrence cases",
    )


if __name__ == "__main__":
    main()
