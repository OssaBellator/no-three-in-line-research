#!/usr/bin/env python3
"""Verify the SAS5b consecutive-block diagonal obstruction."""

from __future__ import annotations

from itertools import combinations
from math import comb

Cell = tuple[int, int]


def collinear(first: Cell, second: Cell, third: Cell) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (third[0] - first[0]) * (second[1] - first[1])
    )


def verify(blocks: int, degree: int) -> None:
    host = {
        (block * degree + row, block * degree + column)
        for block in range(blocks)
        for row in range(degree)
        for column in range(degree)
    }
    witnessed: set[tuple[Cell, Cell, Cell]] = set()
    for block in range(blocks):
        diagonal = tuple(
            (block * degree + offset, block * degree + offset)
            for offset in range(degree)
        )
        for triple in combinations(diagonal, 3):
            assert all(cell in host for cell in triple)
            assert len({cell[0] for cell in triple}) == 3
            assert len({cell[1] for cell in triple}) == 3
            assert collinear(*triple)
            witnessed.add(triple)

    assert len(witnessed) == blocks * comb(degree, 3)
    vertex_count = blocks * degree
    assert len(witnessed) == vertex_count * (degree - 1) * (degree - 2) // 6


def main() -> None:
    for blocks in range(1, 5):
        for degree in range(3, 7):
            verify(blocks, degree)
    print("sparse block geometry: consecutive diagonal obstruction verified")


if __name__ == "__main__":
    main()
