#!/usr/bin/env python3
from fractions import Fraction
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


def observables(permutation):
    fixed = sum(action == source for source, action in enumerate(permutation))
    forward = sum(action == (source + 1) % 4 for source, action in enumerate(permutation))
    return fixed, forward


def prefix_discrepancy(order):
    vectors = tuple(observables(layer) for layer in order)
    mean = tuple(Fraction(sum(vector[j] for vector in vectors), 4) for j in range(2))
    prefix = [Fraction(0), Fraction(0)]
    best = Fraction(0)
    for vector in vectors:
        for j in range(2):
            prefix[j] += vector[j] - mean[j]
        best = max(best, abs(prefix[0]), abs(prefix[1]))
    return best


legal = tuple(permutation for permutation in PERMUTATIONS if legal_layer(permutation))
assert len(legal) == 18

best_distance = None
nearest = []
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
assert all(all(sum(row) == 4 for row in matrix) for matrix, _ in nearest)
assert all(all(sum(matrix[i][j] for i in range(4)) == 4 for j in range(4)) for matrix, _ in nearest)

selected_matrix, selected_layers = min(nearest)
assert selected_matrix == (
    (1, 1, 1, 1),
    (0, 2, 1, 1),
    (2, 0, 1, 1),
    (1, 1, 1, 1),
)
assert selected_layers == (
    (0, 1, 3, 2),
    (1, 2, 0, 3),
    (2, 3, 0, 1),
    (3, 1, 2, 0),
)

orders = tuple(permutations(selected_layers))
minimum_discrepancy = min(prefix_discrepancy(order) for order in orders)
optimal_orders = tuple(order for order in orders if prefix_discrepancy(order) == minimum_discrepancy)
assert minimum_discrepancy == 1
assert len(optimal_orders) == 8

print({
    "source_matrix": SOURCE,
    "legal_permutation_layers": len(legal),
    "legal_four_layer_multisets_checked": len(tuple(combinations_with_replacement(range(len(legal)), 4))),
    "minimum_entrywise_l1_distance": best_distance,
    "nearest_matrices": len(nearest),
    "selected_matrix": selected_matrix,
    "selected_legal_layers": selected_layers,
    "minimum_fixed_forward_prefix_discrepancy": str(minimum_discrepancy),
    "optimal_orders": len(optimal_orders),
    "remaining_gap": "the nearest legal matrix changes six units of source-cell mass and is not derived from the prime-patching threshold inequalities",
    "evidence_level": "exact_geometric_replacement_search",
    "status": "passed",
})
