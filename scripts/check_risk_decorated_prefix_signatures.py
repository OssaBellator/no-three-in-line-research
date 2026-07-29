#!/usr/bin/env python3
from collections import Counter
from itertools import combinations


def ordered_shapes(leaves):
    if leaves == 1:
        return [("leaf",)]
    out = []
    for left_leaves in range(1, leaves):
        for left in ordered_shapes(left_leaves):
            for right in ordered_shapes(leaves - left_leaves):
                out.append(("node", left, right))
    return out


def decorate(shape, high_positions):
    counter = [0]

    def walk(node):
        if node[0] == "leaf":
            index = counter[0]
            counter[0] += 1
            return ("H",) if index in high_positions else ("L",)
        return ("node", walk(node[1]), walk(node[2]))

    return walk(shape)


def canonical(tree):
    if tree[0] in {"L", "H"}:
        return tree
    left = canonical(tree[1])
    right = canonical(tree[2])
    a, b = sorted((left, right), key=repr)
    return ("node", a, b)


def leaf_depths(tree, depth=0):
    if tree[0] in {"L", "H"}:
        return [(tree[0], depth)]
    return leaf_depths(tree[1], depth + 1) + leaf_depths(tree[2], depth + 1)


def value(tree):
    return max((1 if label == "L" else 2) * (2 ** depth) for label, depth in leaf_depths(tree))

shapes = ordered_shapes(6)
assert len(shapes) == 42
orbits = {}
ordered_total = 0
ordered_optimal = 0
for shape in shapes:
    for highs in combinations(range(6), 2):
        decorated = decorate(shape, set(highs))
        ordered_total += 1
        if value(decorated) == 8:
            ordered_optimal += 1
        orbits.setdefault(canonical(decorated), 0)
        orbits[canonical(decorated)] += 1

histogram = Counter(value(tree) for tree in orbits)
assert ordered_total == 630
assert len(orbits) == 41
assert histogram == Counter({16: 16, 32: 18, 64: 5, 8: 2})
assert ordered_optimal == 6

for tree in orbits:
    assert canonical(tree) == tree
    if tree[0] == "node":
        swapped = ("node", tree[2], tree[1])
        assert canonical(swapped) == tree

print({
    "ordered_decorated_trees": ordered_total,
    "canonical_orbits": len(orbits),
    "orbit_value_histogram": dict(sorted(histogram.items())),
    "optimal_orbits": histogram[8],
    "ordered_optimal_lifts": ordered_optimal,
})
