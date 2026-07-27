#!/usr/bin/env python3
"""Verify the exact support-thirteen swapped-orbit repair certificate for p=37."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%&@?!()[]<>{}=*+|-/~^_:;,."
Point = tuple[int, int]


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def cycle_data(permutation: list[int], signs: list[int] | None = None) -> tuple[list[int], list[int]]:
    seen = [False] * len(permutation)
    lengths: list[int] = []
    parities: list[int] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        parity = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            if signs is not None:
                parity ^= signs[current]
            current = permutation[current]
        lengths.append(length)
        parities.append(parity)
    order = sorted(range(len(lengths)), key=lambda index: (-lengths[index], index))
    return [lengths[index] for index in order], [parities[index] for index in order]


def relative_permutation(sigma: list[int], tau: list[int]) -> list[int]:
    inverse = [0] * len(sigma)
    for column, row in enumerate(sigma):
        inverse[row] = column
    return [inverse[tau[column]] for column in range(len(sigma))]


def selected_set_from_code(code: str, n: int) -> set[Point]:
    if len(code) != 1 + 2 * n:
        raise ValueError(f"standard code length {len(code)} != {1 + 2 * n}")
    points: set[Point] = set()
    payload = code[1:]
    for row in range(n):
        for symbol in payload[2 * row : 2 * row + 2]:
            if symbol not in ALPHABET:
                raise ValueError(f"unknown standard-code symbol {symbol!r}")
            column = ALPHABET.index(symbol)
            if column >= n:
                raise ValueError(f"decoded column {column + 1} exceeds n={n}")
            points.add((column, row))
    if len(points) != 2 * n:
        raise ValueError("standard code does not decode to 2n distinct cells")
    return points


def canonical_assignment(target: int, orientation: int, source: int) -> tuple[int, int]:
    return target, 0 if target == source else orientation


def verify(certificate_raw: Any, near_raw: Any) -> dict[str, Any]:
    if not isinstance(certificate_raw, dict) or not isinstance(near_raw, dict):
        raise ValueError("both inputs must be JSON objects")
    p = require_int(certificate_raw.get("p"), "certificate.p", 3)
    if p != 37:
        raise ValueError("this checker expects p=37")
    n = p - 1
    m = n // 2

    layers: list[list[int]] = []
    for name in ("sigma", "tau"):
        raw = certificate_raw.get(name)
        if not isinstance(raw, list) or len(raw) != n:
            raise ValueError(f"{name}: expected length {n}")
        layer = [require_int(value, f"{name} entry", 1) - 1 for value in raw]
        if sorted(layer) != list(range(n)):
            raise ValueError(f"{name}: expected a permutation of 1..{n}")
        layers.append(layer)
    sigma, tau = layers
    if any(sigma[column] == tau[column] for column in range(n)):
        raise ValueError("the two layers share a cell")

    reversal = [n - 1 - value for value in range(n)]
    if any(sigma[reversal[x]] != reversal[sigma[x]] for x in range(n)):
        raise ValueError("sigma does not commute with coordinate reversal")
    inverse_sigma = [0] * n
    for column, row in enumerate(sigma):
        inverse_sigma[row] = column
    if tau != [inverse_sigma[reversal[x]] for x in range(n)]:
        raise ValueError("tau is not sigma^(-1) composed with reversal")

    pair_permutation: list[int] = []
    pair_orientations: list[int] = []
    for source in range(m):
        image = sigma[source]
        pair_permutation.append(image if image < m else n - 1 - image)
        pair_orientations.append(0 if image < m else 1)
    if sorted(pair_permutation) != list(range(m)):
        raise ValueError("derived pair map is not a permutation")

    expected_pair = certificate_raw.get("pair_permutation")
    expected_signs = certificate_raw.get("pair_orientations")
    if not isinstance(expected_pair, list) or [value - 1 for value in expected_pair] != pair_permutation:
        raise ValueError("stored pair permutation does not match sigma")
    if expected_signs != pair_orientations:
        raise ValueError("stored pair orientations do not match sigma")

    pair_cycles, pair_parities = cycle_data(pair_permutation, pair_orientations)
    if pair_cycles != certificate_raw.get("pair_cycle_partition"):
        raise ValueError("pair-cycle partition mismatch")
    if pair_parities != certificate_raw.get("pair_cycle_orientation_parities"):
        raise ValueError("pair-cycle parity mismatch")

    relative = relative_permutation(sigma, tau)
    relative_cycles, _ = cycle_data(relative)
    if relative_cycles != certificate_raw.get("relative_cycle_partition"):
        raise ValueError("relative-cycle partition mismatch")
    if any(relative[x] == x for x in range(n)):
        raise ValueError("relative permutation is not a derangement")

    near_pair_raw = near_raw.get("pair_permutation")
    near_sign_raw = near_raw.get("pair_orientations")
    if not isinstance(near_pair_raw, list) or not isinstance(near_sign_raw, list):
        raise ValueError("near-state pair data missing")
    near_pair = [require_int(value, "near pair", 1) - 1 for value in near_pair_raw]
    near_sign = [require_int(value, "near orientation", 0) for value in near_sign_raw]
    support = [
        source + 1
        for source in range(m)
        if canonical_assignment(pair_permutation[source], pair_orientations[source], source)
        != canonical_assignment(near_pair[source], near_sign[source], source)
    ]
    if support != certificate_raw.get("repair_support"):
        raise ValueError(f"repair support mismatch: derived {support}")
    if len(support) != 13:
        raise ValueError("repair support is not thirteen")

    assignments_raw = certificate_raw.get("repair_assignments")
    if not isinstance(assignments_raw, list):
        raise ValueError("repair_assignments: expected list")
    assignments: dict[int, tuple[int, int]] = {}
    for entry in assignments_raw:
        if not isinstance(entry, dict):
            raise ValueError("repair assignment must be an object")
        source = require_int(entry.get("source"), "assignment source", 1)
        assignments[source] = (
            require_int(entry.get("target"), "assignment target", 1),
            require_int(entry.get("orientation"), "assignment orientation", 0),
        )
    if sorted(assignments) != support:
        raise ValueError("repair assignment sources do not equal repair support")
    for source_one in support:
        source = source_one - 1
        if assignments[source_one] != (pair_permutation[source] + 1, pair_orientations[source]):
            raise ValueError(f"repair assignment mismatch at source {source_one}")

    points = {(column, sigma[column]) for column in range(n)}
    points |= {(column, tau[column]) for column in range(n)}
    if len(points) != 2 * n:
        raise ValueError("selected set does not have 2n cells")
    row_degree = [0] * n
    column_degree = [0] * n
    for column, row in points:
        column_degree[column] += 1
        row_degree[row] += 1
    if row_degree != [2] * n or column_degree != [2] * n:
        raise ValueError("selected set is not saturated")

    determinant_checks = 0
    minimum_absolute_determinant: int | None = None
    for a, b, c in combinations(sorted(points), 3):
        value = determinant(a, b, c)
        determinant_checks += 1
        if value == 0:
            raise ValueError(f"collinear triple {a}, {b}, {c}")
        absolute = abs(value)
        minimum_absolute_determinant = absolute if minimum_absolute_determinant is None else min(minimum_absolute_determinant, absolute)
    if determinant_checks != certificate_raw.get("determinant_checks"):
        raise ValueError("determinant-check count mismatch")
    if minimum_absolute_determinant != certificate_raw.get("minimum_absolute_determinant"):
        raise ValueError("minimum determinant mismatch")

    standard_code = certificate_raw.get("standard_code")
    if not isinstance(standard_code, str):
        raise ValueError("standard_code: expected string")
    if selected_set_from_code(standard_code, n) != points:
        raise ValueError("standard code does not encode the selected set")

    lower_bound = near_raw.get("minimum_pair_orbit_repair_support_lower_bound")
    if lower_bound is not None and require_int(lower_bound, "near-state lower bound", 1) != 13:
        raise ValueError("near-state lower bound is not thirteen")

    return {
        "outcome": "p37_support_thirteen_repair_certificate_verified",
        "p": p,
        "n": n,
        "point_count": len(points),
        "repair_support": support,
        "repair_support_size": len(support),
        "pair_cycle_partition": pair_cycles,
        "pair_cycle_orientation_parities": pair_parities,
        "relative_cycle_partition": relative_cycles,
        "determinant_checks": determinant_checks,
        "minimum_absolute_determinant": minimum_absolute_determinant,
        "standard_code_reconstructs_seed": True,
        "saturated": True,
        "no_three_in_line": True,
        "valid_seed": True,
        "asymptotic_seed_theorem_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("near_state", type=Path)
    args = parser.parse_args()
    try:
        certificate_raw = json.loads(args.certificate.read_text(encoding="utf-8"))
        near_raw = json.loads(args.near_state.read_text(encoding="utf-8"))
        result = verify(certificate_raw, near_raw)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
