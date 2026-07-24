#!/usr/bin/env python3
"""Solve a protected corner-disjoint rectangle trade bank exactly.

Input JSON contains a saturated base configuration and a list of rectangles.
Each rectangle supplies the selected diagonal in the base state and its alternate
diagonal.  The program constructs the exact rank-at-most-three CNF from all
potential collinear triples, solves it by unit-propagating DPLL, and independently
verifies any returned configuration with exact integer determinants.
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
Rectangle = tuple[str, tuple[Point, Point], tuple[Point, Point]]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: tuple[Point, ...] | set[Point]) -> bool:
    ordered = tuple(points)
    return all(determinant(*triple) != 0 for triple in combinations(ordered, 3))


def saturated(points: tuple[Point, ...] | set[Point], n: int) -> bool:
    ordered = tuple(points)
    return (
        len(ordered) == 2 * n
        and len(set(ordered)) == len(ordered)
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


def load_bank(path: Path) -> tuple[int, tuple[Point, ...], tuple[Rectangle, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("bank must be a JSON object")

    n = payload.get("n")
    raw_points = payload.get("points")
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError("invalid side length")
    if not isinstance(raw_points, list):
        raise ValueError("points must be a list")
    points = tuple(
        sorted(parse_point(raw, f"point {index}") for index, raw in enumerate(raw_points))
    )
    if not saturated(points, n):
        raise ValueError("base points are not saturated")

    raw_rectangles = payload.get("rectangles")
    if not isinstance(raw_rectangles, list) or not raw_rectangles:
        raise ValueError("rectangles must be a nonempty list")

    rectangles: list[Rectangle] = []
    used_corners: set[Point] = set()
    point_set = set(points)
    for index, raw in enumerate(raw_rectangles, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"rectangle {index}: expected an object")
        label = str(raw.get("label", f"R{index}"))
        raw_selected = raw.get("selected")
        raw_alternate = raw.get("alternate")
        if not isinstance(raw_selected, list) or not isinstance(raw_alternate, list):
            raise ValueError(f"{label}: selected and alternate must be lists")
        selected = tuple(
            sorted(
                parse_point(point, f"{label} selected {ordinal}")
                for ordinal, point in enumerate(raw_selected)
            )
        )
        alternate = tuple(
            sorted(
                parse_point(point, f"{label} alternate {ordinal}")
                for ordinal, point in enumerate(raw_alternate)
            )
        )
        if len(selected) != 2 or len(alternate) != 2:
            raise ValueError(f"{label}: each diagonal must contain two points")
        corners = set(selected + alternate)
        if len(corners) != 4:
            raise ValueError(f"{label}: rectangle needs four distinct corners")
        x_values = {x for x, _ in corners}
        y_values = {y for _, y in corners}
        expected = {(x, y) for x in x_values for y in y_values}
        if len(x_values) != 2 or len(y_values) != 2 or corners != expected:
            raise ValueError(f"{label}: cells are not the corners of one rectangle")
        if selected[0][0] == selected[1][0] or selected[0][1] == selected[1][1]:
            raise ValueError(f"{label}: selected points are not a diagonal")
        if alternate[0][0] == alternate[1][0] or alternate[0][1] == alternate[1][1]:
            raise ValueError(f"{label}: alternate points are not a diagonal")
        if not set(selected).issubset(point_set) or set(alternate).intersection(point_set):
            raise ValueError(f"{label}: base orientation does not match the point set")
        if used_corners.intersection(corners):
            raise ValueError(f"{label}: a corner overlaps another bank rectangle")
        used_corners.update(corners)
        rectangles.append((label, selected, alternate))

    return n, points, tuple(rectangles)


def construct_formula(
    points: tuple[Point, ...], rectangles: tuple[Rectangle, ...]
) -> tuple[set[Point], tuple[Clause, ...], int, dict[int, int], dict[int, int]]:
    controlled: dict[Point, tuple[int, bool]] = {}
    selected_corners: set[Point] = set()
    for variable, (_, selected, alternate) in enumerate(rectangles):
        for point in selected:
            controlled[point] = variable, False
            selected_corners.add(point)
        for point in alternate:
            controlled[point] = variable, True

    fixed = set(points).difference(selected_corners)
    universe = tuple(sorted(fixed.union(controlled)))
    clauses: set[Clause] = set()
    potential_rank_histogram: Counter[int] = Counter()
    potential_triples = 0

    for triple in combinations(universe, 3):
        if determinant(*triple) != 0:
            continue
        requirements: dict[int, bool] = {}
        possible = True
        for point in triple:
            if point in fixed:
                continue
            variable, required_value = controlled[point]
            if variable in requirements and requirements[variable] != required_value:
                possible = False
                break
            requirements[variable] = required_value
        if not possible:
            continue
        potential_triples += 1
        potential_rank_histogram[len(requirements)] += 1
        clause = tuple(
            sorted((variable, not required_value) for variable, required_value in requirements.items())
        )
        clauses.add(clause)

    distinct_rank_histogram: Counter[int] = Counter(len(clause) for clause in clauses)
    return (
        fixed,
        tuple(sorted(clauses)),
        potential_triples,
        dict(sorted(potential_rank_histogram.items())),
        dict(sorted(distinct_rank_histogram.items())),
    )


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
    n: int, points: tuple[Point, ...], rectangles: tuple[Rectangle, ...]
) -> dict[str, Any]:
    (
        fixed,
        clauses,
        potential_triples,
        potential_rank_histogram,
        distinct_rank_histogram,
    ) = construct_formula(points, rectangles)
    assignment = solve_cnf(clauses, len(rectangles))
    final_points: list[list[int]] | None = None
    assignment_object: dict[str, bool] | None = None

    if assignment is not None:
        final = set(fixed)
        for variable, (label, selected, alternate) in enumerate(rectangles):
            final.update(alternate if assignment[variable] else selected)
        if not saturated(final, n) or not no_three(final):
            raise AssertionError("solver assignment failed independent verification")
        assignment_object = {
            label: assignment[variable]
            for variable, (label, _, _) in enumerate(rectangles)
        }
        final_points = [list(point) for point in sorted(final)]

    maximum_rank = max((len(clause) for clause in clauses), default=0)
    return {
        "n": n,
        "variable_count": len(rectangles),
        "potential_triple_count": potential_triples,
        "potential_triple_rank_histogram": {
            str(rank): count for rank, count in potential_rank_histogram.items()
        },
        "distinct_clause_count": len(clauses),
        "distinct_clause_rank_histogram": {
            str(rank): count for rank, count in distinct_rank_histogram.items()
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
        n, points, rectangles = load_bank(args.bank)
        result = analyze(n, points, rectangles)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
