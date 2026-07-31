#!/usr/bin/env python3
from fractions import Fraction

# Adapter-derived base rows in boundary, Hall, threshold, prefix, shell,
# interaction order.
BASE = (
    Fraction(7, 120),
    Fraction(11723, 524288),
    Fraction(1, 24),
    Fraction(1, 40),
    Fraction(1, 40),
    Fraction(1, 48),
)

# Nonnegative cross-frontier coupling matrix C, with C[i][j] the loss returned
# to row i by one unit of realized loss in row j.
C = [[Fraction(0) for _ in range(6)] for _ in range(6)]
C[0][5] = Fraction(1, 200)
C[1][0] = Fraction(1, 100)
C[2][1] = Fraction(1, 120)
C[3][2] = Fraction(1, 160)
C[4][3] = Fraction(1, 120)
C[5][4] = Fraction(1, 200)

# A simple exact supersolution y >= b + Cy. It avoids storing the much less
# transparent exact inverse of I-C.
Y = tuple(Fraction(value, 1000) for value in (59, 23, 42, 26, 26, 22))

for i in range(6):
    returned = BASE[i] + sum(C[i][j] * Y[j] for j in range(6))
    assert returned <= Y[i]

assert sum(Y) == Fraction(99, 500)
slack = Fraction(1, 4) - sum(Y)
assert slack == Fraction(13, 250)

# The interaction base row is itself the exact optimum of the normal-fan fixture
# with weights alpha=1/48 < beta=1/32.
alpha = Fraction(1, 48)
beta = Fraction(1, 32)
for n in range(1, 301):
    frontier = [(n - 2 * k, 2 * k) for k in range(n // 2 + 1)]
    optimum = min(alpha * x + beta * y for x, y in frontier)
    assert optimum == alpha * n

# Balanced integerization contributes less than 6/N. The supersolution leaves
# 13/250 slack, so the coupled fixture is strictly feasible from N=116; the
# boundary signature row raises the common threshold to N=120.
assert Fraction(6, 116) < slack
assert Fraction(6, 115) >= slack
for n in range(120, 5001):
    assert sum(Y) + Fraction(6, n) < Fraction(1, 4)

print({
    "base_sum": str(sum(BASE)),
    "supersolution": [str(value) for value in Y],
    "coupled_sum": str(sum(Y)),
    "coupled_slack": str(slack),
    "rounding_threshold": 116,
    "common_adapter_threshold": 120,
    "lengths_checked": 5000 - 120 + 1,
    "status": "passed",
})
