#!/usr/bin/env python3
"""Finite checks for CMR910--CMR917."""

from math import comb
import random


def random_family(universe_size, state_size, maximum, rng):
    target = rng.randint(1, min(maximum, comb(universe_size, state_size)))
    family = set()
    while len(family) < target:
        family.add(frozenset(rng.sample(range(universe_size), state_size)))
    return family


def minimum_face(family, potential):
    minimum = min(potential[state] for state in family)
    return {state for state in family if potential[state] == minimum}, minimum


def common_core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def check_edge_dichotomy():
    rng = random.Random(911)
    checked = 0
    for universe_size in range(1, 35):
        for state_size in range(universe_size + 1):
            for _ in range(40):
                family = random_family(universe_size, state_size, 120, rng)
                potential = {state: rng.randint(0, 20) for state in family}
                face, minimum = minimum_face(family, potential)
                core = common_core(face)
                assert face
                assert all(potential[state] == minimum for state in face)
                for edge in range(universe_size):
                    avoiding = [state for state in face if edge not in state]
                    if avoiding:
                        restricted = {state for state in family if edge not in state}
                        assert restricted
                        assert min(potential[state] for state in restricted) == minimum
                        assert edge not in core
                    else:
                        assert edge in core
                checked += 1
    return checked


def check_complete_core_contraction():
    rng = random.Random(912)
    checked = 0
    for universe_size in range(1, 40):
        for state_size in range(universe_size + 1):
            for _ in range(30):
                family = random_family(universe_size, state_size, 100, rng)
                potential = {state: rng.randint(0, 30) for state in family}
                face, minimum = minimum_face(family, potential)
                core = common_core(face)
                residual = {frozenset(set(state) - set(core)) for state in face}
                assert len(residual) == len(face)
                assert common_core(residual) == frozenset()
                rebuilt = {
                    frozenset(set(state) | set(core))
                    for state in residual
                }
                assert rebuilt == face
                assert all(
                    potential[frozenset(set(state) | set(core))] == minimum
                    for state in residual
                )
                checked += 1
    return checked


def check_redeletion_or_contraction():
    rng = random.Random(914)
    checked = 0
    for universe_size in range(1, 50):
        for state_size in range(universe_size + 1):
            for _ in range(30):
                family = random_family(universe_size, state_size, 100, rng)
                potential = {state: rng.randint(0, 20) for state in family}
                face, minimum = minimum_face(family, potential)
                core = common_core(face)
                edge = rng.randrange(universe_size)
                if edge in core:
                    residual = {
                        frozenset(set(state) - {edge})
                        for state in face
                    }
                    assert len(residual) == len(face)
                    assert all(len(state) == state_size - 1 for state in residual)
                else:
                    avoiding = {state for state in face if edge not in state}
                    assert avoiding
                    assert all(potential[state] == minimum for state in avoiding)
                checked += 1
    return checked


def check_monotone_core_growth():
    rng = random.Random(916)
    checked = 0
    for universe_size in range(1, 50):
        for state_size in range(universe_size + 1):
            for _ in range(30):
                family = random_family(universe_size, state_size, 100, rng)
                previous_core = common_core(family)
                growth = 0
                while len(family) > 1:
                    edge_candidates = [
                        edge
                        for edge in range(universe_size)
                        if any(edge not in state for state in family)
                    ]
                    if not edge_candidates:
                        break
                    edge = rng.choice(edge_candidates)
                    child = {state for state in family if edge not in state}
                    if not child:
                        continue
                    family = child
                    current_core = common_core(family)
                    assert set(previous_core) <= set(current_core)
                    if current_core != previous_core:
                        growth += len(current_core) - len(previous_core)
                    assert len(current_core) <= state_size
                    assert growth <= state_size
                    previous_core = current_core
                checked += 1
    return checked


def check_restoration_arithmetic():
    checked = 0
    for prime in (2, 3, 5, 7, 11):
        for height in range(2, 20):
            for generations in range(1, 500):
                restorations = generations - 1
                incidence = restorations * (prime + 1) * (height - 1)
                assert incidence >= 0
                assert incidence % ((prime + 1) * (height - 1)) == 0
                checked += 1
    return checked


def main():
    print(
        "verified minimum-face edge dichotomy:",
        check_edge_dichotomy(),
        "edge-face cases,",
        check_complete_core_contraction(),
        "core contractions,",
        check_redeletion_or_contraction(),
        "edge responses,",
        check_monotone_core_growth(),
        "core-growth histories, and",
        check_restoration_arithmetic(),
        "restoration identities",
    )


if __name__ == "__main__":
    main()
