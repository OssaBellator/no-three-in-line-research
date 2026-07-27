#!/usr/bin/env python3
"""Verify the adjacent-transposition subgraph of Hamilton successor rotations."""
from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import permutations
from pathlib import Path


def rho_from_order(order: tuple[int, ...]) -> tuple[int, ...]:
    rho = [0] * len(order)
    for index, source in enumerate(order):
        rho[source] = order[(index + 1) % len(order)]
    return tuple(rho)


def order_from_rho(rho: tuple[int, ...]) -> tuple[int, ...]:
    order = [0]
    current = rho[0]
    while current != 0:
        order.append(current)
        current = rho[current]
    if len(order) != len(rho):
        raise ValueError("rho is not one Hamilton cycle")
    return tuple(order)


def switch_rho(
    rho: tuple[int, ...], sources: tuple[int, int, int]
) -> tuple[int, ...]:
    selected = set(sources)
    cyclic: list[int] = []
    current = min(selected)
    for _ in range(len(rho)):
        if current in selected:
            cyclic.append(current)
        current = rho[current]
    if len(cyclic) != 3:
        raise ValueError("selected sources not found")
    a1, a2, a3 = cyclic
    b1, b2, b3 = rho[a1], rho[a2], rho[a3]
    changed = list(rho)
    changed[a1], changed[a2], changed[a3] = b2, b3, b1
    return tuple(changed)


def audit_case(m: int) -> dict[str, object]:
    cycles = 0
    adjacent_checks = 0
    for tail in permutations(range(1, m)):
        order = (0,) + tail
        rho = rho_from_order(order)
        cycles += 1
        for position in range(1, m - 1):
            predecessor = order[position - 1]
            left = order[position]
            right = order[position + 1]
            changed = switch_rho(rho, (predecessor, left, right))
            expected = list(order)
            expected[position], expected[position + 1] = (
                expected[position + 1],
                expected[position],
            )
            if order_from_rho(changed) != tuple(expected):
                raise ValueError(f"adjacent swap mismatch at m={m}")
            adjacent_checks += 1

    comparison = Fraction(m - 2, 8 * math.comb(m, 3))
    if comparison != Fraction(3, 4 * m * (m - 1)):
        raise ValueError("comparison coefficient simplification failed")

    return {
        "m": m,
        "hamilton_cycles": cycles,
        "adjacent_transposition_checks": adjacent_checks,
        "adjacent_generators_per_cycle": m - 2,
        "unsigned_rotation_degree": math.comb(m, 3),
        "signed_combined_degree": m + 8 * math.comb(m, 3),
        "dirichlet_comparison_coefficient": (
            f"{comparison.numerator}/{comparison.denominator}"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()

    try:
        expected = json.loads(args.audit.read_text())
        minimum = expected.get("minimum_pair_size")
        maximum = expected.get("maximum_pair_size")
        if (
            isinstance(minimum, bool)
            or not isinstance(minimum, int)
            or isinstance(maximum, bool)
            or not isinstance(maximum, int)
            or minimum < 4
            or maximum < minimum
        ):
            raise ValueError("invalid pair-size range")
        result = {
            "minimum_pair_size": minimum,
            "maximum_pair_size": maximum,
            "cases": [audit_case(m) for m in range(minimum, maximum + 1)],
            "total_adjacent_transposition_checks": sum(
                math.factorial(m - 1) * (m - 2)
                for m in range(minimum, maximum + 1)
            ),
            "asymptotic_seed_theorem_proved": False,
        }
        if result != expected:
            raise ValueError("stored adjacent-transposition audit mismatch")
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
