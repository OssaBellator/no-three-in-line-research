#!/usr/bin/env python3
"""Exact checks for CMR1270--CMR1277."""

from fractions import Fraction
from math import gcd
import random


def lcm(first, second):
    return abs(first * second) // gcd(first, second) if first and second else 0


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def random_certificate(size, rng):
    weight = [Fraction(rng.randint(1, 40)) for _ in range(size)]
    slack = [Fraction(rng.randint(1, 10), 10) * weight[row] for row in range(size)]
    matrix = []
    for row in range(size):
        raw = [rng.randint(0, 30) for _column in range(size)]
        weighted_raw = sum(
            Fraction(raw[column]) * weight[column]
            for column in range(size)
        )
        target = weight[row] - slack[row]
        if weighted_raw == 0:
            matrix.append([Fraction(0)] * size)
        else:
            matrix.append([
                target * Fraction(raw[column], 1) / weighted_raw
                for column in range(size)
            ])
    return matrix, weight, slack


def clear_denominators(matrix, weight, slack):
    denominator = 1
    for row in matrix:
        for entry in row:
            denominator = lcm(denominator, entry.denominator)
    for value in weight + slack:
        denominator = lcm(denominator, value.denominator)
    integer_matrix = [
        [int(denominator * entry) for entry in row]
        for row in matrix
    ]
    integer_weight = [int(denominator * value) for value in weight]
    integer_slack = [int(denominator * denominator * value) for value in slack]
    # Matrix scaling and vector scaling contribute denominator^2 on the left.
    return denominator, integer_matrix, integer_weight, integer_slack


def check_rational_and_integer_certificates():
    rng = random.Random(1270)
    checked = 0
    for size in range(1, 18):
        for _ in range(250):
            matrix, weight, slack = random_certificate(size, rng)
            image = matvec(matrix, weight)
            assert all(image[row] == weight[row] - slack[row] < weight[row] for row in range(size))

            denominator, integer_matrix, integer_weight, integer_slack = clear_denominators(
                matrix, weight, slack
            )
            integer_image = matvec(integer_matrix, integer_weight)
            right = [
                denominator * integer_weight[row] - integer_slack[row]
                for row in range(size)
            ]
            assert integer_image == right
            checked += 1
    return checked


def check_error_robustness():
    rng = random.Random(1272)
    checked = 0
    for size in range(1, 20):
        for _ in range(250):
            matrix, weight, slack = random_certificate(size, rng)
            theta = Fraction(rng.randint(0, 9), 10)
            error = []
            for row in range(size):
                raw = [rng.randint(0, 20) for _column in range(size)]
                weighted_raw = sum(
                    Fraction(raw[column]) * weight[column]
                    for column in range(size)
                )
                target = theta * slack[row]
                if weighted_raw == 0:
                    error.append([Fraction(0)] * size)
                else:
                    error.append([
                        target * Fraction(raw[column], 1) / weighted_raw
                        for column in range(size)
                    ])
            combined = [
                [matrix[row][column] + error[row][column] for column in range(size)]
                for row in range(size)
            ]
            image = matvec(combined, weight)
            assert all(
                image[row] == weight[row] - (1 - theta) * slack[row] < weight[row]
                for row in range(size)
            )
            checked += 1
    return checked


def check_constructive_block_gluing():
    rng = random.Random(1273)
    checked = 0
    for first_size in range(1, 10):
        for second_size in range(1, 10):
            for _ in range(120):
                first, first_weight, first_slack = random_certificate(first_size, rng)
                second, second_weight, second_slack = random_certificate(second_size, rng)
                cross = [
                    [Fraction(rng.randint(0, 50), 10) for _column in range(second_size)]
                    for _row in range(first_size)
                ]
                cross_image = matvec(cross, second_weight)
                ratios = [
                    cross_image[row] / first_slack[row]
                    for row in range(first_size)
                ]
                scale = max(ratios, default=Fraction(0)) + 1
                glued_weight = [scale * value for value in first_weight] + second_weight
                zero = [[Fraction(0)] * first_size for _row in range(second_size)]
                matrix = [
                    first[row] + cross[row]
                    for row in range(first_size)
                ] + [
                    zero[row] + second[row]
                    for row in range(second_size)
                ]
                image = matvec(matrix, glued_weight)
                assert all(image[row] < glued_weight[row] for row in range(len(glued_weight)))
                checked += 1
    return checked


def check_deterministic_row_selection():
    rng = random.Random(1274)
    checked = 0
    selected = 0
    for size in range(1, 30):
        weight = [Fraction(rng.randint(1, 30)) for _ in range(size)]
        for parent in range(size):
            for _ in range(300):
                rows = [
                    [Fraction(rng.randint(0, 20), 10) for _column in range(size)]
                    for _law in range(rng.randint(2, 12))
                ]
                mixing = [rng.randint(1, 30) for _law in rows]
                total = sum(mixing)
                mixed = [
                    sum(
                        Fraction(mixing[index], total) * rows[index][column]
                        for index in range(len(rows))
                    )
                    for column in range(size)
                ]
                if sum(mixed[column] * weight[column] for column in range(size)) < weight[parent]:
                    assert any(
                        sum(row[column] * weight[column] for column in range(size)) < weight[parent]
                        for row in rows
                    )
                    selected += 1
                checked += 1
    return checked, selected


def check_finite_bank_integer_rows():
    rng = random.Random(1275)
    checked = 0
    strict_rows = 0
    for class_count in range(1, 30):
        weight = [rng.randint(1, 100) for _class in range(class_count)]
        for parent in range(class_count):
            for _ in range(300):
                bank_size = rng.randint(1, 100)
                totals = [rng.randint(0, 5 * bank_size) for _class in range(class_count)]
                rational_left = sum(Fraction(totals[index], bank_size) * weight[index] for index in range(class_count))
                integer_left = sum(totals[index] * weight[index] for index in range(class_count))
                assert (rational_left < weight[parent]) == (integer_left < bank_size * weight[parent])
                if integer_left < bank_size * weight[parent]:
                    strict_rows += 1
                checked += 1
    return checked, strict_rows


def check_coarse_class_lifting():
    rng = random.Random(1276)
    checked = 0
    for coarse_count in range(1, 20):
        for _ in range(250):
            matrix, weight, _slack = random_certificate(coarse_count, rng)
            exact_types = [rng.randrange(coarse_count) for _ in range(rng.randint(coarse_count, 8 * coarse_count))]
            for parent_type in set(exact_types):
                coarse_image = sum(matrix[parent_type][target] * weight[target] for target in range(coarse_count))
                exact_upper = [Fraction(0)] * coarse_count
                for target in range(coarse_count):
                    exact_upper[target] = matrix[parent_type][target] * Fraction(rng.randint(0, 10), 10)
                exact_image = sum(exact_upper[target] * weight[target] for target in range(coarse_count))
                assert exact_image <= coarse_image < weight[parent_type]
                checked += 1
    return checked


def main():
    deterministic = check_deterministic_row_selection()
    finite_rows = check_finite_bank_integer_rows()
    print(
        "verified rational spectral certificates:",
        check_rational_and_integer_certificates(),
        "rational/integer systems,",
        check_error_robustness(),
        "robust perturbations,",
        check_constructive_block_gluing(),
        "block gluings,",
        deterministic[0],
        "policy mixtures with",
        deterministic[1],
        "deterministic selections,",
        finite_rows[0],
        "finite-bank rows with",
        finite_rows[1],
        "strict certificates, and",
        check_coarse_class_lifting(),
        "coarse lifts",
    )


if __name__ == "__main__":
    main()
