#!/usr/bin/env python3
from fractions import Fraction as F
from functools import lru_cache
from math import comb

risks = [F(1, 50), F(1, 40), F(1, 30), F(1, 24), F(1, 18), F(1, 12), F(1, 8)]
p0, p1 = F(1, 3), F(2, 3)
K = len(risks)


@lru_cache(None)
def lower(mask):
    return sum(risks[i] for i in range(K) if mask & (1 << i))


stats = {"candidate_splits": 0, "evaluated_splits": 0, "pruned_splits": 0}
choice = {}


@lru_cache(None)
def dp(mask):
    if mask & (mask - 1) == 0:
        return lower(mask)
    first = mask & -mask
    candidates = []
    sub = (mask - 1) & mask
    while sub:
        if sub & first:
            other = mask ^ sub
            if other:
                lb1 = max(lower(sub) / p0, lower(other) / p1)
                lb2 = max(lower(sub) / p1, lower(other) / p0)
                candidates.append((min(lb1, lb2), sub, other))
        sub = (sub - 1) & mask
    candidates.sort(key=lambda z: (z[0], z[1]))
    best = None
    best_split = None
    for split_lb, a, b in candidates:
        stats["candidate_splits"] += 1
        if best is not None and split_lb >= best:
            stats["pruned_splits"] += 1
            continue
        va, vb = dp(a), dp(b)
        oriented = [
            (max(va / p0, vb / p1), 0),
            (max(va / p1, vb / p0), 1),
        ]
        val, orientation = min(oriented)
        stats["evaluated_splits"] += 1
        if best is None or val < best:
            best = val
            best_split = (a, b, orientation)
    choice[mask] = best_split
    return best


full = (1 << K) - 1
optimum = dp(full)
assert optimum == F(27, 64)
assert stats == {"candidate_splits": 379, "evaluated_splits": 143, "pruned_splits": 236}
full_partition_count = sum(comb(K, s) * (2 ** (s - 1) - 1) for s in range(2, K + 1))
assert full_partition_count == 966
assert dp.cache_info().currsize == 76


@lru_cache(None)
def full_dp(mask):
    if mask & (mask - 1) == 0:
        return lower(mask)
    first = mask & -mask
    best = None
    sub = (mask - 1) & mask
    while sub:
        if sub & first:
            other = mask ^ sub
            if other:
                va, vb = full_dp(sub), full_dp(other)
                val = min(max(va / p0, vb / p1), max(va / p1, vb / p0))
                best = val if best is None or val < best else best
        sub = (sub - 1) & mask
    return best


assert full_dp(full) == optimum

print({
    "banks": K,
    "symbol_survivals": [str(p0), str(p1)],
    "exact_optimum": str(optimum),
    "subset_states_visited": dp.cache_info().currsize,
    "all_subset_states": 2 ** K - 1,
    "candidate_splits_seen": stats["candidate_splits"],
    "evaluated_splits": stats["evaluated_splits"],
    "pruned_splits": stats["pruned_splits"],
    "full_partition_count": full_partition_count,
})
