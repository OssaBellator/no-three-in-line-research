#!/usr/bin/env python3
from collections import Counter
from itertools import combinations


def tree_group(depth):
    if depth == 0:
        return [(0,)]
    child = tree_group(depth - 1)
    width = 2 ** (depth - 1)
    group = []
    for left in child:
        for right in child:
            group.append(tuple(list(left) + [width + x for x in right]))
            group.append(tuple([width + x for x in left] + list(right)))
    return list(dict.fromkeys(group))


def cycle_lengths(permutation):
    seen = [False] * len(permutation)
    lengths = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        node = start
        length = 0
        while not seen[node]:
            seen[node] = True
            length += 1
            node = permutation[node]
        lengths.append(length)
    return tuple(sorted(lengths))


def fixed_four_colorings(lengths):
    coeff = [0] * 9
    coeff[0] = 1
    for length in lengths:
        for degree in range(8, length - 1, -1):
            coeff[degree] += coeff[degree - length]
    return coeff[4]


def act(subset, permutation):
    return frozenset(permutation[i] for i in subset)


GROUP = tree_group(3)
assert len(GROUP) == 128
COLORINGS = [frozenset(choice) for choice in combinations(range(8), 4)]
assert len(COLORINGS) == 70

cycle_type_counts = Counter()
fixed_sum = 0
for permutation in GROUP:
    lengths = cycle_lengths(permutation)
    cycle_type_counts[lengths] += 1
    fixed = fixed_four_colorings(lengths)
    exhaustive = sum(act(coloring, permutation) == coloring for coloring in COLORINGS)
    assert fixed == exhaustive
    fixed_sum += fixed

assert fixed_sum == 640
burnside_orbits = fixed_sum // len(GROUP)
assert burnside_orbits == 5

seen = set()
orbits = []
for coloring in COLORINGS:
    if coloring in seen:
        continue
    orbit = {act(coloring, permutation) for permutation in GROUP}
    seen.update(orbit)
    representative = min(tuple(sorted(item)) for item in orbit)
    stabilizer = sum(act(coloring, permutation) == coloring for permutation in GROUP)
    assert len(orbit) * stabilizer == len(GROUP)
    orbits.append((len(orbit), stabilizer, representative))

orbits.sort()
assert [size for size, _, _ in orbits] == [2, 4, 16, 16, 32]
assert len(orbits) == burnside_orbits

sizes = [len(tree_group(depth)) for depth in range(4)]
assert sizes == [1, 2, 8, 128]
assert all(sizes[d] == 2 * sizes[d - 1] ** 2 for d in range(1, 4))

print({
    "tree_depth": 3,
    "tree_automorphism_group_order": len(GROUP),
    "balanced_leaf_colorings": len(COLORINGS),
    "burnside_fixed_sum": fixed_sum,
    "symmetry_orbits": burnside_orbits,
    "orbit_sizes": [size for size, _, _ in orbits],
    "stabilizer_sizes": [stabilizer for _, stabilizer, _ in orbits],
    "cycle_types": len(cycle_type_counts),
})
