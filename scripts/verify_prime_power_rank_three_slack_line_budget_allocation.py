#!/usr/bin/env python3
"""Finite checks for CMR1886--CMR1893."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import comb, gcd

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
    return [
        tuple((left, permutation[left]) for left in range(side))
        for permutation in permutations(range(side))
        if all((left, permutation[left]) not in forbidden for left in range(side))
    ]


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


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


EXPECTED = {
    4: {
        1: {
            "active": 601,
            "fitting": 395,
            "hosts_any": 32,
            "hosts_all": 12,
            "lengths": Counter({2: 328, 3: 48, 4: 19}),
        },
        2: {
            "active": 1934,
            "fitting": 676,
            "hosts_any": 32,
            "hosts_all": 0,
            "lengths": Counter({2: 631, 3: 45}),
        },
    },
    5: {
        1: {
            "active": 34017,
            "fitting": 26797,
            "hosts_any": 562,
            "hosts_all": 14,
            "lengths": Counter({2: 21166, 3: 4571, 4: 935, 5: 125}),
        },
        2: {
            "active": 70258,
            "fitting": 16162,
            "hosts_any": 460,
            "hosts_all": 0,
            "lengths": Counter({2: 14852, 3: 1252, 4: 39, 5: 19}),
        },
    },
}


def main() -> None:
    raw_hosts = 0
    strict_hosts = 0
    strict_host_line_pairs = 0
    exact_budget_checks = 0
    total_active = Counter()
    total_fitting = Counter()
    total_hosts_any = Counter()
    total_hosts_all = Counter()

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        lines = nonaxis_lines(side)

        observed = {
            1: {
                "active": 0,
                "fitting": 0,
                "hosts_any": 0,
                "hosts_all": 0,
                "lengths": Counter(),
            },
            2: {
                "active": 0,
                "fitting": 0,
                "hosts_any": 0,
                "hosts_all": 0,
                "lengths": Counter(),
            },
        }

        for deletion in partial_matchings(allowed):
            responses = perfect_matchings(side, opposite | target | set(deletion))
            if not responses:
                continue
            raw_hosts += 1
            denominator = len(responses)
            line_data: list[tuple[int, int, int, int]] = []
            rank_three_numerator = 0

            for cells in lines.values():
                cell_set = set(cells)
                occupancies = [
                    sum(edge in cell_set for edge in response)
                    for response in responses
                ]
                z_1 = sum(occupancies)
                z_2 = sum(comb(value, 2) for value in occupancies)
                z_3 = sum(comb(value, 3) for value in occupancies)
                line_data.append((len(cells), z_1, z_2, z_3))
                rank_three_numerator += z_3

            direct_rank_three = sum(
                sum(
                    collinear(first, second, third)
                    for first, second, third in combinations(response, 3)
                )
                for response in responses
            )
            assert rank_three_numerator == direct_rank_three
            slack = denominator - rank_three_numerator
            if slack <= 0:
                continue

            strict_hosts += 1
            strict_host_line_pairs += len(line_data)
            budget = slack - 1

            for height in (1, 2):
                active_lines = []
                fitting = 0
                for length, z_1, z_2, _z_3 in line_data:
                    relevant = z_2 > 0 if height == 1 else z_1 > 0
                    if not relevant:
                        continue
                    cost = comb(height, 2) * z_1 + height * z_2
                    active_lines.append(cost)
                    observed[height]["active"] += 1
                    if cost <= budget:
                        fitting += 1
                        observed[height]["fitting"] += 1
                        observed[height]["lengths"][length] += 1
                    assert (
                        rank_three_numerator + cost < denominator
                    ) == (cost <= budget)
                    exact_budget_checks += 1

                if fitting:
                    observed[height]["hosts_any"] += 1
                if active_lines and fitting == len(active_lines):
                    observed[height]["hosts_all"] += 1

        assert observed == EXPECTED[side]
        for height in (1, 2):
            total_active[height] += observed[height]["active"]
            total_fitting[height] += observed[height]["fitting"]
            total_hosts_any[height] += observed[height]["hosts_any"]
            total_hosts_all[height] += observed[height]["hosts_all"]

    assert raw_hosts == 740
    assert strict_hosts == 651
    assert strict_host_line_pairs == 80602
    assert total_active == Counter({2: 72192, 1: 34618})
    assert total_fitting == Counter({1: 27192, 2: 16838})
    assert total_hosts_any == Counter({1: 594, 2: 492})
    assert total_hosts_all == Counter({1: 26, 2: 0})
    assert exact_budget_checks == 106810

    print(
        "verified rank-three slack line-budget allocation: "
        f"{raw_hosts} raw hosts, {strict_hosts} strict hosts, "
        f"{strict_host_line_pairs} strict host-line pairs, "
        f"{exact_budget_checks} exact line-budget equivalences, "
        f"{total_fitting[1]}/{total_active[1]} fitting load-one active lines and "
        f"{total_fitting[2]}/{total_active[2]} fitting load-two active lines"
    )


if __name__ == "__main__":
    main()
