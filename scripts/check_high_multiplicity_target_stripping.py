#!/usr/bin/env python3
"""Exact checks for docs/425 high-multiplicity target stripping."""

from fractions import Fraction
from itertools import combinations
import json


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


sources = tuple(f"x{i}" for i in range(4))
adj = {
    x: {"hub", f"{x}_a", f"{x}_b"}
    for x in sources
}
targets = sorted(set().union(*adj.values()))
multiplicity = {
    y: sum(y in adj[x] for x in sources)
    for y in targets
}

lambda_star = Fraction(0)
worst_subset = None
for r in range(1, len(sources) + 1):
    for A in combinations(sources, r):
        N = set().union(*(adj[x] for x in A))
        ratio = Fraction(len(A), len(N))
        if ratio > lambda_star:
            lambda_star = ratio
            worst_subset = A
assert lambda_star == Fraction(4, 9)

threshold_rows = []
envelope = None
for h in range(1, max(multiplicity.values()) + 1):
    high = {y for y, m in multiplicity.items() if m > h}
    residual_degrees = {
        x: len(adj[x] - high)
        for x in sources
    }
    d_h = min(residual_degrees.values())
    if d_h > 0:
        bound = Fraction(h, d_h)
        assert lambda_star <= bound
        envelope = bound if envelope is None else min(envelope, bound)
    else:
        bound = None
    edge_count = sum(len(adj[x]) for x in sources)
    assert len(high) * (h + 1) <= edge_count
    threshold_rows.append({
        "h": h,
        "high_targets": sorted(high),
        "d_h": d_h,
        "bound": None if bound is None else frac(bound),
    })

assert envelope == Fraction(1, 2)

rho = Fraction(2, 5)
assert lambda_star > rho
for row in threshold_rows:
    h = row["h"]
    d_h = row["d_h"]
    if d_h == 0:
        continue
    assert Fraction(d_h) < Fraction(h, 1) / rho
    high = set(row["high_targets"])
    x = min(sources, key=lambda z: len(adj[z] - high))
    high_neighbours = len(adj[x] & high)
    assert Fraction(high_neighbours) > len(adj[x]) - Fraction(h, 1) / rho

print(json.dumps({
    "all_checks_passed": True,
    "exact_lambda_star": frac(lambda_star),
    "worst_subset": list(worst_subset),
    "optimized_threshold_envelope": frac(envelope),
    "tail_test_rho": frac(rho),
    "thresholds": threshold_rows,
}, indent=2))
