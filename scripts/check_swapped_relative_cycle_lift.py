#!/usr/bin/env python3
"""Exhaustively verify swapped-quarter-turn cycle lifts and cover counts."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


def require_int(value: Any, label: str, minimum: int = 0, maximum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{label}: expected integer <= {maximum}")
    return value


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


def cycles_with_vertices(permutation: tuple[int, ...]) -> list[list[int]]:
    seen = [False] * len(permutation)
    cycles: list[list[int]] = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        cycle: list[int] = []
        while not seen[current]:
            seen[current] = True
            cycle.append(current)
            current = permutation[current]
        cycles.append(cycle)
    return cycles


def signed_sigma(rho: tuple[int, ...], orientations: list[int]) -> list[int]:
    m = len(rho)
    n = 2 * m
    sigma = [0] * n
    for pair in range(m):
        for bit in (0, 1):
            column = pair if bit == 0 else n - 1 - pair
            target_pair = rho[pair]
            target_bit = bit ^ orientations[pair]
            sigma[column] = target_pair if target_bit == 0 else n - 1 - target_pair
    return sigma


def direct_relative(
    rho: tuple[int, ...], orientations: list[int]
) -> tuple[list[int], list[int], list[int]]:
    sigma = signed_sigma(rho, orientations)
    n = len(sigma)
    inverse = [0] * n
    for column, row in enumerate(sigma):
        inverse[row] = column
    reversal = [n - 1 - column for column in range(n)]
    tau = [inverse[reversal[column]] for column in range(n)]
    relative = [inverse[tau[column]] for column in range(n)]
    return sigma, tau, relative


def predicted_relative_partition(
    rho: tuple[int, ...], orientations: list[int]
) -> list[int]:
    predicted: list[int] = []
    for cycle in cycles_with_vertices(rho):
        length = len(cycle)
        if length % 2 == 1:
            predicted.append(2 * length)
            continue
        delta = (length // 2) & 1
        for pair in cycle:
            delta ^= orientations[pair]
        if delta:
            predicted.extend((length, length))
        else:
            predicted.extend([length // 2] * 4)
    return sorted(predicted, reverse=True)


def coefficient(m: int, kind: str) -> int:
    total = Fraction(0)
    if kind == "ordered_valid":
        # exp(-z^2)/(1-2z)
        for square_power in range(m // 2 + 1):
            total += Fraction(
                (-1) ** square_power * 2 ** (m - 2 * square_power),
                math.factorial(square_power),
            )
    elif kind == "canonical_total":
        # exp(-z)/(1-2z)
        for linear_power in range(m + 1):
            total += Fraction(
                (-1) ** linear_power * 2 ** (m - linear_power),
                math.factorial(linear_power),
            )
    elif kind == "canonical_valid":
        # exp(-z-z^2)/(1-2z)
        for linear_power in range(m + 1):
            for square_power in range((m - linear_power) // 2 + 1):
                total += Fraction(
                    (-1) ** (linear_power + square_power)
                    * 2 ** (m - linear_power - 2 * square_power),
                    math.factorial(linear_power) * math.factorial(square_power),
                )
    else:
        raise ValueError(f"unknown coefficient kind {kind!r}")
    value = total * math.factorial(m)
    if value.denominator != 1:
        raise ValueError(f"nonintegral coefficient for m={m}, kind={kind}")
    return value.numerator


def verify(max_pair_vertices: int) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    signed_permutations_tested = 0

    for m in range(max_pair_vertices + 1):
        ordered_edge_disjoint = 0
        canonical_orbit_covers = 0
        canonical_edge_disjoint = 0

        for rho in itertools.permutations(range(m)):
            for orientation_mask in range(1 << m):
                orientations = [
                    (orientation_mask >> pair) & 1 for pair in range(m)
                ]
                sigma, tau, relative = direct_relative(rho, orientations)

                collision = any(
                    sigma[column] == tau[column] for column in range(2 * m)
                )
                opposite_sign_two_cycle = any(
                    pair < rho[pair]
                    and rho[rho[pair]] == pair
                    and (orientations[pair] ^ orientations[rho[pair]])
                    for pair in range(m)
                )
                if collision != opposite_sign_two_cycle:
                    raise ValueError(
                        f"m={m}: collision and two-cycle criteria disagree"
                    )

                direct_partition = cycle_partition(relative)
                predicted_partition = predicted_relative_partition(rho, orientations)
                if direct_partition != predicted_partition:
                    raise ValueError(
                        f"m={m}: direct relative cycles {direct_partition} "
                        f"!= predicted {predicted_partition}"
                    )

                if not collision:
                    ordered_edge_disjoint += 1
                    multiplicities = {
                        length: direct_partition.count(length)
                        for length in set(direct_partition)
                    }
                    if any(
                        length % 2 == 1 and multiplicity % 4 != 0
                        for length, multiplicity in multiplicities.items()
                    ):
                        raise ValueError(
                            f"m={m}: odd relative-cycle multiplicity is not divisible by four"
                        )

                canonical = all(
                    rho[pair] != pair or orientations[pair] == 0
                    for pair in range(m)
                )
                if canonical:
                    canonical_orbit_covers += 1
                    if not collision:
                        canonical_edge_disjoint += 1

                signed_permutations_tested += 1

        expected = {
            "ordered_edge_disjoint": coefficient(m, "ordered_valid"),
            "canonical_orbit_covers": coefficient(m, "canonical_total"),
            "canonical_edge_disjoint": coefficient(m, "canonical_valid"),
        }
        observed = {
            "ordered_edge_disjoint": ordered_edge_disjoint,
            "canonical_orbit_covers": canonical_orbit_covers,
            "canonical_edge_disjoint": canonical_edge_disjoint,
        }
        if observed != expected:
            raise ValueError(
                f"m={m}: observed counts {observed} != exact coefficients {expected}"
            )

        rows.append(
            {
                "m": m,
                "ordered_signed_permutations": (1 << m) * math.factorial(m),
                **observed,
            }
        )

    return {
        "outcome": "swapped_relative_cycle_lift_verified",
        "max_pair_vertices": max_pair_vertices,
        "signed_permutations_tested": signed_permutations_tested,
        "counts": rows,
        "ordered_edge_disjoint_limit": "exp(-1/4)",
        "canonical_edge_disjoint_limit": "exp(-1/4)",
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
            raw.get("max_pair_vertices", 7),
            "max_pair_vertices",
            minimum=0,
            maximum=8,
        )
        result = verify(max_pair_vertices)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
