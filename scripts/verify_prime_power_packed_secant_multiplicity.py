#!/usr/bin/env python3
"""Finite checks for CMR1742--CMR1749."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import comb, gcd
from random import Random


Point = tuple[int, int]


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def primitive_direction(first: Point, second: Point) -> tuple[int, int]:
    delta_x = second[0] - first[0]
    delta_y = second[1] - first[1]
    divisor = gcd(abs(delta_x), abs(delta_y))
    delta_x //= divisor
    delta_y //= divisor
    if delta_x < 0 or (delta_x == 0 and delta_y < 0):
        delta_x = -delta_x
        delta_y = -delta_y
    return delta_x, delta_y


def packed_value(total: int, maximum: int) -> int:
    quotient, remainder = divmod(total, maximum)
    return quotient * comb(maximum, 2) + comb(remainder, 2)


def main() -> None:
    random = Random(1742)
    partition_checks = 0
    exact_attainment_checks = 0
    linear_checks = 0
    point_systems = 0
    rank_one_checks = 0
    combined_rank_checks = 0

    for _ in range(100_000):
        maximum = random.randint(1, 25)
        parts = [
            random.randint(0, maximum)
            for _ in range(random.randint(1, 35))
        ]
        total = sum(parts)
        packed = packed_value(total, maximum)
        assert sum(comb(part, 2) for part in parts) <= packed
        partition_checks += 1

        quotient, remainder = divmod(total, maximum)
        extremal = [maximum] * quotient
        if remainder:
            extremal.append(remainder)
        assert sum(comb(part, 2) for part in extremal) == packed
        exact_attainment_checks += 1

        assert 2 * packed <= (maximum - 1) * total
        linear_checks += 1

    grid = [(x, y) for x in range(8) for y in range(8)]
    for _ in range(1_200):
        points = random.sample(grid, random.randint(7, 24))
        split = random.randint(3, len(points) - 2)
        background = set(points[:split])
        response = set(points[split:])

        maximum_line_load = 1
        for first, second in combinations(background, 2):
            maximum_line_load = max(
                maximum_line_load,
                sum(
                    collinear(first, second, point)
                    for point in background
                ),
            )

        for response_point in response:
            direction_loads: dict[tuple[int, int], int] = defaultdict(int)
            for point in background:
                direction_loads[
                    primitive_direction(response_point, point)
                ] += 1
            multiplicity = sum(
                comb(height, 2)
                for height in direction_loads.values()
            )
            packed = packed_value(len(background), maximum_line_load)
            assert multiplicity <= packed
            assert 2 * multiplicity <= (
                (maximum_line_load - 1) * len(background)
            )
            rank_one_checks += 1

        maximum_rank_two = 0
        for first, second in combinations(response, 2):
            maximum_rank_two = max(
                maximum_rank_two,
                sum(
                    collinear(first, second, point)
                    for point in background
                ),
            )
        assert maximum_rank_two <= maximum_line_load
        combined_rank_checks += 1
        point_systems += 1

    print(
        "verified packed secant multiplicity bounds: "
        f"{partition_checks} convex-packing inequalities, "
        f"{exact_attainment_checks} exact extremizers, "
        f"{linear_checks} linear relaxations, "
        f"{point_systems} finite point systems, "
        f"{rank_one_checks} rank-one packed bounds and "
        f"{combined_rank_checks} combined rankwise caps"
    )


if __name__ == "__main__":
    main()
