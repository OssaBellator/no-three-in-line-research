#!/usr/bin/env python3
"""Finite checks for CMR1750--CMR1757."""

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


def main() -> None:
    local_inequalities = 0
    explicit_pair_maps = 0
    explicit_point_maps = 0

    for height in range(0, 501):
        assert comb(height, 2) <= (
            (1 if height == 2 else 0) + 3 * comb(height, 3)
        )
        assert height <= 2 + comb(height, 3)
        local_inequalities += 2

        if 3 <= height <= 30:
            pairs = list(combinations(range(height), 2))
            triple_slots = [
                (triple, slot)
                for triple in combinations(range(height), 3)
                for slot in range(3)
            ]
            assert len(pairs) <= len(triple_slots)
            assignment = dict(zip(pairs, triple_slots))
            assert len(set(assignment.values())) == len(assignment)
            explicit_pair_maps += 1

            remaining_points = list(range(2, height))
            triples = list(combinations(range(height), 3))
            assert len(remaining_points) <= len(triples)
            point_assignment = dict(zip(remaining_points, triples))
            assert len(set(point_assignment.values())) == len(point_assignment)
            explicit_point_maps += 1

    random = Random(1750)
    grid = [(x, y) for x in range(8) for y in range(8)]
    point_systems = 0
    rank_one_shadow_checks = 0
    rank_two_shadow_checks = 0
    uniform_cap_checks = 0

    for _ in range(1_200):
        points = random.sample(grid, random.randint(7, 24))
        split = random.randint(3, len(points) - 2)
        background = set(points[:split])
        response = set(points[split:])

        maximum_pair_only = 0
        maximum_triple_shadow = 0
        maximum_line_triples = 0

        for response_point in response:
            loads: dict[tuple[int, int], int] = defaultdict(int)
            for point in background:
                loads[
                    primitive_direction(response_point, point)
                ] += 1

            multiplicity = sum(comb(height, 2) for height in loads.values())
            pair_only = sum(height == 2 for height in loads.values())
            triple_shadow = sum(comb(height, 3) for height in loads.values())
            assert multiplicity <= pair_only + 3 * triple_shadow
            maximum_pair_only = max(maximum_pair_only, pair_only)
            maximum_triple_shadow = max(
                maximum_triple_shadow,
                triple_shadow,
            )
            rank_one_shadow_checks += 1

        maximum_rank_two_multiplicity = 0
        for first, second in combinations(response, 2):
            line_load = sum(
                collinear(first, second, point)
                for point in background
            )
            line_triples = comb(line_load, 3)
            assert line_load <= 2 + line_triples
            maximum_rank_two_multiplicity = max(
                maximum_rank_two_multiplicity,
                line_load,
            )
            maximum_line_triples = max(
                maximum_line_triples,
                line_triples,
            )
            rank_two_shadow_checks += 1

        assert maximum_rank_two_multiplicity <= 2 + maximum_line_triples
        for response_point in response:
            loads: dict[tuple[int, int], int] = defaultdict(int)
            for point in background:
                loads[
                    primitive_direction(response_point, point)
                ] += 1
            multiplicity = sum(comb(height, 2) for height in loads.values())
            assert multiplicity <= (
                maximum_pair_only + 3 * maximum_triple_shadow
            )
            uniform_cap_checks += 1

        point_systems += 1

    print(
        "verified background-triple multiplicity charges: "
        f"{local_inequalities} local binomial inequalities, "
        f"{explicit_pair_maps} explicit pair charge maps, "
        f"{explicit_point_maps} explicit point charge maps, "
        f"{point_systems} finite point systems, "
        f"{rank_one_shadow_checks} rank-one shadow bounds, "
        f"{rank_two_shadow_checks} rank-two shadow bounds and "
        f"{uniform_cap_checks} uniform charged-cap checks"
    )


if __name__ == "__main__":
    main()
