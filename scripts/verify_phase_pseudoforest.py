#!/usr/bin/env python3
"""Verify constructive completion of canonical phase pseudoforests."""

from __future__ import annotations

from itertools import product

Constraint = tuple[tuple[int, int], ...]


def avoids(assignment: dict[int, int], constraints: tuple[Constraint, ...]) -> bool:
    return all(
        any(assignment[variable] != label for variable, label in constraint)
        for constraint in constraints
    )


def is_pseudoforest(
    alphabets: dict[int, int], constraints: tuple[Constraint, ...]
) -> bool:
    nodes = [("v", variable) for variable in alphabets]
    nodes += [("c", index) for index in range(len(constraints))]
    neighbours: dict[tuple[str, int], set[tuple[str, int]]] = {
        node: set() for node in nodes
    }
    for index, constraint in enumerate(constraints):
        for variable, _ in constraint:
            neighbours[("v", variable)].add(("c", index))
            neighbours[("c", index)].add(("v", variable))

    unseen = set(nodes)
    while unseen:
        root = unseen.pop()
        stack = [root]
        component = {root}
        while stack:
            node = stack.pop()
            for other in neighbours[node]:
                if other in unseen:
                    unseen.remove(other)
                    component.add(other)
                    stack.append(other)
        edges = sum(len(neighbours[node]) for node in component) // 2
        if edges > len(component):
            return False
    return True


def solve_pseudoforest(
    alphabets: dict[int, int], constraints: tuple[Constraint, ...]
) -> dict[int, int]:
    assert all(size >= 2 for size in alphabets.values())
    assert all(len(constraint) >= 2 for constraint in constraints)
    assert is_pseudoforest(alphabets, constraints)

    active_variables = set(alphabets)
    active_constraints = set(range(len(constraints)))
    incidence = {
        variable: {
            index
            for index, constraint in enumerate(constraints)
            if any(other == variable for other, _ in constraint)
        }
        for variable in alphabets
    }
    elimination: list[tuple[int, int | None]] = []

    while True:
        leaf = next(
            (
                variable
                for variable in active_variables
                if len(incidence[variable] & active_constraints) <= 1
            ),
            None,
        )
        if leaf is None:
            break
        adjacent = list(incidence[leaf] & active_constraints)
        check = adjacent[0] if adjacent else None
        elimination.append((leaf, check))
        active_variables.remove(leaf)
        if check is not None:
            active_constraints.remove(check)

    assignment: dict[int, int] = {}
    unseen = set(active_variables)
    while unseen:
        start = next(iter(unseen))
        cycle_checks = incidence[start] & active_constraints
        assert len(cycle_checks) == 2
        closing = next(iter(cycle_checks))
        closing_labels = dict(constraints[closing])
        assignment[start] = (closing_labels[start] + 1) % alphabets[start]

        previous_check = closing
        current = start
        unseen.remove(start)
        while True:
            next_check = next(
                check
                for check in incidence[current] & active_constraints
                if check != previous_check
            )
            scope = [variable for variable, _ in constraints[next_check]]
            assert len(scope) == 2
            next_variable = scope[0] if scope[1] == current else scope[1]
            if next_variable == start:
                assert next_check == closing
                break
            forbidden = dict(constraints[next_check])
            if assignment[current] == forbidden[current]:
                assignment[next_variable] = (
                    forbidden[next_variable] + 1
                ) % alphabets[next_variable]
            else:
                assignment[next_variable] = 0
            unseen.remove(next_variable)
            previous_check = next_check
            current = next_variable

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
        assignment[variable] = (
            (forbidden[variable] + 1) % alphabets[variable]
            if others_match
            else 0
        )

    assert avoids(assignment, constraints)
    return assignment


def brute_force_satisfiable(
    alphabets: dict[int, int], constraints: tuple[Constraint, ...]
) -> bool:
    variables = sorted(alphabets)
    return any(
        avoids(dict(zip(variables, labels)), constraints)
        for labels in product(*(range(alphabets[v]) for v in variables))
    )


def verify_cycles(max_length: int = 7) -> None:
    for length in range(2, max_length + 1):
        alphabets = {variable: 2 for variable in range(length)}
        for patterns in product(range(4), repeat=length):
            constraints = tuple(
                (
                    (index, pattern // 2),
                    ((index + 1) % length, pattern % 2),
                )
                for index, pattern in enumerate(patterns)
            )
            solve_pseudoforest(alphabets, constraints)


def verify_ternary_leaf() -> None:
    alphabets = {variable: 2 for variable in range(4)}
    scopes = ((0, 1, 3), (1, 2), (2, 0))
    pattern_ranges = (range(8), range(4), range(4))
    for patterns in product(*pattern_ranges):
        constraints = tuple(
            tuple(
                (variable, (pattern >> offset) & 1)
                for offset, variable in enumerate(scope)
            )
            for scope, pattern in zip(scopes, patterns)
        )
        solve_pseudoforest(alphabets, constraints)


def verify_multiple_cycle_obstruction() -> None:
    constraints = tuple(
        ((0, left), (1, right))
        for left, right in product(range(2), repeat=2)
    )
    assert not is_pseudoforest({0: 2, 1: 2}, constraints)
    assert not brute_force_satisfiable({0: 2, 1: 2}, constraints)


def main() -> None:
    verify_cycles()
    verify_ternary_leaf()
    verify_multiple_cycle_obstruction()
    print("phase pseudoforest completion: verified through cycle length seven")


if __name__ == "__main__":
    main()
