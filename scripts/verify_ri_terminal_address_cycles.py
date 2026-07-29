#!/usr/bin/env python3
"""Finite audit for RI5ay--RI5bc."""

from itertools import product
import random

SEED = 20260728

SQ_TYPES = (
    (1, 0),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2), (3, 3),
)


def terminal_records(n, k_occ):
    """Generate a deliberately overcounted terminal dictionary."""
    records = []
    occurrences = range(k_occ + 1)  # zero is the null padding symbol
    for word_type in range(22):
        for rank, overlap in SQ_TYPES:
            for occupancy in range(1, n + 1):
                for triple in product(occurrences, repeat=3):
                    records.append(
                        (word_type, rank, overlap, occupancy) + triple
                    )
    return records


def first_repeat_cycle(history):
    seen = {}
    for index, state in enumerate(history):
        if state in seen:
            return history[seen[state]:index]
        seen[state] = index
    return None


def canonical_gate(cycle):
    changed = [
        j for j in range(len(cycle[0]))
        if len({state[j] for state in cycle}) > 1
    ]
    if not changed:
        return None
    field = min(changed)
    base = min(state[field] for state in cycle)
    n = len(cycle)
    exits = [
        i for i in range(n)
        if cycle[i][field] == base
        and cycle[(i + 1) % n][field] != base
    ]
    assert exits
    start = min(exits)
    rotated = cycle[start:] + cycle[:start]
    return_step = next(
        step for step in range(1, n + 1)
        if rotated[step % n][field] == base
    )
    return field, base, rotated, return_step


def main():
    rng = random.Random(SEED)
    counters = {
        "dictionaries": 0,
        "records": 0,
        "histories": 0,
        "cycles": 0,
        "restoration_gates": 0,
    }

    for n in range(2, 5):
        for k_occ in range(1, 4):
            records = terminal_records(n, k_occ)
            bound = 264 * n * (k_occ + 1) ** 3
            assert len(records) <= bound
            counters["dictionaries"] += 1
            counters["records"] += len(records)

            # Pigeonhole histories: repeat one selected complete record.
            sample_size = min(120, len(records))
            sample = rng.sample(records, sample_size)
            for _ in range(500):
                prefix_length = rng.randint(1, sample_size)
                prefix = rng.sample(sample, prefix_length)
                repeated_index = rng.randrange(prefix_length)
                history = prefix + [prefix[repeated_index]]
                cycle = first_repeat_cycle(history)
                assert cycle is not None
                assert len(cycle) <= len(records)
                counters["histories"] += 1
                counters["cycles"] += 1

                gate = canonical_gate(cycle)
                if gate is None:
                    assert len(cycle) == 1
                    continue
                field, base, rotated, return_step = gate
                assert rotated[0][field] == base
                assert rotated[1][field] != base
                assert rotated[(return_step - 1) % len(rotated)][field] != base
                assert rotated[return_step % len(rotated)][field] == base
                assert all(
                    rotated[step][field] != base
                    for step in range(1, return_step)
                )
                counters["restoration_gates"] += 1

    print("RI terminal-address cycle audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
