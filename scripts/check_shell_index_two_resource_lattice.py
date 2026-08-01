#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

INCIDENCE = (
    (1, 1, 0),
    (0, 1, 1),
    (1, 0, 1),
)


def determinant(matrix):
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def apply(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def inverse_image(cycle_vector):
    y1, y2, y3 = map(Fraction, cycle_vector)
    return (
        (y1 - y2 + y3) / 2,
        (y1 + y2 - y3) / 2,
        (-y1 + y2 + y3) / 2,
    )


assert determinant(INCIDENCE) == 2
unit_cycles = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
unit_preimages = tuple(inverse_image(vector) for vector in unit_cycles)
assert all(any(entry.denominator == 2 for entry in preimage) for preimage in unit_preimages)

for vector in product(range(-3, 4), repeat=3):
    preimage = inverse_image(vector)
    integral = all(entry.denominator == 1 for entry in preimage)
    assert integral == (sum(vector) % 2 == 0)
    if integral:
        integer_preimage = tuple(int(entry) for entry in preimage)
        assert apply(INCIDENCE, integer_preimage) == vector

period_actions = (5, 7, 3)
period_cycles = apply(INCIDENCE, period_actions)
assert period_cycles == (12, 10, 8)
action_buffer = (Fraction(2, 5), Fraction(0), Fraction(0))
cycle_buffer = apply(INCIDENCE, action_buffer)
assert cycle_buffer == (Fraction(2, 5), Fraction(0), Fraction(2, 5))

print({
    "incidence_matrix": INCIDENCE,
    "determinant": determinant(INCIDENCE),
    "integer_cycle_image": "vectors with even coordinate sum",
    "unit_cycle_preimages": tuple(tuple(str(entry) for entry in vector) for vector in unit_preimages),
    "unit_cycle_resources_integrally_realisable": False,
    "stored_period_action_counts": period_actions,
    "stored_period_cycle_totals": period_cycles,
    "stored_cycle_buffer": tuple(str(entry) for entry in cycle_buffer),
    "conclusion": "the identity-debt shell model and the docs/517 cycle-resource model are separated by an index-two lattice obstruction",
    "evidence_level": "exact_source_type_mismatch",
    "status": "passed",
})
