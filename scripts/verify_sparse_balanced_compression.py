#!/usr/bin/env python3
"""Verify SAS5f exact balanced-colour compression energy."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


def falling(number: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= number - offset
    return result


def balanced_colourings(block_count: int, block_size: int) -> list[tuple[int, ...]]:
    total = block_count * block_size
    return [
        colouring
        for colouring in product(range(block_count), repeat=total)
        if all(colouring.count(label) == block_size for label in range(block_count))
    ]


def collinear_column_triples(
    rows: tuple[int, int, int],
    total: int,
) -> list[tuple[int, int, int]]:
    first_row, second_row, third_row = rows
    return [
        columns
        for columns in permutations(range(total), 3)
        if (
            (second_row - first_row) * (columns[2] - columns[0])
            == (third_row - first_row) * (columns[1] - columns[0])
        )
    ]


def triple_count(
    row_colours: tuple[int, ...],
    column_colours: tuple[int, ...],
) -> int:
    total = len(row_colours)
    return sum(
        all(column_colours[columns[index]] == row_colours[rows[index]]
            for index in range(3))
        for rows in combinations(range(total), 3)
        for columns in collinear_column_triples(rows, total)
    )


def profile_counts(row_colours: tuple[int, ...]) -> tuple[int, int, int]:
    total = len(row_colours)
    profile = [0, 0, 0]
    for rows in combinations(range(total), 3):
        labels = tuple(row_colours[row] for row in rows)
        multiplicities = sorted(
            (
                labels.count(label)
                for label in set(labels)
            ),
            reverse=True,
        )
        if multiplicities == [3]:
            index = 0
        elif multiplicities == [2, 1]:
            index = 1
        else:
            assert multiplicities == [1, 1, 1]
            index = 2
        profile[index] += len(collinear_column_triples(rows, total))
    return tuple(profile)


def verify_partition(
    row_colours: tuple[int, ...],
    block_count: int,
    block_size: int,
) -> None:
    total = block_count * block_size
    assert len(row_colours) == total
    assert all(row_colours.count(label) == block_size for label in range(block_count))
    colourings = balanced_colourings(block_count, block_size)
    values = [triple_count(row_colours, colouring) for colouring in colourings]
    same, double, distinct = profile_counts(row_colours)
    expected = Fraction(
        same * falling(block_size, 3)
        + double * falling(block_size, 2) * block_size
        + distinct * block_size**3,
        falling(total, 3),
    )
    assert Fraction(sum(values), len(values)) == expected
    assert min(values) <= expected


def verify() -> None:
    for block_count, block_size in ((1, 3), (2, 2), (2, 3), (3, 2)):
        total = block_count * block_size
        consecutive = tuple(
            row // block_size for row in range(total)
        )
        interlaced = tuple(row % block_count for row in range(total))
        verify_partition(
            consecutive,
            block_count,
            block_size,
        )
        verify_partition(
            interlaced,
            block_count,
            block_size,
        )


def main() -> None:
    verify()
    print("sparse balanced compression energy: exhaustive regressions passed")


if __name__ == "__main__":
    main()
