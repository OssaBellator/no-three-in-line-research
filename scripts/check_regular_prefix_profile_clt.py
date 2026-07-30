#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, sqrt

MAX_N = 200


def profile(n):
    out = []
    for j in range((n - 1) // 2 + 1):
        a = n - 1 - 2 * j
        count = factorial(n - 1) // (factorial(a) * factorial(j) * factorial(j + 1))
        out.append((j, count))
    return out

for n in range(1, MAX_N + 1):
    prof = profile(n)
    total = sum(c for _, c in prof)
    mean = Fraction(sum(j * c for j, c in prof), total)
    second = Fraction(sum(j * j * c for j, c in prof), total)
    variance = second - mean * mean
    # Exact ratio test gives unimodality.
    seen_decrease = False
    last = None
    for _, c in prof:
        if last is not None and c < last:
            seen_decrease = True
        if seen_decrease and last is not None:
            assert c <= last
        last = c
    assert abs(float(mean) - n / 3) < 1
    if n >= 10:
        assert abs(float(variance) - n / 18) < 1

p30 = profile(30)
peak = max(c for _, c in p30)
assert [j for j, c in p30 if c == peak] == [9, 10]
assert peak == 168212023980

p200 = profile(200)
total200 = sum(c for _, c in p200)
mean200 = Fraction(sum(j * c for j, c in p200), total200)
var200 = Fraction(sum(j * j * c for j, c in p200), total200) - mean200 * mean200
assert abs(float(mean200 / 200) - 1 / 3) < 0.003
assert abs(float(var200 / 200) - 1 / 18) < 0.001

# Central-window mass is consistent with the Gaussian scale sqrt(n/18).
sigma = sqrt(float(var200))
central = sum(c for j, c in p200 if abs(j - float(mean200)) <= 2 * sigma)
central_mass = central / total200
assert 0.94 < central_mass < 0.97

print({
    "leaves_checked": MAX_N,
    "peak_at_30": [9, 10],
    "mean_over_n_at_200": float(mean200 / 200),
    "variance_over_n_at_200": float(var200 / 200),
    "two_sigma_mass_at_200": central_mass,
    "asymptotic": "J_n = n/3 + O(1), Var(J_n)=n/18+O(1)",
    "status": "passed",
})
