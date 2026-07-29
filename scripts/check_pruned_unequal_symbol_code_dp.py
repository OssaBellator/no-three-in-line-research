#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction as F
from itertools import permutations

p = (F(3, 5), F(4, 5))
rho = (F(1, 20), F(1, 18), F(1, 15), F(1, 12), F(1, 10), F(1, 8))
K = len(rho)
pruned = 0
partitions = 0


def sq_lb(mask):
    return sum(rho[i] * rho[i] for i in range(K) if mask >> i & 1)


@lru_cache(None)
def V(mask):
    global pruned, partitions
    if mask & (mask - 1) == 0:
        i = (mask & -mask).bit_length() - 1
        return rho[i]
    first = mask & -mask
    best = None
    sub = (mask - 1) & mask
    while sub:
        other = mask ^ sub
        if other and (sub & first):
            partitions += 1
            for a, b in ((sub, other), (other, sub)):
                if best is not None:
                    lower_sq = max(sq_lb(a) / (p[0] * p[0]), sq_lb(b) / (p[1] * p[1]))
                    if lower_sq >= best * best:
                        pruned += 1
                        continue
                cand = max(V(a) / p[0], V(b) / p[1])
                if best is None or cand < best:
                    best = cand
        sub = (sub - 1) & mask
    return best

opt = V((1 << K) - 1)
assert opt * opt >= sum(x * x for x in rho)

@lru_cache(None)
def shapes(n):
    if n == 1:
        return (None,)
    out = []
    for a in range(1, n):
        for L in shapes(a):
            for R in shapes(n - a):
                out.append((L, R))
    return tuple(out)


def leaf_probs(tree, acc=F(1)):
    if tree is None:
        return [acc]
    L, R = tree
    return leaf_probs(L, acc * p[0]) + leaf_probs(R, acc * p[1])

brute = None
assignments = 0
for tree in shapes(K):
    probs = leaf_probs(tree)
    for perm in permutations(range(K)):
        assignments += 1
        cand = max(rho[perm[j]] / probs[j] for j in range(K))
        if brute is None or cand < brute:
            brute = cand
assert brute == opt

candidates = set()
for i in range(K):
    for depth in range(K):
        for a in range(depth + 1):
            b = depth - a
            candidates.add(rho[i] / (p[0] ** a * p[1] ** b))
assert opt in candidates

print({
    "optimal_risk": str(opt),
    "subset_states": V.cache_info().currsize,
    "partition_orientations_pruned": pruned,
    "ordered_trees": len(shapes(K)),
    "assignments_checked": assignments,
    "finite_candidates": len(candidates),
})
