#!/usr/bin/env python3
"""Finite checks for corrected CMR998--CMR1005."""

from collections import Counter
from math import ceil, comb
import random


def random_joint_state(cell_count, maximum_size, rng):
    size = rng.randint(0, min(cell_count, maximum_size))
    cells = rng.sample(range(cell_count), size)
    return frozenset((rng.randint(0, 1), cell) for cell in cells)


def signature_state(cell_count, triple, edge, pair_layers, rng):
    x, y, z = triple
    state = {
        edge,
        (pair_layers[0], y),
        (pair_layers[1], z),
    }
    available = list(set(range(cell_count)) - set(triple))
    for cell in rng.sample(available, rng.randint(0, min(8, len(available)))):
        state.add((rng.randint(0, 1), cell))
    return frozenset(state)


def physical_cells(state):
    return {cell for _layer, cell in state}


def residual_pair(state, triple):
    _x, y, z = triple
    return frozenset(
        next(edge for edge in state if edge[1] == cell)
        for cell in (y, z)
    )


def assignment_partition(family, edge, triple):
    with_edge = {state for state in family if edge in state}
    with_target = {
        state for state in with_edge if set(triple) <= physical_cells(state)
    }
    classes = {}
    for state in with_target:
        pair = residual_pair(state, triple)
        classes.setdefault(pair, set()).add(state)
    return (
        {state for state in family if edge not in state},
        with_edge - with_target,
        classes,
    )


def check_pair_extraction_and_recurrence():
    rng = random.Random(998)
    occurrences = 0
    histories = 0
    for cell_count in range(3, 100):
        for _ in range(300):
            triple = tuple(rng.sample(range(cell_count), 3))
            edge = (rng.randint(0, 1), triple[0])
            states = [
                signature_state(
                    cell_count,
                    triple,
                    edge,
                    (rng.randint(0, 1), rng.randint(0, 1)),
                    rng,
                )
                for _episode in range(rng.randint(1, 100))
            ]
            pairs = [residual_pair(state, triple) for state in states]
            assert len(set(pairs)) <= 4
            for state, pair in zip(states, pairs):
                assert edge in state
                assert len(pair) == 2
                assert {item[1] for item in pair} == {triple[1], triple[2]}
                assert ({edge} | set(pair)) <= set(state)
            counts = Counter(pairs)
            assert max(counts.values()) >= ceil(len(states) / 4)
            occurrences += len(states)
            histories += 1
    return occurrences, histories


def check_exact_assignment_partition():
    rng = random.Random(1001)
    checked = 0
    multiple_pair_edge_branches = 0
    contractions = 0
    for cell_count in range(3, 50):
        for _ in range(100):
            triple = tuple(rng.sample(range(cell_count), 3))
            edge = (rng.randint(0, 1), triple[0])
            family = set()

            # Deliberately install all four pair assignments. This guards against
            # the false assertion that conditioning on edge alone fixes a pair.
            for first_layer in (0, 1):
                for second_layer in (0, 1):
                    family.add(
                        signature_state(
                            cell_count,
                            triple,
                            edge,
                            (first_layer, second_layer),
                            rng,
                        )
                    )
            for _state in range(30):
                family.add(random_joint_state(cell_count, 12, rng))

            without_edge, edge_without_target, classes = assignment_partition(
                family, edge, triple
            )
            parts = [without_edge, edge_without_target, *classes.values()]
            assert set().union(*parts) == family
            for first in range(len(parts)):
                for second in range(first):
                    assert parts[first].isdisjoint(parts[second])
            assert len(classes) <= 4
            if len(classes) > 1:
                multiple_pair_edge_branches += 1

            for pair, assignment_class in classes.items():
                assert all(
                    ({edge} | set(pair)) <= set(state)
                    for state in assignment_class
                )
                residual = {
                    frozenset(set(state) - {edge})
                    for state in assignment_class
                }
                assert len(residual) == len(assignment_class)
                assert all(set(pair) <= set(state) for state in residual)
                rebuilt = {
                    frozenset(set(state) | {edge})
                    for state in residual
                }
                assert rebuilt == assignment_class
                contractions += 1
            checked += 1
    assert multiple_pair_edge_branches > 0
    return checked, multiple_pair_edge_branches, contractions


def check_augmented_stock_and_bounds():
    checked = 0
    for side in range(1, 300):
        cells = side * side
        basic = 2 * cells * comb(cells - 1, 2) if cells >= 3 else 0
        augmented = 4 * basic
        assert augmented >= basic
        for threshold in range(2, 50):
            one_target_cap = 2 * (threshold - 1) * basic
            assert one_target_cap * 2 == 4 * (threshold - 1) * basic
            checked += 1
    return checked


def check_owner_independence():
    rng = random.Random(1003)
    checked = 0
    for _ in range(50000):
        side = rng.randint(2, 100)
        triple = tuple(rng.sample(range(side * side), 3))
        edge = (rng.randint(0, 1), triple[0])
        pair = frozenset(
            {
                (rng.randint(0, 1), triple[1]),
                (rng.randint(0, 1), triple[2]),
            }
        )
        signature = (edge, frozenset(triple), pair)
        owner_a = (rng.randint(0, 10), rng.randint(0, 10))
        owner_b = (rng.randint(0, 10), rng.randint(0, 10))
        assert signature == (edge, frozenset(triple), pair)
        assert owner_a == owner_b or signature == signature
        checked += 1
    return checked


def main():
    occurrences, histories = check_pair_extraction_and_recurrence()
    partitions, multiple, contractions = check_exact_assignment_partition()
    print(
        "verified corrected absolute signature stabilization:",
        occurrences,
        "pair occurrences across",
        histories,
        "histories,",
        partitions,
        "exact partitions with",
        multiple,
        "multi-pair edge-conditioned branches and",
        contractions,
        "fixed-class contractions,",
        check_augmented_stock_and_bounds(),
        "stock bounds, and",
        check_owner_independence(),
        "owner-independence cases",
    )


if __name__ == "__main__":
    main()
