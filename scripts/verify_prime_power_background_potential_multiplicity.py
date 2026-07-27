#!/usr/bin/env python3
"""Finite checks for CMR1758--CMR1765."""

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


def background_triples(background: set[Point]) -> int:
    return sum(
        collinear(*triple)
        for triple in combinations(background, 3)
    )


def main() -> None:
    random = Random(1758)
    grid = [(x, y) for x in range(9) for y in range(9)]
    systems = 0
    pair_matching_checks = 0
    pair_bound_checks = 0
    shadow_checks = 0
    rank_one_checks = 0
    rank_two_checks = 0
    clean_background_checks = 0

    for _ in range(1_500):
        points = random.sample(grid, random.randint(7, 28))
        split = random.randint(3, len(points) - 2)
        background = set(points[:split])
        response = set(points[split:])
        triple_count = background_triples(background)

        for response_point in response:
            direction_points: dict[tuple[int, int], list[Point]] = defaultdict(list)
            for point in background:
                direction_points[
                    primitive_direction(response_point, point)
                ].append(point)

            pair_only_edges = [
                frozenset(points_on_line)
                for points_on_line in direction_points.values()
                if len(points_on_line) == 2
            ]
            used_points: set[Point] = set()
            for edge in pair_only_edges:
                assert used_points.isdisjoint(edge)
                used_points.update(edge)
                pair_matching_checks += 1
            assert len(pair_only_edges) <= len(background) // 2
            pair_bound_checks += 1

            triple_shadow = sum(
                comb(len(points_on_line), 3)
                for points_on_line in direction_points.values()
            )
            assert triple_shadow <= triple_count
            shadow_checks += 1

            rank_one_multiplicity = sum(
                comb(len(points_on_line), 2)
                for points_on_line in direction_points.values()
            )
            assert rank_one_multiplicity <= (
                len(background) // 2 + 3 * triple_count
            )
            rank_one_checks += 1

            if triple_count == 0:
                assert rank_one_multiplicity <= len(background) // 2
                clean_background_checks += 1

        for first, second in combinations(response, 2):
            line_load = sum(
                collinear(first, second, point)
                for point in background
            )
            line_triples = comb(line_load, 3)
            assert line_triples <= triple_count
            assert line_load <= 2 + triple_count
            rank_two_checks += 1
            if triple_count == 0:
                assert line_load <= 2
                clean_background_checks += 1

        systems += 1

    print(
        "verified background-potential multiplicity bounds: "
        f"{systems} finite point systems, "
        f"{pair_matching_checks} pair-only matching edges, "
        f"{pair_bound_checks} pair-only size bounds, "
        f"{shadow_checks} global triple-shadow bounds, "
        f"{rank_one_checks} rank-one potential caps, "
        f"{rank_two_checks} rank-two potential caps and "
        f"{clean_background_checks} triple-free specializations"
    )


if __name__ == "__main__":
    main()
