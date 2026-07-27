#!/usr/bin/env python3
"""Finite checks for CMR1734--CMR1741."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations
from math import comb, gcd
from random import Random


Point = tuple[int, int]
Prescription = frozenset[Point]


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


def main() -> None:
    random = Random(1734)
    grid = [(x, y) for x in range(7) for y in range(7)]
    systems = 0
    collinear_triples = 0
    rank_one_checks = 0
    rank_two_checks = 0
    rank_three_checks = 0
    line_height_checks = 0
    direction_checks = 0

    for _ in range(1_200):
        points = random.sample(grid, random.randint(6, 20))
        split = random.randint(2, len(points) - 2)
        background = set(points[:split])
        response = set(points[split:])

        multiplicity: dict[Prescription, int] = defaultdict(int)
        for triple in combinations(background.union(response), 3):
            if not collinear(*triple):
                continue
            prescription = frozenset(set(triple).intersection(response))
            if 1 <= len(prescription) <= 3:
                multiplicity[prescription] += 1
                collinear_triples += 1

        maximum_background_line_load = 0
        for first, second in combinations(background, 2):
            line_load = sum(
                collinear(first, second, point)
                for point in background
            )
            maximum_background_line_load = max(
                maximum_background_line_load,
                line_load,
            )

        for prescription, count in multiplicity.items():
            rank = len(prescription)
            if rank == 3:
                assert count == 1
                rank_three_checks += 1
                continue

            if rank == 2:
                first, second = tuple(prescription)
                expected = sum(
                    collinear(first, second, point)
                    for point in background
                )
                assert count == expected
                assert count <= maximum_background_line_load
                rank_two_checks += 1
                line_height_checks += 1
                continue

            response_point = next(iter(prescription))
            direction_loads: dict[tuple[int, int], int] = defaultdict(int)
            for point in background:
                direction_loads[
                    primitive_direction(response_point, point)
                ] += 1

            expected = sum(
                comb(height, 2)
                for height in direction_loads.values()
            )
            assert count == expected
            assert count <= comb(len(background), 2)

            heavy_directions = sum(
                height >= 2 for height in direction_loads.values()
            )
            if maximum_background_line_load >= 2:
                assert count <= (
                    heavy_directions
                    * comb(maximum_background_line_load, 2)
                )
            else:
                assert count == 0

            rank_one_checks += 1
            line_height_checks += 2
            direction_checks += 1

        systems += 1

    print(
        "verified geometric prescription multiplicities: "
        f"{systems} finite point systems, "
        f"{collinear_triples} collinear triples, "
        f"{rank_one_checks} rank-one secant formulas, "
        f"{rank_two_checks} rank-two line-load formulas, "
        f"{rank_three_checks} rank-three injectivity checks, "
        f"{line_height_checks} line-height bounds and "
        f"{direction_checks} primitive-direction decompositions"
    )


if __name__ == "__main__":
    main()
