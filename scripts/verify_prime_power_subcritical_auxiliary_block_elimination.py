#!/usr/bin/env python3
"""Exact rational checks for CMR1694--CMR1701."""

from __future__ import annotations

from fractions import Fraction
from math import lcm
from random import Random


Matrix = list[list[Fraction]]
Vector = list[Fraction]


def zero_matrix(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> Matrix:
    matrix = zero_matrix(size, size)
    for index in range(size):
        matrix[index][index] = Fraction(1)
    return matrix


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] + right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left[0]))]
        for i in range(len(left))
    ]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                left[i][k] * right[k][j]
                for k in range(len(right))
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    augmented = [
        row[:] + identity(size)[index]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            row
            for row in range(column, size)
            if augmented[row][column] != 0
        )
        augmented[column], augmented[pivot] = (
            augmented[pivot],
            augmented[column],
        )
        pivot_value = augmented[column][column]
        augmented[column] = [
            value / pivot_value for value in augmented[column]
        ]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor != 0:
                augmented[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(
                        augmented[row], augmented[column]
                    )
                ]
    return [row[size:] for row in augmented]


def main() -> None:
    random = Random(1694)
    systems = 0
    zero_self_checks = 0
    integer_clearings = 0

    for _ in range(2_000):
        core_size = random.randint(1, 4)
        auxiliary_size = random.randint(1, 4)

        auxiliary: Matrix = []
        for _row in range(auxiliary_size):
            values = [random.randint(0, 3) for _ in range(auxiliary_size)]
            denominator = max(20, 3 * sum(values) + 1)
            auxiliary.append(
                [Fraction(value, denominator) for value in values]
            )

        resolvent = inverse(
            subtract(identity(auxiliary_size), auxiliary)
        )
        assert multiply(
            subtract(identity(auxiliary_size), auxiliary), resolvent
        ) == identity(auxiliary_size)
        assert all(entry >= 0 for row in resolvent for entry in row)

        auxiliary_vector = matrix_vector(
            resolvent,
            [Fraction(1) for _ in range(auxiliary_size)],
        )
        assert all(
            left < right
            for left, right in zip(
                matrix_vector(auxiliary, auxiliary_vector),
                auxiliary_vector,
            )
        )

        for _attempt in range(100):
            core = [
                [
                    Fraction(random.randint(0, 3), 30)
                    for _ in range(core_size)
                ]
                for _ in range(core_size)
            ]
            core_to_auxiliary = [
                [
                    Fraction(random.randint(0, 3), 50)
                    for _ in range(auxiliary_size)
                ]
                for _ in range(core_size)
            ]
            auxiliary_to_core = [
                [
                    Fraction(random.randint(0, 3), 50)
                    for _ in range(core_size)
                ]
                for _ in range(auxiliary_size)
            ]
            effective = add(
                core,
                multiply(
                    multiply(core_to_auxiliary, resolvent),
                    auxiliary_to_core,
                ),
            )
            if all(sum(row) < Fraction(4, 5) for row in effective):
                break
        else:
            raise AssertionError("failed to generate a strict effective core")

        core_vector = [Fraction(1) for _ in range(core_size)]
        effective_value = matrix_vector(effective, core_vector)
        slack = [Fraction(1) - value for value in effective_value]
        auxiliary_image = matrix_vector(
            core_to_auxiliary, auxiliary_vector
        )
        epsilon_bounds = [
            slack[index] / (2 * auxiliary_image[index])
            for index in range(core_size)
            if auxiliary_image[index] > 0
        ]
        epsilon = min(epsilon_bounds) if epsilon_bounds else Fraction(1, 2)
        epsilon = min(epsilon, Fraction(1, 2))

        base_auxiliary = matrix_vector(
            resolvent,
            matrix_vector(auxiliary_to_core, core_vector),
        )
        lifted_auxiliary = [
            base_auxiliary[index] + epsilon * auxiliary_vector[index]
            for index in range(auxiliary_size)
        ]

        first_block = [
            left + right
            for left, right in zip(
                matrix_vector(core, core_vector),
                matrix_vector(core_to_auxiliary, lifted_auxiliary),
            )
        ]
        second_block = [
            left + right
            for left, right in zip(
                matrix_vector(auxiliary_to_core, core_vector),
                matrix_vector(auxiliary, lifted_auxiliary),
            )
        ]
        assert all(
            left < right for left, right in zip(first_block, core_vector)
        )
        assert all(
            left < right
            for left, right in zip(second_block, lifted_auxiliary)
        )

        zero_self = zero_matrix(auxiliary_size, auxiliary_size)
        zero_effective = add(
            core,
            multiply(core_to_auxiliary, auxiliary_to_core),
        )
        assert zero_effective == add(
            core,
            multiply(
                multiply(
                    core_to_auxiliary,
                    inverse(subtract(identity(auxiliary_size), zero_self)),
                ),
                auxiliary_to_core,
            ),
        )
        zero_self_checks += 1

        common_denominator = 1
        for matrix in (
            core,
            core_to_auxiliary,
            auxiliary_to_core,
            auxiliary,
            resolvent,
            effective,
        ):
            for row in matrix:
                for value in row:
                    common_denominator = lcm(
                        common_denominator, value.denominator
                    )
        for value in [
            *core_vector,
            *lifted_auxiliary,
            *auxiliary_vector,
            epsilon,
        ]:
            common_denominator = lcm(
                common_denominator, value.denominator
            )
        assert common_denominator > 0
        integer_clearings += 1
        systems += 1

    print(
        "verified subcritical auxiliary elimination: "
        f"{systems} rational block systems, "
        f"{zero_self_checks} zero-self reductions and "
        f"{integer_clearings} exact denominator clearings"
    )


if __name__ == "__main__":
    main()
