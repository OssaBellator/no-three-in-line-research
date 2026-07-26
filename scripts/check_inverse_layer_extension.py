#!/usr/bin/env python3
"""Verify inverse-conic layers and exact fixed-layer seed extension results."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import gcd
from pathlib import Path
from typing import Any

Point = tuple[int, int]
Line = tuple[Point, ...]


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    divisor = 3
    while divisor * divisor <= p:
        if p % divisor == 0:
            return False
        divisor += 2
    return True


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def maximal_nonaxis_lines(n: int) -> list[Line]:
    lines: list[Line] = []
    for dx in range(1, n):
        for dy in range(-(n - 1), n):
            if dy == 0 or gcd(dx, abs(dy)) != 1:
                continue
            for x in range(n):
                for y in range(n):
                    if 0 <= x - dx < n and 0 <= y - dy < n:
                        continue
                    cells: list[Point] = []
                    xx, yy = x, y
                    while 0 <= xx < n and 0 <= yy < n:
                        cells.append((xx, yy))
                        xx += dx
                        yy += dy
                    if len(cells) >= 3:
                        lines.append(tuple(cells))
    if len(lines) != len(set(lines)):
        raise AssertionError("maximal-line enumeration produced duplicates")
    return lines


def verify_permutation_layer(layer: list[int], label: str) -> None:
    n = len(layer)
    if sorted(layer) != list(range(n)):
        raise ValueError(f"{label}: expected a zero-based permutation")
    points = [(column, layer[column]) for column in range(n)]
    for a, b, c in combinations(points, 3):
        if determinant(a, b, c) == 0:
            raise ValueError(f"{label}: collinear triple {a}, {b}, {c}")


def inverse_layer(p: int, multiplier: int) -> list[int]:
    return [
        (multiplier * pow(column, -1, p)) % p - 1
        for column in range(1, p)
    ]


def fixed_layer_extension(first: list[int]) -> dict[str, Any]:
    """Solve the exact second-permutation extension CSP by MRV, Hall, and line capacities."""
    n = len(first)
    lines = maximal_nonaxis_lines(n)
    first_cells = {(column, first[column]) for column in range(n)}
    capacities: list[int] = []
    cell_lines: list[list[list[int]]] = [[[] for _ in range(n)] for _ in range(n)]

    for line_index, line in enumerate(lines):
        capacity = 2 - sum(cell in first_cells for cell in line)
        if capacity < 0:
            return {
                "extendable": False,
                "nodes": 0,
                "hall_checks": 0,
                "nonaxis_lines": len(lines),
                "reason": "first_layer_not_clean",
            }
        capacities.append(capacity)
        for column, row in line:
            cell_lines[column][row].append(line_index)

    base_domains: list[tuple[int, ...]] = []
    for column in range(n):
        values = tuple(
            row
            for row in range(n)
            if row != first[column]
            and all(capacities[line_index] > 0 for line_index in cell_lines[column][row])
        )
        if not values:
            return {
                "extendable": False,
                "nodes": 0,
                "hall_checks": 0,
                "nonaxis_lines": len(lines),
                "reason": "empty_initial_domain",
                "empty_column": column + 1,
            }
        base_domains.append(values)

    line_counts = [0] * len(lines)
    used_rows = [False] * n
    assignment = [-1] * n
    unassigned = set(range(n))
    nodes = 0
    hall_checks = 0

    def domain(column: int) -> list[int]:
        return [
            row
            for row in base_domains[column]
            if not used_rows[row]
            and all(
                line_counts[line_index] < capacities[line_index]
                for line_index in cell_lines[column][row]
            )
        ]

    def hall_feasible(domains: dict[int, list[int]]) -> bool:
        nonlocal hall_checks
        hall_checks += 1
        row_match = [-1] * n

        def augment(column: int, seen: list[bool]) -> bool:
            for row in domains[column]:
                if seen[row]:
                    continue
                seen[row] = True
                if row_match[row] < 0 or augment(row_match[row], seen):
                    row_match[row] = column
                    return True
            return False

        for column in sorted(domains, key=lambda item: len(domains[item])):
            if not augment(column, [False] * n):
                return False
        return True

    def search() -> bool:
        nonlocal nodes
        if not unassigned:
            return True
        nodes += 1

        domains: dict[int, list[int]] = {}
        chosen_column = -1
        chosen_domain: list[int] | None = None
        for column in unassigned:
            values = domain(column)
            if not values:
                return False
            domains[column] = values
            if chosen_domain is None or len(values) < len(chosen_domain):
                chosen_column = column
                chosen_domain = values

        assert chosen_domain is not None
        if len(unassigned) >= 2 and not hall_feasible(domains):
            return False

        def value_score(row: int) -> tuple[float, int]:
            competing_columns = sum(
                row in domains[other]
                for other in unassigned
                if other != chosen_column
            )
            line_pressure = sum(
                1.0 / (capacities[line_index] - line_counts[line_index])
                for line_index in cell_lines[chosen_column][row]
                if capacities[line_index] > line_counts[line_index]
            )
            return competing_columns + line_pressure, row

        for row in sorted(chosen_domain, key=value_score):
            assignment[chosen_column] = row
            used_rows[row] = True
            unassigned.remove(chosen_column)
            affected = cell_lines[chosen_column][row]
            for line_index in affected:
                line_counts[line_index] += 1

            if search():
                return True

            for line_index in affected:
                line_counts[line_index] -= 1
            unassigned.add(chosen_column)
            used_rows[row] = False
            assignment[chosen_column] = -1
        return False

    extendable = search()
    result: dict[str, Any] = {
        "extendable": extendable,
        "nodes": nodes,
        "hall_checks": hall_checks,
        "nonaxis_lines": len(lines),
        "secant_pruned_cells": sum(
            1
            for column in range(n)
            for row in range(n)
            if row != first[column] and row not in base_domains[column]
        ),
    }
    if extendable:
        result["second_layer"] = [row + 1 for row in assignment]
    return result


def count_union_bad_triples(sigma: list[int], tau: list[int]) -> list[list[Point]]:
    points = [(column, sigma[column]) for column in range(len(sigma))]
    points.extend((column, tau[column]) for column in range(len(tau)))
    return [
        [a, b, c]
        for a, b, c in combinations(points, 3)
        if determinant(a, b, c) == 0
    ]


def verify_payload(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("expected a JSON object")

    raw_primes = payload.get("inverse_primes")
    if not isinstance(raw_primes, list) or not raw_primes:
        raise ValueError("inverse_primes: expected a nonempty list")
    expected_raw = payload.get("expected_extendable_multipliers", {})
    if not isinstance(expected_raw, dict):
        raise ValueError("expected_extendable_multipliers: expected object")

    prime_results: list[dict[str, Any]] = []
    for raw_p in raw_primes:
        p = require_int(raw_p, "inverse prime", 3)
        if not is_prime(p):
            raise ValueError(f"inverse prime {p} is not prime")
        extendable: list[int] = []
        multiplier_results: list[dict[str, Any]] = []
        for multiplier in range(1, p):
            layer = inverse_layer(p, multiplier)
            verify_permutation_layer(layer, f"p={p}, multiplier={multiplier}")
            extension = fixed_layer_extension(layer)
            if extension["extendable"]:
                extendable.append(multiplier)
            multiplier_results.append(
                {
                    "multiplier": multiplier,
                    "extendable": extension["extendable"],
                    "nodes": extension["nodes"],
                    "hall_checks": extension["hall_checks"],
                    "secant_pruned_cells": extension.get("secant_pruned_cells", 0),
                }
            )

        expected = expected_raw.get(str(p))
        if expected is not None:
            if not isinstance(expected, list):
                raise ValueError(f"expected multipliers for p={p}: expected list")
            expected_values = [require_int(value, f"p={p} expected multiplier", 1) for value in expected]
            if extendable != expected_values:
                raise ValueError(
                    f"p={p}: extendable multipliers {extendable} != expected {expected_values}"
                )

        prime_results.append(
            {
                "p": p,
                "n": p - 1,
                "all_inverse_layers_no_three": True,
                "extendable_multipliers": extendable,
                "extendable_count": len(extendable),
                "maximum_search_nodes": max(item["nodes"] for item in multiplier_results),
                "total_search_nodes": sum(item["nodes"] for item in multiplier_results),
                "multipliers": multiplier_results,
            }
        )

    near_raw = payload.get("near_state")
    near_result: dict[str, Any] | None = None
    if near_raw is not None:
        if not isinstance(near_raw, dict):
            raise ValueError("near_state: expected object")
        p = require_int(near_raw.get("p"), "near_state.p", 3)
        n = p - 1
        if not is_prime(p):
            raise ValueError("near_state.p must be prime")
        layers: list[list[int]] = []
        for name in ("sigma", "tau"):
            raw_layer = near_raw.get(name)
            if not isinstance(raw_layer, list) or len(raw_layer) != n:
                raise ValueError(f"near_state.{name}: expected length {n} list")
            layer = [require_int(value, f"near_state.{name} entry", 1) - 1 for value in raw_layer]
            verify_permutation_layer(layer, f"near_state.{name}")
            layers.append(layer)
        sigma, tau = layers
        bad = count_union_bad_triples(sigma, tau)
        expected_bad = near_raw.get("expected_bad_triples")
        if expected_bad is not None and len(bad) != require_int(
            expected_bad, "near_state.expected_bad_triples"
        ):
            raise ValueError(
                f"near_state: found {len(bad)} bad triples, expected {expected_bad}"
            )
        sigma_extension = fixed_layer_extension(sigma)
        tau_extension = fixed_layer_extension(tau)
        if sigma_extension["extendable"] or tau_extension["extendable"]:
            raise ValueError("near_state: one fixed layer unexpectedly has an extension")
        near_result = {
            "p": p,
            "both_layers_individually_no_three": True,
            "union_bad_triple_count": len(bad),
            "bad_triples_one_based": [
                [[column + 1, row + 1] for column, row in triple]
                for triple in bad
            ],
            "fixed_sigma_extendable": False,
            "fixed_tau_extendable": False,
            "fixed_sigma_search_nodes": sigma_extension["nodes"],
            "fixed_tau_search_nodes": tau_extension["nodes"],
            "coordinated_two_layer_change_required": True,
        }

    return {
        "outcome": "inverse_layer_extension_csp_verified",
        "inverse_prime_cases": prime_results,
        "near_state": near_result,
        "asymptotic_seed_theorem_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        result = verify_payload(payload)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
