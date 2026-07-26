#!/usr/bin/env python3
"""Finite checks for CMR894--CMR901."""

from itertools import combinations
from math import comb, ceil
import random


def ordered_partition(family, prescription):
    prescription = tuple(prescription)
    parts = []
    for index, edge in enumerate(prescription):
        prefix = set(prescription[:index])
        parts.append(
            {state for state in family if prefix <= set(state) and edge not in state}
        )
    parts.append({state for state in family if set(prescription) <= set(state)})
    return parts


def check_partitions_and_contractions():
    rng = random.Random(894)
    partition_cases = 0
    contraction_cases = 0
    for universe_size in range(1, 13):
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(range(universe_size), state_size)
            ]
            for _ in range(min(100, max(1, 2 * len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                if not chosen:
                    continue
                rank = rng.randint(1, min(3, len(chosen)))
                prescription = tuple(rng.sample(tuple(chosen), rank))
                parts = ordered_partition(family, prescription)
                assert set().union(*parts) == family
                for first in range(len(parts)):
                    for second in range(first):
                        assert parts[first].isdisjoint(parts[second])
                partition_cases += 1

                for index, part in enumerate(parts):
                    if not part:
                        continue
                    fixed = (
                        set(prescription[:index])
                        if index < rank
                        else set(prescription)
                    )
                    assert all(fixed <= set(state) for state in part)
                    residual = {frozenset(set(state) - fixed) for state in part}
                    rebuilt = {frozenset(set(state) | fixed) for state in residual}
                    assert rebuilt == part
                    assert len(residual) == len(part)
                    contraction_cases += 1
    return partition_cases, contraction_cases


def check_undecided_progress():
    rng = random.Random(896)
    checked = 0
    for universe_size in range(3, 80):
        universe = set(range(universe_size))
        for _ in range(200):
            anchor = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            fixed = set(rng.sample(tuple(anchor), rng.randint(0, len(anchor))))
            outside = tuple(universe - anchor)
            deleted = set(rng.sample(outside, rng.randint(0, len(outside))))
            feasible_pool = tuple(universe - deleted)
            if not feasible_pool:
                continue
            candidate = set(
                rng.sample(feasible_pool, rng.randint(1, min(12, len(feasible_pool))))
            )
            outside_anchor = tuple(candidate - anchor)
            if not outside_anchor:
                continue
            prescription = {rng.choice(outside_anchor)}
            remaining = tuple(candidate - prescription)
            prescription.update(
                rng.sample(remaining, rng.randint(0, min(2, len(remaining))))
            )
            residual = prescription - fixed
            assert residual
            assert residual.isdisjoint(deleted)
            assert residual <= universe - fixed - deleted
            checked += 1
    return checked


def check_depth_and_grouping():
    rng = random.Random(897)
    depth_cases = 0
    for universe_size in range(1, 200):
        for _ in range(20):
            fixed = set()
            deleted = set()
            steps = 0
            while len(fixed | deleted) < universe_size:
                undecided = list(set(range(universe_size)) - fixed - deleted)
                rank = rng.randint(1, min(3, len(undecided)))
                prescription = rng.sample(undecided, rank)
                child = rng.randint(0, rank)
                if child == rank:
                    fixed.update(prescription)
                else:
                    fixed.update(prescription[:child])
                    deleted.add(prescription[child])
                steps += 1
                assert fixed.isdisjoint(deleted)
                assert steps <= universe_size
            depth_cases += 1

    grouping_cases = 0
    cells = tuple(range(12))
    targets = list(combinations(cells, 3))
    for _ in range(2000):
        leaves = []
        next_state = 0
        for _leaf in range(rng.randint(1, 60)):
            target = rng.choice(targets)
            states = set()
            for _state in range(rng.randint(1, 8)):
                assignment = tuple(rng.randint(0, 1) for _ in range(3))
                states.add((next_state, target, assignment))
                next_state += 1
            leaves.append((target, states))
        all_states = set().union(*(states for _, states in leaves))
        by_target = {}
        for target, states in leaves:
            by_target.setdefault(target, set()).update(states)
        assert set().union(*by_target.values()) == all_states
        by_label = {}
        for target, states in by_target.items():
            for state in states:
                by_label.setdefault((target, state[2]), set()).add(state)
        assert set().union(*by_label.values()) == all_states
        assert len(by_label) <= 8 * len(by_target)
        grouping_cases += 1
    return depth_cases, grouping_cases


def check_density():
    checked = 0
    for side in range(2, 80):
        class_count = 8 * comb(side * side, 3)
        for total in range(1, 500):
            lower = ceil(total / class_count)
            assert lower * class_count >= total
            checked += 1
    return checked


def main():
    partitions, contractions = check_partitions_and_contractions()
    depths, groupings = check_depth_and_grouping()
    print(
        "verified disjoint leaf certificate compression:",
        partitions,
        "ordered partitions,",
        contractions,
        "prefix contractions,",
        check_undecided_progress(),
        "undecided-edge cases,",
        depths,
        "status paths,",
        groupings,
        "leaf-grouping cases, and",
        check_density(),
        "density cases",
    )


if __name__ == "__main__":
    main()
