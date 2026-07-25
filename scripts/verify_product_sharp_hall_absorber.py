#!/usr/bin/env python3
"""Finite checks for PX281--PX283."""

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
            if order != 2 * delta - 1:
                continue
            if perfect_matching(order, forbidden) is not None:
                continue
            deficiency, rows, columns = hall_witness(order, forbidden)
            assert deficiency == 1
            assert len(rows) == len(columns) == delta
            assert all((row, column) in forbidden for row in rows for column in columns)
            assert rows & columns
            for label in rows & columns:
                residual = set(range(order)) - {label}
                matching = perfect_matching(order, forbidden, residual)
                assert matching is not None
                assert len(matching) == order - 1
                for row, column in matching:
                    assert (row in rows) != (column in columns)
            checked += 1
    assert checked > 0


def main() -> None:
    exhaustive()
    print("PX281--PX283 sharp Hall-core absorber checks passed")


if __name__ == "__main__":
    main()
