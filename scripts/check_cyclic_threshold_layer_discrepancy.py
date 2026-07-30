#!/usr/bin/env python3
from itertools import permutations

NAMES = "ABCDEF"
VECTORS = (
    (2, 0),
    (-2, 0),
    (0, -2),
    (1, 2),
    (1, -1),
    (-2, 1),
)
assert tuple(sum(v[j] for v in VECTORS) for j in range(2)) == (0, 0)


def prefix_path(order):
    path = [(0, 0)]
    x = y = 0
    for i in order:
        x += VECTORS[i][0]
        y += VECTORS[i][1]
        path.append((x, y))
    assert path[-1] == (0, 0)
    return path


def cyclic_discrepancy(order):
    path = prefix_path(order)
    return max(max(p[j] for p in path) - min(p[j] for p in path) for j in range(2))

scores = [(cyclic_discrepancy(order), order) for order in permutations(range(6))]
optimum = min(score for score, _ in scores)
optimal_orders = [order for score, order in scores if score == optimum]
assert optimum == 2
assert len(optimal_orders) == 48


def canonical_rotation(order):
    rotations = [order[k:] + order[:k] for k in range(len(order))]
    return min(rotations)


cyclic_classes = {canonical_rotation(order) for order in optimal_orders}
assert len(cyclic_classes) == 8
lex_order = min(optimal_orders)
assert ''.join(NAMES[i] for i in lex_order) == "ABCDEF"
assert prefix_path(lex_order) == [(0, 0), (2, 0), (0, 0), (0, -2), (1, 0), (2, -1), (0, 0)]

period = lex_order
sequence = period * 50
for start in range(len(sequence)):
    x = y = 0
    for end in range(start, min(len(sequence), start + 60)):
        v = VECTORS[sequence[end]]
        x += v[0]
        y += v[1]
        assert max(abs(x), abs(y)) <= 2

print({
    "orders_checked": 720,
    "minimum_cyclic_linf_discrepancy": optimum,
    "optimal_linear_orders": len(optimal_orders),
    "optimal_cyclic_classes": len(cyclic_classes),
    "lexicographic_order": "ABCDEF",
    "repeated_windows_checked": True,
    "status": "passed",
})
