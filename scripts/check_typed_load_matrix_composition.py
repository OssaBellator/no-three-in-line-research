#!/usr/bin/env python3
"""Exact rational audit for PP3bxs--PP3bxv."""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]


def matmul(A: Matrix, B: Matrix) -> Matrix:
    return [
        [
            sum((A[i][k] * B[k][j] for k in range(len(B))), Fraction(0))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]


def kernel_compose(P: Matrix, Q: Matrix) -> Matrix:
    return matmul(P, Q)


def block_load(
    P: Matrix,
    source_types: list[list[int]],
    target_types: list[list[int]],
) -> Matrix:
    result: Matrix = []
    for source_block in source_types:
        row: list[Fraction] = []
        for target_block in target_types:
            row.append(
                max(
                    sum((P[x][y] for x in source_block), Fraction(0))
                    for y in target_block
                )
            )
        result.append(row)
    return result


def elementwise_leq(A: Matrix, B: Matrix) -> bool:
    return all(A[i][j] <= B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def row_vector_times(vector: list[Fraction], matrix: Matrix) -> list[Fraction]:
    return [
        sum((vector[i] * matrix[i][j] for i in range(len(vector))), Fraction(0))
        for j in range(len(matrix[0]))
    ]


def main() -> None:
    P: Matrix = [
        [Fraction(1, 2), Fraction(1, 2), 0, 0, 0],
        [Fraction(1, 3), 0, Fraction(2, 3), 0, 0],
        [0, Fraction(1, 4), Fraction(1, 4), Fraction(1, 2), 0],
        [0, 0, Fraction(1, 5), Fraction(2, 5), Fraction(2, 5)],
    ]
    Q: Matrix = [
        [Fraction(1, 2), Fraction(1, 2), 0],
        [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)],
        [0, Fraction(3, 4), Fraction(1, 4)],
        [Fraction(1, 5), 0, Fraction(4, 5)],
        [Fraction(2, 3), 0, Fraction(1, 3)],
    ]
    source_types = [[0, 1], [2, 3]]
    middle_types = [[0, 1], [2, 3, 4]]
    target_types = [[0], [1, 2]]

    MP = block_load(P, source_types, middle_types)
    MQ = block_load(Q, middle_types, target_types)
    PQ = kernel_compose(P, Q)
    MPQ = block_load(PQ, source_types, target_types)
    product_bound = matmul(MP, MQ)
    assert elementwise_leq(MPQ, product_bound)

    direct_load = max(
        sum((PQ[x][z] for x in range(len(PQ))), Fraction(0))
        for z in range(len(PQ[0]))
    )
    vector_bound = row_vector_times([Fraction(1), Fraction(1)], product_bound)
    assert direct_load <= max(vector_bound)

    retained: Matrix = [
        [Fraction(1, 2), Fraction(0), 0, 0, 0],
        [Fraction(1, 3), 0, Fraction(1, 3), 0, 0],
        [0, Fraction(1, 4), Fraction(0), Fraction(1, 2), 0],
        [0, 0, Fraction(1, 5), Fraction(0), Fraction(2, 5)],
    ]
    row_mass = [sum(row, Fraction(0)) for row in retained]
    p = [
        min(row_mass[x] for x in source_types[i])
        for i in range(len(source_types))
    ]
    conditioned = [
        [entry / row_mass[x] for entry in row]
        for x, row in enumerate(retained)
    ]
    M_retained = block_load(retained, source_types, middle_types)
    M_conditioned = block_load(conditioned, source_types, middle_types)
    diagonal_bound = [
        [M_retained[i][j] / p[i] for j in range(len(M_retained[0]))]
        for i in range(len(M_retained))
    ]
    assert elementwise_leq(M_conditioned, diagonal_bound)

    M: Matrix = [
        [Fraction(1, 4), Fraction(1, 8)],
        [Fraction(1, 10), Fraction(1, 3)],
    ]
    u = [Fraction(1), Fraction(5, 4)]
    rho = Fraction(1, 2)
    assert all(
        value <= rho * u[j]
        for j, value in enumerate(row_vector_times(u, M))
    )
    vector = [Fraction(1), Fraction(1)]
    for n in range(1, 9):
        vector = row_vector_times(vector, M)
        assert max(vector) <= max(u) * rho**n

    print({
        "all_checks_passed": True,
        "M_P": [[str(x) for x in row] for row in MP],
        "M_Q": [[str(x) for x in row] for row in MQ],
        "M_PQ": [[str(x) for x in row] for row in MPQ],
        "matrix_product_bound": [[str(x) for x in row] for row in product_bound],
        "conditioned_block_bound": [[str(x) for x in row] for row in diagonal_bound],
        "eight_stage_type_bound": str(max(vector)),
    })


if __name__ == "__main__":
    main()
