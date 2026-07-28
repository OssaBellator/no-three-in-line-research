#!/usr/bin/env python3
"""Finite audit for SRR2am--SRR2aq: near-product perturbation stability."""

import random
from itertools import product

rng = random.Random(20260728)
systems = left_vertices = right_vertices = perturbations = 0

for _ in range(7000):
    systems += 1
    la, ra = rng.randint(1, 5), rng.randint(1, 5)
    lb, rb = rng.randint(1, 5), rng.randint(1, 5)

    LA, RA = list(range(la)), list(range(ra))
    LB, RB = list(range(lb)), list(range(rb))

    def random_factor(left, right):
        edges = set()
        for x in left:
            edges.add((x, rng.choice(right)))
            for y in right:
                if rng.random() < 0.55:
                    edges.add((x, y))
        return edges

    EA = random_factor(LA, RA)
    EB = random_factor(LB, RB)
    left = list(product(LA, LB))
    right = list(product(RA, RB))
    base_edges = {
        ((xa, xb), (ya, yb))
        for (xa, ya) in EA
        for (xb, yb) in EB
    }

    left0 = {x: 0 for x in left}
    right0 = {y: 0 for y in right}
    for x, y in base_edges:
        left0[x] += 1
        right0[y] += 1
    d0 = min(left0.values())
    D0 = max(right0.values())

    lamL = rng.randint(0, min(3, d0))
    lamR = rng.randint(0, 3)
    edges = set(base_edges)

    for x in left:
        incident = [(x, y) for y in right if (x, y) in edges]
        rng.shuffle(incident)
        for edge in incident[: rng.randint(0, min(lamL, len(incident)))]:
            edges.discard(edge)
            perturbations += 1

    additions_by_right = {y: 0 for y in right}
    candidates = [(x, y) for x in left for y in right if (x, y) not in edges]
    rng.shuffle(candidates)
    for x, y in candidates:
        if additions_by_right[y] >= lamR:
            continue
        if rng.random() < 0.08:
            edges.add((x, y))
            additions_by_right[y] += 1
            perturbations += 1

    left_deg = {x: 0 for x in left}
    right_load = {y: 0 for y in right}
    for x, y in edges:
        left_deg[x] += 1
        right_load[y] += 1
    d = min(left_deg.values())
    D = max(right_load.values())

    assert d >= d0 - lamL
    assert D <= D0 + lamR

    b = rng.randint(0, min(2, d))
    eps_bound = max(0.0, 1.0 - (d0 - lamL - b) / (D0 + lamR))
    eps_actual = 1.0 if D == 0 else max(0.0, 1.0 - (d - b) / D)
    assert eps_actual <= eps_bound + 1e-12

    left_vertices += len(left)
    right_vertices += len(right)

print(f"{systems=}")
print(f"{left_vertices=}")
print(f"{right_vertices=}")
print(f"{perturbations=}")
