#!/usr/bin/env python3
"""Finite audit for OP4ad--OP4ah."""

from itertools import combinations, product
from math import comb
import random

SEED = 20260728


def blocker_subsets(k, b):
    states = []
    for size in range(b + 1):
        states.extend(frozenset(c) for c in combinations(range(k), size))
    return states


def canonical_gate(cycle):
    universe = sorted(set().union(*(state[0] for state in cycle)))
    blocker_changed = [
        atom for atom in universe
        if len({atom in state[0] for state in cycle}) > 1
    ]

    if blocker_changed:
        atom = min(blocker_changed)
        kind = ("blocker", atom)
    else:
        width = len(cycle[0][1])
        variable_changed = [
            index for index in range(width)
            if len({state[1][index] for state in cycle}) > 1
        ]
        if variable_changed:
            kind = ("variable", min(variable_changed))
        else:
            max_mask = max(state[2] for state in cycle)
            factor_changed = [
                bit for bit in range(max_mask.bit_length() + 1)
                if len({(state[2] >> bit) & 1 for state in cycle}) > 1
            ]
            if factor_changed:
                kind = ("factor", min(factor_changed))
            elif len({state[3] for state in cycle}) > 1:
                kind = ("boundary", 0)
            else:
                return None

    def value(state):
        name, index = kind
        if name == "blocker":
            return index in state[0]
        if name == "variable":
            return state[1][index]
        if name == "factor":
            return (state[2] >> index) & 1
        return state[3]

    n = len(cycle)
    change_index = next(
        i for i in range(n)
        if value(cycle[i]) != value(cycle[(i + 1) % n])
    )
    rotated = cycle[change_index:] + cycle[:change_index]
    initial = value(rotated[0])
    return_step = next(
        step for step in range(1, n + 1)
        if value(rotated[step % n]) == initial
    )
    return kind, initial, rotated, return_step, value


def main():
    rng = random.Random(SEED)
    counters = {
        "parameter_sets": 0,
        "states": 0,
        "cycles": 0,
        "blocker_gates": 0,
        "variable_gates": 0,
        "factor_gates": 0,
        "boundary_gates": 0,
    }

    for k in range(1, 7):
        for b in range(0, min(3, k) + 1):
            for width in range(1, 4):
                alphabet = 2
                factors = 3
                blockers = blocker_subsets(k, b)
                exact_blockers = sum(comb(k, size) for size in range(b + 1))
                assert len(blockers) == exact_blockers
                bound = (b + 1) * k ** b if b else 1
                assert exact_blockers <= bound

                states = [
                    (fibre, assignment, mask, boundary)
                    for fibre in blockers
                    for assignment in product(range(alphabet), repeat=width)
                    for mask in range(1 << factors)
                    for boundary in range(2)
                ]
                expected = exact_blockers * alphabet ** width * (1 << factors) * 2
                assert len(states) == expected
                counters["parameter_sets"] += 1
                counters["states"] += expected

                sample = states if len(states) <= 100 else rng.sample(states, 100)
                for _ in range(250):
                    length = rng.randint(2, min(10, len(sample)))
                    cycle = rng.sample(sample, length)
                    gate = canonical_gate(cycle)
                    assert gate is not None
                    kind, initial, rotated, return_step, value = gate
                    assert value(rotated[0]) == initial
                    assert value(rotated[1]) != initial
                    assert value(rotated[(return_step - 1) % length]) != initial
                    assert value(rotated[return_step % length]) == initial
                    assert all(
                        value(rotated[step]) != initial
                        for step in range(1, return_step)
                    )
                    counters["cycles"] += 1
                    counters[f"{kind[0]}_gates"] += 1

    print("OP bounded fibre/kernel audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
