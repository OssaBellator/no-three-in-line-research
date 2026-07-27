#!/usr/bin/env python3
"""Finite checks for CMR1806--CMR1813."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations


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
    expected_response_values = {
        4: Counter({0: 137, 1: 34, 4: 35}),
        5: Counter({0: 4116, 1: 4115, 2: 548, 4: 275}),
    }
    expected_host_maxima = {
        4: Counter({0: 37, 1: 14, 4: 35}),
        5: Counter({1: 116, 2: 263, 4: 275}),
    }
    expected_denominator_caps = {
        4: {
            1: (14, 4),
            2: (40, 5),
            3: (20, 5),
            4: (9, 5),
            5: (2, 5),
            6: (1, 5),
        },
        5: {
            8: (21, 10),
            9: (18, 10),
            10: (93, 14),
            11: (48, 11),
            12: (104, 15),
            13: (30, 14),
            14: (111, 15),
            15: (50, 15),
            16: (63, 16),
            17: (12, 15),
            18: (24, 17),
            19: (15, 16),
            20: (45, 16),
            22: (6, 18),
            24: (1, 16),
            25: (6, 19),
            26: (6, 20),
            33: (1, 23),
        },
    }
    expected_totals = {
        4: (86, 206, 174, 37),
        5: (654, 9054, 6311, 0),
    }

    total_hosts = 0
    total_responses = 0
    total_triples = 0

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        base_allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - {target}

        response_values: Counter[int] = Counter()
        host_maxima: Counter[int] = Counter()
        by_denominator: dict[int, list[int]] = defaultdict(list)
        host_count = 0
        response_count = 0
        triple_sum = 0
        triple_free_hosts = 0

        for deletion_tuple in partial_matchings(base_allowed):
            deletion = set(deletion_tuple)
            responses = perfect_matchings(side, opposite | {target} | deletion)
            if not responses:
                continue

            values = [triple_count(response) for response in responses]
            denominator = len(responses)
            numerator = sum(values)

            response_values.update(values)
            host_maxima[max(values)] += 1
            by_denominator[denominator].append(numerator)
            triple_free_hosts += numerator == 0
            host_count += 1
            response_count += denominator
            triple_sum += numerator

            assert set(values) <= {0, 1, 2, 4}
            assert max(values) <= 4
            if side == 4:
                assert numerator <= 4 * denominator
            else:
                assert 5 * numerator <= 7 * denominator

        assert response_values == expected_response_values[side]
        assert host_maxima == expected_host_maxima[side]
        assert (
            host_count,
            response_count,
            triple_sum,
            triple_free_hosts,
        ) == expected_totals[side]

        observed_caps = {
            denominator: (len(numerators), max(numerators))
            for denominator, numerators in by_denominator.items()
        }
        assert observed_caps == expected_denominator_caps[side]

        if side == 4:
            assert Fraction(triple_sum, response_count) == Fraction(87, 103)
        else:
            assert Fraction(triple_sum, response_count) == Fraction(6311, 9054)

        total_hosts += host_count
        total_responses += response_count
        total_triples += triple_sum

    assert total_hosts == 740
    assert total_responses == 9260
    assert total_triples == 6485

    print(
        "verified exact rank-three geometric fibre census: "
        f"{total_hosts} raw hosts, "
        f"{total_responses} response occurrences, "
        f"{total_triples} collinear response triples, "
        "exact host maxima and denominator-specific numerator caps"
    )


if __name__ == "__main__":
    main()
