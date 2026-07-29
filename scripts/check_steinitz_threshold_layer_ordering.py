#!/usr/bin/env python3
from fractions import Fraction
from itertools import permutations

LAYERS = (
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
    (3, 0, 1, 2),
)
OBS = (
    (Fraction(3), Fraction(0)),
    (Fraction(0), Fraction(3)),
    (Fraction(2), Fraction(1)),
    (Fraction(1), Fraction(2)),
)
MEAN = (Fraction(3, 2), Fraction(3, 2))
CENTERED = tuple((x - MEAN[0], y - MEAN[1]) for x, y in OBS)

pairs = {(s, layer[s]) for layer in LAYERS for s in range(4)}
assert len(pairs) == 16
assert all(sorted(layer) == [0, 1, 2, 3] for layer in LAYERS)


def order_discrepancy(order):
    sx = sy = Fraction(0)
    best = Fraction(0)
    for i in order:
        sx += CENTERED[i][0]
        sy += CENTERED[i][1]
        best = max(best, abs(sx), abs(sy))
    return best

all_orders = list(permutations(range(4)))
values = {order: order_discrepancy(order) for order in all_orders}
best = min(values.values())
optimal = sorted(order for order, value in values.items() if value == best)
assert best == 1
assert optimal == [(2, 1, 0, 3), (3, 0, 1, 2)]

size = 1 << 4
dp = [None] * size
count = [0] * size
dp[0] = Fraction(0)
count[0] = 1
for mask in range(1, size):
    sx = sum(CENTERED[i][0] for i in range(4) if mask & (1 << i))
    sy = sum(CENTERED[i][1] for i in range(4) if mask & (1 << i))
    endpoint = max(abs(sx), abs(sy))
    candidates = []
    for i in range(4):
        if mask & (1 << i):
            prev = mask ^ (1 << i)
            candidates.append((max(dp[prev], endpoint), i, prev))
    dp[mask] = min(c[0] for c in candidates)
    count[mask] = sum(count[prev] for value, _, prev in candidates if value == dp[mask])

assert dp[-1] == best
assert count[-1] == 2
R = max(max(abs(x), abs(y)) for x, y in CENTERED)
assert R == Fraction(3, 2)
assert best <= 2 * R

print({
    "permutation_layers": len(LAYERS),
    "ordered_decompositions_checked": len(all_orders),
    "optimal_prefix_discrepancy": str(best),
    "optimal_orders": optimal,
    "steinitz_bound": str(2 * R),
    "status": "passed",
})
