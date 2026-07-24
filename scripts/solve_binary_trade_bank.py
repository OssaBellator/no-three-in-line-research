#!/usr/bin/env python3
"""Solve an equal-margin binary local-trade bank exactly.

Input JSON supplies fixed points and binary variables with state0/state1 point
sets.  Variable supports must be disjoint and the two states of each variable
must have identical row and column incidence vectors.  The program constructs
the exact rank-at-most-three CNF from all potentially selected collinear triples,
solves it by unit-propagating DPLL, and independently verifies any solution.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Literal = tuple[int, bool]
Clause = tuple[Literal, ...]
Variable = tuple[str, frozenset[Point], frozenset[Point]]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: set[Point] | tuple[Point, ...]) -> bool:
    ordered = tuple(points)
    return all(determinant(*triple) != 0 for triple in combinations(ordered, 3))


def saturated(points: set[Point] | tuple[Point, ...], n: int) -> bool:
    ordered = tuple(points)
    return (
        len(ordered) == 2 * n
        and len(set(ordered)) == len(ordered)
        and all(1 <= x <= n and 1 <= y <= n for x, y in ordered)
        and all(sum(x == index for x, _ in ordered) == 2 for index in range(1, n + 1))
        and all(sum(y == index for _, y in ordered) == 2 for index in range(1, n + 1))
    )


def parse_point(raw: Any, label: str) -> Point:
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{label}: malformed point")
    x, y = raw
    if (
        isinstance(x, bool)
        or isinstance(y, bool)
        or not isinstance(x, int)
        or not isinstance(y, int)
    ):
        raise ValueError(f"{label}: nonintegral point")
    return x, y


def incidence_vector(
    state: frozenset[Point], n: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    columns: Counter[int] = Counter(x for x, _ in state)
    rows: Counter[int] = Counter(y for _, y in state)
    return (
        tuple(columns[index] for index in range(1, n + 1)),
        tuple(rows[index] for index in range(1, n + 1)),
    )


def load_bank(path: Path) -> tuple[int, set[Point], tuple[Variable, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("bank must be a JSON object")

    n = payload.get("n")
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError("invalid side length")

    raw_fixed = payload.get("fixed")
    if not isinstance(raw_fixed, list):
        raise ValueError("fixed must be a list")
    fixed = tuple(
        sorted(parse_point(raw, f"fixed point {index}") for index, raw in enumerate(raw_fixed))
    )
    if len(set(fixed)) != len(fixed):
        raise ValueError("duplicate fixed point")
    if any(not (1 <= x <= n and 1 <= y <= n) for x, y in fixed):
        raise ValueError("fixed point outside the grid")

    raw_variables = payload.get("variables")
    if not isinstance(raw_variables, list) or not raw_variables:
        raise ValueError("variables must be a nonempty list")

    used = set(fixed)
    labels: set[str] = set()
    variables: list[Variable] = []
    for index, raw in enumerate(raw_variables, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"variable {index}: expected an object")
        label = str(raw.get("label", f"V{index}"))
        if label in labels:
            raise ValueError(f"duplicate variable label: {label}")
        labels.add(label)

        raw_state_zero = raw.get("state0")
        raw_state_one = raw.get("state1")
        if not isinstance(raw_state_zero, list) or not isinstance(raw_state_one, list):
            raise ValueError(f"{label}: state0 and state1 must be lists")
        state_zero = frozenset(
            parse_point(point, f"{label} state0 point {ordinal}")
            for ordinal, point in enumerate(raw_state_zero)
        )
        state_one = frozenset(
            parse_point(point, f"{label} state1 point {ordinal}")
            for ordinal, point in enumerate(raw_state_one)
        )
        if not state_zero or not state_one:
            raise ValueError(f"{label}: both states must be nonempty")
        support = state_zero.union(state_one)
        if any(not (1 <= x <= n and 1 <= y <= n) for x, y in support):
            raise ValueError(f"{label}: point outside the grid")
        if used.intersection(support):
            raise ValueError(f"{label}: support overlaps fixed points or another variable")
        if incidence_vector(state_zero, n) != incidence_vector(state_one, n):
            raise ValueError(f"{label}: states have different row or column margins")
        used.update(support)
        variables.append((label, state_zero, state_one))

    reference = set(fixed)
    for _, state_zero, _ in variables:
        reference.update(state_zero)
    if not saturated(reference, n):
        raise ValueError("the all-zero reference assignment is not saturated")

    return n, set(fixed), tuple(variables)


def construct_formula(
    fixed: set[Point], variables: tuple[Variable, ...]
) -> tuple[tuple[Clause, ...], dict[int, int]]:
    owner: dict[Point, int] = {}
    allowed_values: dict[Point, frozenset[bool]] = {}
    for variable, (_, state_zero, state_one) in enumerate(variables):
        for point in state_zero.union(state_one):
            owner[point] = variable
            values: set[bool] = set()
            if point in state_zero:
                values.add(False)
            if point in state_one:
                values.add(True)
            allowed_values[point] = frozenset(values)

    universe = tuple(sorted(fixed.union(owner)))
    clauses: set[Clause] = set()
    potential_rank_histogram: Counter[int] = Counter()

    for triple in combinations(universe, 3):
        if determinant(*triple) != 0:
            continue
        requirements: dict[int, frozenset[bool]] = {}
        possible = True
        for point in triple:
            if point in fixed:
                continue
            variable = owner[point]
            current = requirements.get(variable, frozenset((False, True)))
            current = current.intersection(allowed_values[point])
            if not current:
                possible = False
                break
            requirements[variable] = current
        if not possible:
            continue

        singleton_requirements = {
            variable: next(iter(values))
            for variable, values in requirements.items()
            if len(values) == 1
        }
        clause = tuple(
            sorted(
                (variable, not required_value)
                for variable, required_value in singleton_requirements.items()
            )
        )
        clauses.add(clause)
        potential_rank_histogram[len(clause)] += 1

    return tuple(sorted(clauses)), dict(sorted(potential_rank_histogram.items()))


def clause_status(
    clause: Clause, assignment: list[bool | None]
) -> tuple[bool, list[Literal]]:
    unresolved: list[Literal] = []
    for variable, satisfying_value in clause:
        value = assignment[variable]
        if value is None:
            unresolved.append((variable, satisfying_value))
        elif value == satisfying_value:
            return True, []
    return False, unresolved


def solve_cnf(clauses: tuple[Clause, ...], variable_count: int) -> list[bool] | None:
    def recurse(assignment: list[bool | None]) -> list[bool] | None:
        assignment = assignment.copy()
        while True:
            changed = False
            for clause in clauses:
                satisfied, unresolved = clause_status(clause, assignment)
                if satisfied:
                    continue
                if not unresolved:
                    return None
                if len(unresolved) == 1:
                    variable, required_value = unresolved[0]
                    current = assignment[variable]
                    if current is not None and current != required_value:
                        return None
                    if current is None:
                        assignment[variable] = required_value
                        changed = True
            if not changed:
                break

        if all(value is not None for value in assignment):
            return [bool(value) for value in assignment]

        scores: Counter[int] = Counter()
        for clause in clauses:
            satisfied, unresolved = clause_status(clause, assignment)
            if not satisfied:
                for variable, _ in unresolved:
                    scores[variable] += 1
        variable = max(
            (index for index, value in enumerate(assignment) if value is None),
            key=lambda index: scores[index],
        )
        for value in (False, True):
            child = assignment.copy()
            child[variable] = value
            result = recurse(child)
            if result is not None:
                return result
        return None

    return recurse([None] * variable_count)


def analyze(
    n: int, fixed: set[Point], variables: tuple[Variable, ...]
) -> dict[str, Any]:
    clauses, potential_rank_histogram = construct_formula(fixed, variables)
    assignment = solve_cnf(clauses, len(variables))
    final_points: list[list[int]] | None = None
    assignment_object: dict[str, bool] | None = None

    if assignment is not None:
        final = set(fixed)
        for variable, (label, state_zero, state_one) in enumerate(variables):
            final.update(state_one if assignment[variable] else state_zero)
        if not saturated(final, n) or not no_three(final):
            raise AssertionError("solver assignment failed independent verification")
        assignment_object = {
            label: assignment[variable]
            for variable, (label, _, _) in enumerate(variables)
        }
        final_points = [list(point) for point in sorted(final)]

    distinct_rank_histogram: Counter[int] = Counter(len(clause) for clause in clauses)
    maximum_rank = max((len(clause) for clause in clauses), default=0)
    return {
        "n": n,
        "variable_count": len(variables),
        "distinct_clause_count": len(clauses),
        "distinct_clause_rank_histogram": {
            str(rank): count for rank, count in sorted(distinct_rank_histogram.items())
        },
        "potential_triple_rank_histogram": {
            str(rank): count for rank, count in potential_rank_histogram.items()
        },
        "maximum_clause_rank": maximum_rank,
        "is_2sat_instance": maximum_rank <= 2,
        "satisfiable": assignment is not None,
        "assignment": assignment_object,
        "final_points": final_points,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bank", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        n, fixed, variables = load_bank(args.bank)
        result = analyze(n, fixed, variables)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
