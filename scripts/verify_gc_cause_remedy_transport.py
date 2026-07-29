#!/usr/bin/env python3
from collections import deque
from itertools import combinations
import random

RNG = random.Random(20260728)


def maxflow(demands, caps, neigh):
    C, R = len(demands), len(caps)
    N = 2 + C + R
    s, t = N - 2, N - 1
    cap = [[0] * N for _ in range(N)]
    for i, d in enumerate(demands):
        cap[s][i] = d
    inf = sum(demands) + 1
    for i in range(C):
        for j in neigh[i]:
            cap[i][C + j] = inf
    for j, c in enumerate(caps):
        cap[C + j][t] = c
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
    C = len(demands)
    best = 0
    best_X = ()
    for r in range(1, C + 1):
        for X in combinations(range(C), r):
            N = set().union(*(neigh[i] for i in X))
            deficit = sum(demands[i] for i in X) - sum(caps[j] for j in N)
            if deficit > best:
                best, best_X = deficit, X
    return best, best_X


systems = 8500
payable = 0
deficient = 0
cause_units = 0
remedy_capacity = 0
canonical_cuts = 0

for _ in range(systems):
    C = RNG.randint(1, 7)
    R = RNG.randint(1, 6)
    demands = [RNG.randint(1, 7) for _ in range(C)]
    caps = [RNG.randint(0, 12) for _ in range(R)]
    neigh = [{j for j in range(R) if RNG.random() < 0.5} for _ in range(C)]
    total = sum(demands)
    flow = maxflow(demands, caps, neigh)
    deficit, X = max_deficit(demands, caps, neigh)
    assert total - flow == deficit
    cause_units += total
    remedy_capacity += sum(caps)
    if deficit == 0:
        payable += 1
    else:
        deficient += 1
        canonical_cuts += 1
        N = set().union(*(neigh[i] for i in X))
        assert sum(demands[i] for i in X) > sum(caps[j] for j in N)

print(f"systems={systems}")
print(f"payable={payable}")
print(f"deficient={deficient}")
print(f"cause_units={cause_units}")
print(f"remedy_capacity={remedy_capacity}")
print(f"canonical_cuts={canonical_cuts}")
