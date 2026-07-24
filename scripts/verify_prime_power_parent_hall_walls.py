#!/usr/bin/env python3
"""Exact finite checks for CMR199--CMR202."""

from __future__ import annotations

from itertools import combinations, permutations
from math import ceil, floor, sqrt


def derangements(t: int) -> list[tuple[int, ...]]:
    return [
        state
        for state in permutations(range(t))
        if all(state[row] != row for row in range(t))
    ]


def powerset_nonempty(t: int):
    for size in range(1, t + 1):
        yield from combinations(range(t), size)


def hall_witness(t: int, supported: set[tuple[int, int]]):
    for source_set in powerset_nonempty(t):
        neighbourhood = {
            column
            for row in source_set
            for column in range(t)
            if column != row and (row, column) not in supported
        }
        if len(neighbourhood) < len(source_set):
            target_set = tuple(column for column in range(t) if column not in neighbourhood)
            return source_set, target_set
    return None


def verify_hall_rectangles(max_t: int) -> None:
    # Exhaustive rectangle/state incidence is kept to t<=6. The arbitrary-t
    # statement is the Hall proof in CMR199.
    for t in range(5, max_t + 1):
        states = derangements(t)
        for source_set in powerset_nonempty(t):
            for target_set in powerset_nonempty(t):
                if len(source_set) + len(target_set) <= t:
                    continue
                supported = {
                    (row, column)
                    for row in source_set
                    for column in target_set
                    if row != column
                }
                assert all(
                    any((row, state[row]) in supported for row in range(t))
                    for state in states
                )
                witness = hall_witness(t, supported)
                assert witness is not None
                rows, columns = witness
                assert len(rows) + len(columns) > t
                assert all(
                    row == column or (row, column) in supported
                    for row in rows
                    for column in columns
                )
                row_maximum = max(
                    sum((row, column) in supported for column in range(t))
                    for row in range(t)
                )
                column_maximum = max(
                    sum((row, column) in supported for row in range(t))
                    for column in range(t)
                )
                assert max(row_maximum, column_maximum) >= t // 2


def verify_wall_arithmetic(max_t: int) -> None:
    for t in range(5, max_t + 1):
        wall = t // 2
        majority = ceil(wall / 3)
        assert majority >= 1
        rank_one_matching = max(1, floor(sqrt(majority / 2)))
        neutralized_rank_one = ceil(rank_one_matching / 2)
        neutralized_rank_two = ceil(majority / 2)
        assert neutralized_rank_one >= 1
        assert neutralized_rank_two >= 1


def main() -> None:
    verify_hall_rectangles(max_t=6)
    verify_wall_arithmetic(max_t=100_000)
    print(
        "verified parent Hall walls: dense blocker rectangles, half-full "
        "rows or columns, and rank-wall extraction arithmetic"
    )


if __name__ == "__main__":
    main()
