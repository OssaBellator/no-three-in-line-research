#!/usr/bin/env python3
from fractions import Fraction as F


def rowmul(v, A):
    return [sum(v[k] * A[k][j] for k in range(len(v))) for j in range(len(A[0]))]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

J = [
    [F(0), F(1, 4), F(1, 10), F(0)],
    [F(0), F(0), F(1, 5), F(1, 10)],
    [F(0), F(0), F(0), F(1, 4)],
    [F(0), F(0), F(0), F(0)],
]
a = [F(1, 2), F(1, 3), F(1, 4), F(1, 5)]
b = [F(1, 5), F(1, 4), F(1, 3), F(1, 2)]
w = [F(1)] * 4
q = max(sum(row) for row in J)
beta = max(b)
assert q == F(7, 20)

orders = []
v = a[:]
for r in range(1, 6):
    orders.append(dot(v, b))
    v = rowmul(v, J)
assert orders[4] == 0
exact = sum(orders)

bounds = {}
for m in (1, 2, 3):
    v = a[:]
    for _ in range(m):
        v = rowmul(v, J)
    bound = beta * dot(v, w) / (F(1) - q)
    actual = sum(orders[m:])
    assert actual <= bound
    bounds[m] = (actual, bound)

print({
    "order_terms": [str(x) for x in orders[:4]],
    "exact_interaction_sum": str(exact),
    "potential_rate": str(q),
    "truncation_bounds": {str(m): {"actual_tail": str(a), "bound": str(bd)} for m, (a, bd) in bounds.items()},
})
