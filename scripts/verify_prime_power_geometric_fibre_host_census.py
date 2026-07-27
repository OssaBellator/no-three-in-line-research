#!/usr/bin/env python3
"""Finite checks for CMR1798--CMR1805."""

from __future__ import annotations

from collections import Counter, defaultdict
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


def canonical_deleted(side: int, deleted: set[Edge]) -> tuple[Edge, ...]:
    best: tuple[Edge, ...] | None = None
    for image in permutations(range(2, side)):
        permutation = list(range(side))
        for old, new in zip(range(2, side), image):
            permutation[old] = new
        code = tuple(
            sorted((permutation[left], permutation[right]) for left, right in deleted)
        )
        if best is None or code < best:
            best = code
    assert best is not None
    return best


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


def triple_count(points: tuple[Point, ...]) -> int:
    return sum(
        collinear(first, second, third)
        for first, second, third in combinations(points, 3)
    )


def main() -> None:
    expected_fibres = {
        4: Counter({2: 41, 1: 4}),
        5: Counter({6: 96, 3: 24, 1: 2, 2: 2}),
    }

    random = Random(1798)
    raw_hosts = 0
    response_matchings = 0
    line_occupancy_checks = 0
    background_pair_checks = 0

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        base_allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - {target}

        fibres: dict[tuple[Edge, ...], list[set[Edge]]] = defaultdict(list)

        for deletion_tuple in partial_matchings(base_allowed):
            deletion = set(deletion_tuple)
            responses = perfect_matchings(side, opposite | {target} | deletion)
            if not responses:
                continue

            fibres[canonical_deleted(side, deletion)].append(deletion)
            raw_hosts += 1
            allowed = base_allowed - deletion

            line_cells: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
            for first, second in combinations(sorted(allowed), 2):
                if first[0] == second[0] or first[1] == second[1]:
                    continue
                key = line_key(first, second)
                line_cells[key].update((first, second))
            maximum_line_occupancy = max(
                (len(points) for points in line_cells.values()),
                default=1,
            )

            grid = {
                (left, right)
                for left in range(side)
                for right in range(side)
            }

            for response in responses:
                response_triples = triple_count(response)
                triple_bound = (
                    max(maximum_line_occupancy - 2, 0) * comb(side, 2)
                ) // 3
                assert response_triples <= triple_bound
                line_occupancy_checks += 1

                remaining = sorted(grid - set(response))
                background = set(
                    random.sample(
                        remaining,
                        random.randint(0, min(len(remaining), side + 3)),
                    )
                )

                pair_score = 0
                maximum_background_load = 0
                for first, second in combinations(response, 2):
                    load = sum(
                        collinear(first, second, point)
                        for point in background
                    )
                    pair_score += load
                    maximum_background_load = max(maximum_background_load, load)

                assert pair_score <= maximum_background_load * comb(side, 2)
                background_pair_checks += 1
                response_matchings += 1

        fibre_distribution = Counter(len(fibre) for fibre in fibres.values())
        assert fibre_distribution == expected_fibres[side]

    assert raw_hosts == 740
    assert response_matchings == 9260

    print(
        "verified geometric fibre host census and line caps: "
        f"{raw_hosts} raw geometric hosts, "
        f"{response_matchings} response matchings, "
        f"{line_occupancy_checks} response-triple caps and "
        f"{background_pair_checks} background rank-two caps"
    )


if __name__ == "__main__":
    main()
