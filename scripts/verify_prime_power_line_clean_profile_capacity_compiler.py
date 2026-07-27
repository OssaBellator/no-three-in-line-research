#!/usr/bin/env python3
"""Finite checks for CMR1678--CMR1685."""

from __future__ import annotations

from fractions import Fraction
from math import ceil, floor
from random import Random


def main() -> None:
    random = Random(1678)
    systems = 0
    overflow_checks = 0
    mixed_checks = 0

    for _ in range(6_000):
        side = random.randint(4, 30)
        destroyed_load = random.randint(0, 100)
        class_count = random.randint(1, 20)
        ranks = [random.randint(1, 3) for _ in range(class_count)]
        rank_cost = {
            1: (side - 1) * (side - 2),
            2: side - 2,
            3: 1,
        }
        capacities = [random.randint(0, 30) for _ in range(class_count)]
        actual_counts = [
            random.randint(0, capacity) for capacity in capacities
        ]
        potential = random.randint(0, 20)
        unavailable_cap = random.randint(0, 10)
        unavailable_count = random.randint(0, unavailable_cap)

        capacity_weight = sum(
            rank_cost[rank] * capacity
            for rank, capacity in zip(ranks, capacities)
        ) + (
            (potential + 1)
            * unavailable_cap
            * (side - 1)
            * (side - 2)
        )
        exact_weight = sum(
            rank_cost[rank] * count
            for rank, count in zip(ranks, actual_counts)
        ) + (
            (potential + 1)
            * unavailable_count
            * (side - 1)
            * (side - 2)
        )
        assert exact_weight <= capacity_weight

        coefficient_type = random.randrange(3)
        if coefficient_type == 0:
            numerator, denominator = side - 2, 1
            universal_ratio = Fraction(1, 16)
        elif coefficient_type == 1:
            numerator = (side - 1) * (side - 3)
            denominator = side - 2
            universal_ratio = Fraction(81, 4096)
        else:
            numerator, denominator = side - 3, 1
            universal_ratio = Fraction(1, 256)

        exact_budget = floor(
            Fraction(
                destroyed_load
                * numerator**side
                * side
                * (side - 1)
                * (side - 2)
                - 1,
                (side * denominator) ** side,
            )
        )
        universal_budget = (
            ceil(
                Fraction(
                    destroyed_load * side * (side - 1) * (side - 2)
                )
                * universal_ratio
            )
            - 1
        )
        if destroyed_load >= 1:
            assert universal_budget <= exact_budget

        if capacity_weight <= exact_budget:
            assert (
                (side * denominator) ** side * exact_weight
                < destroyed_load
                * numerator**side
                * side
                * (side - 1)
                * (side - 2)
            )

        coordinate_count = class_count + 1
        tested_budget = random.randint(0, max(0, exact_weight + 20))
        if exact_weight > tested_budget:
            coordinates = [
                rank_cost[rank] * count
                for rank, count in zip(ranks, actual_counts)
            ] + [
                (potential + 1)
                * unavailable_count
                * (side - 1)
                * (side - 2)
            ]
            threshold = tested_budget // coordinate_count + 1
            assert max(coordinates) >= threshold

            witness = max(range(coordinate_count), key=coordinates.__getitem__)
            if witness < class_count:
                assert actual_counts[witness] >= ceil(
                    Fraction(threshold, rank_cost[ranks[witness]])
                )
            else:
                unavailable_cost = (
                    (potential + 1) * (side - 1) * (side - 2)
                )
                assert unavailable_count >= ceil(
                    Fraction(threshold, unavailable_cost)
                )
            overflow_checks += 1

        exact_prefix = random.randint(0, class_count)
        mixed_weight = sum(
            rank_cost[rank] * count
            for rank, count in zip(
                ranks[:exact_prefix], actual_counts[:exact_prefix]
            )
        ) + sum(
            rank_cost[rank] * capacity
            for rank, capacity in zip(
                ranks[exact_prefix:], capacities[exact_prefix:]
            )
        ) + (
            (potential + 1)
            * unavailable_cap
            * (side - 1)
            * (side - 2)
        )
        assert exact_weight <= mixed_weight
        mixed_checks += 1
        systems += 1

    print(
        "verified line-clean profile capacities: "
        f"{systems} capacity systems, "
        f"{overflow_checks} overflow localizations and "
        f"{mixed_checks} mixed exact/residual slack checks"
    )


if __name__ == "__main__":
    main()
