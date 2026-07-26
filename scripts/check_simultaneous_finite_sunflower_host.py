#!/usr/bin/env python3
"""Finite checker for simultaneous optional-core and empty-core support avoidance."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any


def falling(n: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= n - j
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    N = int(data["N"])
    b = int(data["b"])
    omitted = set(map(int, data["omitted_core_indices"]))
    residual_objective = Fraction(str(data["residual_objective"]))
    families = [
        [frozenset(map(int, edge)) for edge in family]
        for family in data["empty_core_families"]
    ]

    centre = N - 1
    if centre in omitted:
        raise ValueError("marked centre cannot be omitted")
    available = [v for v in range(N) if v != centre and v not in omitted]
    helper_size = b - 1
    if helper_size > len(available):
        raise ValueError("not enough available helpers")

    for family in families:
        used: set[int] = set()
        for edge in family:
            if len(edge) < 2:
                raise ValueError("empty-core supports must have size at least two")
            if edge & omitted or centre in edge:
                raise ValueError("empty-core support uses omitted/core index")
            if used & edge:
                raise ValueError("petals must be disjoint within one family")
            used |= set(edge)

    blocks = [frozenset(B) for B in combinations(available, helper_size)]
    total_selected = 0
    zero_blocks = 0
    max_selected = 0
    for block in blocks:
        count = sum(edge.issubset(block) for family in families for edge in family)
        total_selected += count
        max_selected = max(max_selected, count)
        if count == 0:
            zero_blocks += 1

    exact_expectation = Fraction(total_selected, len(blocks))
    formula_expectation = Fraction(0, 1)
    N_prime = len(available)
    for family in families:
        for edge in family:
            s = len(edge)
            formula_expectation += Fraction(falling(helper_size, s), falling(N_prime, s))

    if exact_expectation != formula_expectation:
        raise AssertionError((exact_expectation, formula_expectation))

    union_bound = Fraction(2 * len(families) * b * b, N)
    combined = residual_objective + exact_expectation
    if combined >= 1:
        raise AssertionError("stored residual plus target expectation must be below one")
    if zero_blocks == 0:
        raise AssertionError("there must be at least one simultaneously avoiding block")

    print(f"N {N}")
    print(f"b {b}")
    print(f"omitted optional cores {len(omitted)}")
    print(f"available helpers {N_prime}")
    print(f"empty-core families {len(families)}")
    print(f"uniform helper blocks {len(blocks)}")
    print(f"exact target-support expectation {float(exact_expectation):.12f}")
    print(f"formula target-support expectation {float(formula_expectation):.12f}")
    print(f"coarse 2Lb^2/N bound {float(union_bound):.12f}")
    print(f"zero-target block fraction {zero_blocks/len(blocks):.12f}")
    print(f"maximum target supports in one block {max_selected}")
    print(f"residual objective {float(residual_objective):.12f}")
    print(f"combined objective {float(combined):.12f}")
    print("outcome simultaneous_finite_sunflower_host")


if __name__ == "__main__":
    main()
