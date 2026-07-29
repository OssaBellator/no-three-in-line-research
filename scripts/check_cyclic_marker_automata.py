#!/usr/bin/env python3
from fractions import Fraction as F


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def rowmul(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v))) for j in range(len(A[0]))]


def inv(A):
    n = len(A)
    aug = [row[:] + eye(n)[i] for i, row in enumerate(A)]
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


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


Q = [
    [F(1, 4), F(1, 6), F(0)],
    [F(0), F(1, 5), F(1, 4)],
    [F(1, 10), F(0), F(1, 6)],
]
b = [F(1, 3), F(1, 4), F(1, 5)]
R = inv(matsub(eye(3), Q))
B = rowmul(b, R)
assert B == [x + y for x, y in zip(b, rowmul(B, Q))]

w = [F(1), F(1), F(1)]
Qw = [sum(row[j] * w[j] for j in range(3)) for row in Q]
q = max(Qw)
assert q == F(9, 20)
assert all(Qw[i] <= q * w[i] for i in range(3))

v = b[:]
weighted = []
for n in range(8):
    mass = sum(v[i] * w[i] for i in range(3))
    weighted.append(mass)
    assert mass <= (q ** n) * sum(b)
    v = rowmul(v, Q)

Q_bad = [[F(3, 5), F(3, 5)], [F(3, 5), F(3, 5)]]
z = [F(1), F(1)]
zQ = rowmul(z, Q_bad)
assert all(zQ[i] >= z[i] for i in range(2))
v = [F(1), F(0)]
bad_masses = []
for _ in range(6):
    bad_masses.append(sum(v))
    v = rowmul(v, Q_bad)
assert bad_masses[-1] > bad_masses[0]

print({
    "resolvent_load": [str(x) for x in B],
    "potential_rate": str(q),
    "checked_tail_depth": len(weighted) - 1,
    "bad_dual_witness": [str(x) for x in z],
    "bad_mass_depth_5": str(bad_masses[-1]),
})
