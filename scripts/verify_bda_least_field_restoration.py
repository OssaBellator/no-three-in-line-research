#!/usr/bin/env python3
"""Finite audit for BDA5bg--BDA5bk."""

from itertools import permutations, product
import random

SEED = 20260728


def canonical_gate(cycle):
    """Return the canonical least-field restoration excursion."""
    width = len(cycle[0])
    changed = [
        j for j in range(width)
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


def audit_cycle(cycle, counters):
    gate = canonical_gate(cycle)
    if gate is None:
        counters["constant"] += 1
        return

    field, base, rotated, return_step = gate
    n = len(rotated)
    assert rotated[0][field] == base
    assert rotated[1][field] != base
    assert rotated[(return_step - 1) % n][field] != base
    assert rotated[return_step % n][field] == base
    assert all(
        rotated[step][field] != base
        for step in range(1, return_step)
    )

    values = [state[field] for state in rotated]
    nondecreasing = all(
        values[(i + 1) % n] >= values[i]
        for i in range(n)
    )
    nonincreasing = all(
        values[(i + 1) % n] <= values[i]
        for i in range(n)
    )
    assert not nondecreasing
    assert not nonincreasing

    restoration = (
        field,
        base,
        rotated[(return_step - 1) % n],
        rotated[return_step % n],
    )
    counters["restoration_addresses"].add(restoration)
    counters["nonconstant"] += 1


def main():
    rng = random.Random(SEED)
    counters = {
        "cycles": 0,
        "constant": 0,
        "nonconstant": 0,
        "restoration_addresses": set(),
    }

    # Exhaustive small product-state cycles.
    for width in range(1, 4):
        states = list(product(range(3), repeat=width))
        for length in range(2, min(5, len(states)) + 1):
            for cycle in permutations(states, length):
                audit_cycle(list(cycle), counters)
                counters["cycles"] += 1
                if counters["cycles"] >= 120_000:
                    break
            if counters["cycles"] >= 120_000:
                break
        if counters["cycles"] >= 120_000:
            break

    # Random larger alphabets and dimensions.
    for _ in range(25_000):
        width = rng.randint(1, 6)
        alphabet = rng.randint(2, 6)
        all_states = list(product(range(alphabet), repeat=width))
        length = rng.randint(2, min(10, len(all_states)))
        cycle = rng.sample(all_states, length)
        audit_cycle(cycle, counters)
        counters["cycles"] += 1

    ticket_stock = len(counters["restoration_addresses"])
    assert counters["nonconstant"] <= counters["cycles"]
    assert ticket_stock <= counters["nonconstant"]

    print("BDA least-field restoration audit passed")
    print(f"  cycles: {counters['cycles']}")
    print(f"  nonconstant cycles: {counters['nonconstant']}")
    print(f"  distinct restoration addresses: {ticket_stock}")


if __name__ == "__main__":
    main()
