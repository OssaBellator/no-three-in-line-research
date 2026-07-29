#!/usr/bin/env python3
from fractions import Fraction

NODES = range(6)
ROOTS = {0: Fraction(1, 4), 1: Fraction(1, 5)}
EDGES = [
    (0, 2, Fraction(1, 2)), (0, 3, Fraction(1, 3)),
    (1, 2, Fraction(2, 5)), (1, 3, Fraction(1, 4)),
    (2, 3, Fraction(1, 6)), (2, 4, Fraction(1, 2)),
    (2, 5, Fraction(1, 5)), (3, 4, Fraction(1, 3)),
    (3, 5, Fraction(2, 7)),
]

def dp(mask):
    bound = {v: ROOTS.get(v, Fraction(0)) for v in NODES}
    for u in NODES:
        for i, (a, b, r) in enumerate(EDGES):
            if a == u and ((mask >> i) & 1):
                bound[b] += bound[a] * r
    return bound

def path_sum(mask, target):
    adj = {v: [] for v in NODES}
    for i, (u, v, r) in enumerate(EDGES):
        if (mask >> i) & 1:
            adj[u].append((v, r))
    total = Fraction(0)
    def walk(v, weight):
        nonlocal total
        if v == target:
            total += weight
        for w, r in adj[v]:
            walk(w, weight * r)
    for root, base in ROOTS.items():
        walk(root, base)
    return total

for mask in range(1 << len(EDGES)):
    bound = dp(mask)
    assert bound[4] == path_sum(mask, 4)
    assert bound[5] == path_sum(mask, 5)

full = dp((1 << len(EDGES)) - 1)
assert full[4] == Fraction(19, 120)
assert full[5] == Fraction(311, 3500)
assert Fraction(1, 2) > EDGES[1][2]

print({
    "automaton_subgraphs_checked": 512,
    "terminal_4_load": str(full[4]),
    "terminal_5_load": str(full[5]),
    "localized_bad_edge": (0, 3),
})
