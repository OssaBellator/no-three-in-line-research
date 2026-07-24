#!/usr/bin/env python3
"""Solve an equal-margin finite-state local trade bank exactly.

Input JSON supplies fixed selected points and variables with two or more local
states. Variable supports must be disjoint, and every state of one variable
must have the same row and column incidence vectors. The program constructs
the exact rank-at-most-three forbidden-box CSP from all potentially selected
collinear triples, evaluates uniform first-moment and bounded-dependency LLL
criteria, solves the CSP by domain propagation and backtracking, and
independently verifies any returned configuration.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]
State = frozenset[Point]
Variable = tuple[str, tuple[State, ...]]
BoxEntry = tuple[int, tuple[int, ...]]
Box = tuple[BoxEntry, ...]


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


def incidence_vector(state: State, n: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
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
    fixed_list = [
        parse_point(raw, f"fixed point {index}") for index, raw in enumerate(raw_fixed)
    ]
    if len(set(fixed_list)) != len(fixed_list):
        raise ValueError("duplicate fixed point")
    fixed = set(fixed_list)
    if any(not (1 <= x <= n and 1 <= y <= n) for x, y in fixed):
        raise ValueError("fixed point outside the grid")

    raw_variables = payload.get("variables")
    if not isinstance(raw_variables, list) or not raw_variables:
        raise ValueError("variables must be a nonempty list")

    used = set(fixed)
    labels: set[str] = set()
    variables: list[Variable] = []
    for variable_index, raw in enumerate(raw_variables, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"variable {variable_index}: expected an object")
        label = str(raw.get("label", f"V{variable_index}"))
        if label in labels:
            raise ValueError(f"duplicate variable label: {label}")
        labels.add(label)

        raw_states = raw.get("states")
        if not isinstance(raw_states, list) or len(raw_states) < 2:
            raise ValueError(f"{label}: states must contain at least two point lists")
        states: list[State] = []
        for state_index, raw_state in enumerate(raw_states):
            if not isinstance(raw_state, list):
                raise ValueError(f"{label} state {state_index}: expected a point list")
            point_list = [
                parse_point(point, f"{label} state {state_index} point {point_index}")
                for point_index, point in enumerate(raw_state)
            ]
            if len(set(point_list)) != len(point_list):
                raise ValueError(f"{label} state {state_index}: duplicate point")
            state = frozenset(point_list)
            if any(not (1 <= x <= n and 1 <= y <= n) for x, y in state):
                raise ValueError(f"{label} state {state_index}: point outside the grid")
            states.append(state)

        reference_margin = incidence_vector(states[0], n)
        if any(incidence_vector(state, n) != reference_margin for state in states[1:]):
            raise ValueError(f"{label}: states have different row or column margins")

        support = frozenset().union(*states)
        if used.intersection(support):
            raise ValueError(f"{label}: support overlaps fixed points or another variable")
        used.update(support)
        variables.append((label, tuple(states)))

    reference = set(fixed)
    for _, states in variables:
        reference.update(states[0])
    if not saturated(reference, n):
        raise ValueError("the all-zero reference assignment is not saturated")

    return n, fixed, tuple(variables)


def construct_boxes(
    fixed: set[Point], variables: tuple[Variable, ...]
) -> tuple[tuple[Box, ...], dict[str, int]]:
    owner: dict[Point, int] = {}
    selected_states: dict[Point, frozenset[int]] = {}
    state_counts = tuple(len(states) for _, states in variables)

    for variable, (_, states) in enumerate(variables):
        support = frozenset().union(*states)
        for point in support:
            owner[point] = variable
            selected_states[point] = frozenset(
                state_index
                for state_index, state in enumerate(states)
                if point in state
            )

    universe = tuple(sorted(fixed.union(owner)))
    boxes: set[Box] = set()
    potential_collinear = 0
    impossible_by_local_state = 0
    potential_rank_histogram: Counter[int] = Counter()

    for triple in combinations(universe, 3):
        if determinant(*triple) != 0:
            continue
        potential_collinear += 1
        requirements: dict[int, frozenset[int]] = {}
        possible = True

        for point in triple:
            if point in fixed:
                continue
            variable = owner[point]
            current = requirements.get(
                variable, frozenset(range(state_counts[variable]))
            )
            current = current.intersection(selected_states[point])
            if not current:
                possible = False
                break
            requirements[variable] = current

        if not possible:
            impossible_by_local_state += 1
            continue

        box_entries: list[BoxEntry] = []
        for variable, allowed in sorted(requirements.items()):
            if len(allowed) == state_counts[variable]:
                continue
            box_entries.append((variable, tuple(sorted(allowed))))
        box = tuple(box_entries)
        boxes.add(box)
        potential_rank_histogram[len(box)] += 1

    return tuple(sorted(boxes)), {
        "candidate_collinear_triples": potential_collinear,
        "locally_impossible_triples": impossible_by_local_state,
        **{
            f"potential_rank_{rank}": count
            for rank, count in sorted(potential_rank_histogram.items())
        },
    }


def box_probability(box: Box, state_counts: tuple[int, ...]) -> Fraction:
    probability = Fraction(1, 1)
    for variable, allowed in box:
        probability *= Fraction(len(allowed), state_counts[variable])
    return probability


def dependency_data(
    boxes: tuple[Box, ...], variable_count: int
) -> tuple[int, int]:
    incident: list[set[int]] = [set() for _ in range(variable_count)]
    for box_index, box in enumerate(boxes):
        for variable, _ in box:
            incident[variable].add(box_index)

    maximum_degree = 0
    for box_index, box in enumerate(boxes):
        neighbours: set[int] = set()
        for variable, _ in box:
            neighbours.update(incident[variable])
        neighbours.discard(box_index)
        maximum_degree = max(maximum_degree, len(neighbours))

    maximum_occurrence = max((len(indices) for indices in incident), default=0)
    return maximum_degree, maximum_occurrence


def propagate(domains: list[set[int]], boxes: tuple[Box, ...]) -> bool:
    changed = True
    while changed:
        changed = False
        for box in boxes:
            if not box:
                return False

            flexible: list[tuple[int, set[int]]] = []
            satisfied = False
            for variable, raw_bad_states in box:
                bad_states = set(raw_bad_states)
                domain = domains[variable]
                bad_part = domain.intersection(bad_states)
                if not bad_part:
                    satisfied = True
                    break
                if not domain.issubset(bad_states):
                    flexible.append((variable, bad_states))

            if satisfied:
                continue
            if not flexible:
                return False
            if len(flexible) == 1:
                variable, bad_states = flexible[0]
                reduced = domains[variable].difference(bad_states)
                if not reduced:
                    return False
                if reduced != domains[variable]:
                    domains[variable] = reduced
                    changed = True
    return True


def solve_boxes(boxes: tuple[Box, ...], state_counts: tuple[int, ...]) -> list[int] | None:
    occurrence: Counter[int] = Counter(
        variable for box in boxes for variable, _ in box
    )

    def recurse(domains: list[set[int]]) -> list[int] | None:
        domains = [set(domain) for domain in domains]
        if not propagate(domains, boxes):
            return None
        if all(len(domain) == 1 for domain in domains):
            return [next(iter(domain)) for domain in domains]

        variable = min(
            (index for index, domain in enumerate(domains) if len(domain) > 1),
            key=lambda index: (len(domains[index]), -occurrence[index], index),
        )
        for state in sorted(domains[variable]):
            child = [set(domain) for domain in domains]
            child[variable] = {state}
            result = recurse(child)
            if result is not None:
                return result
        return None

    return recurse([set(range(count)) for count in state_counts])


def analyze(
    n: int, fixed: set[Point], variables: tuple[Variable, ...]
) -> dict[str, Any]:
    boxes, triple_data = construct_boxes(fixed, variables)
    state_counts = tuple(len(states) for _, states in variables)
    probabilities = tuple(box_probability(box, state_counts) for box in boxes)
    expectation = sum(probabilities, Fraction(0, 1))
    maximum_probability = max(probabilities, default=Fraction(0, 1))
    maximum_dependency, maximum_occurrence = dependency_data(
        boxes, len(variables)
    )
    has_empty_box = any(not box for box in boxes)

    lll_left = 3 * maximum_probability * (maximum_dependency + 1)
    if maximum_occurrence == 0:
        occurrence_left = Fraction(0, 1)
    else:
        occurrence_left = (
            3 * maximum_probability * (3 * maximum_occurrence - 2)
        )

    assignment = solve_boxes(boxes, state_counts)
    final_points: list[list[int]] | None = None
    assignment_object: dict[str, int] | None = None

    if assignment is not None:
        final = set(fixed)
        for variable, (label, states) in enumerate(variables):
            final.update(states[assignment[variable]])
        if not saturated(final, n) or not no_three(final):
            raise AssertionError("solver assignment failed independent verification")
        assignment_object = {
            label: assignment[variable]
            for variable, (label, _) in enumerate(variables)
        }
        final_points = [list(point) for point in sorted(final)]

    distinct_rank_histogram: Counter[int] = Counter(len(box) for box in boxes)
    return {
        "n": n,
        "variable_count": len(variables),
        "state_counts": list(state_counts),
        "support_point_count": len(
            fixed.union(
                *(
                    frozenset().union(*states)
                    for _, states in variables
                )
            )
        ),
        **triple_data,
        "distinct_bad_box_count": len(boxes),
        "distinct_bad_box_rank_histogram": {
            str(rank): count
            for rank, count in sorted(distinct_rank_histogram.items())
        },
        "has_empty_box": has_empty_box,
        "uniform_bad_box_expectation_fraction": str(expectation),
        "uniform_first_moment_passes": not has_empty_box and expectation < 1,
        "maximum_bad_box_probability_fraction": str(maximum_probability),
        "maximum_dependency_degree": maximum_dependency,
        "symmetric_LLL_exact_left_fraction": str(lll_left),
        "symmetric_LLL_exact_criterion_passes": not has_empty_box and lll_left <= 1,
        "maximum_variable_bad_box_occurrence": maximum_occurrence,
        "occurrence_corollary_left_fraction": str(occurrence_left),
        "occurrence_corollary_passes": not has_empty_box and occurrence_left <= 1,
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
