#!/usr/bin/env python3
"""Verify the SAS5c affine-shape formula by determinant enumeration."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def shape_histogram(values: tuple[int, ...]) -> Counter[Fraction]:
    histogram: Counter[Fraction] = Counter()
    for first, middle, last in combinations(sorted(values), 3):
        histogram[Fraction(middle - first, last - first)] += 1
    return histogram


def energy_formula(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
) -> int:
    row_shapes = shape_histogram(rows)
    column_shapes = shape_histogram(columns)
    return sum(
        multiplicity
        * (
            column_shapes[shape]
            + column_shapes[1 - shape]
        )
        for shape, multiplicity in row_shapes.items()
    )


def determinant_count(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
) -> int:
    points = tuple((row, column) for row in rows for column in columns)
    total = 0
    for first, second, third in combinations(points, 3):
        if len({first[0], second[0], third[0]}) < 3:
            continue
        if len({first[1], second[1], third[1]}) < 3:
            continue
        if (
            (second[0] - first[0]) * (third[1] - first[1])
            == (third[0] - first[0]) * (second[1] - first[1])
        ):
            total += 1
    return total


def verify() -> None:
    universe = range(7)
    for size in range(3, 6):
        subsets = tuple(combinations(universe, size))
        for rows in subsets:
            for columns in subsets:
                assert energy_formula(rows, columns) == determinant_count(
                    rows,
                    columns,
                )

        for rows in subsets:
            positive_affine = tuple(3 * value + 2 for value in rows)
            negative_affine = tuple(23 - 2 * value for value in rows)
            assert energy_formula(rows, positive_affine) >= comb(size, 3)
            assert energy_formula(rows, negative_affine) >= comb(size, 3)


def main() -> None:
    verify()
    print("sparse-block affine energy: all subset pairs passed")


if __name__ == "__main__":
    main()
