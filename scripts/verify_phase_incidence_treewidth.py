#!/usr/bin/env python3
"""Verify OP2f on every binary canonical two-by-three ladder."""

from __future__ import annotations

from itertools import product

Edge = tuple[int, int]
Pattern = tuple[int, int]


def vertex(row: int, column: int) -> int:
    return 2 * column + row


def ladder_edges(columns: int) -> tuple[Edge, ...]:
    vertical = tuple(
        (vertex(0, column), vertex(1, column))
        for column in range(columns)
    )
    horizontal = tuple(
        (vertex(row, column), vertex(row, column + 1))
        for column in range(columns - 1)
        for row in range(2)
    )
    return vertical + horizontal


def satisfies(
    assignment: tuple[int, ...],
    edges: tuple[Edge, ...],
    forbidden: tuple[Pattern, ...],
) -> bool:
    return all(
        (assignment[left], assignment[right]) != pattern
        for (left, right), pattern in zip(edges, forbidden)
    )


def brute_force(
    columns: int,
    edges: tuple[Edge, ...],
    forbidden: tuple[Pattern, ...],
) -> bool:
    return any(
        satisfies(assignment, edges, forbidden)
        for assignment in product(range(2), repeat=2 * columns)
    )


def transfer_solve(
    columns: int,
    edges: tuple[Edge, ...],
    forbidden: tuple[Pattern, ...],
) -> bool:
    patterns = dict(zip(edges, forbidden))
    column_states = tuple(product(range(2), repeat=2))

    feasible = {
        state
        for state in column_states
        if state != patterns[vertex(0, 0), vertex(1, 0)]
    }
    for column in range(1, columns):
        next_feasible: set[tuple[int, int]] = set()
        vertical_pattern = patterns[
            vertex(0, column),
            vertex(1, column),
        ]
        for current in column_states:
            if current == vertical_pattern:
                continue
            for previous in feasible:
                if any(
                    (previous[row], current[row])
                    == patterns[
                        vertex(row, column - 1),
                        vertex(row, column),
                    ]
                    for row in range(2)
                ):
                    continue
                next_feasible.add(current)
                break
        feasible = next_feasible
    return bool(feasible)


def verify() -> None:
    columns = 3
    edges = ladder_edges(columns)
    patterns = tuple(product(range(2), repeat=2))
    assert len(edges) == 7
    for forbidden in product(patterns, repeat=len(edges)):
        brute = brute_force(columns, edges, forbidden)
        transfer = transfer_solve(columns, edges, forbidden)
        assert transfer == brute


def main() -> None:
    verify()
    print("incidence-treewidth completion: all binary ladders passed")


if __name__ == "__main__":
    main()
