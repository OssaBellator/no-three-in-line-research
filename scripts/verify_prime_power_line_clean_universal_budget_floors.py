#!/usr/bin/env python3
"""Finite checks for CMR1638--CMR1645."""

from __future__ import annotations

from fractions import Fraction
from math import ceil


def main() -> None:
    previous: tuple[Fraction, Fraction, Fraction] | None = None
    monotonicity_checks = 0
    destroyed_load_checks = 0
    rank_weight_checks = 0

    for side in range(4, 501):
        ratios = (
            Fraction(side - 2, side) ** side,
            Fraction((side - 1) * (side - 3), side * (side - 2)) ** side,
            Fraction(side - 3, side) ** side,
        )
        universal_floors = (
            Fraction(1, 16),
            Fraction(81, 4096),
            Fraction(1, 256),
        )

        for ratio, floor_value in zip(ratios, universal_floors):
            assert ratio >= floor_value

        if previous is not None:
            for ratio, old_ratio in zip(ratios, previous):
                assert ratio > old_ratio
                monotonicity_checks += 1
        previous = ratios

        falling_three = side * (side - 1) * (side - 2)
        for destroyed_load in range(1, 121):
            for ratio, floor_value in zip(ratios, universal_floors):
                universal_budget = (
                    ceil(Fraction(destroyed_load * falling_three) * floor_value)
                    - 1
                )
                assert Fraction(universal_budget) < (
                    Fraction(destroyed_load * falling_three) * ratio
                )

                for weighted_count in {
                    0,
                    max(0, universal_budget // 2),
                    max(0, universal_budget),
                }:
                    if weighted_count <= universal_budget:
                        assert Fraction(weighted_count) < (
                            Fraction(destroyed_load * falling_three) * ratio
                        )
                    rank_weight_checks += 1
                destroyed_load_checks += 1

    print(
        "verified universal line-clean floors: "
        f"{monotonicity_checks} strict monotonicity steps, "
        f"{destroyed_load_checks} destroyed-load budgets and "
        f"{rank_weight_checks} rank-weight checks through side 500"
    )


if __name__ == "__main__":
    main()
