#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import floor

P = (
    (Fraction(5, 12), Fraction(1, 4), Fraction(1, 6), Fraction(1, 6)),
    (Fraction(1, 3), Fraction(1, 6), Fraction(1, 4), Fraction(1, 4)),
    (Fraction(1, 4), Fraction(1, 3), Fraction(1, 3), Fraction(1, 12)),
)
M = 4


def margins(matrix):
    rows = tuple(sum(row) for row in matrix)
    cols = tuple(sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0])))
    return rows, cols


def main():
    row_sums, col_sums = margins(P)
    assert row_sums == (1, 1, 1)
    assert col_sums == (1, Fraction(3, 4), Fraction(3, 4), Fraction(1, 2))

    base = [[floor(M * P[i][j]) for j in range(4)] for i in range(3)]
    fractional_edges = [
        (i, j) for i in range(3) for j in range(4)
        if Fraction(base[i][j]) != M * P[i][j]
    ]
    assert len(fractional_edges) == 8
    target_rows = (M, M, M)
    target_cols = tuple(int(M * x) for x in col_sums)

    valid = []
    for bits in product((0, 1), repeat=len(fractional_edges)):
        candidate = [row[:] for row in base]
        for bit, (i, j) in zip(bits, fractional_edges):
            candidate[i][j] += bit
        rows, cols = margins(candidate)
        if rows == target_rows and cols == target_cols:
            valid.append(tuple(tuple(row) for row in candidate))

    assert len(valid) == 3
    chosen = min(valid)
    assert chosen == ((1, 1, 1, 1), (2, 0, 1, 1), (1, 2, 1, 0))
    for i in range(3):
        for j in range(4):
            assert abs(Fraction(chosen[i][j], M) - P[i][j]) < Fraction(1, M)

    row_potential = (Fraction(2), Fraction(-1), Fraction(1, 2))
    col_potential = (Fraction(0), Fraction(3, 2), Fraction(-1, 2), Fraction(1))
    residual = (
        (Fraction(1, 5), Fraction(-1, 7), Fraction(0), Fraction(1, 9)),
        (Fraction(-1, 6), Fraction(1, 8), Fraction(1, 10), Fraction(0)),
        (Fraction(0), Fraction(-1, 11), Fraction(1, 12), Fraction(-1, 13)),
    )
    coefficients = tuple(
        tuple(row_potential[i] + col_potential[j] + residual[i][j] for j in range(4))
        for i in range(3)
    )
    delta = tuple(
        tuple(Fraction(chosen[i][j], M) - P[i][j] for j in range(4))
        for i in range(3)
    )
    assert all(sum(delta[i][j] for j in range(4)) == 0 for i in range(3))
    assert all(sum(delta[i][j] for i in range(3)) == 0 for j in range(4))

    actual = abs(sum(delta[i][j] * coefficients[i][j] for i in range(3) for j in range(4)))
    residual_actual = abs(sum(delta[i][j] * residual[i][j] for i in range(3) for j in range(4)))
    assert actual == residual_actual
    bound = Fraction(1, M) * sum(abs(residual[i][j]) for i in range(3) for j in range(4))
    assert actual < bound

    print({
        "fractional_edges": len(fractional_edges),
        "valid_integral_roundings": len(valid),
        "chosen_rounding": chosen,
        "row_totals": target_rows,
        "column_totals": target_cols,
        "structured_load_error": str(actual),
        "potential_quotient_bound": str(bound),
    })


if __name__ == "__main__":
    main()
