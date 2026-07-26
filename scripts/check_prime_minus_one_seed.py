#!/usr/bin/env python3
"""Verify prime-minus-one seed certificates given by two permutations."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def is_prime(p: int) -> bool:
    if p < 2:
        return False
    if p % 2 == 0:
        return p == 2
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def verify_case(raw: Any, ordinal: int) -> dict[str, Any]:
    if not isinstance(raw, dict):
        raise ValueError(f"case {ordinal}: expected object")
    p = require_int(raw.get("p"), f"case {ordinal}.p", 3)
    if not is_prime(p):
        raise ValueError(f"case {ordinal}.p={p} is not prime")
    n = p - 1

    layers: list[list[int]] = []
    for name in ("sigma", "tau"):
        values = raw.get(name)
        if not isinstance(values, list):
            raise ValueError(f"case {ordinal}.{name}: expected list")
        layer = [require_int(v, f"case {ordinal}.{name} entry", 1) for v in values]
        if len(layer) != n:
            raise ValueError(f"case {ordinal}.{name}: expected length {n}")
        if sorted(layer) != list(range(1, n + 1)):
            raise ValueError(f"case {ordinal}.{name}: expected a permutation of 1..{n}")
        layers.append(layer)

    sigma, tau = layers
    collisions = [i + 1 for i in range(n) if sigma[i] == tau[i]]
    if collisions:
        raise ValueError(f"case {ordinal}: layers share cells in columns {collisions}")

    points = [(i + 1, sigma[i]) for i in range(n)]
    points.extend((i + 1, tau[i]) for i in range(n))
    if len(set(points)) != 2 * n:
        raise ValueError(f"case {ordinal}: duplicate cells")

    determinant_checks = 0
    minimum_abs_determinant: int | None = None
    for a, b, c in combinations(points, 3):
        value = determinant(a, b, c)
        determinant_checks += 1
        if value == 0:
            raise ValueError(f"case {ordinal}: collinear triple {a}, {b}, {c}")
        absolute = abs(value)
        minimum_abs_determinant = (
            absolute
            if minimum_abs_determinant is None
            else min(minimum_abs_determinant, absolute)
        )

    return {
        "p": p,
        "n": n,
        "point_count": len(points),
        "permutation_layers": 2,
        "edge_disjoint": True,
        "saturated": True,
        "no_three_in_line": True,
        "determinant_checks": determinant_checks,
        "minimum_absolute_determinant": minimum_abs_determinant,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        cases = payload if isinstance(payload, list) else [payload]
        if not cases:
            raise ValueError("expected at least one seed case")
        checked = [verify_case(raw, i + 1) for i, raw in enumerate(cases)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "prime_minus_one_seed_certificates_verified",
                "case_count": len(checked),
                "cases": checked,
                "largest_prime": max(case["p"] for case in checked),
                "asymptotic_seed_theorem_proved": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
