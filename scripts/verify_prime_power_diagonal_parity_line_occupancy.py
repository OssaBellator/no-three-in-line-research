#!/usr/bin/env python3
"""Finite checks for CMR1846--CMR1853."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import gcd

Edge = tuple[int, int]
Point = tuple[int, int]
Line = tuple[int, int, int]


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
    output: list[tuple[Edge, ...]] = []
    for permutation in permutations(range(side)):
        matching = tuple((left, permutation[left]) for left in range(side))
        if all(edge not in forbidden for edge in matching):
            output.append(matching)
    return output


def line_key(first: Point, second: Point) -> Line:
    x_1, y_1 = first
    x_2, y_2 = second
    a = y_2 - y_1
    b = x_1 - x_2
    c = a * x_1 + b * y_1
    divisor = gcd(gcd(abs(a), abs(b)), abs(c))
    if divisor:
        a //= divisor
        b //= divisor
        c //= divisor
    if a < 0 or (a == 0 and b < 0):
        a = -a
        b = -b
        c = -c
    return a, b, c


def nonaxis_lines(side: int) -> dict[Line, tuple[Point, ...]]:
    points = [(left, right) for left in range(side) for right in range(side)]
    output: dict[Line, tuple[Point, ...]] = {}
    for first, second in combinations(points, 2):
        key = line_key(first, second)
        a, b, c = key
        if a == 0 or b == 0:
            continue
        cells = tuple(
            point for point in points if a * point[0] + b * point[1] == c
        )
        if len(cells) >= 2:
            output[key] = cells
    return output


EXPECTED_COUNTS = {
    4: Counter(
        {
            (2, 0): 1278,
            (2, 1): 2148,
            (2, 2): 702,
            (3, 0): 45,
            (3, 1): 195,
            (3, 2): 70,
            (3, 3): 34,
            (4, 0): 97,
            (4, 2): 40,
            (4, 4): 35,
        }
    ),
    5: Counter(
        {
            (2, 0): 7345,
            (2, 1): 36691,
            (2, 2): 26596,
            (3, 0): 311,
            (3, 1): 3147,
            (3, 2): 5407,
            (3, 3): 1599,
            (4, 0): 7,
            (4, 1): 145,
            (4, 2): 1033,
            (4, 3): 1156,
            (4, 4): 275,
            (5, 0): 655,
            (5, 1): 34,
            (5, 2): 67,
            (5, 3): 552,
        }
    ),
}


def anti_diagonal_matching(side: int) -> tuple[Edge, ...]:
    return tuple((index, side - 1 - index) for index in range(side))


def odd_side_construction(side: int, omitted: int) -> tuple[Edge, ...]:
    center = side // 2
    assert side % 2 == 1 and side >= 5 and omitted != center
    matching = [
        (index, side - 1 - index)
        for index in range(side)
        if index not in {center, omitted}
    ]
    matching.extend(((center, side - 1 - omitted), (omitted, center)))
    return tuple(sorted(matching))


def main() -> None:
    full_line_checks = 0
    parity_checks = 0
    construction_checks = 0
    raw_hosts = 0
    host_line_checks = 0
    response_line_checks = 0

    for side in range(3, 13):
        lines = nonaxis_lines(side)
        full_lines = [set(cells) for cells in lines.values() if len(cells) == side]
        main_diagonal = {(index, index) for index in range(side)}
        anti_diagonal = set(anti_diagonal_matching(side))
        assert len(full_lines) == 2
        assert {frozenset(line) for line in full_lines} == {
            frozenset(main_diagonal),
            frozenset(anti_diagonal),
        }
        full_line_checks += 1

        opposite = main_diagonal
        target = {(0, 1)}
        base_forbidden = opposite | target

        if side % 2 == 0:
            anti_matching = anti_diagonal_matching(side)
            assert all(edge not in base_forbidden for edge in anti_matching)
            assert len({edge[0] for edge in anti_matching}) == side
            assert len({edge[1] for edge in anti_matching}) == side
            parity_checks += 1
        else:
            center = side // 2
            assert (center, center) in anti_diagonal
            if side >= 5:
                for omitted in range(side):
                    if omitted == center:
                        continue
                    matching = odd_side_construction(side, omitted)
                    assert len(matching) == side
                    assert len({edge[0] for edge in matching}) == side
                    assert len({edge[1] for edge in matching}) == side
                    assert all(edge not in base_forbidden for edge in matching)
                    assert sum(edge in anti_diagonal for edge in matching) == side - 2
                    construction_checks += 1
            parity_checks += 1

    for side in range(3, 9):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        responses = perfect_matchings(side, opposite | target)
        anti_diagonal = set(anti_diagonal_matching(side))
        observed = max(
            sum(edge in anti_diagonal for edge in response)
            for response in responses
        )
        expected = side if side % 2 == 0 else side - 2
        assert observed == expected
        parity_checks += 1

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        lines = nonaxis_lines(side)
        observed_counts: Counter[tuple[int, int]] = Counter()

        for deletion_tuple in partial_matchings(allowed):
            forbidden = opposite | target | set(deletion_tuple)
            responses = perfect_matchings(side, forbidden)
            if not responses:
                continue
            raw_hosts += 1
            for cells in lines.values():
                cell_set = set(cells)
                capacity = max(
                    sum(edge in cell_set for edge in response)
                    for response in responses
                )
                observed_counts[len(cells), capacity] += 1
                host_line_checks += 1
                for response in responses:
                    assert sum(edge in cell_set for edge in response) <= capacity
                    response_line_checks += 1

        assert observed_counts == EXPECTED_COUNTS[side]

    print(
        "verified diagonal parity and line-length occupancy census: "
        f"{full_line_checks} full-line classifications, {parity_checks} parity "
        f"checks, {construction_checks} odd-side constructions, {raw_hosts} raw "
        f"hosts, {host_line_checks} host-line capacities and "
        f"{response_line_checks} response-line checks"
    )


if __name__ == "__main__":
    main()
