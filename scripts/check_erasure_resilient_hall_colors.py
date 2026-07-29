#!/usr/bin/env python3
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations

sources = range(4)
targets = range(4)
edges = []
for x in sources:
    for y in targets:
        if x == y:
            continue
        c = ((y - x) % 4) - 1
        edges.append((x, y, c))

for x in sources:
    colors = [c for xx, _, c in edges if xx == x]
    assert sorted(colors) == [0, 1, 2]
for y in targets:
    colors = [c for _, yy, c in edges if yy == y]
    assert sorted(colors) == [0, 1, 2]

code = {0: (0, 0, 0), 1: (0, 1, 1), 2: (1, 0, 1)}
for a, b in combinations(code, 2):
    assert sum(u != v for u, v in zip(code[a], code[b])) >= 2

for erased_count, expected in [(0, F(1, 3)), (1, F(1, 3)), (2, F(2, 3))]:
    for erased in combinations(range(3), erased_count):
        kept = tuple(i for i in range(3) if i not in erased)
        loads = defaultdict(F)
        for x, y, c in edges:
            tag = tuple(code[c][i] for i in kept)
            loads[(y, tag)] += F(1, 3)
        assert max(loads.values()) == expected

print({
    "residual_edges": len(edges),
    "colors": len(code),
    "minimum_distance": 2,
    "one_erasure_load": "1/3",
    "two_erasure_load": "2/3",
})
