#!/usr/bin/env python3
from itertools import combinations, product

p = 5
k = 2
e = 2
points = (0, 1, 2, 3)
L = len(points)
assert L == k + e

colors = list(product(range(p), repeat=k))


def encode(coeffs):
    a, b = coeffs
    return tuple((a + b * x) % p for x in points)


code = {c: encode(c) for c in colors}
assert len(set(code.values())) == p ** k

min_distance = L
for c1, c2 in combinations(colors, 2):
    d = sum(x != y for x, y in zip(code[c1], code[c2]))
    min_distance = min(min_distance, d)
assert min_distance == e + 1

max_lists = []
fiber_counts = []
for erased in range(L + 1):
    max_list = 0
    fibers_seen = 0
    for erased_positions in combinations(range(L), erased):
        keep = tuple(i for i in range(L) if i not in erased_positions)
        fibers = {}
        for c in colors:
            obs = tuple(code[c][i] for i in keep)
            fibers.setdefault(obs, 0)
            fibers[obs] += 1
        max_list = max(max_list, max(fibers.values()))
        fibers_seen += len(fibers)
    expected = p ** max(0, erased - e)
    assert max_list == expected
    max_lists.append(max_list)
    fiber_counts.append(fibers_seen)

assert p ** (L - e) == p ** k

d = 3
loads = [f"{m}/{d}" for m in max_lists]
print({
    "field_size": p,
    "colors": len(colors),
    "tag_length": L,
    "erasure_budget": e,
    "minimum_distance": min_distance,
    "max_lists_by_erased_coordinates": max_lists,
    "observation_fibers_checked": fiber_counts,
    "reverse_loads_for_degree_3": loads,
})
