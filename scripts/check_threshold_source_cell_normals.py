#!/usr/bin/env python3
from fractions import Fraction

M = (
    (2, 1, 1, 0),
    (0, 2, 1, 1),
    (1, 0, 2, 1),
    (1, 1, 0, 2),
)
SELECTED = (
    (0, 2, 3, 1),
    (0, 1, 2, 3),
    (1, 3, 2, 0),
    (2, 1, 0, 3),
)


def rank(rows):
    work = [list(map(Fraction, row)) for row in rows]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry / value for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][index] - factor * work[pivot_row][index]
                for index in range(len(work[0]))
            ]
        pivot_row += 1
    return pivot_row


def solve_coefficients(rows, target):
    equations = [
        [Fraction(rows[index][column]) for index in range(len(rows))]
        + [Fraction(target[column])]
        for column in range(len(target))
    ]
    pivot_row = 0
    pivots = []
    for column in range(len(rows)):
        pivot = next(
            (row for row in range(pivot_row, len(equations)) if equations[row][column]),
            None,
        )
        if pivot is None:
            continue
        equations[pivot_row], equations[pivot] = equations[pivot], equations[pivot_row]
        value = equations[pivot_row][column]
        equations[pivot_row] = [entry / value for entry in equations[pivot_row]]
        for row in range(len(equations)):
            if row == pivot_row or not equations[row][column]:
                continue
            factor = equations[row][column]
            equations[row] = [
                equations[row][index] - factor * equations[pivot_row][index]
                for index in range(len(equations[row]))
            ]
        pivots.append(column)
        pivot_row += 1
    if any(
        all(row[column] == 0 for column in range(len(rows))) and row[-1] != 0
        for row in equations
    ):
        return None
    solution = [Fraction(0)] * len(rows)
    for row, column in enumerate(pivots):
        solution[column] = equations[row][-1]
    return tuple(solution)


fixed = tuple(
    sum(action == source for source, action in enumerate(permutation))
    for permutation in SELECTED
)
cyclic_forward = tuple(
    sum(action == (source + 1) % 4 for source, action in enumerate(permutation))
    for permutation in SELECTED
)
Q = ((1, 1, 1, 1), fixed, cyclic_forward)
assert Q == ((1, 1, 1, 1), (1, 4, 1, 2), (2, 0, 2, 0))
assert rank(Q) == 3

cell_normals = {}
controlled = {}
hidden = {}
absent = {}
for source in range(4):
    for action in range(4):
        normal = tuple(
            int(permutation[source] == action)
            for permutation in SELECTED
        )
        cell_normals[(source, action)] = normal
        if M[source][action] == 0:
            absent[(source, action)] = normal
            assert normal == (0, 0, 0, 0)
            continue
        coefficients = solve_coefficients(Q, normal)
        if coefficients is None:
            hidden[(source, action)] = normal
        else:
            controlled[(source, action)] = {
                "normal": normal,
                "coefficients": coefficients,
            }

assert len(absent) == 4
assert len(controlled) == 4
assert len(hidden) == 8
assert hidden[(0, 0)] == (1, 1, 0, 0)
assert controlled[(0, 2)] == {
    "normal": (0, 0, 0, 1),
    "coefficients": (
        Fraction(2),
        Fraction(-1, 2),
        Fraction(-3, 4),
    ),
}

for data in controlled.values():
    reconstructed = tuple(
        sum(data["coefficients"][row] * Q[row][column] for row in range(3))
        for column in range(4)
    )
    assert reconstructed == data["normal"]

print(
    {
        "source_matrix_positive_cells": 12,
        "source_cell_normals": cell_normals,
        "aligned_quotient": Q,
        "controlled_positive_cell_normals": len(controlled),
        "hidden_positive_cell_normals": len(hidden),
        "absent_cells": len(absent),
        "controlled_certificate": controlled,
        "minimal_hidden_witness": {
            "cell": (0, 0),
            "normal": hidden[(0, 0)],
        },
        "conclusion": "the aligned two-observable quotient misses eight of the twelve positive source-cell occupancy normals",
        "evidence_level": "source_matrix_cell_normal_census",
        "status": "passed",
    }
)
