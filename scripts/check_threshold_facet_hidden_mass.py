#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations

SOURCE = ((2,1,1,0),(0,2,1,1),(1,0,2,1),(1,1,0,2))
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

def rank(rows):
    work = [[Fraction(value) for value in row] for row in rows if any(row)]
    if not work:
        return 0
    row = 0
    columns = len(work[0])
    for column in range(columns):
        pivot = next((index for index in range(row, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        pivot_value = work[row][column]
        work[row] = [value / pivot_value for value in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            multiplier = work[index][column]
            work[index] = [
                value - multiplier * pivot_entry
                for value, pivot_entry in zip(work[index], work[row])
            ]
        row += 1
        if row == len(work):
            break
    return row

def affine_dimension(matrices):
    base = flatten(matrices[0])
    return rank([
        tuple(value - base_value for value, base_value in zip(flatten(matrix), base))
        for matrix in matrices[1:]
    ])

def row_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in row_compositions(total - first, length - 1):
            yield (first,) + rest

layers = tuple(permutation for permutation in permutations(range(4)) if legal(permutation))
assert len(layers) == 18
legal_matrices = tuple(sorted({
    layer_matrix(indices, layers)
    for indices in combinations_with_replacement(range(len(layers)), 4)
}))
assert len(legal_matrices) == 4475
score_histogram = Counter(score(matrix) for matrix in legal_matrices)
assert score_histogram == Counter({0:495,1:956,2:1193,3:1012,4:590,5:176,6:44,7:8,8:1})
face = tuple(matrix for matrix in legal_matrices if score(matrix) == 0)
assert affine_dimension(legal_matrices) == 9
assert affine_dimension(face) == 8
assert score(SOURCE) == -3

distance = lambda first, second: sum(
    abs(first[row][column] - second[row][column])
    for row in range(4) for column in range(4)
)
minimum_distance = min(distance(SOURCE, matrix) for matrix in legal_matrices)
nearest = tuple(matrix for matrix in legal_matrices if distance(SOURCE, matrix) == minimum_distance)
assert minimum_distance == 6 and len(nearest) == 8
assert {score(matrix) for matrix in nearest} == {0}

rows = tuple(row_compositions(4, 4))
transport_matrices = []
def build_transport(row_index, column_remaining, chosen):
    if row_index == 3:
        final_row = tuple(column_remaining)
        if sum(final_row) == 4 and all(value >= 0 for value in final_row):
            transport_matrices.append(tuple(chosen + [final_row]))
        return
    for candidate in rows:
        if all(candidate[column] <= column_remaining[column] for column in range(4)):
            build_transport(
                row_index + 1,
                tuple(column_remaining[column] - candidate[column] for column in range(4)),
                chosen + [candidate],
            )
build_transport(0, (4,4,4,4), [])
assert len(transport_matrices) == 10147
transport_histogram = Counter(score(matrix) for matrix in transport_matrices)
assert min(transport_histogram) == -8
minimum_states = tuple(matrix for matrix in transport_matrices if score(matrix) == -8)
assert minimum_states == (((4,0,0,0),(0,4,0,0),(0,0,4,0),(0,0,0,4)),)

for batch_size in range(1, 65):
    minimum_hidden = (3 * batch_size + 7) // 8
    assert 8 * minimum_hidden >= 3 * batch_size
    assert minimum_hidden == 0 or 8 * (minimum_hidden - 1) < 3 * batch_size

print({
    "legal_permutation_layers": len(layers),
    "legal_four_layer_matrices": len(legal_matrices),
    "legal_hull_affine_dimension": 9,
    "separating_face_vertices": len(face),
    "separating_face_affine_dimension": 8,
    "separating_face_is_facet": True,
    "source_score": -3,
    "nearest_legal_targets": len(nearest),
    "nearest_target_l1_distance": minimum_distance,
    "nearest_targets_on_facet": True,
    "transportation_matrices": len(transport_matrices),
    "minimum_transport_score": -8,
    "unique_minimum_transport_state": minimum_states[0],
    "necessary_hidden_weight": "at least 3/8",
    "equal_weight_batch_hidden_count": "ceil(3N/8)",
    "remaining_gap": "the hidden-mass lower bound is necessary only; no legal hidden-state primitive or enlarged source recurrence is constructed",
    "evidence_level": "exact_threshold_facet_and_hidden_mass_obstruction",
    "status": "passed",
})
