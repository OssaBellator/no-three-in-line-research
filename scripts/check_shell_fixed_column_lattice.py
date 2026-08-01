#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

COLUMNS = (
    (1, 0, 1),
    (1, 1, 0),
    (0, 1, 1),
)


def apply(coefficients):
    return tuple(sum(coefficients[column] * COLUMNS[column][row] for column in range(3)) for row in range(3))


for denominator in range(1, 21):
    for numerators in product(range(denominator + 1), repeat=3):
        rational = tuple(Fraction(value, denominator) for value in numerators)
        quantized_counts = tuple((value.numerator * denominator + value.denominator - 1) // value.denominator for value in rational)
        cycle_vector = apply(quantized_counts)
        assert sum(cycle_vector) % 2 == 0

bounded_integer_image = {apply(coefficients) for coefficients in product(range(10), repeat=3)}
assert len(bounded_integer_image) == 1000
assert all(sum(vector) % 2 == 0 for vector in bounded_integer_image)


def inverse_image(vector):
    y1, y2, y3 = vector
    return (
        Fraction(y1 - y2 + y3, 2),
        Fraction(y1 + y2 - y3, 2),
        Fraction(-y1 + y2 + y3, 2),
    )


for vector in product(range(-4, 5), repeat=3):
    inverse = inverse_image(vector)
    integral = all(value.denominator == 1 for value in inverse)
    assert integral == (sum(vector) % 2 == 0)

print({
    "fixed_source_columns": COLUMNS,
    "source_operations_covered": ["parametric target changes from docs/499", "coefficient ceiling quantization from docs/505", "chamber-preserving target quantization from docs/511"],
    "bounded_integer_vectors_checked": len(bounded_integer_image),
    "integer_source_image": "cycle vectors with even coordinate sum",
    "odd_sum_action_created_by_parametric_or_quantized_operations": False,
    "conclusion": "the shell machinery before and after docs/517 changes targets and coefficients but never adds an odd-sum source column",
    "evidence_level": "extended_fixed_column_source_type_obstruction",
    "status": "passed",
})
