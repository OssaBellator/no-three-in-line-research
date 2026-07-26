#!/usr/bin/env python3
"""Finite checks for AC3qf--AC3qj."""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import ceil
from random import Random


def exhaustive_vectors(counts: Counter[str]) -> None:
    for atom_count in range(1, 5):
        for capacities in product(range(3), repeat=atom_count):
            physical_cap = sum(capacities)
            for occupancy in product(range(4), repeat=atom_count):
                total = sum(occupancy)
                excess = max(total - physical_cap, 0)
                overloads = [max(occupancy[p] - capacities[p], 0) for p in range(atom_count)]
                overload_total = sum(overloads)
                assert overload_total >= excess

                feasible = all(occupancy[p] <= capacities[p] for p in range(atom_count))
                if feasible:
                    assert total <= physical_cap
                    counts["feasible occupancy vectors"] += 1
                if excess > 0:
                    overloaded = [p for p, value in enumerate(overloads) if value > 0]
                    assert overloaded
                    assert max(overloads) >= ceil(excess / atom_count)
                    assert min(overloaded) == next(p for p, value in enumerate(overloads) if value > 0)
                    counts["overloaded occupancy vectors"] += 1
                counts["occupancy vectors"] += 1


def random_histories(counts: Counter[str]) -> None:
    rng = Random(20260726)
    for _ in range(50000):
        atom_count = rng.randint(1, 8)
        capacities = [rng.randint(0, 8) for _ in range(atom_count)]
        if sum(capacities) == 0:
            capacities[rng.randrange(atom_count)] = 1
        occupancy = [rng.randint(0, cap) for cap in capacities]
        if sum(occupancy) == 0:
            candidates = [p for p, cap in enumerate(capacities) if cap > 0]
            p = rng.choice(candidates)
            occupancy[p] = 1

        initial_total = sum(occupancy)
        physical_cap = sum(capacities)
        amplification = 0
        losses = 0
        transitions = 0
        crossed = False

        for _step in range(150):
            live = [p for p, value in enumerate(occupancy) if value > 0]
            if not live:
                break
            debit = rng.choice(live)
            outputs_count = rng.randrange(4)
            outputs = [rng.randrange(atom_count) for _ in range(outputs_count)]

            before = occupancy[:]
            after = occupancy[:]
            after[debit] -= 1
            for p in outputs:
                after[p] += 1

            assert sum(after) - sum(before) == outputs_count - 1
            amplification += max(outputs_count - 1, 0)
            losses += max(1 - outputs_count, 0)
            transitions += 1

            overloaded_after = [p for p in range(atom_count) if after[p] > capacities[p]]
            if overloaded_after:
                newly_overloaded = [
                    p
                    for p in overloaded_after
                    if before[p] <= capacities[p]
                ]
                assert newly_overloaded
                for p in newly_overloaded:
                    assert after[p] - before[p] > 0
                    assert p in outputs
                canonical = min(newly_overloaded)
                assert canonical in outputs
                assert sum(after) > physical_cap or any(
                    after[p] > capacities[p] for p in range(atom_count)
                )
                counts["first crossing certificates"] += 1
                counts["newly overloaded atoms"] += len(newly_overloaded)
                crossed = True
                break

            occupancy = after
            assert all(occupancy[p] <= capacities[p] for p in range(atom_count))
            assert sum(occupancy) <= physical_cap
            assert amplification <= losses + physical_cap - initial_total

        counts["histories"] += 1
        counts["history transitions"] += transitions
        counts["amplification units"] += amplification
        counts["loss units"] += losses
        if crossed:
            counts["crossing histories"] += 1
        else:
            counts["feasible histories"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    exhaustive_vectors(counts)
    random_histories(counts)
    print("AC3qf--AC3qj physical source-capacity audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
