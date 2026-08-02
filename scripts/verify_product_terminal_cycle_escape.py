#!/usr/bin/env python3
"""Finite checks for PX287--PX290."""

from __future__ import annotations

import itertools
import math


def maximum_row_degree(order: int, forbidden: set[tuple[int, int]]) -> int:
    return max(
        [sum((row, column) in forbidden for column in range(order)) for row in range(order)]
        + [0]
    )


def simple_cycles(order: int, forbidden: set[tuple[int, int]]):
    cycles = set()
    for length in range(2, order + 1):
        for vertices in itertools.permutations(range(order), length):
            if min(vertices) != vertices[0]:
                continue
            if all((vertices[index], vertices[(index + 1) % length]) not in forbidden for index in range(length)):
                rotations = [vertices[shift:] + vertices[:shift] for shift in range(length)]
                cycles.add(min(rotations))
    return cycles


def principal_rematchings(order: int, forbidden: set[tuple[int, int]]):
    output = set()
    labels = range(order)
    for size in range(2, order + 1):
        for subset in itertools.combinations(labels, size):
            for image in itertools.permutations(subset):
                if any(subset[index] == image[index] for index in range(size)):
                    continue
                if all((subset[index], image[index]) not in forbidden for index in range(size)):
                    output.add(tuple(zip(subset, image)))
    return output


def has_cycle_cover(rematching: tuple[tuple[int, int], ...]) -> bool:
    domain = {row for row, _column in rematching}
    image = {column for _row, column in rematching}
    return domain == image and len(domain) == len(rematching)


def exhaustive(max_order: int = 4) -> None:
    checked = 0
    for order in range(2, max_order + 1):
        off_diagonal = [(row, column) for row in range(order) for column in range(order) if row != column]
        diagonal = {(label, label) for label in range(order)}
        for mask in range(1 << len(off_diagonal)):
            forbidden = diagonal | {
                cell for index, cell in enumerate(off_diagonal) if mask & (1 << index)
            }
            delta = maximum_row_degree(order, forbidden)
            cycles = simple_cycles(order, forbidden)
            if order > delta:
                assert cycles
            rematchings = principal_rematchings(order, forbidden)
            assert bool(rematchings) == bool(cycles)
            assert all(has_cycle_cover(rematching) for rematching in rematchings)
            checked += 1
    assert checked > 0


def check_count_bound() -> None:
    for order in range(2, 100):
        count = sum(math.prod(range(order - length + 1, order + 1)) / length for length in range(2, order + 1))
        assert count < math.e * math.factorial(order)


def main() -> None:
    exhaustive()
    check_count_bound()
    print("PX287--PX290 terminal cycle-escape checks passed")


if __name__ == "__main__":
    main()
