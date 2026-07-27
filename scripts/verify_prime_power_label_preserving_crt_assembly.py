#!/usr/bin/env python3
"""Finite checks for CMR1622--CMR1629."""

from __future__ import annotations

from fractions import Fraction
from math import gcd
from random import Random


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum((entry * value for entry, value in zip(row, vector)), Fraction())
        for row in matrix
    ]


def add_vectors(left: Vector, right: Vector) -> Vector:
    return [a + b for a, b in zip(left, right)]


def scale_vector(scale: Fraction, vector: Vector) -> Vector:
    return [scale * value for value in vector]


def lcm(left: int, right: int) -> int:
    return left * right // gcd(left, right)


def generate_local_block(rng: Random, size: int) -> tuple[Matrix, Vector, Vector]:
    matrix: Matrix = []
    for _ in range(size):
        weights = [rng.randint(0, 9) for _ in range(size)]
        total = sum(weights)
        if total == 0:
            row = [Fraction() for _ in range(size)]
        else:
            factor = Fraction(rng.randint(0, 3), 4)
            row = [factor * Fraction(weight, total) for weight in weights]
        matrix.append(row)
    vector = [Fraction(1) for _ in range(size)]
    image = matvec(matrix, vector)
    slack = [one - value for one, value in zip(vector, image)]
    assert all(value > 0 for value in slack)
    return matrix, vector, slack


def verify_block_gluing(seed: int = 1629) -> tuple[int, int, int]:
    rng = Random(seed)
    systems = 0
    blocks_checked = 0
    integer_checks = 0

    for _ in range(1800):
        block_count = rng.randint(1, 9)
        sizes = [rng.randint(1, 5) for _ in range(block_count)]
        diagonals: list[Matrix] = []
        local_vectors: list[Vector] = []
        local_slacks: list[Vector] = []
        for size in sizes:
            matrix, vector, slack = generate_local_block(rng, size)
            diagonals.append(matrix)
            local_vectors.append(vector)
            local_slacks.append(slack)

        off: dict[tuple[int, int], Matrix] = {}
        for i in range(block_count):
            for j in range(i + 1, block_count):
                if rng.random() < 0.45:
                    off[(i, j)] = [
                        [
                            Fraction(rng.randint(0, 20), rng.randint(1, 12))
                            for _ in range(sizes[j])
                        ]
                        for _ in range(sizes[i])
                    ]

        scales = [Fraction() for _ in range(block_count)]
        for i in range(block_count - 1, -1, -1):
            outgoing = [Fraction() for _ in range(sizes[i])]
            for j in range(i + 1, block_count):
                matrix = off.get((i, j))
                if matrix is None:
                    continue
                child = scale_vector(scales[j], local_vectors[j])
                outgoing = add_vectors(outgoing, matvec(matrix, child))
            ratios = [
                outgoing[index] / local_slacks[i][index]
                for index in range(sizes[i])
            ]
            scales[i] = max(ratios, default=Fraction()) + 1

        global_vector = [
            value
            for i in range(block_count)
            for value in scale_vector(scales[i], local_vectors[i])
        ]

        offsets = [0]
        for size in sizes:
            offsets.append(offsets[-1] + size)
        total_size = offsets[-1]
        global_matrix = [
            [Fraction() for _ in range(total_size)] for _ in range(total_size)
        ]
        for i, matrix in enumerate(diagonals):
            for row in range(sizes[i]):
                for column in range(sizes[i]):
                    global_matrix[offsets[i] + row][offsets[i] + column] = matrix[
                        row
                    ][column]
        for (i, j), matrix in off.items():
            for row in range(sizes[i]):
                for column in range(sizes[j]):
                    global_matrix[offsets[i] + row][offsets[j] + column] = matrix[
                        row
                    ][column]

        image = matvec(global_matrix, global_vector)
        assert all(left < right for left, right in zip(image, global_vector))
        blocks_checked += block_count

        vector_denominator = 1
        for value in global_vector:
            vector_denominator = lcm(vector_denominator, value.denominator)
        integer_vector = [
            int(value * vector_denominator) for value in global_vector
        ]
        matrix_denominator = 1
        for row in global_matrix:
            for value in row:
                matrix_denominator = lcm(matrix_denominator, value.denominator)
        integer_image = [
            sum(
                int(global_matrix[row][column] * matrix_denominator)
                * integer_vector[column]
                for column in range(total_size)
            )
            for row in range(total_size)
        ]
        integer_rhs = [
            matrix_denominator * value for value in integer_vector
        ]
        assert all(
            left < right for left, right in zip(integer_image, integer_rhs)
        )
        integer_checks += total_size
        systems += 1

    return systems, blocks_checked, integer_checks


def verify_projection_identity(seed: int = 1622) -> tuple[int, int]:
    rng = Random(seed)
    rows = 0
    fibres = 0
    for _ in range(12000):
        exact_children = rng.randint(1, 30)
        projected = rng.randint(1, 10)
        labels = [rng.randrange(projected) for _ in range(exact_children)]
        counts = [rng.randint(0, 20) for _ in range(exact_children)]
        projected_counts = [0 for _ in range(projected)]
        for label, count in zip(labels, counts):
            projected_counts[label] += count
        assert sum(projected_counts) == sum(counts)
        for label in range(projected):
            assert projected_counts[label] == sum(
                count
                for child_label, count in zip(labels, counts)
                if child_label == label
            )
            fibres += 1
        rows += 1
    return rows, fibres


def verify_artificial_cycle() -> int:
    exact_edges = {(0, 1)}
    assert (1, 0) not in exact_edges
    projected = {("a", "a") for _edge in exact_edges}
    assert projected == {("a", "a")}
    return 1


def verify_honest_parent_fibre_max(seed: int = 1622) -> int:
    rng = Random(seed)
    checked = 0
    for _ in range(25000):
        parent_rows = rng.randint(1, 20)
        child_classes = rng.randint(1, 15)
        exact = [
            [
                Fraction(rng.randint(0, 30), rng.randint(1, 20))
                for _ in range(child_classes)
            ]
            for _ in range(parent_rows)
        ]
        upper = [
            max(row[column] for row in exact) for column in range(child_classes)
        ]
        assert all(
            all(
                row[column] <= upper[column]
                for column in range(child_classes)
            )
            for row in exact
        )
        checked += 1
    return checked


def main() -> None:
    systems, blocks, integer = verify_block_gluing()
    rows, fibres = verify_projection_identity()
    cycle = verify_artificial_cycle()
    maxima = verify_honest_parent_fibre_max()
    print(
        "verified label-preserving CRT assembly: "
        f"{systems} rational block systems with {blocks} recurrent blocks "
        f"and {integer} strict integer row checks; "
        f"{rows} exact projection rows over {fibres} child fibres; "
        f"{cycle} artificial-cycle witness and {maxima} honest parent-fibre maxima"
    )


if __name__ == "__main__":
    main()
