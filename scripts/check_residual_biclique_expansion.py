#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import json

C = {"c0", "c1"}
R = {
    "s0": {"a", "b", "c", "d"},
    "s1": {"a", "b", "e", "f"},
    "s2": {"c", "d", "e", "f"},
    "s3": {"g", "h", "i", "j"},
}
N = {x: C | ys for x, ys in R.items()}

def exact_lambda(graph):
    ss = list(graph)
    best = Fraction(0)
    witness = None
    for r in range(1, len(ss)+1):
        for A in combinations(ss, r):
            neigh = set().union(*(graph[x] for x in A))
            val = Fraction(len(A), len(neigh))
            if val > best:
                best, witness = val, A
    return best, witness

mult = {y: sum(y in ys for ys in R.values()) for y in set().union(*R.values())}
d_R = min(map(len, R.values()))
h_R = max(mult.values())
assert d_R == 4 and h_R == 2
lam, witness = exact_lambda(R)
assert lam <= Fraction(h_R, d_R)
second_hubs = [y for y, m in mult.items() if m >= 2]
assert second_hubs
d0 = min(map(len, N.values()))
assert d0 - len(C) == d_R

print(json.dumps({
    "all_checks_passed": True,
    "common_core_size": len(C),
    "minimum_original_degree": d0,
    "minimum_residual_degree": d_R,
    "maximum_residual_multiplicity": h_R,
    "uniform_bound": str(Fraction(h_R, d_R)),
    "exact_residual_lambda": str(lam),
    "exact_witness": witness,
    "second_hubs_for_h1": sorted(second_hubs),
}, indent=2))
