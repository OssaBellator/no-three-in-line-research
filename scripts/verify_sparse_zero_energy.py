#!/usr/bin/env python3
"""Verify the SAS5d zero-energy companion construction."""

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


def energy(rows: tuple[int, ...], columns: tuple[int, ...]) -> int:
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


def zero_energy_companion(rows: tuple[int, ...]) -> tuple[int, ...]:
    row_shapes = shape_histogram(rows)
    forbidden_shapes = set(row_shapes)
    forbidden_shapes.update(1 - shape for shape in row_shapes)
    columns = [0, 1]
    while len(columns) < len(rows):
        forbidden_values = {
            Fraction(first)
            + Fraction(second - first, 1) / shape
            for first, second in combinations(columns, 2)
            for shape in forbidden_shapes
        }
        candidate = columns[-1] + 1
        while Fraction(candidate) in forbidden_values:
            candidate += 1
        columns.append(candidate)
    return tuple(columns)


def verify() -> None:
    universe = range(8)
    for size in range(3, 7):
        for rows in combinations(universe, size):
            columns = zero_energy_companion(rows)
            shapes = shape_histogram(rows)
            symmetric_support = set(shapes)
            symmetric_support.update(1 - shape for shape in shapes)
            bound = (
                size
                - 1
                + len(symmetric_support) * comb(size, 3)
            )
            assert len(columns) == size
            assert tuple(sorted(columns)) == columns
            assert len(set(columns)) == size
            assert columns[-1] <= bound
            assert columns[-1] <= (
                size - 1 + 2 * comb(size, 3) ** 2
            )
            assert energy(rows, columns) == 0


def main() -> None:
    verify()
    print("sparse zero-energy companions: all small row sets passed")


if __name__ == "__main__":
    main()
