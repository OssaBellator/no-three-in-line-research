#!/usr/bin/env python3
from collections import defaultdict
from math import ceil
import random

RNG = random.Random(20260728)

systems = 10000
ledger_classes = 0
boundary_signatures = 0
output_units = 0
barrier_epochs = 0
neutral_epochs = 0
coordinate_witnesses = 0

for _ in range(systems):
    d = RNG.randint(1, 4)
    B = RNG.randint(1, 4)
    L = RNG.randint(1, 9)
    profiles = [tuple(RNG.randint(0, B) for _ in range(d)) for _ in range(L)]
    outputs = [RNG.randint(0, 25) for _ in range(L)]

    aggregate = defaultdict(int)
    raw_vector = [0] * d
    for profile, output in zip(profiles, outputs):
        aggregate[profile] += output
        for j in range(d):
            raw_vector[j] += profile[j] * output
    quotient_vector = [0] * d
    for profile, output in aggregate.items():
        for j in range(d):
            quotient_vector[j] += profile[j] * output
    assert raw_vector == quotient_vector
    assert len(aggregate) <= (B + 1) ** d

    boundary_mass = sum(raw_vector)
    output_units += sum(outputs)
    ledger_classes += L
    boundary_signatures += len(aggregate)

    if boundary_mass == 0:
        neutral_epochs += 1
        assert all(outputs[i] == 0 or all(x == 0 for x in profiles[i]) for i in range(L))
    else:
        barrier_epochs += 1
        heavy = max(raw_vector)
        assert heavy >= ceil(boundary_mass / d)
        coordinate_witnesses += 1

print(f"systems={systems}")
print(f"ledger_classes={ledger_classes}")
print(f"boundary_signatures={boundary_signatures}")
print(f"output_units={output_units}")
print(f"barrier_epochs={barrier_epochs}")
print(f"neutral_epochs={neutral_epochs}")
print(f"coordinate_witnesses={coordinate_witnesses}")
