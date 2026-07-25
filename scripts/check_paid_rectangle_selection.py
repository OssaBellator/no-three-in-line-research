#!/usr/bin/env python3
"""Exact checker for PP3oy--PP3pb paid binary rectangle selection."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--max-variables", type=int, default=24)
    return parser.parse_args()


def as_fraction(value: Any, label: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{label}: booleans are not rational values")
    try:
        result = Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label}: invalid rational value") from exc
    return result


def fraction_object(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def load_instance(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("top-level JSON must be an object")

    raw_biases = data.get("biases")
    if not isinstance(raw_biases, list) or not raw_biases:
        raise ValueError("biases must be a nonempty list")
    biases = [as_fraction(value, f"biases[{i}]") for i, value in enumerate(raw_biases)]
    if any(value < 0 or value > 1 for value in biases):
        raise ValueError("every bias must lie in [0,1]")
    k = len(biases)

    raw_clauses = data.get("clauses", [])
    if not isinstance(raw_clauses, list):
        raise ValueError("clauses must be a list")
    clauses: list[dict[int, int]] = []
    for index, raw_clause in enumerate(raw_clauses):
        if not isinstance(raw_clause, dict) or not raw_clause:
            raise ValueError(f"clauses[{index}] must be a nonempty object")
        clause: dict[int, int] = {}
        for raw_variable, raw_state in raw_clause.items():
            try:
                variable = int(raw_variable)
            except ValueError as exc:
                raise ValueError(f"clauses[{index}]: invalid variable") from exc
            if not 0 <= variable < k or raw_state not in (0, 1):
                raise ValueError(f"clauses[{index}]: invalid variable/state")
            clause[variable] = raw_state
        if len(clause) > 3:
            raise ValueError(f"clauses[{index}] has rank above three")
        clauses.append(clause)

    constant_cost = as_fraction(data.get("constant_cost", 0), "constant_cost")
    removal_credit = as_fraction(data.get("removal_credit"), "removal_credit")
    if constant_cost < 0 or removal_credit <= 0:
        raise ValueError("cost must be nonnegative and removal credit positive")

    raw_unary = data.get("unary_costs")
    if not isinstance(raw_unary, list) or len(raw_unary) != k:
        raise ValueError("unary_costs must contain one two-state table per variable")
    unary: list[tuple[Fraction, Fraction]] = []
    for index, raw_table in enumerate(raw_unary):
        if not isinstance(raw_table, list) or len(raw_table) != 2:
            raise ValueError(f"unary_costs[{index}] must have two entries")
        table = (
            as_fraction(raw_table[0], f"unary_costs[{index}][0]"),
            as_fraction(raw_table[1], f"unary_costs[{index}][1]"),
        )
        if min(table) < 0:
            raise ValueError("unary costs must be nonnegative")
        unary.append(table)

    raw_binary = data.get("binary_costs", [])
    if not isinstance(raw_binary, list):
        raise ValueError("binary_costs must be a list")
    binary: list[tuple[int, int, tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]]] = []
    for index, raw_entry in enumerate(raw_binary):
        if not isinstance(raw_entry, dict):
            raise ValueError(f"binary_costs[{index}] must be an object")
        variables = raw_entry.get("variables")
        table = raw_entry.get("table")
        if (
            not isinstance(variables, list)
            or len(variables) != 2
            or any(not isinstance(value, int) or isinstance(value, bool) for value in variables)
        ):
            raise ValueError(f"binary_costs[{index}].variables must contain two integers")
        first, second = variables
        if not (0 <= first < second < k):
            raise ValueError(f"binary_costs[{index}]: require 0 <= first < second < k")
        if (
            not isinstance(table, list)
            or len(table) != 2
            or any(not isinstance(row, list) or len(row) != 2 for row in table)
        ):
            raise ValueError(f"binary_costs[{index}].table must be 2 by 2")
        parsed = tuple(
            tuple(as_fraction(table[a][b], f"binary_costs[{index}].table[{a}][{b}]") for b in range(2))
            for a in range(2)
        )
        if min(value for row in parsed for value in row) < 0:
            raise ValueError("binary costs must be nonnegative")
        binary.append((first, second, parsed))

    return {
        "biases": biases,
        "clauses": clauses,
        "constant_cost": constant_cost,
        "removal_credit": removal_credit,
        "unary": unary,
        "binary": binary,
    }


def state_probability(bias: Fraction, state: int) -> Fraction:
    return bias if state else 1 - bias


def clause_probability(clause: dict[int, int], biases: list[Fraction]) -> Fraction:
    probability = Fraction(1)
    for variable, state in clause.items():
        probability *= state_probability(biases[variable], state)
    return probability


def assignment_cost(
    assignment: tuple[int, ...],
    constant_cost: Fraction,
    unary: list[tuple[Fraction, Fraction]],
    binary: list[tuple[int, int, tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]]],
) -> Fraction:
    value = constant_cost
    value += sum(unary[index][state] for index, state in enumerate(assignment))
    for first, second, table in binary:
        value += table[assignment[first]][assignment[second]]
    return value


def main() -> None:
    args = parse_args()
    try:
        instance = load_instance(args.input)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    biases: list[Fraction] = instance["biases"]
    clauses: list[dict[int, int]] = instance["clauses"]
    constant_cost: Fraction = instance["constant_cost"]
    removal_credit: Fraction = instance["removal_credit"]
    unary = instance["unary"]
    binary = instance["binary"]
    k = len(biases)

    clause_probabilities = [clause_probability(clause, biases) for clause in clauses]
    clause_sum = sum(clause_probabilities, Fraction())
    local_masses = [Fraction() for _ in range(k)]
    for clause, probability in zip(clauses, clause_probabilities):
        for variable in clause:
            local_masses[variable] += probability
    lambda_value = max(local_masses, default=Fraction())

    unary_expectation = Fraction()
    for variable, table in enumerate(unary):
        unary_expectation += (
            (1 - biases[variable]) * table[0]
            + biases[variable] * table[1]
        )

    binary_expectation = Fraction()
    for first, second, table in binary:
        for state_first in range(2):
            for state_second in range(2):
                binary_expectation += (
                    state_probability(biases[first], state_first)
                    * state_probability(biases[second], state_second)
                    * table[state_first][state_second]
                )

    expected_cost = constant_cost + unary_expectation + binary_expectation
    first_moment_value = clause_sum + expected_cost / removal_credit

    lambda_float = float(lambda_value)
    inflated_cost = (
        float(constant_cost)
        + math.exp(8 * lambda_float) * float(unary_expectation)
        + math.exp(16 * lambda_float) * float(binary_expectation)
    )
    lll_mass_ok = lambda_value <= Fraction(1, 24)
    lll_cost_ok = inflated_cost < float(removal_credit)

    exact_result: dict[str, object] | None = None
    if k <= args.max_variables:
        satisfying_count = 0
        best_cost: Fraction | None = None
        best_assignment: tuple[int, ...] | None = None
        for assignment in itertools.product((0, 1), repeat=k):
            violates = any(
                all(assignment[variable] == state for variable, state in clause.items())
                for clause in clauses
            )
            if violates:
                continue
            satisfying_count += 1
            cost = assignment_cost(assignment, constant_cost, unary, binary)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_assignment = assignment
        exact_result = {
            "satisfying_assignment_count": satisfying_count,
            "minimum_satisfying_cost": (
                None if best_cost is None else fraction_object(best_cost)
            ),
            "minimum_satisfying_assignment": (
                None if best_assignment is None else list(best_assignment)
            ),
            "negative_paid_assignment_exists": (
                best_cost is not None and best_cost < removal_credit
            ),
        }

    output = {
        "variable_count": k,
        "clause_count": len(clauses),
        "clause_ranks": [len(clause) for clause in clauses],
        "clause_probabilities": [fraction_object(value) for value in clause_probabilities],
        "clause_probability_sum": fraction_object(clause_sum),
        "local_clause_masses": [fraction_object(value) for value in local_masses],
        "lambda": fraction_object(lambda_value),
        "constant_cost": fraction_object(constant_cost),
        "expected_unary_cost": fraction_object(unary_expectation),
        "expected_binary_cost": fraction_object(binary_expectation),
        "expected_total_cost": fraction_object(expected_cost),
        "removal_credit": fraction_object(removal_credit),
        "PP3oy_first_moment_value": fraction_object(first_moment_value),
        "PP3oy_certified": first_moment_value < 1,
        "PP3oz_local_mass_certified": lll_mass_ok,
        "PP3oz_inflated_expected_cost": inflated_cost,
        "PP3oz_cost_certified": lll_cost_ok,
        "PP3oz_certified": lll_mass_ok and lll_cost_ok,
        "exact_enumeration": exact_result,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
