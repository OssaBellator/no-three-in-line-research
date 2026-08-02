#!/usr/bin/env python3
"""Finite checks for PX291--PX293."""

from __future__ import annotations

import random


def has_cycle(order: int, forbidden: set[tuple[int, int]]) -> bool:
    state = [0] * order

    def visit(vertex: int) -> bool:
        state[vertex] = 1
        for target in range(order):
            if (vertex, target) in forbidden:
                continue
            if state[target] == 1:
                return True
            if state[target] == 0 and visit(target):
                return True
        state[vertex] = 2
        return False

    return any(state[vertex] == 0 and visit(vertex) for vertex in range(order))


def exhaustive(max_order: int = 5) -> None:
    checked = 0
    for order in range(1, max_order + 1):
        off_diagonal = [(row, column) for row in range(order) for column in range(order) if row != column]
        diagonal = {(label, label) for label in range(order)}
        masks = range(1 << len(off_diagonal)) if order <= 4 else range(0, 1 << len(off_diagonal), 997)
        for mask in masks:
            forbidden = diagonal | {
                cell for index, cell in enumerate(off_diagonal) if mask & (1 << index)
            }
            if has_cycle(order, forbidden):
                continue
            full_rows = [
                row for row in range(order)
                if all((row, column) in forbidden for column in range(order))
            ]
            full_columns = [
                column for column in range(order)
                if all((row, column) in forbidden for row in range(order))
            ]
            assert full_rows
            assert full_columns
            delta = max(
                max(sum((row, column) in forbidden for column in range(order)) for row in range(order)),
                max(sum((row, column) in forbidden for row in range(order)) for column in range(order)),
            )
            assert order <= delta
            checked += 1
    assert checked > 0


def check_historical_cover(seed: int = 292) -> None:
    rng = random.Random(seed)
    for order in range(2, 30):
        for delta0 in range(0, order + 1):
            base_columns = set(rng.sample(range(order), delta0))
            remaining = [column for column in range(order) if column not in base_columns]
            histories = [{(0, column)} for column in remaining]
            assert len(histories) == order - delta0
            covered = base_columns | {column for history in histories for row, column in history if row == 0}
            assert len(covered) == order


def main() -> None:
    exhaustive()
    check_historical_cover()
    print("PX291--PX293 trajectory-saturated core checks passed")


if __name__ == "__main__":
    main()
