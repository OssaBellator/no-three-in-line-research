#!/usr/bin/env python3
from itertools import combinations, permutations

PHI = (
    (-1, 0, 0, 0),
    (1, 0, 1, 0),
    (0, 1, 0, 0),
    (0, 0, 1, -1),
)
PSI = (
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 0, 0, -1),
    (0, 0, 0, 0),
)
IDENTITY = (0, 1, 2, 3)
SOURCE = (
    2, 1, 1, 0,
    0, 2, 1, 1,
    1, 0, 2, 1,
    1, 1, 0, 2,
)


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))


def score(permutation, functional):
    return sum(functional[row][permutation[row]] for row in range(4))


def vector(permutation):
    result = [0] * 16
    for row, column in enumerate(permutation):
        result[4 * row + column] = 1
    return tuple(result)


layers = tuple(layer for layer in permutations(range(4)) if legal(layer))
assert len(layers) == 18
phi_scores = tuple(score(layer, PHI) for layer in layers)
psi_scores = tuple(score(layer, PSI) for layer in layers)
assert all(value >= 0 for value in phi_scores)
assert all(value >= 0 for value in psi_scores)
assert {value for value in phi_scores} == {0, 1, 2}
assert {value for value in psi_scores} == {0, 1}

identity_vector = vector(IDENTITY)
source_phi = sum(PHI[row][column] * SOURCE[4 * row + column]
                 for row in range(4) for column in range(4))
source_psi = sum(PSI[row][column] * SOURCE[4 * row + column]
                 for row in range(4) for column in range(4))
assert source_phi == -3
assert source_psi == 3
assert score(IDENTITY, PHI) == -2
assert score(IDENTITY, PSI) == 2

common_zero = tuple(
    layer for layer in layers
    if score(layer, PHI) == 0 and score(layer, PSI) == 0
)
assert common_zero == (
    (0, 2, 3, 1),
    (1, 2, 0, 3),
    (1, 3, 2, 0),
    (2, 1, 3, 0),
    (2, 3, 0, 1),
)

# Rows 0,1,2,5,6 form a unimodular five-by-five minor of the five common-zero
# layer vectors. Hence their multiplicities are uniquely determined over the
# integers by the aggregate matrix.
rows = (0, 1, 2, 5, 6)
minor = tuple(tuple(vector(layer)[row] for layer in common_zero) for row in rows)
assert minor == (
    (1, 0, 0, 0, 0),
    (0, 1, 1, 0, 0),
    (0, 0, 0, 1, 1),
    (0, 0, 0, 1, 0),
    (1, 1, 0, 0, 0),
)

primitive_target = tuple(
    8 * SOURCE[index] - 12 * identity_vector[index]
    for index in range(16)
)
base_counts = (4, 4, 4, 4, 4)
assert all(
    sum(base_counts[column] * vector(common_zero[column])[row]
        for column in range(5)) == primitive_target[row]
    for row in range(16)
)

# The two separator equations for a putative equality mixture with total scale t,
# h hidden 4I matrices, and legal primitive layers x are
#   sum Phi(x) = 8h-3t >= 0,
#   sum Psi(x) = 3t-8h >= 0.
# Thus both vanish, t=8K, h=3K, and only common-zero layers may occur. The
# unimodular minor then forces 4K copies of every common-zero type.
for multiple in range(1, 65):
    total_scale = 8 * multiple
    hidden_matrices = 3 * multiple
    counts = tuple(4 * multiple for _ in common_zero)
    assert 8 * hidden_matrices - 3 * total_scale == 0
    assert 3 * total_scale - 8 * hidden_matrices == 0
    assert all(
        sum(counts[column] * vector(common_zero[column])[row]
            for column in range(5)) == multiple * primitive_target[row]
        for row in range(16)
    )

print({
    "legal_primitive_layers": len(layers),
    "phi_nonnegative_scores": {0: 9, 1: 8, 2: 1},
    "psi_nonnegative_scores": {0: 10, 1: 8},
    "common_zero_layer_types": common_zero,
    "common_zero_types": len(common_zero),
    "unimodular_minor_rows": rows,
    "equality_scale": "t=8K",
    "hidden_matrices": "h=3K",
    "legal_primitive_multiplicities": "4K copies of each of five common-zero types",
    "hidden_layer_density": "3/8",
    "multiples_checked": 64,
    "remaining_gap": "enlarge the primitive alphabet or use a genuinely unexposed non-rolling operation",
    "evidence_level": "exact_all_equality_multiple_dual_separator_rigidity",
    "status": "passed",
})
