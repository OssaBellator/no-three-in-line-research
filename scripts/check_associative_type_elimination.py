#!/usr/bin/env python3
"""Exact checks for docs/428 associative SCC type elimination."""

from fractions import Fraction
import json


def f(n, d=1):
    return Fraction(n, d)


def frac(x):
    return f"{x.numerator}/{x.denominator}"


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_mul(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def inverse(A):
    n = len(A)
    aug = [row[:] + eye(n)[i] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor:
                aug[r] = [
                    aug[r][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return [row[n:] for row in aug]


def submatrix(M, rows, cols):
    return [[M[i][j] for j in cols] for i in rows]


def eliminate(M, labels, eliminated):
    E = [i for i, label in enumerate(labels) if label in eliminated]
    R = [i for i, label in enumerate(labels) if label not in eliminated]
    A = submatrix(M, E, E)
    B = submatrix(M, E, R)
    C = submatrix(M, R, E)
    D = submatrix(M, R, R)
    resolvent = inverse(mat_sub(eye(len(E)), A))
    S = mat_add(D, mat_mul(mat_mul(C, resolvent), B))
    return S, [labels[i] for i in R]


labels = ["e0", "e1", "e2", "c0", "c1"]
M = [
    [f(1,10), f(1,5),  f(1,10), f(1,20), 0],
    [f(1,6),  f(1,8),  f(1,12), 0,       f(1,25)],
    [0,       0,        f(1,5),  f(1,10), f(1,20)],
    [f(1,30), 0,        f(1,15), f(1,4),  f(1,20)],
    [0,       f(1,40),  f(1,18), f(1,25), f(1,5)],
]

direct, direct_labels = eliminate(M, labels, {"e0", "e1", "e2"})
assert direct_labels == ["c0", "c1"]

step1, labels1 = eliminate(M, labels, {"e2"})
step2, labels2 = eliminate(step1, labels1, {"e0", "e1"})
assert labels2 == direct_labels
assert step2 == direct

alt1, alt_labels1 = eliminate(M, labels, {"e0", "e1"})
alt2, alt_labels2 = eliminate(alt1, alt_labels1, {"e2"})
assert alt_labels2 == direct_labels
assert alt2 == direct

Mhat = [[entry + f(1,100) for entry in row] for row in M]
direct_hat, _ = eliminate(Mhat, labels, {"e0", "e1", "e2"})
for i in range(2):
    for j in range(2):
        assert direct[i][j] <= direct_hat[i][j]

transient = {"e0", "e1", "e2"}
edges = {
    labels[i]: {labels[j] for j in range(3) if M[i][j] > 0}
    for i in range(3)
}
reach = {u: {u} | edges[u] for u in transient}
changed = True
while changed:
    changed = False
    for u in transient:
        expanded = set().union(*(reach[v] for v in list(reach[u])))
        if not expanded <= reach[u]:
            reach[u] |= expanded
            changed = True
sccs = []
unused = set(transient)
while unused:
    u = next(iter(unused))
    comp = {v for v in transient if v in reach[u] and u in reach[v]}
    sccs.append(sorted(comp))
    unused -= comp
assert sorted(map(tuple, sccs)) == sorted([("e0", "e1"), ("e2",)])

print(json.dumps({
    "all_checks_passed": True,
    "transient_sccs": sccs,
    "effective_core": [[frac(x) for x in row] for row in direct],
    "inflated_effective_core": [[frac(x) for x in row] for row in direct_hat],
    "direct_equals_sink_first": True,
    "direct_equals_scc_first": True,
    "monotone_envelope_verified": True,
}, indent=2))
