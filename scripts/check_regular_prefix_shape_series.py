#!/usr/bin/env python3
from collections import defaultdict
from functools import lru_cache

# DFA for avoiding 000. States 0,1,2 record the trailing zero run; 3 is dead.
DEAD = 3
ACCEPT = {0, 1, 2}
DELTA = {}
for q in range(4):
    if q == DEAD:
        DELTA[(q, 0)] = DEAD
        DELTA[(q, 1)] = DEAD
    else:
        DELTA[(q, 0)] = q + 1 if q < 2 else DEAD
        DELTA[(q, 1)] = 0

KMAX = 10


def multiply(a, b):
    out = defaultdict(int)
    for i, x in a.items():
        for j, y in b.items():
            if i + j <= KMAX:
                out[i + j] += x * y
    return dict(out)


@lru_cache(None)
def poly(q, depth):
    out = defaultdict(int)
    if q in ACCEPT:
        out[1] += 1
    if depth > 0:
        prod = multiply(poly(DELTA[(q, 0)], depth - 1), poly(DELTA[(q, 1)], depth - 1))
        for k, v in prod.items():
            out[k] += v
    return dict(out)

stable = poly(0, KMAX - 1)
expected = {1: 1, 2: 1, 3: 2, 4: 4, 5: 9, 6: 21, 7: 51, 8: 127, 9: 323, 10: 835}
assert stable == expected

# Coefficient z^K stabilizes once the allowed depth reaches K-1.
for k in range(1, KMAX + 1):
    target = poly(0, k - 1).get(k, 0)
    assert target == expected[k]
    for depth in range(k - 1, KMAX + 2):
        assert poly(0, depth).get(k, 0) == target

print({
    "language": "avoid 000",
    "coefficients_1_to_10": tuple(expected[k] for k in range(1, 11)),
    "stabilization_depth_for_k_leaves": "k-1",
    "status": "passed",
})
