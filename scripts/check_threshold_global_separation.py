#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = (
    (2,1,1,0),
    (0,2,1,1),
    (1,0,2,1),
    (1,1,0,2),
)
WEIGHT = (
    (0,0,0,1),
    (1,-1,0,0),
    (0,0,-1,0),
    (1,0,1,0),
)

def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

def legal_layer(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))

def layer_matrix(layers):
    return tuple(
        tuple(sum(layer[row] == column for layer in layers) for column in range(4))
        for row in range(4)
    )

def phi(matrix):
    return sum(WEIGHT[row][column] * matrix[row][column]
               for row in range(4) for column in range(4))

layers = tuple(item for item in permutations(range(4)) if legal_layer(item))
assert len(layers) == 18

legal_matrices = {
    layer_matrix(tuple(layers[index] for index in indices))
    for indices in combinations_with_replacement(range(len(layers)), 4)
}
assert len(legal_matrices) == 4475
assert SOURCE not in legal_matrices

source_value = phi(SOURCE)
distribution = Counter(phi(matrix) for matrix in legal_matrices)
assert source_value == -3
assert distribution == Counter({0:495,1:956,2:1193,3:1012,4:590,5:176,6:44,7:8,8:1})

margins = Counter(phi(matrix) - source_value for matrix in legal_matrices)
assert min(margins) == 3
assert margins == Counter({3:495,4:956,5:1193,6:1012,7:590,8:176,9:44,10:8,11:1})

ordered = tuple(sorted(legal_matrices))
for size in range(1, 8):
    sample = ordered[:size]
    aggregate_margin = sum(phi(matrix) - source_value for matrix in sample)
    assert aggregate_margin >= 3 * size

print({
    "legal_permutation_layers": len(layers),
    "legal_four_layer_matrices": len(legal_matrices),
    "source_in_legal_catalogue": False,
    "separating_weight": WEIGHT,
    "source_functional_value": source_value,
    "legal_functional_distribution": dict(sorted(distribution.items())),
    "minimum_legal_displacement_margin": min(margins),
    "nonempty_legal_endpoint_zero_sum_cycle": False,
    "source_in_convex_hull_of_legal_endpoints": False,
    "remaining_gap": "a successful threshold mechanism must leave the native legal-endpoint catalogue or alter the conserved source interface",
    "evidence_level": "exact_global_threshold_separation",
    "status": "passed",
})
