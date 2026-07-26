#!/usr/bin/env python3
"""Finite checks for CMR1590--CMR1597."""

from __future__ import annotations

from fractions import Fraction
from random import Random


def class_pair(side: int, kind: str) -> tuple[int, int]:
    if kind == "strong":
        return side - 2, 1
    if kind == "singleton":
        return (side - 1) * (side - 3), side - 2
    if kind == "overlap":
        return side - 3, 1
    raise ValueError(kind)


def weighted_count(
    side: int,
    v1: int,
    v2: int,
    v3: int,
    unavailable: int,
    potential: int,
) -> int:
    return (
        (side - 1) * (side - 2) * v1
        + (side - 2) * v2
        + v3
        + (potential + 1) * unavailable * (side - 1) * (side - 2)
    )


def budget(side: int, u: int, v: int, destroyed: int) -> int:
    numerator = destroyed * (u**side) * side * (side - 1) * (side - 2) - 1
    denominator = (side * v) ** side
    return numerator // denominator


def verify_random_instances(seed: int = 1597) -> tuple[int, int, int]:
    rng = Random(seed)
    checked = 0
    positive = 0
    rank_pure = 0

    for side in range(4, 31):
        falling3 = side * (side - 1) * (side - 2)
        for kind in ("strong", "singleton", "overlap"):
            u, v = class_pair(side, kind)
            kappa = Fraction((side * v) ** side, u**side)
            for _ in range(420):
                v1 = rng.randint(0, 4 * side)
                v2 = rng.randint(0, 6 * side)
                v3 = rng.randint(0, 10 * side)
                unavailable = rng.randint(0, side)
                potential = rng.randint(0, 5 * side)
                destroyed = rng.randint(0, 8 * side)

                w = weighted_count(side, v1, v2, v3, unavailable, potential)
                bracket = (
                    Fraction(v1, side)
                    + Fraction(v2, side * (side - 1))
                    + Fraction(v3, falling3)
                    + Fraction((potential + 1) * unavailable, side)
                )
                assert bracket == Fraction(w, falling3)

                rational = kappa * bracket < destroyed
                integer = (
                    (side * v) ** side * w
                    < destroyed * (u**side) * falling3
                )
                assert rational == integer

                bound = budget(side, u, v, destroyed)
                assert integer == (w <= bound)
                slack = (
                    destroyed * (u**side) * falling3
                    - (side * v) ** side * w
                )
                assert integer == (slack > 0)
                if integer:
                    positive += 1

                base = (
                    (side - 1) * (side - 2) * v1
                    + (side - 2) * v2
                    + v3
                )
                cost = (potential + 1) * (side - 1) * (side - 2)
                if base <= bound:
                    bmax = (bound - base) // cost
                    assert unavailable <= bmax if integer else True
                    assert weighted_count(
                        side, v1, v2, v3, bmax, potential
                    ) <= bound
                    assert weighted_count(
                        side, v1, v2, v3, bmax + 1, potential
                    ) > bound

                checked += 1

            for destroyed in range(1, 5 * side + 1):
                bound = budget(side, u, v, destroyed)
                costs = ((side - 1) * (side - 2), side - 2, 1)
                for cost in costs:
                    threshold = bound // cost
                    if threshold >= 0:
                        assert threshold * cost <= bound
                        assert (threshold + 1) * cost > bound
                    rank_pure += 1

    return checked, positive, rank_pure


def verify_class_order() -> int:
    checked = 0
    for side in range(4, 100):
        strong_u, strong_v = class_pair(side, "strong")
        single_u, single_v = class_pair(side, "singleton")
        overlap_u, overlap_v = class_pair(side, "overlap")
        strong = Fraction((side * strong_v) ** side, strong_u**side)
        single = Fraction((side * single_v) ** side, single_u**side)
        overlap = Fraction((side * overlap_v) ** side, overlap_u**side)
        assert strong < single < overlap
        checked += 1
    return checked


def verify_monotonicity() -> int:
    checked = 0
    for side in range(4, 35):
        for kind in ("strong", "singleton", "overlap"):
            u, v = class_pair(side, kind)
            last = budget(side, u, v, 0)
            for destroyed in range(1, 100):
                current = budget(side, u, v, destroyed)
                assert current >= last
                last = current
                checked += 1
    return checked


def main() -> None:
    checked, positive, rank_pure = verify_random_instances()
    order = verify_class_order()
    monotone = verify_monotonicity()
    print(
        "verified line-clean integer budgets: "
        f"{checked} mixed rational/integer comparisons with {positive} positive slacks, "
        f"{rank_pure} exact rank-pure thresholds, {order} coefficient order checks, "
        f"and {monotone} monotone destroyed-load budgets"
    )


if __name__ == "__main__":
    main()
