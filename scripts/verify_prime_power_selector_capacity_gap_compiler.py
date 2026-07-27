#!/usr/bin/env python3
"""Finite checks for CMR1646--CMR1653."""

from __future__ import annotations

from fractions import Fraction
from math import floor
from random import Random


def main() -> None:
    random = Random(1646)
    systems = 0
    positive_gaps = 0
    exact_restoration_caps = 0
    critical_exclusions = 0

    for _ in range(50_000):
        denominator = random.randint(1, 10_000)
        side = random.randint(2, 80)
        class_count = random.randint(1, 25)
        capacities = [
            random.randint(0, max(1, denominator // class_count))
            for _ in range(class_count)
        ]

        if random.random() < 0.7:
            total = max(1, sum(capacities))
            target = random.randint(0, denominator - 1)
            capacities = [capacity * target // total for capacity in capacities]

        actual_numerators = [
            random.randint(0, capacity) for capacity in capacities
        ]
        total_capacity = sum(capacities)
        total_actual = sum(actual_numerators)
        unavailable_edges = random.randint(0, 100)

        if total_capacity < denominator:
            gap = Fraction(denominator - total_capacity, denominator)
            assert Fraction(total_actual, denominator) <= 1 - gap

            rational_cap = floor(
                Fraction(2 * denominator, denominator - total_capacity)
                + Fraction(
                    denominator * unavailable_edges,
                    (side - 1) * (denominator - total_capacity),
                )
            )
            integer_cap = (
                denominator * (2 * (side - 1) + unavailable_edges)
            ) // ((side - 1) * (denominator - total_capacity))
            assert rational_cap == integer_cap

            positive_gaps += 1
            exact_restoration_caps += 1
            assert total_actual < denominator
            critical_exclusions += 1

        systems += 1

    print(
        "verified selector capacity-to-gap certificates: "
        f"{systems} class systems, "
        f"{positive_gaps} positive capacity gaps, "
        f"{exact_restoration_caps} exact restoration caps and "
        f"{critical_exclusions} critical-state exclusions"
    )


if __name__ == "__main__":
    main()
