#!/usr/bin/env python3
"""Finite audit for BDA5cf--BDA5cj: paid source replenishment bank."""

import random
from math import ceil, floor

rng = random.Random(20260728)
epochs = restorations = deposits = unit_checks = dyadic_checks = 0

for _ in range(8000):
    epochs += 1
    length_cap = rng.randint(2, 10)
    threshold = rng.randint(2, 12)
    initial = rng.randint(0, 80)
    balance = initial
    total_deposit = 0
    consumed = 0
    count = 0

    for _step in range(rng.randint(5, 80)):
        if rng.random() < 0.38:
            amount = rng.randint(0, 20)
            balance += amount
            total_deposit += amount
            deposits += amount
        else:
            jump = rng.randint(threshold, 80)
            cost = ceil(jump / (length_cap - 1))
            if cost <= balance:
                balance -= cost
                consumed += cost
                count += 1
                restorations += 1
                unit_checks += 1
                assert cost >= ceil(threshold / (length_cap - 1))
                b = jump.bit_length() - 1
                assert cost >= ceil((1 << b) / (length_cap - 1))
                dyadic_checks += 1

    c0 = ceil(threshold / (length_cap - 1))
    assert consumed <= initial + total_deposit
    assert count <= floor((initial + total_deposit) / c0)

print(f"{epochs=}")
print(f"{restorations=}")
print(f"{deposits=}")
print(f"{unit_checks=}")
print(f"{dyadic_checks=}")
