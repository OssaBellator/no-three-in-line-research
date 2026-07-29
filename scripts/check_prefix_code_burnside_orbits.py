#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter

leaves = ("00", "01", "10", "11")
labels = ("A1", "A2", "B1", "B2")
assignments = [dict(zip(leaves, perm)) for perm in permutations(labels)]

label_group = []
for swap_a, swap_b in product((0, 1), repeat=2):
    label_group.append({
        "A1": "A2" if swap_a else "A1",
        "A2": "A1" if swap_a else "A2",
        "B1": "B2" if swap_b else "B1",
        "B2": "B1" if swap_b else "B2",
    })

def tree_automorphism(root_swap, left_swap, right_swap):
    mapping = {}
    for word in leaves:
        first, second = word
        output_first = str(1 - int(first)) if root_swap else first
        child_swap = left_swap if first == "0" else right_swap
        output_second = str(1 - int(second)) if child_swap else second
        mapping[word] = output_first + output_second
    return mapping

tree_group = [
    tree_automorphism(r, l, rr)
    for r, l, rr in product((0, 1), repeat=3)
]
assert len({tuple(g[x] for x in leaves) for g in tree_group}) == 8

def transform(assignment, label_perm, tree_perm):
    output = {}
    for leaf, label in assignment.items():
        output[tree_perm[leaf]] = label_perm[label]
    return output

fixed_histogram = Counter()
fixed_sum = 0
for label_perm in label_group:
    for tree_perm in tree_group:
        fixed = sum(
            transform(assignment, label_perm, tree_perm) == assignment
            for assignment in assignments
        )
        fixed_histogram[fixed] += 1
        fixed_sum += fixed

orbit_count = fixed_sum // (len(label_group) * len(tree_group))
assert fixed_sum == 64
assert orbit_count == 2
assert fixed_histogram == Counter({0: 24, 4: 4, 8: 3, 24: 1})

index = {
    tuple(assignment[leaf] for leaf in leaves): i
    for i, assignment in enumerate(assignments)
}
unseen = set(range(len(assignments)))
orbits = []
while unseen:
    seed = min(unseen)
    orbit = set()
    for label_perm in label_group:
        for tree_perm in tree_group:
            image = transform(assignments[seed], label_perm, tree_perm)
            orbit.add(index[tuple(image[leaf] for leaf in leaves)])
    orbits.append(orbit)
    unseen -= orbit

orbit_sizes = sorted(len(orbit) for orbit in orbits)
canonical = sorted(
    min(tuple(assignments[i][leaf] for leaf in leaves) for i in orbit)
    for orbit in orbits
)
assert orbit_sizes == [8, 16]
assert canonical == [
    ("A1", "A2", "B1", "B2"),
    ("A1", "B1", "A2", "B2"),
]

print({
    "labeled_optimal_codes": len(assignments),
    "symmetry_group_order": len(label_group) * len(tree_group),
    "burnside_fixed_sum": fixed_sum,
    "symmetry_orbits": orbit_count,
    "orbit_sizes": orbit_sizes,
    "canonical_representatives": canonical,
})
