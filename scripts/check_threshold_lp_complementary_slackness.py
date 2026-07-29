#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

Y = range(5)
OPTIONS = [
    [(3, 4), (0, 1, 2)],
    [(0, 1), (0, 1, 3)],
    [(2, 4), (0, 1, 2)],
]


def dist(support):
    p = Fraction(1, len(support))
    return [p if y in support else Fraction(0) for y in Y]

D = [[dist(S) for S in opts] for opts in OPTIONS]


def loads(alpha):
    out = [Fraction(0) for _ in Y]
    for x in range(3):
        for h in range(2):
            for y in Y:
                out[y] += alpha[x][h] * D[x][h][y]
    return out


def dual_value(z):
    mins = []
    for x in range(3):
        costs = [sum(z[y] * D[x][h][y] for y in Y) for h in range(2)]
        mins.append(min(costs))
    return sum(mins), mins


def gap_decomposition(alpha, z):
    L = loads(alpha)
    lam = max(L)
    phi, mins = dual_value(z)
    target_slack = sum(z[y] * (lam - L[y]) for y in Y)
    reduced = Fraction(0)
    for x in range(3):
        for h in range(2):
            cost = sum(z[y] * D[x][h][y] for y in Y)
            reduced += alpha[x][h] * (cost - mins[x])
    assert lam - phi == target_slack + reduced
    return lam, phi, target_slack, reduced, L

# Exact optimum mixture.
alpha_star = [
    [Fraction(8, 15), Fraction(7, 15)],
    [Fraction(0), Fraction(1)],
    [Fraction(2, 3), Fraction(1, 3)],
]
z_uniform = [Fraction(1, 5)] * 5
lam, phi, target_slack, reduced, L = gap_decomposition(alpha_star, z_uniform)
assert L == [Fraction(3, 5)] * 5
assert lam == phi == Fraction(3, 5)
assert target_slack == reduced == 0

# Exhaust deterministic assignments: optimum is 5/6.
deterministic_best = None
best_choice = None
for choice in product(range(2), repeat=3):
    alpha = [[Fraction(int(h == choice[x])) for h in range(2)] for x in range(3)]
    value = max(loads(alpha))
    if deterministic_best is None or value < deterministic_best:
        deterministic_best = value
        best_choice = choice
assert deterministic_best == Fraction(5, 6)

alpha_det = [[Fraction(int(h == best_choice[x])) for h in range(2)] for x in range(3)]
lam_d, phi_d, target_d, reduced_d, loads_d = gap_decomposition(alpha_det, z_uniform)
assert lam_d == Fraction(5, 6)
assert phi_d == Fraction(3, 5)
assert target_d == Fraction(7, 30)
assert reduced_d == 0

# A nonuniform price vector exposes a positive reduced-cost threshold class.
z_skew = [Fraction(2, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(0)]
lam_s, phi_s, target_s, reduced_s, _ = gap_decomposition(alpha_star, z_skew)
assert reduced_s > 0
assert target_s >= 0

print({
    "mixed_optimum": str(lam),
    "deterministic_optimum": str(deterministic_best),
    "deterministic_gap": str(lam_d - phi_d),
    "skew_target_slack": str(target_s),
    "skew_reduced_cost": str(reduced_s),
})
