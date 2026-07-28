#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import combinations
import random

RNG = random.Random(20260728)


def maxflow(demands, caps, neigh):
    P, S = len(demands), len(caps)
    N = 2 + P + S
    source, sink = N - 2, N - 1
    cap = [[0] * N for _ in range(N)]
    for i, d in enumerate(demands):
        cap[source][i] = d
    inf = sum(demands) + 1
    for i in range(P):
        for j in neigh[i]:
            cap[i][P + j] = inf
    for j, c in enumerate(caps):
        cap[P + j][sink] = c
    flow = 0
    while True:
        parent = [-1] * N
        parent[source] = source
        q = deque([source])
        while q and parent[sink] == -1:
            u = q.popleft()
            for v, c in enumerate(cap[u]):
                if c > 0 and parent[v] == -1:
                    parent[v] = u
                    q.append(v)
        if parent[sink] == -1:
            break
        aug = 10**9
        v = sink
        while v != source:
            u = parent[v]
            aug = min(aug, cap[u][v])
            v = u
        v = sink
        while v != source:
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
            best = max(best, sum(demands[i] for i in X) - sum(caps[j] for j in N))
    return best


systems = 7500
residual_states = 0
signature_classes = 0
payable = 0
deficient = 0
unit_sensitive_resets = 0

for _ in range(systems):
    P = RNG.randint(1, 7)
    S = RNG.randint(1, 5)
    U = RNG.randint(1, 4)
    demands = [RNG.randint(1, 6) for _ in range(P)]
    caps = [RNG.randint(0, 10) for _ in range(S)]
    units = [RNG.randrange(U) for _ in range(P)]
    neigh = [{j for j in range(S) if RNG.random() < 0.5} for _ in range(P)]

    groups = defaultdict(int)
    neighborhood_units = defaultdict(set)
    for d, u, N in zip(demands, units, neigh):
        sig = tuple(sorted(N))
        groups[(u, sig)] += d
        neighborhood_units[sig].add(u)
    q_demands = list(groups.values())
    q_neigh = [set(sig) for u, sig in groups]

    f1 = maxflow(demands, caps, neigh)
    f2 = maxflow(q_demands, caps, q_neigh)
    assert f1 == f2
    total = sum(demands)
    assert total - f1 == max_deficit(demands, caps, neigh)
    assert total - f2 == max_deficit(q_demands, caps, q_neigh)

    if any(len(classes) > 1 for classes in neighborhood_units.values()):
        unit_sensitive_resets += 1
    residual_states += P
    signature_classes += len(groups)
    if f1 == total:
        payable += 1
    else:
        deficient += 1

print(f"systems={systems}")
print(f"residual_states={residual_states}")
print(f"signature_classes={signature_classes}")
print(f"payable={payable}")
print(f"deficient={deficient}")
print(f"unit_sensitive_resets={unit_sensitive_resets}")
