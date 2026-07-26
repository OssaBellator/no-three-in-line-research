#!/usr/bin/env python3
"""Finite checks for CMR886--CMR893."""

from collections import Counter
from itertools import combinations
from math import ceil
import random


def check_physical_cell_labels():
    rng = random.Random(886)
    checked = 0
    for count in range(1, 10000):
        labels = [rng.randrange(2) for _ in range(count)]
        assert max(Counter(labels).values()) >= ceil(count / 2)
        checked += 1
    return checked


def check_matching_vertex_edges():
    rng = random.Random(887)
    checked = 0
    for side in range(1, 200):
        for count in range(1, 1000):
            edges = [rng.randrange(side) for _ in range(count)]
            assert max(Counter(edges).values()) >= ceil(count / side)
            checked += 1
    return checked


def check_uniform_bound():
    checked = 0
    for side in range(1, 500):
        for count in range(1, 5000):
            assert ceil(count / 2) >= ceil(count / (2 * side))
            assert ceil(count / side) >= ceil(count / (2 * side))
            checked += 1
    return checked


def check_binary_partition_and_contraction():
    rng = random.Random(889)
    checked = 0
    for universe_size in range(1, 18):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(100, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                edge = rng.randrange(universe_size)
                absent = {state for state in family if edge not in state}
                present = {state for state in family if edge in state}
                assert absent.isdisjoint(present)
                assert absent | present == family

                residual = {frozenset(state - {edge}) for state in present}
                assert len(residual) == len(present)
                rebuilt = {frozenset(set(state) | {edge}) for state in residual}
                assert rebuilt == present
                if present:
                    assert all(len(state) == state_size - 1 for state in residual)
                checked += 1
    return checked


def check_rank_two_transfer():
    rng = random.Random(891)
    checked = 0
    universe = list(range(50))
    for _ in range(100000):
        triple = frozenset(rng.sample(universe, 3))
        edge = rng.choice(tuple(triple))
        pair = triple - {edge}
        assert len(pair) == 2
        state = set(triple)
        state.update(rng.sample([item for item in universe if item not in triple], 10))
        assert triple.issubset(state)
        assert pair.issubset(state - {edge})
        checked += 1
    return checked


def check_pair_multiplicity():
    checked = 0
    for count in range(1, 10000):
        for threshold in range(2, 20):
            distinct = ceil(count / (threshold - 1))
            assert distinct * (threshold - 1) >= count
            checked += 1
    return checked


def main():
    print(
        "verified support atom edge batching:",
        check_physical_cell_labels(),
        "physical-label cases,",
        check_matching_vertex_edges(),
        "vertex-edge cases,",
        check_uniform_bound(),
        "uniform bounds,",
        check_binary_partition_and_contraction(),
        "partition/contraction cases,",
        check_rank_two_transfer(),
        "rank-two cases, and",
        check_pair_multiplicity(),
        "pair thresholds",
    )


if __name__ == "__main__":
    main()
