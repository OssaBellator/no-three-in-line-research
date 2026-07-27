#!/usr/bin/env python3
"""Exhaustively audit first-layer collinearity in edge-disjoint signed states."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def require_int(value: Any, label: str, minimum: int, maximum: int) -> int:
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or value < minimum
        or value > maximum
    ):
        raise ValueError(f"{label}: expected integer in {minimum}..{maximum}")
    return value


def edge_disjoint(rho: tuple[int, ...], orientations: list[int]) -> bool:
    return not any(
        pair < rho[pair]
        and rho[rho[pair]] == pair
        and (orientations[pair] ^ orientations[rho[pair]])
        for pair in range(len(rho))
    )


def signed_sigma(rho: tuple[int, ...], orientations: list[int]) -> list[int]:
    m = len(rho)
    n = 2 * m
    sigma = [0] * n
    for pair in range(m):
        for bit in (0, 1):
            column = pair if bit == 0 else n - 1 - pair
            target_pair = rho[pair]
            target_bit = bit ^ orientations[pair]
            sigma[column] = (
                target_pair if target_bit == 0 else n - 1 - target_pair
            )
    return sigma


def determinant(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )


def ordered_edge_disjoint_count(m: int) -> int:
    coefficient = sum(
        Fraction(
            (-1) ** square_power * 2 ** (m - 2 * square_power),
            math.factorial(square_power),
        )
        for square_power in range(m // 2 + 1)
    )
    value = coefficient * math.factorial(m)
    if value.denominator != 1:
        raise ValueError(f"nonintegral ordered count coefficient for m={m}")
    return value.numerator


def verify(max_pair_vertices: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    states_tested = 0
    determinant_checks = 0

    for m in range(2, max_pair_vertices + 1):
        n = 2 * m
        column_triples = list(itertools.combinations(range(n), 3))
        state_count = 0
        collinear_total = 0

        for rho in itertools.permutations(range(m)):
            for orientation_mask in range(1 << m):
                orientations = [
                    (orientation_mask >> pair) & 1 for pair in range(m)
                ]
                if not edge_disjoint(rho, orientations):
                    continue

                state_count += 1
                states_tested += 1
                sigma = signed_sigma(rho, orientations)
                for first, second, third in column_triples:
                    determinant_checks += 1
                    if determinant(
                        (first, sigma[first]),
                        (second, sigma[second]),
                        (third, sigma[third]),
                    ) == 0:
                        collinear_total += 1

        expected_count = ordered_edge_disjoint_count(m)
        if state_count != expected_count:
            raise ValueError(
                f"m={m}: enumerated {state_count} states != exact count {expected_count}"
            )

        mean = Fraction(collinear_total, state_count)
        rows.append(
            {
                "m": m,
                "n": n,
                "ordered_edge_disjoint_states": state_count,
                "determinant_checks": state_count * len(column_triples),
                "same_layer_collinear_triples_total": collinear_total,
                "mean_numerator": mean.numerator,
                "mean_denominator": mean.denominator,
                "mean_float": float(mean),
            }
        )

    return {
        "outcome": "swapped_edge_disjoint_first_moment_verified",
        "max_pair_vertices": max_pair_vertices,
        "states_tested": states_tested,
        "determinant_checks": determinant_checks,
        "cases": rows,
        "asymptotic_seed_theorem_proved": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("input must be one JSON object")
        max_pair_vertices = require_int(
            raw.get("max_pair_vertices", 6),
            "max_pair_vertices",
            minimum=2,
            maximum=6,
        )
        result = verify(max_pair_vertices)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
