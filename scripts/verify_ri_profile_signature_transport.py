#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import combinations
import random

RNG = random.Random(20260728)


def maxflow(demands, caps, neigh):
    P, O = len(demands), len(caps)
    N = 2 + P + O
    s, t = N - 2, N - 1
    cap = [[0] * N for _ in range(N)]
    for i, d in enumerate(demands):
        cap[s][i] = d
    inf = sum(demands) + 1
    for i in range(P):
        for j in neigh[i]:
            cap[i][P + j] = inf
    for j, c in enumerate(caps):
        cap[P + j][t] = c
    flow = 0
    while True:
        parent = [-1] * N
        parent[s] = s
        q = deque([s])
        while q and parent[t] == -1:
            u = q.popleft()
            for v, c in enumerate(cap[u]):
                if c > 0 and parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        if parent[t] == -1:
            break
        aug = 10**9
        v = t
        while v != s:
            u = parent[v]
            aug = min(aug, cap[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] -= aug
            cap[v][u] += aug
            v = u
        flow += aug
    return flow


def max_deficit(demands, caps, neigh):
    P = len(demands)
    best = 0
    for r in range(1, P + 1):
        for X in combinations(range(P), r):
            N = set().union(*(neigh[i] for i in X))
            deficit = sum(demands[i] for i in X) - sum(caps[j] for j in N)
            best = max(best, deficit)
    return best


systems = 7000
original_profiles = 0
signature_classes = 0
payable = 0
deficient = 0
demand_units = 0

for _ in range(systems):
    P = RNG.randint(1, 7)
    O = RNG.randint(1, 5)
    demands = [RNG.randint(1, 6) for _ in range(P)]
    caps = [RNG.randint(0, 10) for _ in range(O)]
    neigh = []
    for _ in range(P):
        S = {j for j in range(O) if RNG.random() < 0.5}
        neigh.append(S)

    groups = defaultdict(int)
    for d, S in zip(demands, neigh):
        groups[tuple(sorted(S))] += d
    q_demands = list(groups.values())
    q_neigh = [set(sig) for sig in groups]

    f1 = maxflow(demands, caps, neigh)
    f2 = maxflow(q_demands, caps, q_neigh)
    assert f1 == f2
    total = sum(demands)
    d1 = max_deficit(demands, caps, neigh)
    d2 = max_deficit(q_demands, caps, q_neigh)
    assert total - f1 == d1 == d2

    original_profiles += P
    signature_classes += len(groups)
    demand_units += total
    if f1 == total:
        payable += 1
    else:
        deficient += 1

print(f"systems={systems}")
print(f"original_profiles={original_profiles}")
print(f"signature_classes={signature_classes}")
print(f"payable={payable}")
print(f"deficient={deficient}")
print(f"demand_units={demand_units}")
