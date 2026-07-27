#!/usr/bin/env python3
"""Verify quarter-turn-equivariant two-permutation normal forms for seed codes."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;. ,".replace(" ", "")
Point = tuple[int, int]


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


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


def decode_standard_code(code: str, n: int) -> tuple[str, set[Point]]:
    if len(code) != 1 + 2 * n:
        raise ValueError(f"code length {len(code)} does not equal 1+2n={1 + 2 * n}")
    points: set[Point] = set()
    for row in range(n):
        columns: list[int] = []
        for symbol in code[1 + 2 * row : 1 + 2 * row + 2]:
            try:
                column = ALPHABET.index(symbol)
            except ValueError as exc:
                raise ValueError(f"symbol {symbol!r} is not in the standard alphabet") from exc
            if column >= n:
                raise ValueError(f"row {row + 1}: decoded column {column + 1}>n")
            columns.append(column)
        if columns[0] == columns[1]:
            raise ValueError(f"row {row + 1}: duplicate encoded cell")
        points.add((columns[0], row))
        points.add((columns[1], row))
    return code[0], points


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def verify_saturation(points: set[Point], n: int) -> None:
    if len(points) != 2 * n:
        raise ValueError("decoded code does not contain 2n distinct cells")
    row_degree = [0] * n
    column_degree = [0] * n
    for column, row in points:
        column_degree[column] += 1
        row_degree[row] += 1
    if row_degree != [2] * n or column_degree != [2] * n:
        raise ValueError("decoded configuration is not saturated")


def verify_no_three(points: set[Point]) -> int:
    checks = 0
    for a, b, c in combinations(sorted(points), 3):
        checks += 1
        if determinant(a, b, c) == 0:
            raise ValueError(f"collinear triple {a}, {b}, {c}")
    return checks


def rotate_quarter(point: Point, n: int) -> Point:
    column, row = point
    return n - 1 - row, column


def quarter_turn_permutation(permutation: list[int]) -> list[int]:
    n = len(permutation)
    inverse = [0] * n
    for column, row in enumerate(permutation):
        inverse[row] = column
    return [inverse[n - 1 - column] for column in range(n)]


def relative_permutation(sigma: list[int], tau: list[int]) -> list[int]:
    inverse = [0] * len(sigma)
    for column, row in enumerate(sigma):
        inverse[row] = column
    return [inverse[tau[column]] for column in range(len(sigma))]


def cycle_partition(permutation: list[int]) -> list[int]:
    seen = [False] * len(permutation)
    lengths: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        lengths.append(length)
    return sorted(lengths, reverse=True)


def solve_equivariant_colouring(
    points: set[Point], n: int, epsilon: int
) -> tuple[list[int], list[int]] | None:
    rotation = {point: rotate_quarter(point, n) for point in points}
    if set(rotation.values()) != points:
        return None

    row_edges: dict[int, list[Point]] = defaultdict(list)
    column_edges: dict[int, list[Point]] = defaultdict(list)
    for point in points:
        column, row = point
        column_edges[column].append(point)
        row_edges[row].append(point)
    if any(len(row_edges[row]) != 2 for row in range(n)):
        return None
    if any(len(column_edges[column]) != 2 for column in range(n)):
        return None

    constraints: dict[Point, list[tuple[Point, int]]] = defaultdict(list)
    for point in points:
        column, row = point
        for other in row_edges[row] + column_edges[column]:
            if other != point:
                constraints[point].append((other, 1))
        constraints[point].append((rotation[point], epsilon))

    colour: dict[Point, int] = {}
    for start in sorted(points):
        if start in colour:
            continue
        colour[start] = 0
        queue = deque([start])
        while queue:
            point = queue.popleft()
            for other, difference in constraints[point]:
                required = colour[point] ^ difference
                if other in colour:
                    if colour[other] != required:
                        return None
                else:
                    colour[other] = required
                    queue.append(other)

    layers = [[-1] * n, [-1] * n]
    for (column, row), edge_colour in colour.items():
        if layers[edge_colour][column] != -1:
            return None
        layers[edge_colour][column] = row
    if any(sorted(layer) != list(range(n)) for layer in layers):
        return None
    return layers[0], layers[1]


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
    determinant_checks = verify_no_three(points)
    if {rotate_quarter(point, n) for point in points} != points:
        raise ValueError(f"case {ordinal}: selected set is not quarter-turn invariant")

    reversal = [n - 1 - column for column in range(n)]
    modes: list[str] = []
    details: dict[str, Any] = {}
    for epsilon, mode in ((0, "fixed"), (1, "swapped")):
        solution = solve_equivariant_colouring(points, n, epsilon)
        if solution is None:
            continue
        sigma, tau = solution
        if any(sigma[column] == tau[column] for column in range(n)):
            raise ValueError(f"case {ordinal}: equivariant layers share a cell")
        reconstructed = {
            (column, sigma[column]) for column in range(n)
        } | {
            (column, tau[column]) for column in range(n)
        }
        if reconstructed != points:
            raise ValueError(f"case {ordinal}: equivariant layers changed the selected set")

        rotated_sigma = quarter_turn_permutation(sigma)
        rotated_tau = quarter_turn_permutation(tau)
        if mode == "fixed":
            if rotated_sigma != sigma or rotated_tau != tau:
                raise ValueError(f"case {ordinal}: fixed action identity failed")
            if any(
                sigma[sigma[column]] != reversal[column]
                or tau[tau[column]] != reversal[column]
                for column in range(n)
            ):
                raise ValueError(f"case {ordinal}: square-root normal form failed")
            if n % 4 != 0:
                raise ValueError(f"case {ordinal}: fixed mode found with 4 not dividing n")
        else:
            if rotated_sigma != tau or rotated_tau != sigma:
                raise ValueError(f"case {ordinal}: swapped action identity failed")
            if any(
                sigma[reversal[column]] != reversal[sigma[column]]
                for column in range(n)
            ):
                raise ValueError(f"case {ordinal}: sigma does not commute with reversal")
            inverse_sigma = [0] * n
            for column, row in enumerate(sigma):
                inverse_sigma[row] = column
            if tau != [inverse_sigma[reversal[column]] for column in range(n)]:
                raise ValueError(f"case {ordinal}: tau != sigma^(-1) o J")
            if any(
                (sigma[column] == tau[column])
                != (sigma[sigma[column]] == reversal[column])
                for column in range(n)
            ):
                raise ValueError(f"case {ordinal}: edge-disjoint equivalence failed")

        relative = relative_permutation(sigma, tau)
        if any(
            relative[reversal[column]] != reversal[relative[column]]
            for column in range(n)
        ):
            raise ValueError(f"case {ordinal}: relative permutation does not commute with J")
        cycles = cycle_partition(relative)
        multiplicities = Counter(cycles)
        if any(
            length % 2 == 1 and multiplicity % 2 == 1
            for length, multiplicity in multiplicities.items()
        ):
            raise ValueError(f"case {ordinal}: odd relative cycle has odd multiplicity")

        modes.append(mode)
        details[mode] = {
            "sigma": [row + 1 for row in sigma],
            "tau": [row + 1 for row in tau],
            "relative_cycle_partition": cycles,
        }

    expected_modes = raw.get("expected_quarter_turn_modes")
    if expected_modes is not None:
        if not isinstance(expected_modes, list) or not all(
            isinstance(mode, str) for mode in expected_modes
        ):
            raise ValueError(f"case {ordinal}.expected_quarter_turn_modes: expected list")
        if sorted(modes) != sorted(expected_modes):
            raise ValueError(
                f"case {ordinal}: modes {modes} != expected {expected_modes}"
            )
    if not modes:
        raise ValueError(f"case {ordinal}: no equivariant layer colouring")

    return {
        "p": p,
        "n": n,
        "symmetry_tag": symmetry_tag,
        "equivariant_modes": modes,
        "determinant_checks": determinant_checks,
        "details": details,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        cases = payload if isinstance(payload, list) else [payload]
        if not cases:
            raise ValueError("expected at least one quarter-turn seed code")
        verified = [verify_case(raw, index + 1) for index, raw in enumerate(cases)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "quarter_turn_seed_normal_forms_verified",
                "case_count": len(verified),
                "cases": verified,
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
