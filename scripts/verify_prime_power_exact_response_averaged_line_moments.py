#!/usr/bin/env python3
"""Finite checks for CMR1878--CMR1885."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import comb, gcd

Edge = tuple[int, int]
Point = tuple[int, int]
Line = tuple[int, int, int]
Moment = tuple[int, int, int]


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


def score(height: int, moment: Moment) -> int:
    return comb(height, 2) * moment[0] + height * moment[1] + moment[2]


def pareto(values: set[Moment]) -> set[Moment]:
    return {
        value
        for value in values
        if not any(
            value != other
            and all(value[index] <= other[index] for index in range(3))
            for other in values
        )
    }


EXPECTED = {
    4: {
        1: (14, 2, 2, 2, (32, 6, 0)),
        2: (40, 4, 2, 2, (64, 12, 0)),
        3: (20, 2, 2, 2, (93, 18, 1)),
        4: (9, 2, 2, 2, (122, 24, 1)),
        5: (2, 2, 2, 2, (148, 30, 4)),
        6: (1, 1, 1, 0, (177, 36, 5)),
    },
    5: {
        8: (21, 5, 2, 2, (492, 80, 3)),
        9: (18, 3, 2, 2, (544, 90, 6)),
        10: (93, 9, 2, 2, (616, 100, 4)),
        11: (48, 4, 2, 2, (667, 110, 7)),
        12: (104, 9, 2, 2, (738, 120, 5)),
        13: (30, 7, 2, 2, (791, 130, 6)),
        14: (111, 9, 2, 2, (860, 140, 6)),
        15: (50, 8, 3, 3, (913, 150, 7)),
        16: (63, 6, 2, 2, (982, 160, 7)),
        17: (12, 5, 3, 3, (1023, 170, 7)),
        18: (24, 6, 2, 2, (1092, 180, 9)),
        19: (15, 4, 2, 2, (1150, 190, 10)),
        20: (45, 3, 2, 2, (1207, 200, 14)),
        22: (6, 4, 2, 2, (1329, 220, 11)),
        24: (1, 1, 1, 0, (1416, 240, 16)),
        25: (6, 3, 2, 2, (1501, 250, 17)),
        26: (6, 3, 3, 4, (1551, 260, 16)),
        33: (1, 1, 1, 0, (1956, 330, 23)),
    },
}


def main() -> None:
    host_count = 0
    host_line_count = 0
    response_line_count = 0
    line_height_checks = 0
    global_identity_checks = 0
    active_total = 0
    pareto_total = 0

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target
        lines = nonaxis_lines(side)
        by_denominator: dict[int, list[Moment]] = defaultdict(list)

        for deletion in partial_matchings(allowed):
            responses = perfect_matchings(side, opposite | target | set(deletion))
            if not responses:
                continue
            denominator = len(responses)
            totals = [0, 0, 0]

            for cells in lines.values():
                cell_set = set(cells)
                occupancies = [
                    sum(edge in cell_set for edge in response)
                    for response in responses
                ]
                z_1 = sum(occupancies)
                z_2 = sum(comb(value, 2) for value in occupancies)
                z_3 = sum(comb(value, 3) for value in occupancies)
                capacity = max(occupancies)
                totals[0] += z_1
                totals[1] += z_2
                totals[2] += z_3

                for rank, value in enumerate((z_1, z_2, z_3), start=1):
                    assert value <= denominator * comb(capacity, rank)

                for height in range(6):
                    direct = sum(
                        occupancy * comb(height, 2)
                        + comb(occupancy, 2) * height
                        + comb(occupancy, 3)
                        for occupancy in occupancies
                    )
                    formula = comb(height, 2) * z_1 + height * z_2 + z_3
                    assert direct == formula
                    line_height_checks += 1

                response_line_count += denominator
                host_line_count += 1

            moment = tuple(totals)
            assert moment[1] == denominator * comb(side, 2)
            triple_direct = sum(
                sum(
                    1
                    for first, second, third in combinations(response, 3)
                    if (second[0] - first[0]) * (third[1] - first[1])
                    == (second[1] - first[1]) * (third[0] - first[0])
                )
                for response in responses
            )
            assert moment[2] == triple_direct
            global_identity_checks += 1
            by_denominator[denominator].append(moment)
            host_count += 1

        expected = EXPECTED[side]
        assert set(by_denominator) == set(expected)
        for denominator, records in sorted(by_denominator.items()):
            host_expected, pareto_expected, active_expected, terminal_height, terminal = (
                expected[denominator]
            )
            assert len(records) == host_expected
            frontier = pareto(set(records))
            assert len(frontier) == pareto_expected
            pareto_total += len(frontier)

            active: set[Moment] = set()
            for height in range(terminal_height + 1):
                best = max(score(height, value) for value in frontier)
                active.update(
                    value for value in frontier if score(height, value) == best
                )
            assert len(active) == active_expected
            active_total += len(active)

            assert terminal in frontier
            for competitor in frontier:
                assert score(terminal_height, terminal) >= score(
                    terminal_height, competitor
                )
                assert terminal[0] >= competitor[0]
                increment = (
                    terminal_height * (terminal[0] - competitor[0])
                    + terminal[1]
                    - competitor[1]
                )
                assert increment >= 0

    assert host_count == 740
    assert host_line_count == 89664
    assert response_line_count == 1188144
    assert line_height_checks == 537984
    assert global_identity_checks == 740
    assert pareto_total == 103
    assert active_total == 48

    print(
        "verified exact response-averaged line moments: "
        f"{host_count} hosts, {host_line_count} host-line moment triples, "
        f"{response_line_count} response-line occurrences, "
        f"{line_height_checks} exact line-height identities, "
        f"{global_identity_checks} global pair/triple identities, "
        f"{pareto_total} denominator-preserving Pareto triples and "
        f"{active_total} integer-height-active triples"
    )


if __name__ == "__main__":
    main()
