#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

N = 5
R = [Fraction(2, 3), Fraction(3, 4), Fraction(4, 5), Fraction(5, 6), Fraction(6, 7)]
B = [Fraction(1, 5), Fraction(1, 6), Fraction(1, 7), Fraction(0), Fraction(0)]
C = [Fraction(0), Fraction(0), Fraction(1, 8), Fraction(1, 9), Fraction(1, 10)]
BASE = {
    (0, 1): Fraction(1, 4), (0, 2): Fraction(1, 5),
    (1, 2): Fraction(1, 6), (1, 3): Fraction(1, 7),
    (2, 3): Fraction(1, 8), (2, 4): Fraction(1, 9),
    (3, 4): Fraction(1, 10),
}
PERT = {(0, 1): Fraction(1, 20), (1, 2): Fraction(1, 30), (2, 4): Fraction(1, 40)}
ORDERED_PERT = list(PERT)

def transfers(edges):
    T = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        T[i][i] = R[i]
        for j in range(i + 1, N):
            T[i][j] = sum(T[i][k] * edges[(k, j)] * R[j] for k in range(i, j) if (k, j) in edges)
    return T

def correction(edges):
    T = transfers(edges)
    return sum(B[i] * T[i][j] * C[j] for i in range(N) for j in range(i, N))

def forward(edges):
    F = [Fraction(0) for _ in range(N)]
    for j in range(N):
        F[j] = B[j] * R[j] + sum(F[i] * edges[(i, j)] * R[j] for i in range(j) if (i, j) in edges)
    return F

def backward(edges):
    G = [Fraction(0) for _ in range(N)]
    for i in reversed(range(N)):
        G[i] = R[i] * (C[i] + sum(edges[(i, j)] * G[j] for j in range(i + 1, N) if (i, j) in edges))
    return G

base_K = correction(BASE)
F, G, T = forward(BASE), backward(BASE), transfers(BASE)
single = {edge: F[edge[0]] * h * G[edge[1]] for edge, h in PERT.items()}
pair = {}
for e1, e2 in combinations(ORDERED_PERT, 2):
    u, v = e1
    s, t = e2
    pair[(e1, e2)] = F[u] * PERT[e1] * T[v][s] * PERT[e2] * G[t] if v <= s else Fraction(0)

e1, e2, e3 = ORDERED_PERT
triple = F[e1[0]] * PERT[e1] * T[e1[1]][e2[0]] * PERT[e2] * T[e2[1]][e3[0]] * PERT[e3] * G[e3[1]]
upper_edges = dict(BASE)
for edge, h in PERT.items():
    upper_edges[edge] += h
exact_delta = correction(upper_edges) - base_K
assert exact_delta == sum(single.values()) + sum(pair.values()) + triple
remainder = exact_delta - sum(single.values())
assert remainder == sum(pair.values()) + triple and remainder > 0

F_plus, G_plus, T_plus = forward(upper_edges), backward(upper_edges), transfers(upper_edges)
pair_envelope = Fraction(0)
for e1, e2 in combinations(ORDERED_PERT, 2):
    u, v = e1
    s, t = e2
    if v <= s:
        pair_envelope += F_plus[u] * PERT[e1] * T_plus[v][s] * PERT[e2] * G_plus[t]
assert remainder <= pair_envelope

print({
    "baseline_correction": str(base_K),
    "perturbation_atoms": len(PERT),
    "single_terms": len(single),
    "pair_terms": len(pair),
    "triple_term": str(triple),
    "quadratic_remainder_bound_verified": True,
})
