#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction

G = [(a, b) for a in range(3) for b in range(3)]
# Integer block multiplicities. Total mass 7.
mu = {(0, 0): 3, (1, 0): 1, (2, 0): 1, (0, 1): 1, (0, 2): 1}

def convolve(f, g):
    out = defaultdict(int)
    for (a, b), x in f.items():
        for (c, d), y in g.items():
            out[((a + c) % 3, (b + d) % 3)] += x * y
    return dict(out)

counts = {(0, 0): 1}
horizon = None
records = []
for n in range(1, 13):
    counts = convolve(counts, mu)
    total = 7 ** n
    assert sum(counts.values()) == total
    zero_formula = (7 ** n + 4 * 4 ** n + 4) // 9
    assert counts[(0, 0)] == zero_formula
    max_dev = max(abs(Fraction(counts.get(g, 0), total) - Fraction(1, 9)) for g in G)
    spectral_bound = Fraction(8, 9) * Fraction(4, 7) ** n
    assert max_dev <= spectral_bound
    if horizon is None and max_dev <= Fraction(1, 100):
        horizon = n
    records.append((n, counts[(0, 0)], max_dev))

assert horizon == 7
assert records[5][2] > Fraction(1, 100)
assert records[6][2] <= Fraction(1, 100)
# Degree-18 reverse load envelope at the sharp horizon.
load = (Fraction(1, 9) + records[6][2]) / 18

print({
    "group_size": 9,
    "kernel_mass": 7,
    "fourier_magnitudes": (7, 4, 1),
    "powers_checked": 12,
    "one_percent_horizon": horizon,
    "degree_18_exact_load": str(load),
})
