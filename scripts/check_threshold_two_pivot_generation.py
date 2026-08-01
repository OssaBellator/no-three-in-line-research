#!/usr/bin/env python3
"""Generate every nearest legal threshold matrix by two conservative pivots."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))

def layer_matrix(layers):
    return tuple(
        tuple(sum(layer[row] == column for layer in layers) for column in range(4))
        for row in range(4)
    )

def distance(first, second):
    return sum(abs(first[r][c] - second[r][c]) for r in range(4) for c in range(4))

def pivots(matrix):
    for r1, r2 in combinations(range(4), 2):
        for c1, c2 in combinations(range(4), 2):
            for sign in (1, -1):
                changes = (
                    (r1, c1, -sign), (r2, c2, -sign),
                    (r1, c2, sign), (r2, c1, sign),
                )
                if all(matrix[r][c] + delta >= 0 for r, c, delta in changes):
                    updated = [list(row) for row in matrix]
                    for r, c, delta in changes:
                        updated[r][c] += delta
                    yield (r1, r2, c1, c2, sign), tuple(tuple(row) for row in updated)

permutations_all = tuple(permutations(range(4)))
legal_layers = tuple(layer for layer in permutations_all if legal(layer))
assert len(legal_layers) == 18
legal_matrices = {
    layer_matrix(layers)
    for layers in combinations_with_replacement(legal_layers, 4)
}
assert len(legal_matrices) == 4475
minimum_distance = min(distance(SOURCE, matrix) for matrix in legal_matrices)
targets = tuple(sorted(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum_distance))
assert minimum_distance == 6 and len(targets) == 8

first_steps = tuple(pivots(SOURCE))
paths = []
for target in targets:
    assert all(intermediate != target for _, intermediate in first_steps)
    target_paths = []
    for first_pivot, intermediate in first_steps:
        for second_pivot, final in pivots(intermediate):
            if final == target:
                target_paths.append((first_pivot, intermediate, second_pivot))
    assert len(target_paths) == 6
    paths.extend((target, *record) for record in target_paths)

assert len(paths) == 48
assert Counter(record[0] for record in paths) == Counter({target: 6 for target in targets})
intermediates = {record[2] for record in paths}
assert len(intermediates) == 20
assert all(intermediate not in legal_matrices for intermediate in intermediates)
assert all(sum(row) == 4 for intermediate in intermediates for row in intermediate)
assert all(sum(intermediate[row][column] for row in range(4)) == 4 for intermediate in intermediates for column in range(4))

print({
    "legal_permutation_layers": len(legal_layers),
    "distinct_legal_degree_four_matrices": len(legal_matrices),
    "nearest_legal_matrices": len(targets),
    "entrywise_l1_distance": minimum_distance,
    "minimum_conservative_2x2_pivots": 2,
    "ordered_shortest_paths": len(paths),
    "shortest_paths_per_target": 6,
    "distinct_intermediate_matrices": len(intermediates),
    "geometrically_legal_intermediates": 0,
    "source_margins_preserved_at_every_step": True,
    "remaining_gap": "the two-pivot compound is repository-native matrix algebra but lacks an atomic geometric prime-patching realization",
    "evidence_level": "exact_conservative_residual_pivot_source_path",
    "status": "passed",
})
