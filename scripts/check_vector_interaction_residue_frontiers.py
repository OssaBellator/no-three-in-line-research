#!/usr/bin/env python3
from fractions import Fraction

# Critical two-edge block BC has total (work,out1,out2)=(5,1,1).
# Odd residues are corrected by loop A=(3,2,0) or D=(3,0,2).
BC = (5, 1, 1)
A = (3, 2, 0)
D = (3, 0, 2)

def add(x, y):
    return tuple(x[i] + y[i] for i in range(3))

def scale(k, x):
    return tuple(k * z for z in x)

def min_work_frontier(n):
    q, r = divmod(n, 2)
    if r == 0:
        return {scale(q, BC)}
    base = scale(q, BC)
    return {add(base, A), add(base, D)}

for n in range(1, 129):
    frontier = min_work_frontier(n)
    q, r = divmod(n, 2)
    min_work = 5 * q + 3 * r
    assert all(v[0] == min_work for v in frontier)
    # Exhaust all choices of BC blocks and loops at state zero.
    candidates = []
    for k in range(n // 2 + 1):
        loops = n - 2 * k
        for a in range(loops + 1):
            d = loops - a
            candidates.append((5 * k + 3 * loops, k + 2 * a, k + 2 * d))
    mw = min(v[0] for v in candidates)
    raw = {v for v in candidates if v[0] == mw}
    pareto = {v for v in raw if not any(
        u != v and u[1] <= v[1] and u[2] <= v[2] for u in raw
    )}
    assert pareto == frontier
    if r == 0:
        assert len(frontier) == 1
    else:
        assert len(frontier) == 2
        normalized = {(Fraction(v[1], n), Fraction(v[2], n)) for v in frontier}
        target = (Fraction(1, 2), Fraction(1, 2))
        assert all(max(abs(x-target[0]), abs(y-target[1])) <= Fraction(3, 2*n) for x,y in normalized)

print({
    "lengths_checked": 128,
    "critical_period": 2,
    "even_frontier_size": 1,
    "odd_frontier_size": 2,
    "odd_correctors": ("A", "D"),
    "minimum_work_formula": "5 floor(N/2) + 3 (N mod 2)",
})
