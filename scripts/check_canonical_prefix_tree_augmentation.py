#!/usr/bin/env python3
from functools import lru_cache

LEAF = ("L",)


def key(t):
    return repr(t)


def canon(a, b):
    return tuple(sorted((a, b), key=key))


@lru_cache(None)
def trees(n):
    if n == 1:
        return {LEAF}
    out = set()
    for i in range(1, n):
        for a in trees(i):
            for b in trees(n - i):
                out.add(canon(a, b))
    return out


def height(t):
    if t == LEAF:
        return 0
    return 1 + max(height(t[0]), height(t[1]))


def leaves(t):
    if t == LEAF:
        return 1
    return leaves(t[0]) + leaves(t[1])


expected = (1, 1, 1, 2, 3, 6, 11, 23)
counts = []
for n in range(1, 9):
    ts = trees(n)
    assert all(leaves(t) == n for t in ts)
    counts.append(len(ts))
assert tuple(counts) == expected

n = 6
all6 = trees(n)
min_height = min(height(t) for t in all6)
optimal = sorted([t for t in all6 if height(t) == min_height], key=key)
assert min_height == 3
assert len(all6) == 6 and len(optimal) == 2

# For equal risks and equal binary survivals p=1/2, max realized risk is 2^height.
optimum = 2 ** min_height
assert all(2 ** height(t) >= optimum for t in all6)

print({
    "shape_counts_n_1_to_8": counts,
    "six_leaf_shapes": len(all6),
    "optimal_six_leaf_orbits": len(optimal),
    "minimum_height": min_height,
    "equal_risk_optimum": optimum,
    "canonical_representatives": [repr(t) for t in optimal],
})
