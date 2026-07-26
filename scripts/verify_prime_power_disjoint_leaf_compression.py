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
            {
                state
                for state in family
                if prefix.issubset(state) and edge not in state
            }
        )
    parts.append(
        {state for state in family if set(prescription).issubset(state)}
    )
    return parts


def contract_family(family, fixed):
    fixed = set(fixed)
    return {frozenset(set(state) - fixed) for state in family}


def check_ordered_partitions():
    rng = random.Random(894)
    checked = 0
    for universe_size in range(1, 13):
        universe = range(universe_size)
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(universe, state_size)
            ]
            for _ in range(min(100, max(1, 2 * len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                if not chosen:
                    continue
                rank = rng.randint(1, min(3, len(chosen)))
                prescription = rng.sample(tuple(chosen), rank)
                parts = ordered_partition(family, prescription)
                assert set().union(*parts) == family
                for first in range(len(parts)):
                    for second in range(first):
                        assert parts[first].isdisjoint(parts[second])
                checked += 1
    return checked


def check_prefix_contraction():
    rng = random.Random(895)
    checked = 0
    for universe_size in range(1, 13):
        universe = range(universe_size)
        for state_size in range(universe_size + 1):
            states = [
                frozenset(state)
                for state in combinations(universe, state_size)
            ]
            for _ in range(min(80, max(1, len(states)))):
                family = set(rng.sample(states, rng.randint(1, len(states))))
                chosen = rng.choice(tuple(family))
                if not chosen:
                    continue
                rank = rng.randint(1, min(3, len(chosen)))
                prescription = tuple(rng.sample(tuple(chosen), rank))
                parts = ordered_partition(family, prescription)
                for index, part in enumerate(parts):
                    if not part:
                        continue
                    fixed = (
                        set(prescription[:index])
                        if index < rank
                        else set(prescription)
                    )
                    assert all(fixed.issubset(state) for state in part)
                    residual = contract_family(part, fixed)
                    rebuilt = {
                        frozenset(set(state) | fixed)
                        for state in residual
                    }
                    assert rebuilt == part
                    assert len(residual) == len(part)
                    checked += 1
    return checked


def check_undecided_edge_progress():
    rng = random.Random(896)
    checked = 0
    for universe_size in range(3, 100):
        universe = set(range(universe_size))
        for _ in range(500):
            anchor = set(rng.sample(tuple(universe), rng.randint(0, universe_size)))
            fixed = set(rng.sample(tuple(anchor), rng.randint(0, len(anchor))))
            available_for_deleted = tuple(universe - anchor)
            deleted = set(
                rng.sample(
                    available_for_deleted,
                    rng.randint(0, len(available_for_deleted)),
                )
            )
            feasible_pool = tuple(universe - deleted)
            candidate = set(
                rng.sample(
                    feasible_pool,
                    rng.randint(1, min(12, len(feasible_pool))),
                )
            )
            outside_anchor = tuple(candidate - anchor)
            if not outside_anchor:
                continue
            required = {rng.choice(outside_anchor)}
            remaining = tuple(candidate - required)
            extra_count = rng.randint(0, min(2, len(remaining)))
            prescription = required | set(rng.sample(remaining, extra_count))
            residual = prescription - fixed
            assert residual
            assert residual.isdisjoint(deleted)
            assert residual <= universe - fixed - deleted
            checked += 1
    return checked


def check_status_depth():
    rng = random.Random(897)
    checked = 0
    for universe_size in range(1, 500):
        for _ in range(100):
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
            checked += 1
    return checked


def check_target_and_layer_grouping():
    rng = random.Random(899)
    checked = 0
    physical_cells = tuple(range(12))
    targets = list(combinations(physical_cells, 3))
    for _ in range(5000):
        leaf_count = rng.randint(1, 100)
        leaves = []
        used_state_ids = set()
        for leaf_index in range(leaf_count):
            target = rng.choice(targets)
            states = set()
            for _state_index in range(rng.randint(1, 10)):
                state_id = len(used_state_ids)
                used_state_ids.add(state_id)
                assignment = tuple(rng.randint(0, 1) for _ in range(3))
                states.add((state_id, target, assignment))
            leaves.append((target, states))

        target_groups = {}
        for target, states in leaves:
            target_groups.setdefault(target, set()).update(states)
        all_states = set().union(*(states for _, states in leaves))
        assert set().union(*target_groups.values()) == all_states

        labelled_groups = {}
        for target, states in target_groups.items():
            for state in states:
                assignment = state[2]
                labelled_groups.setdefault((target, assignment), set()).add(state)
        assert set().union(*labelled_groups.values()) == all_states
        assert len(labelled_groups) <= 8 * len(target_groups)
        checked += 1
    return checked


def check_density_arithmetic():
    checked = 0
    for side in range(2, 100):
        classes = 8 * comb(side * side, 3)
        for total in range(1, 1000):
            lower = ceil(total / classes)
            assert lower * classes >= total
            checked += 1
    return checked


def main():
    print(
        "verified disjoint leaf certificate compression:",
        check_ordered_partitions(),
        "ordered partitions,",
        check_prefix_contraction(),
        "prefix contractions,",
        check_undecided_edge_progress(),
        "undecided-edge cases,",
        check_status_depth(),
        "status paths,",
        check_target_and_layer_grouping(),
        "leaf-grouping cases, and",
        check_density_arithmetic(),
        "density cases",
    )


if __name__ == "__main__":
    main()
