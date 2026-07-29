#!/usr/bin/env python3
from collections import Counter
from itertools import product

def automorphisms(depth):
    if depth == 0:
        return [(0,)]
    sub = automorphisms(depth - 1)
    n = 2 ** (depth - 1)
    out = []
    for left in sub:
        for right in sub:
            out.append(tuple(list(left) + [n + x for x in right]))
            out.append(tuple([n + x for x in left] + list(right)))
    return list(dict.fromkeys(out))

def cycle_lengths(perm):
    seen = [False] * len(perm)
    lengths = []
    for i in range(len(perm)):
        if not seen[i]:
            j = i
            length = 0
            while not seen[j]:
                seen[j] = True
                length += 1
                j = perm[j]
            lengths.append(length)
    return lengths

def fixed_inventory(lengths):
    coeff = [1]
    for length in lengths:
        nxt = coeff + [0] * length
        for k, value in enumerate(coeff):
            nxt[k + length] += value
        coeff = nxt
    return coeff

def act(word, perm):
    out = [0] * len(word)
    for i, j in enumerate(perm):
        out[j] = word[i]
    return tuple(out)

GROUP = automorphisms(3)
assert len(GROUP) == 128
assert len({tuple(g) for g in GROUP}) == 128

fixed_sum = [0] * 9
cycle_type_distribution = Counter()
for g in GROUP:
    lengths = tuple(sorted(cycle_lengths(g)))
    cycle_type_distribution[lengths] += 1
    poly = fixed_inventory(lengths)
    fixed_sum = [a + b for a, b in zip(fixed_sum, poly)]

orbit_inventory = [x // len(GROUP) for x in fixed_sum]
assert orbit_inventory == [1, 1, 3, 3, 5, 3, 3, 1, 1]
assert fixed_sum == [128, 128, 384, 384, 640, 384, 384, 128, 128]

unseen = set(product((0, 1), repeat=8))
orbit_sizes = Counter()
orbit_count_by_weight = Counter()
representatives = []
while unseen:
    word = min(unseen)
    orbit = {act(word, g) for g in GROUP}
    unseen -= orbit
    representatives.append(word)
    orbit_sizes[len(orbit)] += 1
    orbit_count_by_weight[sum(word)] += 1

assert len(representatives) == sum(orbit_inventory) == 21
assert [orbit_count_by_weight[k] for k in range(9)] == orbit_inventory
assert sum(size * count for size, count in orbit_sizes.items()) == 256

for word in product((0, 1), repeat=8):
    canonical = min(act(word, g) for g in GROUP)
    assert canonical in representatives

print({
    "leaf_count": 8,
    "automorphism_group_order": len(GROUP),
    "cycle_types": {str(k): v for k, v in sorted(cycle_type_distribution.items())},
    "burnside_fixed_sum_by_weight": fixed_sum,
    "orbit_inventory_by_weight": orbit_inventory,
    "total_binary_schedule_orbits": len(representatives),
    "orbit_size_distribution": dict(sorted(orbit_sizes.items())),
})
