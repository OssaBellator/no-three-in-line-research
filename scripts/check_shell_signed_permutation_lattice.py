#!/usr/bin/env python3
from itertools import permutations, product

GENERATORS = (
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
)


def determinant(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def combine(coefficients, columns):
    return tuple(sum(coefficients[index] * columns[index][coordinate] for index in range(3)) for coordinate in range(3))


def inverse_image(vector):
    first, second, third = vector
    return (
        first - second + third,
        first + second - third,
        -first + second + third,
    )


matrix = tuple(tuple(GENERATORS[column][row] for column in range(3)) for row in range(3))
assert determinant(matrix) == 2

signed_vectors = set()
for coordinate_permutation in permutations(range(3)):
    permuted = tuple(
        tuple(generator[index] for index in coordinate_permutation)
        for generator in GENERATORS
    )
    for coefficients in product(range(-8, 9), repeat=3):
        vector = combine(coefficients, permuted)
        signed_vectors.add(vector)
        assert sum(vector) % 2 == 0

assert len(signed_vectors) == 4913
for vector in product(range(-6, 7), repeat=3):
    numerators = inverse_image(vector)
    integral = all(value % 2 == 0 for value in numerators)
    assert integral == (sum(vector) % 2 == 0)

odd_units = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
assert all(vector not in signed_vectors for vector in odd_units)

print({
    "source_columns": GENERATORS,
    "determinant": determinant(matrix),
    "operations_closed": [
        "integer repetition",
        "signed cancellation",
        "simultaneous composition",
        "coordinate permutation",
        "target reoptimization",
        "quantization and chamber transport with fixed columns",
    ],
    "bounded_signed_permuted_vectors_checked": len(signed_vectors),
    "integer_lattice": "all and only vectors with even coordinate sum",
    "odd_unit_columns_generated": False,
    "conclusion": "even after signed cancellation and cycle-coordinate relabelling, the recorded shell catalogue cannot produce an odd-sum action column",
    "remaining_gap": "a clean-macro move with genuinely new incidence support is required",
    "evidence_level": "exact_signed_permuted_source_lattice_obstruction",
    "status": "passed",
})
