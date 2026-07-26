#!/usr/bin/env python3
"""Finite checks for CMR1262--CMR1269."""

from fractions import Fraction
import random


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def identity_minus(matrix):
    size = len(matrix)
    return [
        [
            (Fraction(1) if row == column else Fraction(0)) - matrix[row][column]
            for column in range(size)
        ]
        for row in range(size)
    ]


def solve_linear(matrix, right):
    size = len(matrix)
    augmented = [list(row) + [right[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(row for row in range(column, size) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [value / scale for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(augmented[row], augmented[column])
                ]
    return [augmented[row][-1] for row in range(size)]


def row_sum_bound(matrix, weight):
    values = matvec(matrix, weight)
    return max(values[index] / weight[index] for index in range(len(weight)))


def random_subcritical_matrix(size, rng):
    matrix = []
    for _row in range(size):
        raw = [rng.randint(0, 25) for _column in range(size)]
        denominator = max(1, sum(raw))
        scale = Fraction(rng.randint(0, 8), 10)
        matrix.append([scale * Fraction(value, denominator) for value in raw])
    return matrix


def check_neumann_weight_certificate():
    rng = random.Random(1264)
    checked = 0
    for size in range(1, 13):
        for _ in range(300):
            matrix = random_subcritical_matrix(size, rng)
            vector = solve_linear(identity_minus(matrix), [Fraction(1)] * size)
            assert all(value > 0 for value in vector)
            image = matvec(matrix, vector)
            assert all(image[index] == vector[index] - 1 for index in range(size))
            assert row_sum_bound(matrix, vector) < 1
            checked += 1
    return checked


def check_direct_subinvariant_construction():
    rng = random.Random(1263)
    checked = 0
    descent_rows = 0
    for size in range(1, 20):
        for _ in range(250):
            weight = [Fraction(rng.randint(1, 30)) for _index in range(size)]
            alpha = Fraction(rng.randint(0, 9), 10)
            matrix = []
            for row in range(size):
                coefficients = [rng.randint(0, 20) for _column in range(size)]
                weighted_raw = sum(
                    Fraction(coefficient) * weight[column]
                    for column, coefficient in enumerate(coefficients)
                )
                if weighted_raw == 0:
                    matrix.append([Fraction(0)] * size)
                    continue
                target = alpha * weight[row]
                matrix.append([
                    target * Fraction(coefficient, 1) / weighted_raw
                    for coefficient in coefficients
                ])
            image = matvec(matrix, weight)
            assert all(image[index] <= alpha * weight[index] for index in range(size))
            assert all(image[index] < weight[index] for index in range(size))
            descent_rows += size
            checked += 1
    return checked, descent_rows


def check_upper_matrix_domination():
    rng = random.Random(1265)
    checked = 0
    for size in range(1, 16):
        for _ in range(250):
            upper = random_subcritical_matrix(size, rng)
            lower = [
                [entry * Fraction(rng.randint(0, 10), 10) for entry in row]
                for row in upper
            ]
            vector = solve_linear(identity_minus(upper), [Fraction(1)] * size)
            upper_image = matvec(upper, vector)
            lower_image = matvec(lower, vector)
            assert all(lower_image[index] <= upper_image[index] < vector[index] for index in range(size))
            checked += 1
    return checked


def check_row_policy_mixtures():
    rng = random.Random(1266)
    checked = 0
    for size in range(1, 14):
        for _ in range(300):
            weight = [Fraction(rng.randint(1, 20)) for _index in range(size)]
            policy_rows = []
            for row in range(size):
                choices = []
                for _choice in range(rng.randint(2, 7)):
                    raw = [rng.randint(0, 15) for _column in range(size)]
                    weighted = sum(Fraction(raw[column]) * weight[column] for column in range(size))
                    target = Fraction(rng.randint(0, 8), 10) * weight[row]
                    if weighted == 0:
                        choices.append([Fraction(0)] * size)
                    else:
                        choices.append([
                            target * Fraction(raw[column], 1) / weighted
                            for column in range(size)
                        ])
                mixing_raw = [rng.randint(1, 20) for _choice in choices]
                mixing_total = sum(mixing_raw)
                mixed = [
                    sum(
                        Fraction(mixing_raw[index], mixing_total) * choices[index][column]
                        for index in range(len(choices))
                    )
                    for column in range(size)
                ]
                policy_rows.append(mixed)
            image = matvec(policy_rows, weight)
            assert all(image[row] < weight[row] for row in range(size))
            checked += 1
    return checked


def check_block_triangular_gluing():
    rng = random.Random(1268)
    checked = 0
    for first_size in range(1, 8):
        for second_size in range(1, 8):
            for _ in range(160):
                first = random_subcritical_matrix(first_size, rng)
                second = random_subcritical_matrix(second_size, rng)
                cross = [
                    [Fraction(rng.randint(0, 30), 10) for _column in range(second_size)]
                    for _row in range(first_size)
                ]
                zero = [[Fraction(0)] * first_size for _row in range(second_size)]
                matrix = [
                    first[row] + cross[row]
                    for row in range(first_size)
                ] + [
                    zero[row] + second[row]
                    for row in range(second_size)
                ]

                first_weight = solve_linear(identity_minus(first), [Fraction(1)] * first_size)
                second_weight = solve_linear(identity_minus(second), [Fraction(1)] * second_size)
                cross_image = matvec(cross, second_weight)
                scale = max(cross_image, default=Fraction(0)) + 1
                glued = [scale * value for value in first_weight] + second_weight
                image = matvec(matrix, glued)
                assert all(image[index] < glued[index] for index in range(len(glued)))
                checked += 1
    return checked


def check_weighted_credit_descent():
    rng = random.Random(1262)
    checked = 0
    improving_responses = 0
    for class_count in range(1, 30):
        for _ in range(250):
            weight = [Fraction(rng.randint(1, 30)) for _index in range(class_count)]
            parent = rng.randrange(class_count)
            offspring_samples = []
            for _sample in range(rng.randint(2, 20)):
                offspring = [rng.randint(0, 4) for _class in range(class_count)]
                offspring_samples.append(offspring)
            weighted = [
                sum(Fraction(offspring[index]) * weight[index] for index in range(class_count))
                - weight[parent]
                for offspring in offspring_samples
            ]
            average = sum(weighted) / len(weighted)
            if average < 0:
                assert any(value < 0 for value in weighted)
                improving_responses += 1
            checked += 1
    return checked, improving_responses


def main():
    direct = check_direct_subinvariant_construction()
    descent = check_weighted_credit_descent()
    print(
        "verified collateral reproduction matrices:",
        check_neumann_weight_certificate(),
        "Neumann certificates,",
        direct[0],
        "direct systems over",
        direct[1],
        "descent rows,",
        check_upper_matrix_domination(),
        "upper-matrix systems,",
        check_row_policy_mixtures(),
        "row-policy mixtures,",
        check_block_triangular_gluing(),
        "block-triangular gluings, and",
        descent[0],
        "credit policies with",
        descent[1],
        "negative-average certificates",
    )


if __name__ == "__main__":
    main()
