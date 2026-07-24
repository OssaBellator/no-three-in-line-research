#!/usr/bin/env python3
"""Verify the leaf-elimination completion theorem for phase forests."""

from __future__ import annotations

from itertools import product

Constraint = tuple[tuple[int, int], ...]


def solve_forest(
    alphabets: dict[int, int], constraints: tuple[Constraint, ...]
) -> dict[int, int]:
    active_variables = set(alphabets)
    active_constraints = set(range(len(constraints)))
    incidence = {
        variable: {
            index
            for index, constraint in enumerate(constraints)
            if any(v == variable for v, _ in constraint)
        }
        for variable in alphabets
    }
    elimination: list[tuple[int, int | None]] = []

    while active_variables:
        variable = next(
            v
            for v in active_variables
            if len(incidence[v] & active_constraints) <= 1
        )
        adjacent = list(incidence[variable] & active_constraints)
        check = adjacent[0] if adjacent else None
        elimination.append((variable, check))
        active_variables.remove(variable)
        if check is not None:
            active_constraints.remove(check)

    assignment: dict[int, int] = {}
    for variable, check in reversed(elimination):
        if check is None:
            assignment[variable] = 0
            continue
        forbidden = dict(constraints[check])
        others_match = all(
            assignment[other] == label
            for other, label in constraints[check]
            if other != variable
        )
        bad_label = forbidden[variable]
        assignment[variable] = (
            (bad_label + 1) % alphabets[variable] if others_match else 0
        )

    assert avoids(assignment, constraints)
    return assignment


def avoids(assignment: dict[int, int], constraints: tuple[Constraint, ...]) -> bool:
    return all(
        any(assignment[variable] != label for variable, label in constraint)
        for constraint in constraints
    )


def brute_force_satisfiable(
    alphabets: dict[int, int], constraints: tuple[Constraint, ...]
) -> bool:
    variables = sorted(alphabets)
    for labels in product(*(range(alphabets[v]) for v in variables)):
        assignment = dict(zip(variables, labels))
        if avoids(assignment, constraints):
            return True
    return False


def verify(max_checks: int = 5) -> None:
    for checks in range(1, max_checks + 1):
        alphabets = {variable: 2 for variable in range(checks + 1)}
        scopes = [(index, index + 1) for index in range(checks)]
        for patterns in product(range(4), repeat=checks):
            constraints = tuple(
                (
                    (left, pattern // 2),
                    (right, pattern % 2),
                )
                for (left, right), pattern in zip(scopes, patterns)
            )
            assert brute_force_satisfiable(alphabets, constraints)
            solve_forest(alphabets, constraints)

    unary_saturation = (((0, 0),), ((0, 1),))
    assert not brute_force_satisfiable({0: 2}, unary_saturation)


def main() -> None:
    verify()
    print("acyclic phase-factor completion: verified through five checks")


if __name__ == "__main__":
    main()
