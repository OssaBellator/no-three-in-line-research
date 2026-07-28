#!/usr/bin/env python3
"""Finite audit for SAS5ic--SAS5ig: bounded exact-core capacity bank."""

import random

rng = random.Random(20260728)
epochs = cores = executions = replenishments = overloads = 0

for _ in range(10000):
    epochs += 1
    r = rng.randint(1, 6)
    atoms = tuple(range(r))
    capacities = {a: rng.randint(0, 30) for a in atoms}
    initial = capacities.copy()
    deposited = {a: 0 for a in atoms}

    size = rng.randint(1, r)
    core = atoms[:size]
    cores += 1

    for _j in range(rng.randint(5, 80)):
        if rng.random() < 0.22:
            atom = rng.choice(core)
            amount = rng.randint(0, 5)
            capacities[atom] += amount
            deposited[atom] += amount
            replenishments += amount
            continue

        demand = rng.randint(1, 4)
        if all(capacities[a] >= demand for a in core):
            for atom in core:
                capacities[atom] -= demand
            executions += demand
        else:
            overloads += 1

    used_values = {
        initial[a] + deposited[a] - capacities[a]
        for a in core
    }
    assert len(used_values) == 1
    used = next(iter(used_values))
    assert used <= min(initial[a] + deposited[a] for a in core)

print(f"{epochs=}")
print(f"{cores=}")
print(f"{executions=}")
print(f"{replenishments=}")
print(f"{overloads=}")
