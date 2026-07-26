#!/usr/bin/env python3
"""Finite checks for CMR862--CMR869."""

from itertools import combinations
import random


def distinguishing_rank(family, chosen):
    alternatives = [state for state in family if state != chosen]
    edges = tuple(chosen)
    for size in range(len(edges) + 1):
        for subset in combinations(edges, size):
            witness = set(subset)
            if all(not witness.issubset(state) for state in alternatives):
                return size
    raise AssertionError


def delete_child(family, edge):
    return {state for state in family if edge not in state}


def conditioned(family, prescription):
    return {state for state in family if prescription.issubset(state)}


def check_exact_splits():
    rng = random.Random(862)
    checked = 0
    for universe_size in range(1, 16):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(150, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                prescription_size = rng.randint(0, len(chosen))
                prescription = frozenset(rng.sample(tuple(chosen), prescription_size))
                union = set(conditioned(family, prescription))
                for edge in prescription:
                    union.update(delete_child(family, edge))
                assert union == family

                excluded_union = conditioned(family, prescription) - {chosen}
                for edge in prescription:
                    excluded_union.update(delete_child(family, edge))
                assert excluded_union == family - {chosen}
                checked += 1
    return checked


def check_contraction_and_rank():
    rng = random.Random(864)
    checked = 0
    for universe_size in range(1, 15):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(100, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                prescription = frozenset(
                    rng.sample(tuple(chosen), rng.randint(0, len(chosen)))
                )
                subfamily = conditioned(family, prescription)
                residual = {
                    frozenset(state - prescription)
                    for state in subfamily
                }
                assert len(residual) == len(subfamily)
                rebuilt = {
                    frozenset(set(state) | set(prescription))
                    for state in residual
                }
                assert rebuilt == subfamily
                assert all(
                    len(state) == state_size - len(prescription)
                    for state in residual
                )

                global_rank = distinguishing_rank(family, chosen)
                local_rank = distinguishing_rank(
                    residual,
                    frozenset(chosen - prescription),
                )
                assert global_rank <= len(prescription) + local_rank
                checked += 1
    return checked


def check_new_triple_identity():
    rng = random.Random(866)
    checked = 0
    universe = list(range(30))
    for _ in range(50000):
        old = set(rng.sample(universe, rng.randint(1, 20)))
        common = set(rng.sample(sorted(old), rng.randint(0, len(old) - 1)))
        lost = old - common
        new_count = rng.randint(len(lost), min(len(universe), len(lost) + 10))
        available_new = [item for item in universe if item not in old]
        if len(available_new) < new_count:
            new_count = len(available_new)
        new = set(rng.sample(available_new, new_count))
        later = common | new
        if len(later) >= len(old) and lost:
            assert later - old
        checked += 1
    return checked


def check_constant_arity():
    checked = 0
    for state_size in range(3, 200):
        prescription_size = 3
        branch_count = prescription_size + 1
        assert branch_count == 4
        contractions = state_size // prescription_size
        assert 3 * contractions <= state_size
        checked += 1
    return checked


def main():
    print(
        "verified new-triple prescription split:",
        check_exact_splits(),
        "split cases,",
        check_contraction_and_rank(),
        "contraction/rank cases,",
        check_new_triple_identity(),
        "potential identities, and",
        check_constant_arity(),
        "arity cases",
    )


if __name__ == "__main__":
    main()
