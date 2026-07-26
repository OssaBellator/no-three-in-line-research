#!/usr/bin/env python3
"""Finite checks for CMR1110--CMR1117."""

from itertools import combinations
import random


def minimum_face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def feasible_family(states, host):
    host = set(host)
    return {state for state in states if set(state) <= host}


def check_reconditioning_and_contraction():
    rng = random.Random(1110)
    checked = 0
    for universe_size in range(1, 25):
        universe = tuple(range(universe_size))
        for state_size in range(universe_size + 1):
            all_count = 1
            # Keep large cases sampled rather than materialising all combinations.
            states = []
            seen = set()
            target = min(120, max(1, universe_size * 5))
            while len(states) < target:
                state = frozenset(rng.sample(universe, state_size))
                if state not in seen:
                    seen.add(state)
                    states.append(state)
                if len(seen) == len(list(combinations(universe, state_size))):
                    break
            family = set(states)
            potential = {state: rng.randint(0, 40) for state in family}
            face, value = minimum_face(family, potential)
            anchor = rng.choice(tuple(face))
            rank = rng.randint(0, min(4, len(anchor)))
            prescription = frozenset(rng.sample(tuple(anchor), rank))

            conditioned = {state for state in family if set(prescription) <= set(state)}
            assert anchor in conditioned
            conditioned_face, conditioned_value = minimum_face(conditioned, potential)
            assert conditioned_value == value
            assert anchor in conditioned_face

            residual = {
                frozenset(set(state) - set(prescription)) for state in conditioned
            }
            assert len(residual) == len(conditioned)
            induced = {
                residual_state: potential[frozenset(set(residual_state) | set(prescription))]
                for residual_state in residual
            }
            residual_face, residual_value = minimum_face(residual, induced)
            assert residual_value == value
            assert frozenset(set(anchor) - set(prescription)) in residual_face
            checked += 1
    return checked


def check_later_host_trichotomy():
    rng = random.Random(1111)
    checked = 0
    missing_cases = 0
    improvement_cases = 0
    survival_cases = 0
    for universe_size in range(2, 80):
        universe = set(range(universe_size))
        for _ in range(300):
            state_size = rng.randint(1, min(universe_size, 15))
            anchor = frozenset(rng.sample(tuple(universe), state_size))
            family = {anchor}
            for _state in range(80):
                family.add(frozenset(rng.sample(tuple(universe), state_size)))
            potential = {state: rng.randint(1, 40) for state in family}
            potential[anchor] = 0
            prescription = frozenset(
                rng.sample(tuple(anchor), rng.randint(0, min(4, len(anchor))))
            )

            later_host = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            later = feasible_family(family, later_host)
            if anchor <= later_host:
                assert anchor in later
                later_value = min(potential[state] for state in later)
                assert later_value == 0
                reconditioned = {
                    state for state in later if set(prescription) <= set(state)
                }
                assert anchor in reconditioned
                assert min(potential[state] for state in reconditioned) == 0
                survival_cases += 1
            else:
                missing = set(anchor) - later_host
                assert missing
                missing_cases += 1
            checked += 1

            # Add a synthetic lower state to test strict improvement independently.
            lower = frozenset(rng.sample(tuple(universe), state_size))
            expanded = set(later)
            expanded.add(lower)
            expanded_potential = dict(potential)
            expanded_potential[lower] = -1
            assert min(expanded_potential[state] for state in expanded) == -1
            improvement_cases += 1
    return checked, survival_cases, missing_cases, improvement_cases


def check_same_value_rollback():
    rng = random.Random(1114)
    checked = 0
    for universe_size in range(2, 100):
        universe = set(range(universe_size))
        for _ in range(200):
            state_size = rng.randint(1, min(universe_size, 12))
            anchor = frozenset(rng.sample(tuple(universe), state_size))
            base_host = set(anchor)
            base_host.update(rng.sample(tuple(universe - set(anchor)), rng.randint(0, len(universe - set(anchor)))))
            expanded_host = set(base_host)
            expanded_host.update(rng.sample(tuple(universe - base_host), rng.randint(0, len(universe - base_host))))
            assert base_host <= expanded_host
            states = {anchor}
            for _state in range(100):
                states.add(frozenset(rng.sample(tuple(universe), state_size)))
            base_family = feasible_family(states, base_host)
            expanded_family = feasible_family(states, expanded_host)
            potential = {state: rng.randint(0, 30) for state in states}
            potential[anchor] = 0
            assert min(potential[state] for state in base_family) == 0
            assert min(potential[state] for state in expanded_family) == 0
            rolled_back = feasible_family(expanded_family, base_host)
            assert rolled_back == base_family
            assert anchor in rolled_back
            checked += 1
    return checked


def main():
    later = check_later_host_trichotomy()
    print(
        "verified fixed-core reopening:",
        check_reconditioning_and_contraction(),
        "conditioned contractions,",
        later[0],
        "later hosts with",
        later[1],
        "surviving anchors and",
        later[2],
        "missing-anchor cases,",
        later[3],
        "strict improvements, and",
        check_same_value_rollback(),
        "same-value rollbacks",
    )


if __name__ == "__main__":
    main()
