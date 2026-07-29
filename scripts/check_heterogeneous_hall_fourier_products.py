#!/usr/bin/env python3
from fractions import Fraction

# Heterogeneous convolution kernels on Z/3Z.  The sequence alternates A,B.
A = (5, 1, 1)  # total 7, nontrivial Fourier eigenvalue 4
B = (3, 2, 2)  # total 7, nontrivial Fourier eigenvalue 1
TARGET = Fraction(1, 4000)
DEGREE = 18
MAX_POWER = 12


def convolve(x, y):
    out = [0, 0, 0]
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            out[(i + j) % 3] += xi * yj
    return tuple(out)

counts = (1, 0, 0)
horizon = None
records = []
for n in range(1, MAX_POWER + 1):
    counts = convolve(counts, A if n % 2 else B)
    total = 7**n
    lam = 4 ** ((n + 1) // 2)
    expected = ((total + 2 * lam) // 3, (total - lam) // 3, (total - lam) // 3)
    assert counts == expected
    deviation = Fraction(2 * lam, 3 * total)
    records.append((n, counts, deviation))
    if horizon is None and deviation <= TARGET:
        horizon = n

assert horizon == 7
assert records[5][2] > TARGET and records[6][2] <= TARGET
max_count = max(records[6][1])
load = Fraction(max_count, 7**7 * DEGREE)
assert load == Fraction(274685, 14823774)

print({
    "powers_checked": MAX_POWER,
    "sharp_horizon": horizon,
    "target_deviation": TARGET,
    "power_7_counts": records[6][1],
    "degree_18_load": load,
    "status": "passed",
})
