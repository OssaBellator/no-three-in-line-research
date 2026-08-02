#!/usr/bin/env python3
"""Verify PX193--PX195 background-rainbow transposition decoder."""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd
from random import Random

Point = tuple[int, int]
Permutation = tuple[int, ...]


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
    if cell[0] == anchor[0]:
        return ("row-axis", cell[1])
    if cell[1] == anchor[1]:
        return ("column-axis", cell[0])
    return ("direction",) + projective_direction(
        cell[0] - anchor[0], cell[1] - anchor[1]
    )


def cells_of(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    permutation: Permutation,
) -> tuple[Point, ...]:
    return tuple(
        (rows[index], columns[permutation[index]])
        for index in range(len(rows))
    )


def collision_potential(
    cells: tuple[Point, ...],
    background: tuple[Point, ...],
) -> int:
    total = 0
    for anchor in background:
        counts = Counter(anchor_color(anchor, cell) for cell in cells)
        total += sum(value * (value - 1) // 2 for value in counts.values())
    return total


def pair_weight(
    first: Point,
    second: Point,
    background: tuple[Point, ...],
) -> int:
    return sum(
        anchor_color(anchor, first) == anchor_color(anchor, second)
        for anchor in background
    )


def forbidden_union(first: Permutation, second: Permutation) -> set[tuple[int, int]]:
    size = len(first)
    return {
        (row, first[row]) for row in range(size)
    } | {
        (row, second[row]) for row in range(size)
    }


def allowed_matching(
    size: int,
    forbidden: set[tuple[int, int]],
    random: Random,
) -> Permutation:
    for _ in range(20000):
        order = list(range(size))
        random.shuffle(order)
        if all((row, order[row]) not in forbidden for row in range(size)):
            return tuple(order)
    raise AssertionError("failed to sample allowed matching")


def executable_swaps(
    permutation: Permutation,
    forbidden: set[tuple[int, int]],
):
    for first, second in combinations(range(len(permutation)), 2):
        if (first, permutation[second]) in forbidden:
            continue
        if (second, permutation[first]) in forbidden:
            continue
        yield first, second


def swap(permutation: Permutation, first: int, second: int) -> Permutation:
    updated = list(permutation)
    updated[first], updated[second] = updated[second], updated[first]
    return tuple(updated)


def verify_instance(size: int, random: Random) -> None:
    rows = tuple(sorted(random.sample(range(5 * size), size)))
    columns = tuple(sorted(random.sample(range(5 * size), size)))
    grid = {(row, column) for row in rows for column in columns}
    background = []
    while len(background) < 3 * size:
        point = (random.randrange(5 * size), random.randrange(5 * size))
        if point in grid or point in background:
            continue
        background.append(point)
    background_tuple = tuple(background)

    first = list(range(size))
    second = list(range(size))
    random.shuffle(first)
    random.shuffle(second)
    forbidden = forbidden_union(tuple(first), tuple(second))
    permutation = allowed_matching(size, forbidden, random)
    cells = cells_of(rows, columns, permutation)
    potential = collision_potential(cells, background_tuple)

    executable = tuple(executable_swaps(permutation, forbidden))
    delta_sum = 0
    two_inserted = 0
    for first_row, second_row in executable:
        updated = swap(permutation, first_row, second_row)
        new_cells = cells_of(rows, columns, updated)
        delta_sum += collision_potential(new_cells, background_tuple) - potential
        inserted_first = (rows[first_row], columns[permutation[second_row]])
        inserted_second = (rows[second_row], columns[permutation[first_row]])
        two_inserted += pair_weight(
            inserted_first, inserted_second, background_tuple
        )

    one_inserted = 0
    maximum_shadow = 0
    for row in range(size):
        for source in range(size):
            if source == row:
                continue
            cell = (rows[row], columns[permutation[source]])
            if (row, permutation[source]) in forbidden:
                continue
            shadow = sum(
                pair_weight(cell, selected, background_tuple)
                for selected in cells
                if selected[0] != cell[0] and selected[1] != cell[1]
            )
            one_inserted += shadow
            maximum_shadow = max(maximum_shadow, shadow)

    destruction_lower = 2 * max(0, size - 6) * potential
    assert delta_sum <= one_inserted + two_inserted - destruction_lower

    maximum_line_background = 0
    for first_cell, second_cell in combinations(
        [(row, column) for row in rows for column in columns], 2
    ):
        if first_cell[0] == second_cell[0] or first_cell[1] == second_cell[1]:
            continue
        maximum_line_background = max(
            maximum_line_background,
            pair_weight(first_cell, second_cell, background_tuple),
        )
    assert two_inserted <= maximum_line_background * len(executable)
    assert one_inserted <= size * (size - 1) * maximum_shadow

    if potential > 0 and all(
        collision_potential(
            cells_of(rows, columns, swap(permutation, first_row, second_row)),
            background_tuple,
        )
        >= potential
        for first_row, second_row in executable
    ):
        numerator = (
            size * (size - 1) * maximum_shadow
            + maximum_line_background * size * (size - 1) // 2
        )
        assert 2 * max(0, size - 6) * potential <= numerator


def main() -> None:
    random = Random(20260725)
    for size in range(7, 12):
        for _ in range(100):
            verify_instance(size, random)
        print(f"size={size}: 100 rainbow-decoder instances verified")
    print("PX193--PX195 verified")


if __name__ == "__main__":
    main()
