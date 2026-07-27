#!/usr/bin/env python3
"""Finite checks for CMR1830--CMR1837."""

from __future__ import annotations

from collections import Counter, defaultdict
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


def perfect_matchings(side: int, forbidden: set[Edge]) -> list[tuple[int, ...]]:
    return [
        permutation
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


EXPECTED = {
    4: {
        "host_count": 86,
        "line_count": 54,
        "max_tau": Counter({2: 37, 3: 14, 4: 35}),
        "m3": Counter({0: 37, 1: 14, 4: 15, 5: 20}),
        "by_denominator": {
            1: (14, 32, 6, 4, 44),
            2: (40, 53, 12, 5, 78),
            3: (20, 62, 17, 5, 98),
            4: (9, 69, 22, 5, 116),
            5: (2, 70, 25, 5, 125),
            6: (1, 77, 30, 5, 142),
        },
    },
    5: {
        "host_count": 654,
        "line_count": 130,
        "max_tau": Counter({3: 379, 4: 275}),
        "m3": Counter(
            {
                1: 1,
                2: 4,
                3: 30,
                4: 63,
                5: 128,
                6: 126,
                7: 64,
                8: 54,
                9: 94,
                10: 62,
                11: 22,
                12: 6,
            }
        ),
        "by_denominator": {
            8: (21, 163, 57, 9, 280),
            9: (18, 163, 57, 9, 280),
            10: (93, 174, 64, 10, 307),
            11: (48, 178, 70, 10, 325),
            12: (104, 181, 70, 11, 323),
            13: (30, 185, 75, 10, 340),
            14: (111, 189, 77, 11, 351),
            15: (50, 191, 81, 11, 361),
            16: (63, 194, 84, 11, 371),
            17: (12, 195, 83, 11, 371),
            18: (24, 198, 84, 12, 373),
            19: (15, 200, 89, 11, 388),
            20: (45, 203, 91, 12, 395),
            22: (6, 205, 90, 12, 396),
            24: (1, 201, 84, 7, 376),
            25: (6, 212, 97, 12, 417),
            26: (6, 212, 97, 11, 417),
            33: (1, 220, 104, 12, 440),
        },
    },
}


def main() -> None:
    raw_hosts_checked = 0
    host_line_checks = 0
    response_checks = 0
    moment_checks = 0
    layer_checks = 0

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        lines = nonaxis_lines(side)

        records: list[tuple[int, int, int, int, int]] = []
        max_tau_distribution: Counter[int] = Counter()
        m3_distribution: Counter[int] = Counter()

        for deletion_tuple in partial_matchings(allowed):
            forbidden = opposite | target | set(deletion_tuple)
            responses = perfect_matchings(side, forbidden)
            if not responses:
                continue

            capacities: list[int] = []
            for cells in lines.values():
                cell_set = set(cells)
                capacity = max(
                    sum((left, permutation[left]) in cell_set for left in range(side))
                    for permutation in responses
                )
                capacities.append(capacity)
                for permutation in responses:
                    occupancy = sum(
                        (left, permutation[left]) in cell_set for left in range(side)
                    )
                    assert occupancy <= capacity
                    response_checks += 1
                host_line_checks += 1

            m_1 = sum(capacities)
            m_2 = sum(comb(capacity, 2) for capacity in capacities)
            m_3 = sum(comb(capacity, 3) for capacity in capacities)
            e_2 = m_1 + 2 * m_2 + m_3
            records.append((len(responses), m_1, m_2, m_3, e_2))
            max_tau_distribution[max(capacities)] += 1
            m3_distribution[m_3] += 1
            raw_hosts_checked += 1

            for height_cap in range(0, 7):
                heights = [
                    (index * 3 + len(responses)) % (height_cap + 1)
                    if height_cap
                    else 0
                    for index in range(len(capacities))
                ]
                exact = sum(
                    capacity * comb(height, 2)
                    + comb(capacity, 2) * height
                    + comb(capacity, 3)
                    for capacity, height in zip(capacities, heights)
                )
                uniform = (
                    comb(height_cap, 2) * m_1
                    + height_cap * m_2
                    + m_3
                )
                assert exact <= uniform
                moment_checks += 1

                layered = m_3
                for threshold in range(2, height_cap + 1):
                    layered += (threshold - 1) * sum(
                        capacity
                        for capacity, height in zip(capacities, heights)
                        if height >= threshold
                    )
                for threshold in range(1, height_cap + 1):
                    layered += sum(
                        comb(capacity, 2)
                        for capacity, height in zip(capacities, heights)
                        if height >= threshold
                    )
                assert layered == exact
                layer_checks += 1

        expected = EXPECTED[side]
        assert len(records) == expected["host_count"]
        assert len(lines) == expected["line_count"]
        assert max_tau_distribution == expected["max_tau"]
        assert m3_distribution == expected["m3"]

        by_denominator: dict[int, list[tuple[int, int, int, int, int]]] = defaultdict(list)
        for record in records:
            by_denominator[record[0]].append(record)

        observed_table = {
            denominator: (
                len(group),
                max(record[1] for record in group),
                max(record[2] for record in group),
                max(record[3] for record in group),
                max(record[4] for record in group),
            )
            for denominator, group in sorted(by_denominator.items())
        }
        assert observed_table == expected["by_denominator"]

    print(
        "verified geometric fibre occupancy moments: "
        f"{raw_hosts_checked} raw hosts, {host_line_checks} host-line capacities, "
        f"{response_checks} response-line checks, {moment_checks} uniform-height "
        f"bounds and {layer_checks} exact height-layer identities"
    )


if __name__ == "__main__":
    main()
