#!/usr/bin/env python3
"""Decode archived row-pair seed codes and verify exact prime-minus-one certificates."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
Point = tuple[int, int]


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


def decode_standard_code(code: str, n: int) -> tuple[str, list[Point]]:
    if len(code) != 1 + 2 * n:
        raise ValueError(
            f"code length {len(code)} does not equal 1+2n={1 + 2 * n}"
        )
    symmetry_tag = code[0]
    points: list[Point] = []
    payload = code[1:]
    for row in range(n):
        symbols = payload[2 * row : 2 * row + 2]
        columns: list[int] = []
        for symbol in symbols:
            try:
                column = ALPHABET.index(symbol)
            except ValueError as exc:
                raise ValueError(f"symbol {symbol!r} is not in the standard alphabet") from exc
            if column >= n:
                raise ValueError(
                    f"row {row + 1}: symbol {symbol!r} decodes to column {column + 1}>n"
                )
            columns.append(column)
        if columns[0] == columns[1]:
            raise ValueError(f"row {row + 1}: duplicate encoded column")
        points.extend((column, row) for column in columns)
    return symmetry_tag, points


def verify_saturation(points: list[Point], n: int) -> None:
    if len(points) != 2 * n or len(set(points)) != 2 * n:
        raise ValueError("decoded code does not contain 2n distinct cells")
    row_degree = [0] * n
    column_degree = [0] * n
    for column, row in points:
        if not (0 <= column < n and 0 <= row < n):
            raise ValueError("decoded point lies outside the board")
        column_degree[column] += 1
        row_degree[row] += 1
    if row_degree != [2] * n:
        raise ValueError(f"row degrees are not all two: {row_degree}")
    if column_degree != [2] * n:
        raise ValueError(f"column degrees are not all two: {column_degree}")


def decompose_two_regular(points: list[Point], n: int) -> tuple[list[int], list[int]]:
    """Alternately colour each even incidence cycle to obtain two permutations."""
    edges = sorted(set(points))
    row_edges: dict[int, list[Point]] = defaultdict(list)
    column_edges: dict[int, list[Point]] = defaultdict(list)
    for edge in edges:
        column, row = edge
        row_edges[row].append(edge)
        column_edges[column].append(edge)
    if any(len(row_edges[row]) != 2 for row in range(n)):
        raise ValueError("row incidence graph is not 2-regular")
    if any(len(column_edges[column]) != 2 for column in range(n)):
        raise ValueError("column incidence graph is not 2-regular")

    adjacency: dict[Point, list[Point]] = {}
    for edge in edges:
        column, row = edge
        neighbours = [
            other
            for other in row_edges[row] + column_edges[column]
            if other != edge
        ]
        if len(neighbours) != 2:
            raise ValueError("edge adjacency graph is not a cycle union")
        adjacency[edge] = sorted(neighbours)

    colour: dict[Point, int] = {}
    for start in edges:
        if start in colour:
            continue
        previous: Point | None = None
        current = start
        current_colour = 0
        while True:
            if current in colour:
                if current != start or colour[current] != current_colour:
                    raise ValueError("inconsistent alternating cycle colouring")
                break
            colour[current] = current_colour
            neighbours = adjacency[current]
            next_edge = neighbours[0] if neighbours[0] != previous else neighbours[1]
            previous, current = current, next_edge
            current_colour = 1 - current_colour

    layers = [[-1] * n, [-1] * n]
    for (column, row), edge_colour in colour.items():
        if layers[edge_colour][column] != -1:
            raise ValueError("cycle colouring assigned two same-colour edges to one column")
        layers[edge_colour][column] = row
    sigma, tau = layers
    if sorted(sigma) != list(range(n)) or sorted(tau) != list(range(n)):
        raise ValueError("cycle colour classes are not permutation layers")
    return sigma, tau


def relative_permutation(sigma: list[int], tau: list[int]) -> list[int]:
    inverse_sigma = [0] * len(sigma)
    for column, row in enumerate(sigma):
        inverse_sigma[row] = column
    return [inverse_sigma[tau[column]] for column in range(len(sigma))]


def cycle_partition(permutation: list[int]) -> list[int]:
    seen = [False] * len(permutation)
    lengths: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        length = 0
        current = start
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        lengths.append(length)
    return sorted(lengths, reverse=True)


def verify_case(raw: Any, ordinal: int) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError(f"case {ordinal}: expected object")
    p = require_int(raw.get("p"), f"case {ordinal}.p", 3)
    if not is_prime(p):
        raise ValueError(f"case {ordinal}: p={p} is not prime")
    n = p - 1
    code = raw.get("code")
    if not isinstance(code, str):
        raise ValueError(f"case {ordinal}.code: expected string")

    symmetry_tag, points = decode_standard_code(code, n)
    verify_saturation(points, n)

    determinant_checks = 0
    minimum_absolute_determinant: int | None = None
    for a, b, c in combinations(points, 3):
        value = determinant(a, b, c)
        determinant_checks += 1
        if value == 0:
            raise ValueError(f"case {ordinal}: collinear triple {a}, {b}, {c}")
        absolute = abs(value)
        minimum_absolute_determinant = (
            absolute
            if minimum_absolute_determinant is None
            else min(minimum_absolute_determinant, absolute)
        )

    sigma, tau = decompose_two_regular(points, n)
    if any(sigma[column] == tau[column] for column in range(n)):
        raise ValueError(f"case {ordinal}: decomposed layers share a cell")
    reconstructed = {
        (column, sigma[column]) for column in range(n)
    } | {
        (column, tau[column]) for column in range(n)
    }
    if reconstructed != set(points):
        raise ValueError(f"case {ordinal}: layer decomposition changed the selected set")

    relative = relative_permutation(sigma, tau)
    if any(relative[column] == column for column in range(n)):
        raise ValueError(f"case {ordinal}: relative permutation is not a derangement")
    cycles = cycle_partition(relative)

    expected_cycles = raw.get("expected_cycles")
    if expected_cycles is not None:
        if not isinstance(expected_cycles, list):
            raise ValueError(f"case {ordinal}.expected_cycles: expected list")
        expected = sorted(
            [require_int(value, f"case {ordinal} expected cycle", 2) for value in expected_cycles],
            reverse=True,
        )
        if cycles != expected:
            raise ValueError(
                f"case {ordinal}: relative cycles {cycles} != expected {expected}"
            )

    return {
        "p": p,
        "n": n,
        "archive_path": raw.get("archive_path"),
        "symmetry_tag": symmetry_tag,
        "point_count": len(points),
        "saturated": True,
        "no_three_in_line": True,
        "determinant_checks": determinant_checks,
        "minimum_absolute_determinant": minimum_absolute_determinant,
        "sigma": [row + 1 for row in sigma],
        "tau": [row + 1 for row in tau],
        "relative_permutation": [column + 1 for column in relative],
        "relative_cycle_partition": cycles,
        "alternating_incidence_component_lengths": [2 * length for length in cycles],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        cases = payload if isinstance(payload, list) else [payload]
        if not cases:
            raise ValueError("expected at least one archived code")
        verified = [verify_case(raw, index + 1) for index, raw in enumerate(cases)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "archived_prime_seed_codes_verified",
                "case_count": len(verified),
                "cases": verified,
                "largest_prime": max(case["p"] for case in verified),
                "total_determinant_checks": sum(
                    case["determinant_checks"] for case in verified
                ),
                "asymptotic_seed_theorem_proved": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
