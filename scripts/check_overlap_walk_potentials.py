#!/usr/bin/env python3
"""Verify the monotone finite-depth overlap-walk certificates PP3bwl--PP3bwo."""

from __future__ import annotations

import json
from fractions import Fraction


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((entry * value for entry, value in zip(row, vector)), Fraction()) for row in matrix]


def main() -> None:
    # Unit-capacity neighbourhoods:
    # x0={a,b,c,d}, x1={c,d,e,f}, x2={d,f,g,h}.
    overlap = [
        [4, 2, 1],
        [2, 4, 2],
        [1, 2, 4],
    ]
    degree = [4, 4, 4]
    kernel = [
        [Fraction(overlap[i][j], degree[i]) for j in range(3)]
        for i in range(3)
    ]

    potential = [Fraction(1) for _ in range(3)]
    rows = []
    previous_upper: Fraction | None = None
    previous_lower: Fraction | None = None
    for depth in range(9):
        next_potential = matvec(kernel, potential)
        ratios = [next_potential[i] / potential[i] for i in range(3)]
        lower = min(ratios)
        upper = max(ratios)
        if previous_upper is not None:
            assert upper <= previous_upper
            assert lower >= previous_lower  # type: ignore[operator]
        rows.append(
            {
                "depth": depth,
                "lower_collatz_ratio": str(lower),
                "upper_collatz_ratio": str(upper),
                "potential": [str(value) for value in potential],
            }
        )
        previous_lower = lower
        previous_upper = upper
        potential = next_potential

    assert rows[0]["upper_collatz_ratio"] == "2"
    assert Fraction(rows[-1]["upper_collatz_ratio"]) < Fraction(19, 10)
    print(json.dumps({"rows": rows, "all_checks_passed": True}, indent=2))


if __name__ == "__main__":
    main()
