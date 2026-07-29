#!/usr/bin/env python3
import math
from math import factorial

MAX_N = 100
coeff = [0] * (MAX_N + 1)
coeff[1] = 1
for n in range(2, MAX_N + 1):
    coeff[n] = coeff[n - 1] + sum(coeff[i] * coeff[n - 1 - i]
                                         for i in range(1, n - 1))

assert coeff[1:11] == [1, 1, 2, 4, 9, 21, 51, 127, 323, 835]


def lagrange(n):
    total = 0
    for j in range((n - 1) // 2 + 1):
        k = n - 1 - 2 * j
        rest = n - j - k
        if rest >= 0:
            total += factorial(n) // (factorial(j) * factorial(k) * factorial(rest))
    assert total % n == 0
    return total // n

for n in range(1, MAX_N + 1):
    assert coeff[n] == lagrange(n), n

for n in range(1, MAX_N + 1):
    convolution = sum(coeff[i] * coeff[n - 1 - i]
                      for i in range(1, n - 1)) if n >= 3 else 0
    lhs = convolution + (coeff[n - 1] if n - 1 >= 1 else 0) - coeff[n] + (1 if n == 1 else 0)
    assert lhs == 0, (n, lhs)

constant = math.sqrt(3) / (2 * math.sqrt(math.pi))
scaled_100 = coeff[100] * (100 ** 1.5) / (3 ** 100)
assert abs(scaled_100 - constant) < 0.01

print({
    "coefficients_checked": MAX_N,
    "first_ten": coeff[1:11],
    "algebraic_equation": "T=z+zT+zT^2",
    "dominant_radius": "1/3",
    "asymptotic_constant": constant,
    "scaled_n_100": scaled_100,
    "status": "passed",
})
