#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
PERMUTATIONS = tuple(permutations(range(4)))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal_layer(permutation):
    points = tuple((source, action) for source, action in enumerate(permutation))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def layer_sum(layers):
    matrix = [[0] * 4 for _ in range(4)]
    for layer in layers:
        for source, action in enumerate(layer):
            matrix[source][action] += 1
    return tuple(tuple(row) for row in matrix)


def l1_distance(left, right):
    return sum(abs(left[i][j] - right[i][j]) for i in range(4) for j in range(4))


def observables(matrix):
    fixed = sum(matrix[i][i] for i in range(4))
    forward = sum(matrix[i][(i + 1) % 4] for i in range(4))
    return fixed, forward


legal = tuple(permutation for permutation in PERMUTATIONS if legal_layer(permutation))
assert len(legal) == 18
nearest = []
best_distance = None
for indices in combinations_with_replacement(range(len(legal)), 4):
    layers = tuple(legal[index] for index in indices)
    matrix = layer_sum(layers)
    distance = l1_distance(matrix, SOURCE)
    if best_distance is None or distance < best_distance:
        best_distance = distance
        nearest = [(matrix, layers)]
    elif distance == best_distance:
        nearest.append((matrix, layers))

assert best_distance == 6
assert len(nearest) == 8
source_fixed, source_forward = observables(SOURCE)
assert (source_fixed, source_forward) == (8, 4)

records = []
loss_histogram = Counter()
for matrix, layers in nearest:
    fixed, forward = observables(matrix)
    loss = (source_fixed - fixed, source_forward - forward)
    loss_histogram[loss] += 1
    delta = tuple(tuple(matrix[i][j] - SOURCE[i][j] for j in range(4)) for i in range(4))
    moved_out = tuple((i, j) for i in range(4) for j in range(4) if delta[i][j] == -1)
    moved_in = tuple((i, j) for i in range(4) for j in range(4) if delta[i][j] == 1)
    assert len(moved_out) == len(moved_in) == 3
    records.append({
        "matrix": matrix,
        "observable_loss": loss,
        "moved_out_cells": moved_out,
        "moved_in_cells": moved_in,
        "legal_layers": layers,
    })

assert loss_histogram == Counter({(2, 1): 4, (3, 0): 4})
assert (0, 0) not in loss_histogram

price_frontier = {
    "branch_A": "2*alpha + beta",
    "branch_B": "3*alpha",
    "switching_wall": "beta = alpha",
    "minimum": "min(2*alpha + beta, 3*alpha)",
}

print({
    "nearest_legal_matrices": len(nearest),
    "entrywise_l1_distance": best_distance,
    "source_observables": {"fixed": source_fixed, "forward": source_forward},
    "observable_loss_histogram": {str(key): value for key, value in sorted(loss_histogram.items())},
    "nearest_matrix_preserving_both_observables": False,
    "mass_units_moved_per_replacement": 3,
    "symbolic_nonnegative_price_frontier": price_frontier,
    "replacement_records": records,
    "conclusion": "geometric legality forces either loss (2,1) or loss (3,0) in the aligned quotient observables",
    "remaining_gap": "the repository contains no geometric residual inequality assigning alpha and beta or authorizing either mass-transfer branch",
    "evidence_level": "exact_replacement_price_frontier",
    "status": "passed",
})
