#!/usr/bin/env python3
"""Finite audit for GC2ge--GC2gi."""

from itertools import combinations
from math import comb
import random

SEED = 20260728


def subsets_upto(k, d):
    states = []
    for size in range(d + 1):
        states.extend(frozenset(c) for c in combinations(range(k), size))
    return states


def canonical_gate(cycle):
    universe = sorted(set().union(*cycle))
    changed = [
        atom for atom in universe
        if len({atom in reservoir for reservoir in cycle}) > 1
    ]
    if not changed:
        return None

    atom = min(changed)
    n = len(cycle)
    change_index = next(
        i for i in range(n)
        if (atom in cycle[i]) != (atom in cycle[(i + 1) % n])
    )
    rotated = cycle[change_index:] + cycle[:change_index]
    initial_bit = atom in rotated[0]
    return_step = next(
        step for step in range(1, n + 1)
        if (atom in rotated[step % n]) == initial_bit
    )
    return atom, initial_bit, rotated, return_step


def main():
    rng = random.Random(SEED)
    counters = {
        "parameter_sets": 0,
        "states": 0,
        "histories": 0,
        "restoration_gates": 0,
    }

    for k in range(1, 11):
        for d in range(0, min(5, k) + 1):
            states = subsets_upto(k, d)
            exact = sum(comb(k, size) for size in range(d + 1))
            assert len(states) == exact
            polynomial = (d + 1) * (k ** d if d else 1)
            assert exact <= polynomial
            counters["parameter_sets"] += 1
            counters["states"] += exact

            if len(states) < 2:
                continue
            sample = states if len(states) <= 80 else rng.sample(states, 80)
            for _ in range(400):
                length = rng.randint(2, min(10, len(sample)))
                cycle = rng.sample(sample, length)
                gate = canonical_gate(cycle)
                assert gate is not None
                atom, initial_bit, rotated, return_step = gate
                assert (atom in rotated[0]) == initial_bit
                assert (atom in rotated[1]) != initial_bit
                assert (atom in rotated[(return_step - 1) % length]) != initial_bit
                assert (atom in rotated[return_step % length]) == initial_bit
                assert all(
                    (atom in rotated[step]) != initial_bit
                    for step in range(1, return_step)
                )
                counters["histories"] += 1
                counters["restoration_gates"] += 1

    print("GC bounded small-reservoir audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
