#!/usr/bin/env python3
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = (
    (2,1,1,0),
    (0,2,1,1),
    (1,0,2,1),
    (1,1,0,2),
)
HIDDEN = (
    (4,0,0,0),
    (0,4,0,0),
    (0,0,4,0),
    (0,0,0,4),
)
PHI = (-1,0,0,0, 1,0,1,0, 0,1,0,0, 0,0,1,-1)

def flatten(matrix):
    return tuple(value for row in matrix for value in row)

def score(matrix):
    return sum(coefficient * value for coefficient, value in zip(PHI, flatten(matrix)))

def collinear(first, second, third):
    return (
        (second[0]-first[0])*(third[1]-first[1])
        == (second[1]-first[1])*(third[0]-first[0])
    )

def legal(permutation):
    points = tuple((row, permutation[row]) for row in range(4))
    return all(not collinear(*triple) for triple in combinations(points, 3))

def layer_matrix(indices, layers):
    matrix = [[0] * 4 for _ in range(4)]
    for index in indices:
        for row, column in enumerate(layers[index]):
            matrix[row][column] += 1
    return tuple(tuple(row) for row in matrix)

layers = tuple(permutation for permutation in permutations(range(4)) if legal(permutation))
assert len(layers) == 18
legal_matrices = tuple(sorted({
    layer_matrix(indices, layers)
    for indices in combinations_with_replacement(range(len(layers)), 4)
}))
assert len(legal_matrices) == 4475
face = tuple(matrix for matrix in legal_matrices if score(matrix) == 0)
assert len(face) == 495
assert score(SOURCE) == -3
assert score(HIDDEN) == -8

LEGAL_WITNESSES = (
    ((0,0,4,0),(0,0,0,4),(4,0,0,0),(0,4,0,0)),
    ((0,0,4,0),(0,4,0,0),(0,0,0,4),(4,0,0,0)),
    ((0,4,0,0),(0,0,0,4),(0,0,4,0),(4,0,0,0)),
    ((0,4,0,0),(0,0,4,0),(4,0,0,0),(0,0,0,4)),
    ((4,0,0,0),(0,0,4,0),(0,0,0,4),(0,4,0,0)),
)
assert all(matrix in face for matrix in LEGAL_WITNESSES)

total = tuple(
    tuple(
        3 * HIDDEN[row][column]
        + sum(matrix[row][column] for matrix in LEGAL_WITNESSES)
        for column in range(4)
    )
    for row in range(4)
)
assert total == tuple(
    tuple(8 * SOURCE[row][column] for column in range(4))
    for row in range(4)
)

# Equality in the hidden-mass lower bound forces every hidden state to have
# minimum score -8 and every exposed legal state to lie on the score-zero facet.
# The minimum-score transportation state is uniquely 4I_4, established in
# check_threshold_facet_hidden_mass.py. For an equal-weight N-state batch,
# -3N=-8H, so N is divisible by eight and H=3N/8.
for batch_size in range(1, 65):
    equality_possible_by_score = (3 * batch_size) % 8 == 0
    assert equality_possible_by_score == (batch_size % 8 == 0)

layer_decompositions = {}
for matrix in LEGAL_WITNESSES:
    witnesses = [
        indices
        for indices in combinations_with_replacement(range(len(layers)), 4)
        if layer_matrix(indices, layers) == matrix
    ]
    assert witnesses
    layer_decompositions[matrix] = witnesses[0]

assert tuple(layers[index] for index in layer_decompositions[LEGAL_WITNESSES[0]]) == (
    (2,3,0,1),
) * 4
assert tuple(layers[index] for index in layer_decompositions[LEGAL_WITNESSES[4]]) == (
    (0,2,3,1),
) * 4

print({
    "legal_permutation_layers": len(layers),
    "legal_four_layer_matrices": len(legal_matrices),
    "facet_matrices": len(face),
    "hidden_state": "4I_4",
    "hidden_state_score": -8,
    "source_score": -3,
    "equal_weight_batch_size": 8,
    "hidden_states": 3,
    "legal_facet_states": 5,
    "hidden_weight": "3/8",
    "source_average_identity": "3*(4I_4)+sum(five legal facet matrices)=8*S",
    "minimum_equal_weight_batch_size": 8,
    "minimum_batch_reason": "-3N=-8H forces 8|N",
    "algebraic_hidden_mass_bound_is_sharp": True,
    "remaining_gap": "4I_4 is not an exposed legal endpoint; no geometric hidden-state primitive realizes the eight-state average",
    "evidence_level": "exact_minimal_equal_weight_hidden_mixture",
    "status": "passed",
})
