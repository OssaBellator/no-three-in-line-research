#!/usr/bin/env python3
"""Finite checks for CMR1870--CMR1877."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations

Edge = tuple[int, int]
Point = tuple[int, int]


EXPECTED = {
    4: {
        "host_count": 86,
        "signs": Counter({"strict": 53, "critical": 6, "excess": 27}),
        "slacks": Counter({-3: 11, -2: 12, -1: 4, 0: 6, 1: 21, 2: 24, 3: 8}),
        "by_denominator": {
            1: (12, 0, 2),
            2: (26, 0, 14),
            3: (11, 0, 9),
            4: (2, 5, 2),
            5: (1, 1, 0),
            6: (1, 0, 0),
        },
    },
    5: {
        "host_count": 654,
        "signs": Counter({"strict": 598, "critical": 38, "excess": 18}),
        "slacks": Counter(
            {
                -4: 1,
                -3: 1,
                -2: 6,
                -1: 10,
                0: 38,
                1: 36,
                2: 67,
                3: 89,
                4: 112,
                5: 84,
                6: 96,
                7: 53,
                8: 39,
                9: 14,
                10: 6,
                11: 2,
            }
        ),
        "by_denominator": {
            8: (15, 3, 3),
            9: (17, 0, 1),
            10: (76, 10, 7),
            11: (42, 6, 0),
            12: (90, 10, 4),
            13: (26, 3, 1),
            14: (105, 4, 2),
            15: (49, 1, 0),
            16: (62, 1, 0),
            17: (12, 0, 0),
            18: (24, 0, 0),
            19: (15, 0, 0),
            20: (45, 0, 0),
            22: (6, 0, 0),
            24: (1, 0, 0),
            25: (6, 0, 0),
            26: (6, 0, 0),
            33: (1, 0, 0),
        },
    },
}


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


def collinear(first: Point, second: Point, third: Point) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def response_triples(permutation: tuple[int, ...]) -> int:
    points = [(left, permutation[left]) for left in range(len(permutation))]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def sign_name(slack: int) -> str:
    if slack > 0:
        return "strict"
    if slack == 0:
        return "critical"
    return "excess"


def main() -> None:
    raw_hosts_checked = 0
    response_occurrences = 0
    residual_budget_checks = 0
    sign_checks = 0

    aggregate_signs: Counter[str] = Counter()

    for side in (4, 5):
        opposite = {(index, index) for index in range(side)}
        target = {(0, 1)}
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - target

        signs: Counter[str] = Counter()
        slacks: Counter[int] = Counter()
        by_denominator: dict[int, Counter[str]] = defaultdict(Counter)

        for deletion_tuple in partial_matchings(allowed):
            forbidden = opposite | target | set(deletion_tuple)
            responses = perfect_matchings(side, forbidden)
            if not responses:
                continue

            denominator = len(responses)
            numerator = sum(response_triples(response) for response in responses)
            slack = denominator - numerator
            sign = sign_name(slack)

            signs[sign] += 1
            aggregate_signs[sign] += 1
            slacks[slack] += 1
            by_denominator[denominator][sign] += 1
            raw_hosts_checked += 1
            response_occurrences += denominator
            sign_checks += 1

            if slack > 0:
                for additional in range(slack + 2):
                    strict = numerator + additional < denominator
                    assert strict == (additional <= slack - 1)
                    residual_budget_checks += 1
            else:
                assert numerator >= denominator
                assert not (numerator < denominator)
                residual_budget_checks += 1

        expected = EXPECTED[side]
        assert sum(signs.values()) == expected["host_count"]
        assert signs == expected["signs"]
        assert slacks == expected["slacks"]

        observed_by_denominator = {
            denominator: (
                counts["strict"],
                counts["critical"],
                counts["excess"],
            )
            for denominator, counts in sorted(by_denominator.items())
        }
        assert observed_by_denominator == expected["by_denominator"]

        if side == 5:
            assert all(
                counts["critical"] == 0 and counts["excess"] == 0
                for denominator, counts in by_denominator.items()
                if denominator >= 17
            )

    assert raw_hosts_checked == 740
    assert response_occurrences == 9260
    assert aggregate_signs == Counter(
        {"strict": 651, "critical": 44, "excess": 45}
    )
    print(
        "verified rank-three fibre slack classification: "
        f"{raw_hosts_checked} raw hosts, {response_occurrences} response occurrences, "
        f"{sign_checks} exact sign classifications and "
        f"{residual_budget_checks} residual-budget checks; "
        "651 strict, 44 critical and 45 excess hosts"
    )


if __name__ == "__main__":
    main()
