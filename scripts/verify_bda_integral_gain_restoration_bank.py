#!/usr/bin/env python3
"""Finite audit for BDA5dy--BDA5ec."""

import math
import random

SEED = 1402
SYSTEMS = 6500
rng = random.Random(SEED)

stats = {
    "systems": 0, "vertices": 0, "edges": 0, "primitive_weight_units": 0,
    "transfers": 0, "raw_transfer_input": 0, "deposit_weight": 0,
    "restoration_weight": 0, "certified_systems": 0, "factor_violations": 0,
}

for _ in range(SYSTEMS):
    n = rng.randint(2, 6)
    weights = [rng.randint(1, 9) for _ in range(n)]
    divisor = math.gcd(*weights)
    weights = [value // divisor for value in weights]
    live = [rng.randint(0, 6) for _ in range(n)]
    initial = sum(weights[i] * live[i] for i in range(n))
    deposited = paid = 0

    edges = []
    for u in range(n):
        for v in range(n):
            if u == v or rng.random() > 0.35:
                continue
            denominator = rng.randint(1, 6)
            max_numerator = max(1, denominator * weights[u] // weights[v])
            numerator = rng.randint(1, max_numerator)
            if numerator * weights[v] <= denominator * weights[u]:
                edges.append((u, v, numerator, denominator))

    bad = False
    for _step in range(rng.randint(10, 35)):
        operation = rng.choices(
            ["transfer", "deposit", "restore", "bad"],
            [50, 15, 30, 2],
        )[0]

        if operation == "transfer" and edges:
            u, v, numerator, denominator = rng.choice(edges)
            input_mass = rng.randint(0, live[u])
            output_mass = rng.randint(0, numerator * input_mass // denominator)
            live[u] -= input_mass
            live[v] += output_mass
            paid += weights[u] * input_mass - weights[v] * output_mass
            stats["transfers"] += 1
            stats["raw_transfer_input"] += input_mass
        elif operation == "deposit":
            v = rng.randrange(n)
            amount = rng.randint(0, 5)
            live[v] += amount
            deposited += weights[v] * amount
            stats["deposit_weight"] += weights[v] * amount
        elif operation == "restore":
            v = rng.randrange(n)
            amount = rng.randint(0, live[v])
            live[v] -= amount
            paid += weights[v] * amount
            stats["restoration_weight"] += weights[v] * amount
        else:
            u = rng.randrange(n)
            v = rng.randrange(n)
            if weights[v] > weights[u]:
                stats["factor_violations"] += 1
                bad = True
                break

        assert sum(weights[i] * live[i] for i in range(n)) + paid == initial + deposited

    if not bad:
        stats["certified_systems"] += 1

    stats["systems"] += 1
    stats["vertices"] += n
    stats["edges"] += len(edges)
    stats["primitive_weight_units"] += sum(weights)

for key, value in stats.items():
    print(f"{key}: {value}")
