#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, log

MAX_N = 100


def profile(n, j):
    a = n - 1 - 2 * j
    if a < 0:
        return 0
    return factorial(n - 1) // (factorial(a) * factorial(j) * factorial(j + 1))


coeff = [0] * (MAX_N + 1)
coeff[1] = 1
for n in range(2, MAX_N + 1):
    unary = coeff[n - 1]
    binary = sum(coeff[i] * coeff[n - 1 - i] for i in range(1, n - 1))
    coeff[n] = unary + binary

for n in range(1, MAX_N + 1):
    total = sum(profile(n, j) for j in range((n - 1) // 2 + 1))
    assert total == coeff[n]

n = 30
values = [profile(n, j) for j in range((n - 1) // 2 + 1)]
peak = max(values)
peak_js = [j for j, value in enumerate(values) if value == peak]
assert peak_js == [9, 10]
assert peak == 168212023980
assert sum(values) == 593742784829


def entropy(beta):
    if beta <= 0 or beta >= Fraction(1, 2):
        return float('-inf')
    b = float(beta)
    return -2 * b * log(b) - (1 - 2 * b) * log(1 - 2 * b)


assert abs(entropy(Fraction(1, 3)) - log(3)) < 1e-12
for q in range(1, 100):
    beta = Fraction(q, 200)
    if beta != Fraction(1, 3):
        assert entropy(beta) < log(3) + 1e-12

print({
    "coefficients_checked": MAX_N,
    "bivariate_formula": "(n-1)!/(a! j! (j+1)!), a=n-1-2j",
    "n30_peak_quadratic_counts": peak_js,
    "n30_peak_coefficient": peak,
    "n30_total": sum(values),
    "entropy_maximizer": "beta=1/3",
    "growth_constant": 3,
    "status": "passed",
})
