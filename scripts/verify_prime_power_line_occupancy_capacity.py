#!/usr/bin/env python3
"""Finite checks for CMR1814--CMR1821."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import comb, gcd
from random import Random


Edge = tuple[int, int]
Point = tuple[int, int]


def partial_matchings(edges: set[Edge]) -> list[tuple[Edge, ...]]:
    edge_list = sorted(edges)
    output: list[tuple[Edge, ...]] = []

    def recurse(
        index: int,
        chosen: list[Edge],
        used_left: set[int],
        used_right: set[int],
    ) -> None:
        if index == len(edge_list):
            output.append(tuple(chosen))
            return

        recurse(index + 1, chosen, used_left, used_right)
        left, right = edge_list[index]
        if left not in used_left and right not in used_right:
            chosen.append((left, right))
            used_left.add(left)
            used_right.add(right)
            recurse(index + 1, chosen, used_left, used_right)
            used_right.remove(right)
            used_left.remove(left)
            chosen.pop()

    recurse(0, [], set(), set())
    return output


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[tuple[Edge, ...]]:
    return [
        tuple((left, permutation[left]) for left in range(side))
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


def line_key(first: Point, second: Point) -> tuple[int, int, int]:
    x_first, y_first = first
    x_second, y_second = second
    coefficient_x = y_second - y_first
    coefficient_y = x_first - x_second
    constant = -(coefficient_x * x_first + coefficient_y * y_first)

    divisor = 0
    for value in (coefficient_x, coefficient_y, constant):
        divisor = gcd(divisor, abs(value))
    if divisor:
        coefficient_x //= divisor
        coefficient_y //= divisor
        constant //= divisor

    if (
        coefficient_x < 0
        or (coefficient_x == 0 and coefficient_y < 0)
        or (coefficient_x == 0 and coefficient_y == 0 and constant < 0)
    ):
        coefficient_x = -coefficient_x
        coefficient_y = -coefficient_y
        constant = -constant

    return coefficient_x, coefficient_y, constant


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def triple_count(points: set[Point] | tuple[Point, ...]) -> int:
    return sum(
        collinear(first, second, third)
        for first, second, third in combinations(sorted(points), 3)
    )


def grid_lines(side: int) -> dict[tuple[int, int, int], set[Point]]:
    grid = {
        (left, right)
        for left in range(side)
        for right in range(side)
    }
    keys = {
        line_key(first, second)
        for first, second in combinations(sorted(grid), 2)
    }
    return {
        key: {
            point
            for point in grid
            if key[0] * point[0] + key[1] * point[1] + key[2] == 0
        }
        for key in keys
    }


def main() -> None:
    random = Random(1814)
    raw_hosts = 0
    host_line_capacities = 0
    response_energy_checks = 0

    expected_line_counts = {4: 62, 5: 140}

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        grid = {
            (left, right)
            for left in range(side)
            for right in range(side)
        }
        base_allowed = grid - opposite - {target}
        lines = grid_lines(side)
        assert len(lines) == expected_line_counts[side]

        for deletion_tuple in partial_matchings(base_allowed):
            deletion = set(deletion_tuple)
            responses = perfect_matchings(side, opposite | {target} | deletion)
            if not responses:
                continue

            occupancy = {
                key: max(
                    sum(point in line_points for point in response)
                    for response in responses
                )
                for key, line_points in lines.items()
            }

            for key, line_points in lines.items():
                direct = max(
                    sum(point in line_points for point in response)
                    for response in responses
                )
                assert occupancy[key] == direct
                host_line_capacities += 1

            for response in responses:
                remaining = sorted(grid - set(response))
                background = set(
                    random.sample(
                        remaining,
                        random.randint(0, min(len(remaining), side + 3)),
                    )
                )

                exact_energy = triple_count(background | set(response)) - triple_count(
                    background
                )

                rank_one_exact = 0
                rank_two_exact = 0
                rank_three_exact = 0
                line_capacity = 0

                for key, line_points in lines.items():
                    background_load = len(background & line_points)
                    response_load = sum(
                        point in line_points
                        for point in response
                    )
                    capacity = occupancy[key]

                    assert response_load <= capacity
                    rank_one_exact += response_load * comb(background_load, 2)
                    rank_two_exact += comb(response_load, 2) * background_load
                    rank_three_exact += comb(response_load, 3)
                    line_capacity += (
                        capacity * comb(background_load, 2)
                        + comb(capacity, 2) * background_load
                        + comb(capacity, 3)
                    )

                assert exact_energy == (
                    rank_one_exact + rank_two_exact + rank_three_exact
                )
                assert exact_energy <= line_capacity
                response_energy_checks += 1

            raw_hosts += 1

    assert raw_hosts == 740
    assert host_line_capacities == 96892
    assert response_energy_checks == 9260

    print(
        "verified line occupancy capacity certificates: "
        f"{raw_hosts} raw hosts, "
        f"{host_line_capacities} exact host-line capacities and "
        f"{response_energy_checks} complete response-energy checks"
    )


if __name__ == "__main__":
    main()
