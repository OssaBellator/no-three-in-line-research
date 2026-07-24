#!/usr/bin/env python3
"""Verify a deletion-minimal line core for one unmodified 2 x 5 host.

The exact degree-two constraints are kept fixed. Thirty-five explicit
collinearity clauses suffice for unsatisfiability, and deleting any one of
those line clauses makes the formula satisfiable.
"""
from __future__ import annotations

from itertools import combinations

Point = tuple[int, int]
Clause = tuple[int, ...]

OUTER = ((0, 1), (1, 0))
INNER = ((0, 1, 3, 4, 2), (2, 0, 4, 1, 3))
CORE_LINES: tuple[tuple[Point, Point, Point], ...] = (
    ((0, 0), (1, 3), (2, 6)),
    ((0, 0), (2, 6), (3, 9)),
    ((0, 0), (3, 3), (4, 4)),
    ((0, 0), (3, 3), (5, 5)),
    ((0, 0), (4, 4), (7, 7)),
    ((0, 1), (1, 2), (8, 9)),
    ((0, 4), (3, 2), (6, 0)),
    ((0, 4), (3, 3), (6, 2)),
    ((0, 5), (2, 7), (3, 8)),
    ((0, 5), (3, 2), (5, 0)),
    ((1, 1), (3, 3), (5, 5)),
    ((1, 2), (3, 3), (5, 4)),
    ((1, 3), (2, 6), (3, 9)),
    ((1, 3), (7, 6), (9, 7)),
    ((2, 6), (4, 4), (6, 2)),
    ((2, 6), (4, 5), (8, 3)),
    ((2, 6), (5, 4), (8, 2)),
    ((2, 7), (4, 5), (5, 4)),
    ((2, 7), (5, 4), (6, 3)),
    ((2, 7), (5, 5), (8, 3)),
    ((2, 8), (4, 5), (6, 2)),
    ((2, 8), (4, 6), (8, 2)),
    ((2, 9), (4, 7), (8, 3)),
    ((3, 2), (5, 4), (7, 6)),
    ((3, 2), (6, 3), (9, 4)),
    ((3, 3), (4, 4), (8, 8)),
    ((3, 3), (5, 1), (6, 0)),
    ((3, 3), (5, 5), (8, 8)),
    ((3, 8), (7, 6), (9, 5)),
    ((4, 4), (6, 3), (8, 2)),
    ((4, 4), (7, 7), (8, 8)),
    ((4, 6), (5, 4), (6, 2)),
    ((5, 0), (6, 1), (9, 4)),
    ((5, 0), (7, 6), (8, 9)),
    ((7, 9), (8, 8), (9, 7)),
)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def product_host() -> tuple[Point, ...]:
    cells = {
        (5 * i + u, 2 * INNER[s][u] + OUTER[r][i])
        for r in (0, 1)
        for s in (0, 1)
        for i in range(2)
        for u in range(5)
    }
    assert len(cells) == 40
    return tuple(sorted(cells))


def exact_degree_two_clauses(host: tuple[Point, ...]) -> tuple[Clause, ...]:
    variable = {cell: index + 1 for index, cell in enumerate(host)}
    clauses: list[Clause] = []
    for coordinate in (0, 1):
        for value in range(10):
            incident = [
                variable[cell]
                for cell in host
                if cell[coordinate] == value
            ]
            assert len(incident) == 4
            for triple in combinations(incident, 3):
                clauses.append(tuple(triple))
                clauses.append(tuple(-literal for literal in triple))
    assert len(clauses) == 160
    return tuple(clauses)


def line_clauses(
    host: tuple[Point, ...],
    lines: tuple[tuple[Point, Point, Point], ...],
) -> tuple[Clause, ...]:
    variable = {cell: index + 1 for index, cell in enumerate(host)}
    clauses: list[Clause] = []
    for triple in lines:
        assert all(cell in variable for cell in triple)
        assert determinant(*triple) == 0
        clauses.append(tuple(-variable[cell] for cell in triple))
    return tuple(clauses)


def satisfiable(clauses: tuple[Clause, ...], variable_count: int) -> bool:
    occurrence = [0] * (variable_count + 1)
    for clause in clauses:
        for literal in clause:
            occurrence[abs(literal)] += 1

    def search(assignment: list[int]) -> bool:
        while True:
            changed = False
            for clause in clauses:
                unresolved: list[int] = []
                clause_true = False
                for literal in clause:
                    value = assignment[abs(literal)]
                    if value == 0:
                        unresolved.append(literal)
                    elif (value == 1) == (literal > 0):
                        clause_true = True
                        break
                if clause_true:
                    continue
                if not unresolved:
                    return False
                if len(unresolved) == 1:
                    literal = unresolved[0]
                    variable = abs(literal)
                    required = 1 if literal > 0 else -1
                    if assignment[variable] not in (0, required):
                        return False
                    if assignment[variable] == 0:
                        assignment[variable] = required
                        changed = True
            if not changed:
                break

        if all(assignment[variable] != 0 for variable in range(1, variable_count + 1)):
            return True

        best_variable = 0
        best_key = (10, 0)
        for clause in clauses:
            if any(
                assignment[abs(literal)]
                and (assignment[abs(literal)] == 1) == (literal > 0)
                for literal in clause
            ):
                continue
            unresolved = [
                abs(literal)
                for literal in clause
                if assignment[abs(literal)] == 0
            ]
            if unresolved:
                candidate = max(unresolved, key=lambda item: occurrence[item])
                key = (len(unresolved), -occurrence[candidate])
                if key < best_key:
                    best_key = key
                    best_variable = candidate
        assert best_variable

        for value in (1, -1):
            next_assignment = assignment.copy()
            next_assignment[best_variable] = value
            if search(next_assignment):
                return True
        return False

    return search([0] * (variable_count + 1))


def main() -> None:
    host = product_host()
    degree = exact_degree_two_clauses(host)
    core = line_clauses(host, CORE_LINES)
    assert len(core) == 35
    formula = degree + core
    assert not satisfiable(formula, len(host))

    for omitted in range(len(core)):
        reduced = degree + core[:omitted] + core[omitted + 1 :]
        assert satisfiable(reduced, len(host)), omitted

    print(
        "canonical 2x5 cf core verified: "
        "160 degree clauses + 35 deletion-minimal line clauses"
    )


if __name__ == "__main__":
    main()
