#!/usr/bin/env python3
"""Finite audit for SRR2n--SRR2r."""

from itertools import permutations
import random


def min_cost(adj, costs):
    n = len(adj)
    best = None
    for p in permutations(range(n)):
        if all(p[u] in adj[u] for u in range(n)):
            val = sum(costs[p[u]] for u in range(n))
            best = val if best is None else min(best, val)
    return best


def deficiency(adj, low):
    n = len(adj)
    best = 0
    for mask in range(1 << n):
        X = [u for u in range(n) if mask >> u & 1]
        N = set()
        for u in X:
            N.update(v for v in adj[u] if v in low)
        best = max(best, len(X) - len(N))
    return best


def loss_bound(adj, conditioned, low):
    n = len(adj)
    best = 0
    for mask in range(1 << n):
        X = [u for u in range(n) if mask >> u & 1]
        old = set()
        new = set()
        for u in X:
            old.update(v for v in adj[u] if v in low)
            new.update(v for v in conditioned[u] if v in low)
        best = max(best, len(old) - len(new))
    return best


def audit(adj, conditioned, costs):
    cmax = max(costs)
    phi = min_cost(adj, costs)
    phi2 = min_cost(conditioned, costs)
    if phi is None or phi2 is None:
        return False
    ds = []
    ds2 = []
    bs = []
    for t in range(1, cmax + 1):
        low = {v for v, c in enumerate(costs) if c < t}
        ds.append(deficiency(adj, low))
        ds2.append(deficiency(conditioned, low))
        bs.append(loss_bound(adj, conditioned, low))
    assert phi == sum(ds)
    assert phi2 == sum(ds2)
    assert all(d2 <= d + b for d, d2, b in zip(ds, ds2, bs))
    assert phi2 <= phi + sum(bs)
    return True


def main():
    rng = random.Random(20260728)
    checked = 0
    for n in range(2, 7):
        for _ in range(2500):
            costs = [rng.randrange(4) for _ in range(n)]
            adj = []
            conditioned = []
            for _u in range(n):
                row = {v for v in range(n) if rng.random() < 0.78}
                row2 = {v for v in row if rng.random() < 0.83}
                adj.append(row)
                conditioned.append(row2)
            checked += audit(adj, conditioned, costs)
    assert checked > 1000
    print("SRR conditioned endpoint-cost audit passed")
    print(f"  feasible graph pairs checked: {checked}")


if __name__ == "__main__":
    main()
