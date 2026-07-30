#!/usr/bin/env python3
from fractions import Fraction

MAX_N = 300
WEIGHTS = [(a, b) for a in range(0, 11) for b in range(0, 11) if (a, b) != (0, 0)]


def frontier(n):
    return [(n - 2 * b, 2 * b) for b in range(n // 2 + 1)]

for n in range(1, MAX_N + 1):
    pts = frontier(n)
    assert len(pts) == n // 2 + 1
    for alpha, beta in WEIGHTS:
        values = [alpha * x + beta * y for x, y in pts]
        optimum = min(values)
        argmin = [pts[i] for i, v in enumerate(values) if v == optimum]
        if alpha < beta:
            assert argmin == [(n, 0)]
            assert optimum == alpha * n
        elif alpha > beta:
            expected = (0, n) if n % 2 == 0 else (1, n - 1)
            assert argmin == [expected]
            expected_value = beta * n if n % 2 == 0 else beta * (n - 1) + alpha
            assert optimum == expected_value
        else:
            assert argmin == pts
            assert optimum == alpha * n

# Rational support-function formulas for one nonintegral weight pair.
alpha, beta = Fraction(5, 3), Fraction(2, 3)
for n in range(1, MAX_N + 1):
    optimum = min(alpha * x + beta * y for x, y in frontier(n))
    expected = beta * n if n % 2 == 0 else beta * (n - 1) + alpha
    assert optimum == expected

print({
    "lengths_checked": MAX_N,
    "integer_weights_checked": len(WEIGHTS),
    "normal_fan": ["alpha<beta", "alpha=beta", "alpha>beta"],
    "frontier_count": "floor(N/2)+1",
    "generating_function": "1/((1-u*z)*(1-v^2*z^2))",
    "status": "passed",
})
