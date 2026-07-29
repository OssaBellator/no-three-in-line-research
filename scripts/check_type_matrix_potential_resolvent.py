#!/usr/bin/env python3
"""Exact rational audits for PP3byl--PP3byo."""

from __future__ import annotations

from fractions import Fraction

Matrix = list[list[Fraction]]
Vector = list[Fraction]


def matvec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(matrix))
    ]


def matadd(first: Matrix, second: Matrix) -> Matrix:
    return [
        [first[i][j] + second[i][j] for j in range(len(first))]
        for i in range(len(first))
    ]


def solve(matrix: Matrix, rhs: Vector) -> Vector:
    n = len(matrix)
    aug = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if aug[row][column] != 0)
        aug[column], aug[pivot] = aug[pivot], aug[column]
        scale = aug[column][column]
        aug[column] = [value / scale for value in aug[column]]
        for row in range(n):
            if row == column:
                continue
            factor = aug[row][column]
            if factor:
                aug[row] = [
                    aug[row][j] - factor * aug[column][j]
                    for j in range(n + 1)
                ]
    return [aug[i][-1] for i in range(n)]


def identity_minus(matrix: Matrix) -> Matrix:
    return [
        [Fraction(int(i == j)) - matrix[i][j] for j in range(len(matrix))]
        for i in range(len(matrix))
    ]


def componentwise_leq(first: Vector, second: Vector) -> bool:
    return all(a <= b for a, b in zip(first, second))


def add_vectors(first: Vector, second: Vector) -> Vector:
    return [a + b for a, b in zip(first, second)]


def scale_vector(scale: Fraction, vector: Vector) -> Vector:
    return [scale * value for value in vector]


def main() -> None:
    M: Matrix = [
        [Fraction(1, 4), Fraction(1, 5), Fraction(0)],
        [Fraction(1, 10), Fraction(1, 3), Fraction(1, 6)],
        [Fraction(0), Fraction(1, 8), Fraction(1, 4)],
    ]
    N: Matrix = [
        [Fraction(0), Fraction(1, 20), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1, 20)],
        [Fraction(1, 20), Fraction(0), Fraction(0)],
    ]
    ones = [Fraction(1) for _ in M]

    a = solve(identity_minus(M), ones)
    Ma = matvec(M, a)
    assert all(Ma[i] == a[i] - 1 for i in range(len(a)))
    assert all(Ma[i] < a[i] for i in range(len(a)))
    q = max(Ma[i] / a[i] for i in range(len(a)))
    assert q < 1
    assert componentwise_leq(Ma, scale_vector(q, a))

    Na = matvec(N, a)
    epsilon = max(Na[i] / a[i] for i in range(len(a)))
    assert componentwise_leq(Na, scale_vector(epsilon, a))
    assert q + epsilon < 1

    beta = Fraction(2, 3)
    b = [Fraction(1, 3), Fraction(1, 2), Fraction(1, 4)]
    assert componentwise_leq(b, scale_vector(beta, a))

    term = b[:]
    cumulative = [Fraction(0) for _ in M]
    for n in range(13):
        cumulative = add_vectors(cumulative, term)
        finite_bound = scale_vector(
            beta * (1 - q ** (n + 1)) / (1 - q),
            a,
        )
        assert componentwise_leq(cumulative, finite_bound)
        term = matvec(M, term)
    infinite_bound = scale_vector(beta / (1 - q), a)
    assert componentwise_leq(cumulative, infinite_bound)

    P = matadd(M, N)
    Pa = matvec(P, a)
    q_perturbed = q + epsilon
    assert componentwise_leq(Pa, scale_vector(q_perturbed, a))
    term = b[:]
    cumulative_perturbed = [Fraction(0) for _ in M]
    for _ in range(13):
        cumulative_perturbed = add_vectors(cumulative_perturbed, term)
        term = matvec(P, term)
    robust_bound = scale_vector(beta / (1 - q_perturbed), a)
    assert componentwise_leq(cumulative_perturbed, robust_bound)

    direct_depth_12 = b[:]
    for _ in range(12):
        direct_depth_12 = matvec(P, direct_depth_12)
    assert componentwise_leq(
        direct_depth_12,
        scale_vector(beta * q_perturbed**12, a),
    )

    print({
        "all_checks_passed": True,
        "potential": [str(value) for value in a],
        "main_contraction_q": str(q),
        "perturbation_epsilon": str(epsilon),
        "robust_q": str(q_perturbed),
        "finite_stages_checked": 12,
        "main_resolvent_bound": [str(value) for value in infinite_bound],
        "robust_resolvent_bound": [str(value) for value in robust_bound],
    })


if __name__ == "__main__":
    main()
