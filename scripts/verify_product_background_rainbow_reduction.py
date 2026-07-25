#!/usr/bin/env python3
"""Verify PX191--PX192 background-anchor rainbow reduction."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import gcd
from random import Random

Point = tuple[int, int]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def projective_direction(delta_row: int, delta_column: int) -> tuple[int, int]:
    common = gcd(abs(delta_row), abs(delta_column))
    assert common > 0
    delta_row //= common
    delta_column //= common
    if delta_row < 0 or (delta_row == 0 and delta_column < 0):
        delta_row = -delta_row
        delta_column = -delta_column
    return delta_row, delta_column


def anchor_color(anchor: Point, cell: Point):
    # Axis lines through the anchor can never contain two cells of one perfect
    # matching, because that would repeat a row or column. Give incident edges
    # private colors so the full bipartite coloring is proper.
    if cell[0] == anchor[0]:
        return ("row-axis", cell[1])
    if cell[1] == anchor[1]:
        return ("column-axis", cell[0])
    return ("direction",) + projective_direction(
        cell[0] - anchor[0], cell[1] - anchor[1]
    )


def verify_proper_coloring(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    anchor: Point,
) -> None:
    for row in rows:
        colors = [anchor_color(anchor, (row, column)) for column in columns]
        assert len(colors) == len(set(colors))
    for column in columns:
        colors = [anchor_color(anchor, (row, column)) for row in rows]
        assert len(colors) == len(set(colors))


def matching_cells(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    permutation: tuple[int, ...],
) -> tuple[Point, ...]:
    return tuple(
        (rows[index], columns[permutation[index]])
        for index in range(len(rows))
    )


def geometric_pair_collateral(
    cells: tuple[Point, ...],
    background: tuple[Point, ...],
) -> int:
    return sum(
        collinear(anchor, first, second)
        for anchor in background
        for first, second in combinations(cells, 2)
    )


def color_collision_collateral(
    cells: tuple[Point, ...],
    background: tuple[Point, ...],
) -> int:
    total = 0
    for anchor in background:
        counts = Counter(anchor_color(anchor, cell) for cell in cells)
        total += sum(value * (value - 1) // 2 for value in counts.values())
    return total


def verify_random_instances() -> None:
    random = Random(20260725)
    for size in range(3, 9):
        for _ in range(100):
            rows = tuple(sorted(random.sample(range(4 * size), size)))
            columns = tuple(sorted(random.sample(range(4 * size), size)))
            grid = {(row, column) for row in rows for column in columns}
            background = []
            while len(background) < 2 * size:
                point = (
                    random.randrange(4 * size),
                    random.randrange(4 * size),
                )
                if point in grid or point in background:
                    continue
                background.append(point)
            background_tuple = tuple(background)
            for anchor in background_tuple:
                verify_proper_coloring(rows, columns, anchor)

            order = list(range(size))
            random.shuffle(order)
            cells = matching_cells(rows, columns, tuple(order))
            geometric = geometric_pair_collateral(cells, background_tuple)
            colored = color_collision_collateral(cells, background_tuple)
            assert geometric == colored
    print("random background-anchor rainbow reductions verified")


def verify_complete_small_matching_space() -> None:
    rows = (0, 2, 5, 9)
    columns = (1, 4, 8, 13)
    background = ((3, 3), (6, 7), (10, 2), (1, 11))
    best = None
    best_permutation = None
    for order in permutations(range(4)):
        cells = matching_cells(rows, columns, order)
        value = geometric_pair_collateral(cells, background)
        assert value == color_collision_collateral(cells, background)
        if best is None or value < best:
            best = value
            best_permutation = order
    assert best is not None and best_permutation is not None
    print(
        f"complete order-four space: minimum pair collateral={best}, "
        f"permutation={best_permutation}"
    )


def main() -> None:
    verify_random_instances()
    verify_complete_small_matching_space()
    print("PX191--PX192 verified")


if __name__ == "__main__":
    main()
