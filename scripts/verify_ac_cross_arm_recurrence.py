#!/usr/bin/env python3
"""Verify AC3hb--AC3he cross-arm pivot recurrence routing."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def verify_weighted_axis_router(max_targets: int = 5, max_weight: int = 4) -> int:
    checks = 0
    for targets in range(1, max_targets + 1):
        for weights in product(range(max_weight + 1), repeat=targets):
            total = sum(weights)
            if total == 0:
                continue
            # Normalize to equality in total >= targets * W / 4.
            w = Fraction(4 * total, targets)
            for mask in range(1 << targets):
                new_weight = sum(
                    weights[i]
                    for i in range(targets)
                    if mask & (1 << i)
                )
                old_weight = total - new_weight
                if 2 * new_weight >= total:
                    heavy = max(
                        (
                            weights[i]
                            for i in range(targets)
                            if mask & (1 << i)
                        ),
                        default=0,
                    )
                    assert targets * heavy >= new_weight
                    assert Fraction(heavy, 1) >= w / 8
                else:
                    assert old_weight > Fraction(total, 2)
                    assert Fraction(old_weight, 1) >= targets * w / 8
                checks += 1
    return checks


def verify_composition(max_weight: int = 100, max_k: int = 20) -> int:
    checks = 0
    for weight in range(1, max_weight + 1):
        for k in range(1, max_k + 1):
            assert 8 * k * Fraction(weight, 8 * k) == weight
            assert 24 * k * Fraction(weight, 24 * k) == weight
            assert 4 * k * Fraction(weight, 4 * k) == weight
            assert 12 * k * Fraction(weight, 12 * k) == weight
            checks += 1
    return checks


def verify_axis_potential(
    max_objects: int = 8,
    max_signatures: int = 8,
    max_n: int = 5,
) -> int:
    checks = 0
    for object_count in range(1, max_objects + 1):
        for signature_count in range(max_signatures + 1):
            for n in range(3, max_n + 1):
                ceiling = (
                    object_count * (signature_count + n * n)
                    + object_count
                    - 1
                )
                for exposed_signatures in range(signature_count + 1):
                    for exposed_cells in range(n * n + 1):
                        for support in range(1, object_count + 1):
                            value = (
                                object_count
                                * (exposed_signatures + exposed_cells)
                                + object_count
                                - support
                            )
                            assert 0 <= value <= ceiling
                            if support > 1:
                                next_value = (
                                    object_count
                                    * (exposed_signatures + exposed_cells)
                                    + object_count
                                    - (support - 1)
                                )
                                assert next_value >= value + 1
                                checks += 1
                            if exposed_signatures < signature_count:
                                next_value = (
                                    object_count
                                    * (exposed_signatures + 1 + exposed_cells)
                                )
                                assert next_value >= value + 1
                                checks += 1
                            if exposed_cells < n * n:
                                next_value = (
                                    object_count
                                    * (exposed_signatures + exposed_cells + 1)
                                )
                                assert next_value >= value + 1
                                checks += 1
    return checks


def main() -> None:
    weighted = verify_weighted_axis_router()
    constants = verify_composition()
    potential = verify_axis_potential()
    print(
        "AC cross-arm recurrence verified:",
        f"{weighted} weighted new/old pivot routers,",
        f"{constants} composition constants,",
        f"{potential} combined-potential transitions",
    )


if __name__ == "__main__":
    main()
