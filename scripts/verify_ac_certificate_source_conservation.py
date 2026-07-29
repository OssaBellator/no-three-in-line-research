#!/usr/bin/env python3
"""Finite audit for AC5cn--AC5cr."""

import random

SEED = 1401
SYSTEMS = 7000

rng = random.Random(SEED)
stats = {
    "systems": 0, "source_classes": 0, "certificate_classes": 0,
    "transfers": 0, "source_deposits": 0, "certificate_deposits": 0,
    "paid_defects": 0, "certified_systems": 0, "amplification_witnesses": 0,
}

for _ in range(SYSTEMS):
    source_count = rng.randint(2, 6)
    certificate_count = rng.randint(2, 6)
    live = [rng.randint(0, 8) for _ in range(source_count)]
    certificates = [0] * certificate_count
    initial = sum(live)
    exogenous = paid = 0
    bad = False

    for _step in range(rng.randint(8, 30)):
        operation = rng.choices(
            ["move", "deposit", "issue", "pay", "bad"],
            [30, 14, 25, 25, 2],
        )[0]

        if operation == "move":
            u = rng.randrange(source_count)
            v = rng.randrange(source_count)
            amount = rng.randint(0, live[u])
            live[u] -= amount
            live[v] += amount
            stats["transfers"] += amount
        elif operation == "deposit":
            u = rng.randrange(source_count)
            amount = rng.randint(0, 5)
            live[u] += amount
            exogenous += amount
            stats["source_deposits"] += amount
        elif operation == "issue":
            u = rng.randrange(source_count)
            k = rng.randrange(certificate_count)
            amount = rng.randint(0, live[u])
            live[u] -= amount
            certificates[k] += amount
            stats["certificate_deposits"] += amount
        elif operation == "pay":
            k = rng.randrange(certificate_count)
            amount = rng.randint(0, certificates[k])
            certificates[k] -= amount
            paid += amount
            stats["paid_defects"] += amount
        else:
            k = rng.randrange(certificate_count)
            certificates[k] += rng.randint(1, 3)
            stats["amplification_witnesses"] += 1
            bad = True
            break

        assert sum(live) + sum(certificates) + paid == initial + exogenous

    if not bad:
        assert sum(live) + sum(certificates) + paid == initial + exogenous
        stats["certified_systems"] += 1

    stats["systems"] += 1
    stats["source_classes"] += source_count
    stats["certificate_classes"] += certificate_count

for key, value in stats.items():
    print(f"{key}: {value}")
