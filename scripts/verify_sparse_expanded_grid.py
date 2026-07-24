#!/usr/bin/env python3
"""Verify SAS5e greedy zero-conflict block-host embeddings."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb

Point = tuple[int, int]


def determinant(points: tuple[Point, Point, Point]) -> int:
    first, second, third = points
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        - (third[0] - first[0]) * (second[1] - first[1])
    )


def expanded_embedding(
    row_blocks: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[Point, ...]]:
    block_size = len(row_blocks[0])
    assert all(len(block) == block_size for block in row_blocks)
    assert len({row for block in row_blocks for row in block}) == (
        len(row_blocks) * block_size
    )

    column_blocks: list[list[int]] = [[] for _ in row_blocks]
    cells: list[Point] = []
    previous = -1
    schedule = [
        label
        for label in range(len(row_blocks))
        for _ in range(block_size)
    ]

    for installed_columns, label in enumerate(schedule):
        assert len(cells) == installed_columns * block_size
        forbidden: set[Fraction] = set()
        for new_row in row_blocks[label]:
            for first, second in combinations(cells, 2):
                if first[0] == second[0]:
                    continue
                candidate = Fraction(first[1]) + Fraction(
                    (second[1] - first[1]) * (new_row - first[0]),
                    second[0] - first[0],
                )
                forbidden.add(candidate)

        column = previous + 1
        while Fraction(column) in forbidden:
            column += 1
        assert (
            column - previous
            <= block_size * comb(installed_columns * block_size, 2) + 1
        )
        column_blocks[label].append(column)
        cells.extend((row, column) for row in row_blocks[label])
        previous = column

    return (
        tuple(tuple(columns) for columns in column_blocks),
        tuple(cells),
    )


def verify_partition(row_blocks: tuple[tuple[int, ...], ...]) -> None:
    block_size = len(row_blocks[0])
    total_columns = len(row_blocks) * block_size
    column_blocks, cells = expanded_embedding(row_blocks)
    flattened_columns = [
        column for block in column_blocks for column in block
    ]
    bound = (
        total_columns
        - 1
        + block_size
        * sum(
            comb(installed * block_size, 2)
            for installed in range(total_columns)
        )
    )
    assert all(len(block) == block_size for block in column_blocks)
    assert len(flattened_columns) == len(set(flattened_columns))
    assert min(flattened_columns) >= 0
    assert max(flattened_columns) <= bound

    for triple in combinations(cells, 3):
        if len({point[0] for point in triple}) < 3:
            continue
        if len({point[1] for point in triple}) < 3:
            continue
        assert determinant(triple) != 0


def verify() -> None:
    for block_count in range(1, 4):
        for block_size in range(1, 4):
            total = block_count * block_size
            consecutive = tuple(
                tuple(range(label * block_size, (label + 1) * block_size))
                for label in range(block_count)
            )
            interlaced = tuple(
                tuple(range(label, total, block_count))
                for label in range(block_count)
            )
            nonuniform_rows = tuple(index * index + 2 * index for index in range(total))
            nonuniform = tuple(
                tuple(
                    nonuniform_rows[label + block_count * offset]
                    for offset in range(block_size)
                )
                for label in range(block_count)
            )
            verify_partition(consecutive)
            verify_partition(interlaced)
            verify_partition(nonuniform)


def main() -> None:
    verify()
    print("sparse expanded-grid embedding: all small block hosts passed")


if __name__ == "__main__":
    main()
