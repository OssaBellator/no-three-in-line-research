#!/usr/bin/env python3
import random

RNG = random.Random(20260728)


def max_independent_weight(weights, supports, active):
    active = list(active)
    best = 0
    for mask in range(1 << len(active)):
        total = 0
        used = set()
        ok = True
        for k, v in enumerate(active):
            if mask >> k & 1:
                if used & supports[v]:
                    ok = False
                    break
                used |= supports[v]
                total += weights[v]
        if ok:
            best = max(best, total)
    return best


systems = 2200
thresholds = 0
candidates = 0
candidate_atom_incidences = 0
exact_checks = 0

for _ in range(systems):
    n = RNG.randint(2, 10)
    A = RNG.randint(2, 8)
    rmax = RNG.randint(1, min(4, A))
    weights = [RNG.randint(1, 6) for _ in range(n)]
    costs = [RNG.randint(0, 6) for _ in range(n)]
    supports = []
    for _ in range(n):
        r = RNG.randint(1, rmax)
        supports.append(set(RNG.sample(range(A), r)))

    candidates += n
    candidate_atom_incidences += sum(map(len, supports))

    for threshold in range(max(costs) + 1):
        active = [v for v in range(n) if costs[v] <= threshold]
        if not active:
            continue
        thresholds += 1
        loads = [sum(a in supports[v] for v in active) for a in range(A)]
        degrees = {}
        for v in active:
            degree = sum(1 for u in active if u != v and supports[u] & supports[v])
            atom_bound = sum(loads[a] - 1 for a in supports[v])
            assert degree <= atom_bound
            degrees[v] = degree
        local_bound = sum(weights[v] / (degrees[v] + 1) for v in active)
        optimum = max_independent_weight(weights, supports, active)
        assert optimum + 1e-12 >= local_bound

        total_weight = sum(weights[v] for v in active)
        Lambda = max(loads)
        rank = max(len(supports[v]) for v in active)
        coarse = total_weight / (1 + rank * (Lambda - 1))
        assert optimum + 1e-12 >= coarse
        exact_checks += 1

print(f"systems={systems}")
print(f"thresholds={thresholds}")
print(f"candidates={candidates}")
print(f"candidate_atom_incidences={candidate_atom_incidences}")
print(f"exact_checks={exact_checks}")
