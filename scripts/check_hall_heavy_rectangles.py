#!/usr/bin/env python3
"""Exact checks for docs/424 two-sided heavy Hall rectangles."""

from fractions import Fraction
import json
from math import ceil


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


sources = ("x0", "x1", "x2", "x3")
targets = tuple(f"y{i}" for i in range(7))
adj = {
    "x0": ("y0", "y1", "y3", "y4"),
    "x1": ("y0", "y2", "y3", "y5"),
    "x2": ("y1", "y2", "y4", "y5"),
    "x3": ("y0", "y1", "y2", "y6"),
}
v = {y: Fraction(1) for y in targets}
mu = {x: Fraction(1, 4) for x in sources}
H = {"y0", "y1", "y2"}

nu = {y: Fraction(0) for y in targets}
g = {}
beta = Fraction(0)
for x in sources:
    D = sum(v[y] for y in adj[x])
    g[x] = sum(v[y] for y in adj[x] if y in H) / D
    for y in adj[x]:
        atom = v[y] / D
        beta = max(beta, atom)
        nu[y] += mu[x] * atom

eta = sum(nu[y] for y in H)
identity_rhs = sum(mu[x] * g[x] for x in sources)
assert eta == identity_rhs == Fraction(9, 16)

alpha = Fraction(1, 2)
X = {x for x in sources if g[x] >= alpha}
mass_X = sum(mu[x] for x in X)
mass_bound = (eta - alpha) / (1 - alpha)
assert mass_X >= mass_bound

gamma = max(mu.values())
delta = max(nu.values())
source_count_bound = ceil(mass_bound / gamma)
target_count_bound = ceil(eta / delta)
row_degree_bound = ceil(alpha / beta)

assert len(X) >= source_count_bound
assert len(H) >= target_count_bound
for x in X:
    assert len(set(adj[x]) & H) >= row_degree_bound

print(json.dumps({
    "all_checks_passed": True,
    "target_mass_eta": frac(eta),
    "heavy_source_threshold_alpha": frac(alpha),
    "heavy_source_mass": frac(mass_X),
    "heavy_source_mass_bound": frac(mass_bound),
    "heavy_source_count": len(X),
    "heavy_source_count_bound": source_count_bound,
    "high_target_count": len(H),
    "high_target_count_bound": target_count_bound,
    "row_atom_beta": frac(beta),
    "row_degree_bound": row_degree_bound,
    "target_marginal": {y: frac(nu[y]) for y in targets},
}, indent=2))
