#!/usr/bin/env python3
"""Finite checks for PX270--PX272."""

from __future__ import annotations

import itertools
import random


def maximum_degree(order: int, forbidden: set[tuple[int, int]]) -> int:
    return max(
        [sum((row, column) in forbidden for column in range(order)) for row in range(order)]
        + [sum((row, column) in forbidden for row in range(order)) for column in range(order)]
        + [0]
    )


def maximum_matching_size(order: int, forbidden: set[tuple[int, int]]) -> int:
    for size in range(order, -1, -1):
        for rows in itertools.combinations(range(order), size):
            for columns in itertools.combinations(range(order), size):
                for image in itertools.permutations(columns):
                    if all((rows[index], image[index]) not in forbidden for index in range(size)):
                        return size
    raise AssertionError("unreachable")


def hall_witness(order: int, forbidden: set[tuple[int, int]]):
    best = (-1, set(), set())
    for mask in range(1, 1 << order):
        rows = {row for row in range(order) if mask & (1 << row)}
        neighbours = {
            column
            for row in rows
            for column in range(order)
            if (row, column) not in forbidden
        }
        deficiency = len(rows) - len(neighbours)
        if deficiency > best[0]:
            best = (deficiency, rows, set(range(order)) - neighbours)
    return best


def check_graph(order: int, forbidden: set[tuple[int, int]]) -> None:
    delta = maximum_degree(order, forbidden)
    matching = maximum_matching_size(order, forbidden)
    deficiency = order - matching
    hall_deficiency, rows, columns = hall_witness(order, forbidden)
    assert hall_deficiency == deficiency

    if deficiency == 0:
        return

    assert rows and columns
    assert all((row, column) in forbidden for row in rows for column in columns)
    assert len(rows) + len(columns) == order + deficiency
    assert len(rows) <= delta
    assert len(columns) <= delta
    assert deficiency <= 2 * delta - order
    assert matching >= max(0, 2 * order - 2 * delta)

    if order == 2 * delta - 1:
        assert deficiency == 1
        assert len(rows) == len(columns) == delta
        for row in rows:
            assert sum((row, column) in forbidden for column in range(order)) == delta
        for column in columns:
            assert sum((row, column) in forbidden for row in range(order)) == delta


def exhaustive(max_order: int = 4) -> None:
    for order in range(1, max_order + 1):
        cells = [(row, column) for row in range(order) for column in range(order)]
        for mask in range(1 << (order * order)):
            forbidden = {
                cell for index, cell in enumerate(cells) if mask & (1 << index)
            }
            check_graph(order, forbidden)


def random_checks(seed: int = 270) -> None:
    rng = random.Random(seed)
    for order in range(5, 9):
        for _ in range(1000):
            forbidden = {
                (row, column)
                for row in range(order)
                for column in range(order)
                if rng.random() < 0.3
            }
            check_graph(order, forbidden)


def main() -> None:
    exhaustive()
    random_checks()
    print("PX270--PX272 terminal Hall-core checks passed")


if __name__ == "__main__":
    main()
