#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product


def inv(A):
    n = len(A)
    aug = [list(map(F, row)) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if aug[i][c])
        aug[c], aug[p] = aug[p], aug[c]
        z = aug[c][c]
        aug[c] = [x / z for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c]:
                z = aug[i][c]
                aug[i] = [aug[i][j] - z * aug[c][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

C = [
    [F(1), F(1), F(0), F(0), F(0)],
    [F(0), F(0), F(1), F(1), F(0)],
    [F(1), F(0), F(1), F(0), F(1)],
]
c = [F(1), F(3), F(2), F(4), F(0)]
Bidx = [0, 2, 4]
Nidx = [1, 3]
CB = [[row[j] for j in Bidx] for row in C]
CBi = inv(CB)
cB = [c[j] for j in Bidx]
y = [sum(cB[k] * CBi[k][i] for k in range(3)) for i in range(3)]
assert y == [F(1), F(2), F(0)]
reduced = {}
for j in Nidx:
    reduced[j] = c[j] - sum(y[i] * C[i][j] for i in range(3))
assert reduced == {1: F(2), 3: F(2)}

checked = 0
inside = 0
facets = 0
for r1, r2, r3 in product(range(1, 5), range(1, 5), range(1, 11)):
    r = [F(r1), F(r2), F(r3)]
    xB = matvec(CBi, r)
    cone = r3 >= r1 + r2
    assert all(v >= 0 for v in xB) == cone
    if cone:
        inside += 1
        value = sum(cB[i] * xB[i] for i in range(3))
        assert value == sum(y[i] * r[i] for i in range(3)) == F(r1 + 2 * r2)
        if r3 == r1 + r2:
            facets += 1
            assert xB[2] == 0
    checked += 1

print({
    "rhs_points_checked": checked,
    "basis_region_points": inside,
    "facet_points": facets,
    "dual_prices": [str(v) for v in y],
    "inactive_reduced_costs": {str(k): str(v) for k, v in reduced.items()},
})
