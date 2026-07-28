#!/usr/bin/env python3
from itertools import combinations
from math import ceil
import random

RNG = random.Random(20260728)


def subsets(n):
    for r in range(1, n + 1):
        for c in combinations(range(n), r):
            yield c


systems = 10000
deficient_cores = 0
missing_incidences = 0
heavy_class_witnesses = 0
paid_incidences = 0
overload_incidences = 0

for _ in range(systems):
    m = RNG.randint(2, 7)
    n = RNG.randint(2, 7)
    p = RNG.uniform(0.15, 0.8)
    adj = [{j for j in range(n) if RNG.random() < p} for _ in range(m)]

    best = None
    for X in subsets(m):
        N = set().union(*(adj[i] for i in X))
        deficit = len(X) - len(N)
        if deficit > 0:
            key = (-deficit, len(X), X)
            if best is None or key < best[0]:
                best = (key, X, N, deficit)
    if best is None:
        continue

    _, X, N, deficit = best
    deficient_cores += 1
    rectangle = [(i, j) for i in X for j in range(n) if j not in N]
    assert len(rectangle) == len(X) * (n - len(N))
    assert all(j not in adj[i] for i, j in rectangle)

    L = RNG.randint(1, 6)
    loads = [0] * L
    for pair in rectangle:
        loads[RNG.randrange(L)] += 1
    total = sum(loads)
    assert total == len(rectangle)
    heavy = max(loads)
    assert heavy >= ceil(total / L)
    heavy_class_witnesses += 1
    missing_incidences += total

    capacities = [RNG.randint(0, x + 2) for x in loads]
    paid = sum(min(loads[k], capacities[k]) for k in range(L))
    overload = sum(max(0, loads[k] - capacities[k]) for k in range(L))
    assert paid + overload == total
    paid_incidences += paid
    overload_incidences += overload

print(f"systems={systems}")
print(f"deficient_cores={deficient_cores}")
print(f"missing_incidences={missing_incidences}")
print(f"heavy_class_witnesses={heavy_class_witnesses}")
print(f"paid_incidences={paid_incidences}")
print(f"overload_incidences={overload_incidences}")
