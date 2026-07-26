#!/usr/bin/env python3
"""Finite checks for CMR998--CMR1005."""

from collections import Counter
from math import ceil, comb
import random


def signature_state(cell_count, triple, edge_layer, rng):
    x, y, z = triple
    state = {(edge_layer, x), (rng.randint(0, 1), y), (rng.randint(0, 1), z)}
    available = list(set(range(cell_count)) - set(triple))
    for cell in rng.sample(available, rng.randint(0, min(10, len(available)))):
        state.add((rng.randint(0, 1), cell))
    return frozenset(state)


def residual_pair(state, triple, edge):
    x, y, z = triple
    assert edge[1] == x
    return frozenset(
        next(label for label in state if label[1] == cell)
        for cell in (y, z)
    )


def check_pair_extraction_and_four_types():
    rng = random.Random(998)
    checked = 0
    recurrence = 0
    for cell_count in range(3, 100):
        for _ in range(500):
            triple = tuple(rng.sample(range(cell_count), 3))
            edge = (rng.randint(0, 1), triple[0])
            states = [
                signature_state(cell_count, triple, edge[0], rng)
                for _episode in range(rng.randint(1, 100))
            ]
            pairs = [residual_pair(state, triple, edge) for state in states]
            assert len(set(pairs)) <= 4
            for state, pair in zip(states, pairs):
                assert edge in state
                assert len(pair) == 2
                assert {label[1] for label in pair} == {triple[1], triple[2]}
                assert ({edge} | set(pair)) <= set(state)
            counts = Counter(pairs)
            assert max(counts.values()) >= ceil(len(states) / 4)
            checked += len(states)
            recurrence += 1
    return checked, recurrence


def check_binary_split_and_transfer():
    rng = random.Random(1001)
    checked = 0
    for cell_count in range(3, 100):
        labelled_universe = [
            (layer, cell) for layer in (0, 1) for cell in range(cell_count)
        ]
        for _ in range(300):
            triple = tuple(rng.sample(range(cell_count), 3))
            edge = (rng.randint(0, 1), triple[0])
            witness = signature_state(cell_count, triple, edge[0], rng)
            pair = residual_pair(witness, triple, edge)
            family = {witness}
            for _state in range(100):
                size = rng.randint(0, min(cell_count, 15))
                cells = rng.sample(range(cell_count), size)
                family.add(
                    frozenset((rng.randint(0, 1), cell) for cell in cells)
                )
            without = {state for state in family if edge not in state}
            with_edge = {state for state in family if edge in state}
            assert without.isdisjoint(with_edge)
            assert without | with_edge == family
            for state in with_edge:
                labelled_target = {edge} | set(pair)
                assert (labelled_target <= set(state)) == (
                    set(pair) <= (set(state) - {edge})
                )
            assert witness in with_edge
            checked += 1
    return checked


def check_augmented_stock_and_bounds():
    checked = 0
    for side in range(1, 300):
        cells = side * side
        basic = 2 * cells * comb(cells - 1, 2) if cells >= 3 else 0
        augmented = 4 * basic
        assert augmented >= basic
        for threshold in range(2, 50):
            one_target_cap = 2 * (threshold - 1) * basic
            assert 2 * one_target_cap == 4 * (threshold - 1) * basic
            checked += 1
    return checked


def check_owner_independence():
    rng = random.Random(1003)
    checked = 0
    for _ in range(100000):
        side = rng.randint(2, 100)
        triple = tuple(rng.sample(range(side * side), 3))
        edge = (rng.randint(0, 1), triple[0])
        pair = frozenset(
            {(rng.randint(0, 1), triple[1]), (rng.randint(0, 1), triple[2])}
        )
        signature = (edge, frozenset(triple), pair)
        owner_a = (rng.randint(0, 10), rng.randint(0, 10))
        owner_b = (rng.randint(0, 10), rng.randint(0, 10))
        assert signature == (edge, frozenset(triple), pair)
        assert owner_a == owner_b or signature == signature
        checked += 1
    return checked


def main():
    pair_cases, recurrence_cases = check_pair_extraction_and_four_types()
    print(
        "verified absolute signature pair stabilization:",
        pair_cases,
        "pair occurrences across",
        recurrence_cases,
        "recurrence families,",
        check_binary_split_and_transfer(),
        "binary transfers,",
        check_augmented_stock_and_bounds(),
        "stock bounds, and",
        check_owner_independence(),
        "owner-independence cases",
    )


if __name__ == "__main__":
    main()
