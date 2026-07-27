#!/usr/bin/env python3
"""Audit two-cycle-free and near-Hamilton swapped signed-cover subfamilies."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from typing import Any


def int_list(raw: dict[str, Any], key: str) -> list[int]:
    value = raw.get(key)
    if not isinstance(value, list) or any(
        isinstance(x, bool) or not isinstance(x, int) for x in value
    ):
        raise ValueError(f"{key} must be an integer list")
    return value


def egf_count(m: int, linear: int, quadratic: int) -> int:
    """Return m![z^m] exp(linear*z+quadratic*z^2)/(1-2z)."""
    coefficient = Fraction(0)
    for j in range(m + 1):
        for k in range((m - j) // 2 + 1):
            degree = j + 2 * k
            coefficient += (
                Fraction(linear**j, math.factorial(j))
                * Fraction(quadratic**k, math.factorial(k))
                * 2 ** (m - degree)
            )
    value = coefficient * math.factorial(m)
    if value.denominator != 1:
        raise AssertionError("EGF coefficient is not integral")
    return value.numerator


def permutation_cycle_counts(permutation: tuple[int, ...]) -> tuple[int, int]:
    seen = [False] * len(permutation)
    one_cycles = 0
    two_cycles = 0
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        if length == 1:
            one_cycles += 1
        elif length == 2:
            two_cycles += 1
    return one_cycles, two_cycles


def exhaustive_coefficient_audit(max_m: int) -> dict[str, Any]:
    permutations_checked = 0
    cases = []
    for m in range(max_m + 1):
        edge_disjoint = 0
        two_cycle_free = 0
        for permutation in permutations(range(m)):
            permutations_checked += 1
            one_cycles, two_cycles = permutation_cycle_counts(permutation)
            edge_disjoint += 2 ** (m - one_cycles - two_cycles)
            if two_cycles == 0:
                two_cycle_free += 2 ** (m - one_cycles)
        expected_edge_disjoint = egf_count(m, -1, -1)
        expected_two_cycle_free = egf_count(m, -1, -2)
        if edge_disjoint != expected_edge_disjoint:
            raise ValueError(f"edge-disjoint coefficient mismatch at m={m}")
        if two_cycle_free != expected_two_cycle_free:
            raise ValueError(f"two-cycle-free coefficient mismatch at m={m}")
        cases.append(
            {
                "m": m,
                "permutations": math.factorial(m),
                "canonical_edge_disjoint": edge_disjoint,
                "canonical_two_cycle_free": two_cycle_free,
            }
        )
    return {
        "maximum_pair_size": max_m,
        "permutations_checked": permutations_checked,
        "cases": cases,
    }


def cycles_on(vertices: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    first = min(vertices)
    rest = tuple(v for v in vertices if v != first)
    cycles: list[tuple[tuple[int, int], ...]] = []
    for tail in permutations(rest):
        order = (first,) + tail
        cycles.append(
            tuple((order[i], order[(i + 1) % len(order)]) for i in range(len(order)))
        )
    return cycles


def exhaustive_cylinder_audit(max_m: int, max_edges: int) -> dict[str, Any]:
    full_checks = 0
    one_fixed_checks = 0

    for m in range(4, max_m + 1):
        counts = [Counter() for _ in range(max_edges + 1)]
        for cycle in cycles_on(tuple(range(m))):
            for r in range(1, min(max_edges, m - 1) + 1):
                for forest in combinations(cycle, r):
                    counts[r][tuple(sorted(forest))] += 1
        for r in range(1, min(max_edges, m - 1) + 1):
            expected = math.factorial(m - r - 1)
            for value in counts[r].values():
                full_checks += 1
                if value != expected:
                    raise ValueError(
                        f"full Hamilton cylinder mismatch at m={m}, r={r}"
                    )

    for m in range(5, max_m + 1):
        counts = [Counter() for _ in range(max_edges + 1)]
        for fixed in range(m):
            vertices = tuple(v for v in range(m) if v != fixed)
            for cycle in cycles_on(vertices):
                for r in range(1, min(max_edges, m - 2) + 1):
                    for forest in combinations(cycle, r):
                        counts[r][tuple(sorted(forest))] += 1
        for r in range(1, min(max_edges, m - 2) + 1):
            for forest, value in counts[r].items():
                used_vertices = len({v for edge in forest for v in edge})
                expected = (m - used_vertices) * math.factorial(m - r - 2)
                one_fixed_checks += 1
                if value != expected:
                    raise ValueError(
                        f"one-fixed cylinder mismatch at m={m}, r={r}"
                    )

    return {
        "maximum_pair_size": max_m,
        "maximum_prescribed_edges": max_edges,
        "full_hamilton_forests_checked": full_checks,
        "one_fixed_forests_checked": one_fixed_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("codes", type=Path)
    parser.add_argument("audit", type=Path)
    args = parser.parse_args()

    try:
        records = json.loads(args.codes.read_text())
        expected = json.loads(args.audit.read_text())
        if not isinstance(records, list) or not records:
            raise ValueError("codes must be a nonempty list")
        if not isinstance(expected, dict):
            raise ValueError("audit object expected")

        no_two_cycle_primes: list[int] = []
        hamilton_primes: list[int] = []
        one_fixed_primes: list[int] = []
        partitions: dict[str, list[int]] = {}

        for index, raw in enumerate(records, 1):
            if not isinstance(raw, dict):
                raise ValueError(f"record {index}: object expected")
            p = raw.get("p")
            if isinstance(p, bool) or not isinstance(p, int) or p < 3 or p % 2 == 0:
                raise ValueError(f"record {index}: odd prime p expected")
            m = (p - 1) // 2
            partition = sorted(int_list(raw, "expected_pair_cycles"), reverse=True)
            if sum(partition) != m:
                raise ValueError(f"p={p}: pair cycle partition does not sum to m")
            partitions[str(p)] = partition
            if 2 not in partition:
                no_two_cycle_primes.append(p)
            if partition == [m]:
                hamilton_primes.append(p)
            if m >= 4 and partition == [m - 1, 1]:
                one_fixed_primes.append(p)

        required = {
            "expected_case_count": len(records),
            "expected_no_pair_two_cycle_primes": no_two_cycle_primes,
            "expected_hamilton_primes": hamilton_primes,
            "expected_one_fixed_near_hamilton_primes": one_fixed_primes,
        }
        for key, value in required.items():
            if expected.get(key) != value:
                raise ValueError(f"{key} mismatch: {value!r} != {expected.get(key)!r}")

        coefficient_max_m = expected.get("coefficient_max_m")
        coefficient_exhaustion_max_m = expected.get("coefficient_exhaustion_max_m")
        cylinder_max_m = expected.get("cylinder_exhaustion_max_m")
        cylinder_max_edges = expected.get("cylinder_max_edges")
        if any(
            isinstance(v, bool) or not isinstance(v, int)
            for v in (
                coefficient_max_m,
                coefficient_exhaustion_max_m,
                cylinder_max_m,
                cylinder_max_edges,
            )
        ):
            raise ValueError("audit limits must be integers")
        if coefficient_exhaustion_max_m > coefficient_max_m:
            raise ValueError("coefficient exhaustion exceeds coefficient table")

        coefficients = []
        for m in range(coefficient_max_m + 1):
            edge_disjoint = egf_count(m, -1, -1)
            two_cycle_free = egf_count(m, -1, -2)
            coefficients.append(
                {
                    "m": m,
                    "canonical_edge_disjoint": edge_disjoint,
                    "canonical_two_cycle_free": two_cycle_free,
                }
            )

        coefficient_exhaustion = exhaustive_coefficient_audit(
            coefficient_exhaustion_max_m
        )
        cylinders = exhaustive_cylinder_audit(cylinder_max_m, cylinder_max_edges)

    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "two_cycle_free_near_hamilton_family_verified",
                "public_code_cases": len(records),
                "all_public_code_cases_two_cycle_free": (
                    len(no_two_cycle_primes) == len(records)
                ),
                "no_pair_two_cycle_primes": no_two_cycle_primes,
                "hamilton_primes": hamilton_primes,
                "one_fixed_near_hamilton_primes": one_fixed_primes,
                "hamilton_or_one_fixed_case_count": (
                    len(hamilton_primes) + len(one_fixed_primes)
                ),
                "pair_cycle_partitions": partitions,
                "coefficient_table": coefficients,
                "coefficient_exhaustion": coefficient_exhaustion,
                "cylinder_audit": cylinders,
                "asymptotic_seed_theorem_proved": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
