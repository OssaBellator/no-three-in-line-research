#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd

M = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
LAYERS_521 = (
    (0, 1, 2, 3),
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
)
LAYERS_527 = (
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
    (3, 0, 1, 2),
)
OBS_527 = (
    (3, 0),
    (0, 3),
    (2, 1),
    (1, 2),
)
Q = (
    tuple(Fraction(value[0]) for value in OBS_527),
    tuple(Fraction(value[1]) for value in OBS_527),
)


def layer_sum(layers):
    matrix = [[0] * 4 for _ in range(4)]
    for layer in layers:
        assert sorted(layer) == [0, 1, 2, 3]
        for source, action in enumerate(layer):
            matrix[source][action] += 1
    return tuple(tuple(row) for row in matrix)


def matrix_difference(left, right):
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(len(left[0])))
        for i in range(len(left))
    )


def rank(rows):
    work = [list(map(Fraction, row)) for row in rows]
    row_count = len(work)
    column_count = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[pivot_row][index]
                for index in range(column_count)
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def canonical_primitive(vector):
    divisor = 0
    for value in vector:
        divisor = gcd(divisor, abs(value))
    if divisor != 1:
        return False
    first = next(value for value in vector if value)
    return first > 0


sum_521 = layer_sum(LAYERS_521)
sum_527 = layer_sum(LAYERS_527)
assert sum_521 == M
assert sum_527 == ((1, 1, 1, 1),) * 4
difference = matrix_difference(sum_521, sum_527)
assert difference == (
    (1, 0, 0, -1),
    (-1, 1, 0, 0),
    (0, -1, 1, 0),
    (0, 0, -1, 1),
)
assert sum_521 != sum_527

base_rank = rank(Q)
assert base_rank == 2
controlled = []
hidden = []
for vector in product(range(-3, 4), repeat=4):
    if vector == (0, 0, 0, 0) or not canonical_primitive(vector):
        continue
    if rank(Q + (vector,)) == base_rank:
        controlled.append(vector)
    else:
        hidden.append(vector)

assert len(controlled) == 6
assert len(hidden) == 1114
assert (3, -3, 1, -1) in controlled
assert (1, -1, -1, 1) in hidden

print({
    "source_matrix": M,
    "docs_521_layer_sum": sum_521,
    "docs_527_layer_sum": sum_527,
    "sum_difference": difference,
    "same_physical_schedule": False,
    "quotient_rank": base_rank,
    "primitive_normals_checked": len(controlled) + len(hidden),
    "controlled_normals": len(controlled),
    "hidden_normals": len(hidden),
    "hidden_witness": (1, -1, -1, 1),
    "evidence_level": "independently_enumerated_lineage_obstruction",
    "status": "passed",
})
