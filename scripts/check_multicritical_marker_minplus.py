#!/usr/bin/env python3
from fractions import Fraction

BLOCKS = (
    ("P", 2, 2, (2, 0)),
    ("Q", 4, 4, (0, 4)),
    ("R", 1, 2, (1, 0)),
)
MAX_N = 400

cost = [None] * (MAX_N + 1)
frontier = [set() for _ in range(MAX_N + 1)]
cost[0] = 0
frontier[0] = {(0, 0)}

for n in range(1, MAX_N + 1):
    candidates = []
    for _, length, block_cost, avec in BLOCKS:
        if n < length or cost[n - length] is None:
            continue
        for old in frontier[n - length]:
            candidates.append((cost[n - length] + block_cost,
                               old[0] + avec[0], old[1] + avec[1]))
    best = min(c[0] for c in candidates)
    cost[n] = best
    frontier[n] = {(x, y) for c, x, y in candidates if c == best}

for n in range(1, MAX_N + 1):
    expected_cost = n if n % 2 == 0 else n + 1
    assert cost[n] == expected_cost, (n, cost[n], expected_cost)
    k = n // 2
    expected = {(n - 4 * q, 4 * q) for q in range(k // 2 + 1)}
    assert frontier[n] == expected, (n, frontier[n], expected)
    assert all(x + y == n for x, y in frontier[n])

for n in range(2, MAX_N + 1, 2):
    ys = sorted(Fraction(y, n) for _, y in frontier[n])
    gaps = [ys[i + 1] - ys[i] for i in range(len(ys) - 1)]
    if gaps:
        assert max(gaps) <= Fraction(4, n)

print({
    "lengths_checked": MAX_N,
    "critical_mean": "1",
    "critical_cyclicity": 2,
    "cost_formula": "N for even N; N+1 for odd N",
    "critical_rate_polytope": "conv((1,0),(0,1))",
    "status": "passed",
})
