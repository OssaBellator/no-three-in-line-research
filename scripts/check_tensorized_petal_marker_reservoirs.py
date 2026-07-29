#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
import json

sources = range(4)
R1 = {x: (f"p{x}a", f"p{x}b") for x in sources}
R2 = {
    0: ("u0", "u1"), 1: ("u0", "u2"),
    2: ("u1", "u3"), 3: ("u2", "u3"),
}
R3 = {
    0: ("v0", "v1"), 1: ("v0", "v1"),
    2: ("v0", "v2"), 3: ("v1", "v2"),
}

def graph(conditioned=False):
    out = {}
    for x in sources:
        vals = list(product(R1[x], R2[x], R3[x]))
        if conditioned:
            vals = [t for i, t in enumerate(vals) if i % 2 == 0]
        out[x] = set(vals)
    return out

def exact_lambda(out):
    best = Fraction(0)
    witness = None
    ss = list(out)
    for r in range(1, len(ss)+1):
        for A in combinations(ss, r):
            N = set().union(*(out[x] for x in A))
            ratio = Fraction(len(A), len(N))
            if ratio > best:
                best, witness = ratio, A
    return best, witness

def max_reuse(out):
    counts = {}
    for x, ys in out.items():
        for y in ys:
            counts[y] = counts.get(y, 0) + 1
    return max(counts.values())

full = graph(False)
cond = graph(True)
lam_full, wit_full = exact_lambda(full)
lam_cond, wit_cond = exact_lambda(cond)
assert all(len(full[x]) == 8 for x in sources)
assert all(len(cond[x]) == 4 for x in sources)
assert max_reuse(full) == 1
assert max_reuse(cond) == 1
assert lam_full == Fraction(1, 8)
assert lam_cond == Fraction(1, 4)

print(json.dumps({
    "all_checks_passed": True,
    "sources": 4,
    "channels": 3,
    "full_degree": 8,
    "full_exact_lambda": str(lam_full),
    "full_witness": wit_full,
    "conditioned_degree": 4,
    "conditioned_exact_lambda": str(lam_cond),
    "conditioned_witness": wit_cond,
}, indent=2))
