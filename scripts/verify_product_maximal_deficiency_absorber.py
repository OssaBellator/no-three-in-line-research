#!/usr/bin/env python3
"""Finite checks for PX284--PX286."""

from __future__ import annotations

import itertools


def maximum_degree(order: int, forbidden: set[tuple[int, int]]) -> int:
    return max(
        [sum((row, column) in forbidden for column in range(order)) for row in range(order)]
        + [sum((row, column) in forbidden for row in range(order)) for column in range(order)]
        + [0]
    )


def perfect_matching(order: int, forbidden: set[tuple[int, int]], labels=None):
    labels = tuple(range(order)) if labels is None else tuple(sorted(labels))
    for image in itertools.permutations(labels):
        if all((labels[index], image[index]) not in forbidden for index in range(len(labels))):
            return tuple(zip(labels, image))
    return None


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


def exhaustive(max_order: int = 4) -> None:
    checked = 0
    for order in range(1, max_order + 1):
        cells = [(row, column) for row in range(order) for column in range(order)]
        for mask in range(1 << (order * order)):
            forbidden = {
                cell for index, cell in enumerate(cells) if mask & (1 << index)
            }
            delta = maximum_degree(order, forbidden)
            if delta == 0 or order >= 2 * delta:
                continue
            r = 2 * delta - order
            deficiency = order - maximum_matching_size(order, forbidden)
            assert deficiency <= r
            if deficiency < r:
                assert maximum_matching_size(order, forbidden) >= order - r + 1
                continue
            hall_deficiency, rows, columns = hall_witness(order, forbidden)
            assert hall_deficiency == r
            assert len(rows) == len(columns) == delta
            assert len(rows & columns) >= r
            for deleted in itertools.combinations(rows & columns, r):
                labels = set(range(order)) - set(deleted)
                matching = perfect_matching(order, forbidden, labels)
                assert matching is not None
                assert len(matching) == order - r
                for row, column in matching:
                    assert (row in rows) != (column in columns)
            checked += 1
    assert checked > 0


def main() -> None:
    exhaustive()
    print("PX284--PX286 maximal-deficiency absorber checks passed")


if __name__ == "__main__":
    main()
