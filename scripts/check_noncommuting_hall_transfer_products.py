#!/usr/bin/env python3
from fractions import Fraction

A = ((2, 1, 0), (0, 2, 1), (1, 0, 2))
B = ((2, 1, 0), (1, 0, 2), (0, 2, 1))
I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
ZERO = ((0, 0, 0), (0, 0, 0), (0, 0, 0))


def mm(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def madd(X, Y):
    return tuple(tuple(X[i][j] + Y[i][j] for j in range(3)) for i in range(3))


def mscale(c, X):
    return tuple(tuple(c * X[i][j] for j in range(3)) for i in range(3))


def rowmul(v, X):
    return tuple(sum(v[k] * X[k][j] for k in range(3)) for j in range(3))


def mpow(X, n):
    out = I
    base = X
    while n:
        if n & 1:
            out = mm(out, base)
        base = mm(base, base)
        n //= 2
    return out

K = mm(A, B)
assert K == ((5, 2, 2), (2, 2, 5), (2, 5, 2))
assert mm(A, B) != mm(B, A)

Kminus9 = madd(K, mscale(-9, I))
Kminus3 = madd(K, mscale(-3, I))
Kplus3 = madd(K, mscale(3, I))
assert mm(mm(Kminus9, Kminus3), Kplus3) == ZERO

horizon = None
for m in range(1, 13):
    counts = rowmul((1, 0, 0), mpow(K, m))
    expected = ((9 ** m + 2 * 3 ** m) // 3,
                (9 ** m - 3 ** m) // 3,
                (9 ** m - 3 ** m) // 3)
    assert counts == expected, (m, counts, expected)
    assert sum(counts) == 9 ** m
    deviation = max(abs(Fraction(c, 9 ** m) - Fraction(1, 3)) for c in counts)
    assert deviation == Fraction(2, 3 ** (m + 1))
    if horizon is None and deviation <= Fraction(1, 100):
        horizon = m

assert horizon == 4
counts4 = rowmul((1, 0, 0), mpow(K, 4))
load = Fraction(max(counts4), sum(counts4) * 12)
assert load == Fraction(83, 2916)

transfers = (A, B) * 4
states = [0]
for T in transfers:
    current = states[-1]
    nxt = next(j for j in range(3) if T[current][j] > 0)
    states.append(nxt)
assert len(states) == 9

print({
    "noncommuting": True,
    "period_product": K,
    "period_eigenvalues": (9, 3, -3),
    "sharp_one_percent_horizon_pairs": horizon,
    "sharp_one_percent_horizon_blocks": 2 * horizon,
    "degree_12_load": str(load),
    "witness_state_path": states,
    "status": "passed",
})
