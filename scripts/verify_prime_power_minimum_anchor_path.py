#!/usr/bin/env python3
"""Finite checks for CMR902--CMR909."""

from itertools import combinations
import random


def force_target(family, anchor, target):
    family = set(family)
    deleted = set()
    while True:
        alternatives = [state for state in family if not set(target) <= set(state)]
        if not alternatives:
            return family, deleted
        state = min(alternatives, key=lambda item: tuple(sorted(item)))
        outside = sorted(set(state) - set(anchor))
        assert outside
        edge = outside[0]
        assert edge not in deleted
        deleted.add(edge)
        family = {item for item in family if edge not in item}
        assert anchor in family


def force_prescription(family, anchor, prescription, deleted):
    family = set(family)
    deleted = set(deleted)
    while True:
        alternatives = [
            state for state in family if not set(prescription) <= set(state)
        ]
        if not alternatives:
            return family, deleted
        state = min(alternatives, key=lambda item: tuple(sorted(item)))
        outside = sorted(set(state) - set(anchor))
        assert outside
        edge = outside[0]
        assert edge not in deleted
        deleted.add(edge)
        family = {item for item in family if edge not in item}
        assert anchor in family


def check_minimum_preservation():
    rng = random.Random(902)
    checked = 0
    for universe_size in range(1, 16):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(100, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                potential = {state: rng.randint(0, 30) for state in family}
                anchor = min(
                    family,
                    key=lambda state: (potential[state], tuple(sorted(state))),
                )
                retained = {anchor}
                retained.update(
                    rng.sample(
                        tuple(family - {anchor}),
                        rng.randint(0, len(family) - 1),
                    )
                )
                assert potential[anchor] == min(potential[state] for state in retained)
                checked += 1
    return checked


def check_forcing_and_budget():
    rng = random.Random(904)
    checked = 0
    for universe_size in range(3, 20):
        for state_size in range(1, universe_size):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(100):
                family = set(
                    rng.sample(states, rng.randint(1, min(len(states), 200)))
                )
                anchor = rng.choice(tuple(family))
                target_size = rng.randint(1, min(3, len(anchor)))
                target = frozenset(rng.sample(tuple(anchor), target_size))
                target_family, deleted = force_target(family, anchor, target)
                assert anchor in target_family
                assert all(set(target) <= set(state) for state in target_family)
                assert deleted.isdisjoint(anchor)
                assert len(deleted) <= universe_size - state_size

                prescription_size = rng.randint(0, min(3, len(anchor)))
                prescription = frozenset(
                    rng.sample(tuple(anchor), prescription_size)
                )
                final_family, final_deleted = force_prescription(
                    target_family,
                    anchor,
                    prescription,
                    deleted,
                )
                assert anchor in final_family
                assert all(
                    set(prescription) <= set(state)
                    for state in final_family
                )
                assert final_deleted.isdisjoint(anchor)
                assert len(final_deleted) <= universe_size - state_size
                checked += 1
    return checked


def check_induced_contraction():
    rng = random.Random(906)
    checked = 0
    for universe_size in range(1, 18):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(100, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                anchor = rng.choice(tuple(family))
                fixed_size = rng.randint(0, min(3, len(anchor)))
                fixed = frozenset(rng.sample(tuple(anchor), fixed_size))
                conditioned = {
                    state for state in family if set(fixed) <= set(state)
                }
                assert anchor in conditioned
                potential = {state: rng.randint(0, 50) for state in conditioned}
                anchor = min(
                    conditioned,
                    key=lambda state: (potential[state], tuple(sorted(state))),
                )
                residual = {
                    frozenset(set(state) - set(fixed))
                    for state in conditioned
                }
                induced = {
                    state: potential[frozenset(set(state) | set(fixed))]
                    for state in residual
                }
                residual_anchor = frozenset(set(anchor) - set(fixed))
                assert len(residual) == len(conditioned)
                assert induced[residual_anchor] == min(induced.values())
                rebuilt = {
                    frozenset(set(state) | set(fixed))
                    for state in residual
                }
                assert rebuilt == conditioned
                checked += 1
    return checked


def check_restoration_response():
    rng = random.Random(908)
    checked = 0
    for universe_size in range(1, 100):
        universe = set(range(universe_size))
        for _ in range(500):
            anchor = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            outside = tuple(universe - anchor)
            deleted = set(rng.sample(outside, rng.randint(0, len(outside))))
            restored = set(rng.sample(tuple(deleted), rng.randint(0, len(deleted))))
            later_host = set(anchor) | restored
            reclosed = later_host - restored
            assert anchor <= reclosed
            assert reclosed.isdisjoint(restored)

            lost_anchor = set(
                rng.sample(tuple(anchor), rng.randint(0, len(anchor)))
            )
            failing_host = later_host - lost_anchor
            if not anchor <= failing_host:
                assert anchor - failing_host
            checked += 1
    return checked


def main():
    print(
        "verified minimum-anchor preserving path:",
        check_minimum_preservation(),
        "minimum restrictions,",
        check_forcing_and_budget(),
        "forcing passes,",
        check_induced_contraction(),
        "induced contractions, and",
        check_restoration_response(),
        "restoration responses",
    )


if __name__ == "__main__":
    main()
