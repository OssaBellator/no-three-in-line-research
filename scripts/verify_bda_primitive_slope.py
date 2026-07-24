#!/usr/bin/env python3
"""Verify BDA3g primitive-slope factorization and residue constraints."""

from __future__ import annotations

from itertools import combinations, product
from math import gcd

Point = tuple[int, int]


def determinant(points: tuple[Point, Point, Point]) -> int:
    first, second, third = points
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (third[0] - first[0]) * (second[1] - first[1])
    )


def factor(
    points: tuple[Point, Point, Point],
) -> tuple[int, int, int, int]:
    first, second, third = points
    row_second = second[0] - first[0]
    row_third = third[0] - first[0]
    column_second = second[1] - first[1]
    column_third = third[1] - first[1]

    displacement_gcd = gcd(abs(row_second), abs(column_second))
    direction_row = row_second // displacement_gcd
    direction_column = column_second // displacement_gcd
    first_scale = displacement_gcd
    if direction_row < 0:
        direction_row = -direction_row
        direction_column = -direction_column
        first_scale = -first_scale

    assert direction_row > 0
    assert gcd(direction_row, abs(direction_column)) == 1
    assert row_third % direction_row == 0
    second_scale = row_third // direction_row
    assert column_third == second_scale * direction_column
    return (
        direction_row,
        direction_column,
        first_scale,
        second_scale,
    )


def verify_box() -> None:
    points = tuple(product(range(-3, 4), repeat=2))
    checked = 0
    for triple in combinations(points, 3):
        if len({point[0] for point in triple}) < 3:
            continue
        if len({point[1] for point in triple}) < 3:
            continue
        if determinant(triple) != 0:
            continue

        a, b, m, n = factor(triple)
        first, second, third = triple
        assert a > 0
        assert b != 0
        assert m != 0
        assert n != 0
        assert (second[0] - first[0], second[1] - first[1]) == (
            m * a,
            m * b,
        )
        assert (third[0] - first[0], third[1] - first[1]) == (
            n * a,
            n * b,
        )

        for q in range(2, 9):
            row_residues = tuple(point[0] % q for point in triple)
            column_residues = tuple(point[1] % q for point in triple)
            assert (m * a - row_residues[1] + row_residues[0]) % q == 0
            assert (n * a - row_residues[2] + row_residues[0]) % q == 0
            assert (
                m * b - column_residues[1] + column_residues[0]
            ) % q == 0
            assert (
                n * b - column_residues[2] + column_residues[0]
            ) % q == 0
        checked += 1

    assert checked > 0


def verify_parameterized() -> None:
    for a in range(1, 5):
        for b in range(-4, 5):
            if b == 0 or gcd(a, abs(b)) != 1:
                continue
            for m in range(-4, 5):
                for n in range(-4, 5):
                    if m == 0 or n == 0 or m == n:
                        continue
                    triple = ((2, -3), (2 + m * a, -3 + m * b), (
                        2 + n * a,
                        -3 + n * b,
                    ))
                    assert determinant(triple) == 0
                    assert factor(triple) == (a, b, m, n)


def main() -> None:
    verify_box()
    verify_parameterized()
    print("BDA primitive-slope factorization: verified")


if __name__ == "__main__":
    main()
