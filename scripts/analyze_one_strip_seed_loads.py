#!/usr/bin/env python3
"""Evaluate the averaging criterion for boundary-only one-strip seed preparation."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_one_strip_extensions import Point, determinant, parse_cases


def analyze_seed(core: tuple[Point, ...], m: int) -> dict[str, Any]:
    q = m + 1
    boundary_cells = tuple(
        [(x, q) for x in range(1, m + 1)]
        + [(q, y) for y in range(1, m + 1)]
    )
    old_pairs = tuple(combinations(core, 2))
    secant_cells = {
        cell
        for cell in boundary_cells
        if any(determinant(first, second, cell) == 0 for first, second in old_pairs)
    }

    core_set = frozenset(core)
    occupied_mixed_pairs = 0
    empty_mixed_pairs = 0
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            top = (x, q)
            right = (q, y)
            if not any(determinant(top, right, anchor) == 0 for anchor in core):
                continue
            if (x, y) in core_set:
                occupied_mixed_pairs += 1
            else:
                empty_mixed_pairs += 1

    type_two_states = m * (2 * m - 3)
    expected_bound = (
        Fraction(2 * len(secant_cells), m)
        + Fraction(
            occupied_mixed_pairs + 4 * empty_mixed_pairs,
            type_two_states,
        )
    )
    return {
        "source_n": m,
        "type_two_states": type_two_states,
        "boundary_secant_cells": len(secant_cells),
        "bad_mixed_pairs_at_selected_cells": occupied_mixed_pairs,
        "bad_mixed_pairs_at_empty_cells": empty_mixed_pairs,
        "averaging_bound_fraction": (
            f"{expected_bound.numerator}/{expected_bound.denominator}"
        ),
        "averaging_bound_decimal": float(expected_bound),
        "criterion_passes": expected_bound < 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int, help="analyze only this side length from a list")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        cases = parse_cases(args.certificate)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    if args.n is not None:
        cases = [case for case in cases if case[0] == args.n]
        if not cases:
            raise SystemExit(f"no certificate with n={args.n}")

    results = [analyze_seed(core, n) for n, core in cases]
    payload: Any = results[0] if len(results) == 1 else results
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
