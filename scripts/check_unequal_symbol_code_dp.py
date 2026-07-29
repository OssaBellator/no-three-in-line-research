#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from itertools import permutations

RHO = [Fraction(1, 20), Fraction(1, 16), Fraction(1, 12), Fraction(1, 10), Fraction(1, 8), Fraction(1, 6)]
P0 = Fraction(4, 5)
P1 = Fraction(3, 5)
N = len(RHO)

@lru_cache(None)
def trees(n):
    if n == 1:
        return (None,)
    result = []
    for left_count in range(1, n):
        for left in trees(left_count):
            for right in trees(n - left_count):
                result.append((left, right))
    return tuple(result)

def leaf_survivals(tree, survival=Fraction(1)):
    if tree is None:
        return [survival]
    left, right = tree
    return leaf_survivals(left, survival * P0) + leaf_survivals(right, survival * P1)

@lru_cache(None)
def subset_dp(mask):
    if mask & (mask - 1) == 0:
        return RHO[mask.bit_length() - 1], None
    first = mask & -mask
    best = best_choice = None
    sub = (mask - 1) & mask
    while sub:
        if (sub & first) and sub != mask:
            other = mask ^ sub
            left_value, _ = subset_dp(sub)
            right_value, _ = subset_dp(other)
            value, orientation = min([
                (max(left_value / P0, right_value / P1), 0),
                (max(left_value / P1, right_value / P0), 1),
            ])
            if best is None or value < best:
                best, best_choice = value, (sub, other, orientation)
        sub = (sub - 1) & mask
    return best, best_choice

exact_dp, _ = subset_dp((1 << N) - 1)
assert exact_dp == Fraction(5, 18)

exhaustive = None
assignments = 0
for tree in trees(N):
    survivals = leaf_survivals(tree)
    for perm in permutations(range(N)):
        risk = max(RHO[perm[i]] / survivals[i] for i in range(N))
        exhaustive = risk if exhaustive is None else min(exhaustive, risk)
        assignments += 1
assert exhaustive == exact_dp

print({
    "ordered_full_trees": len(trees(N)),
    "tree_assignments_checked": assignments,
    "subset_states": (1 << N) - 1,
    "exact_optimum": str(exact_dp),
})
