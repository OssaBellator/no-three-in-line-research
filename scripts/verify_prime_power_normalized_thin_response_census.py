#!/usr/bin/env python3
"""Finite checks for CMR1662--CMR1669."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations


Edge = tuple[int, int]


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


def main() -> None:
    expected = {
        2: (2, 0, 0, Counter(), {}, {}),
        3: (
            13,
            4,
            4,
            Counter({1: 4}),
            {1: Fraction(0), 2: Fraction(0)},
            {1: 12, 2: 12},
        ),
        4: (
            86,
            86,
            45,
            Counter({2: 20, 3: 10, 1: 7, 4: 6, 6: 1, 5: 1}),
            {1: Fraction(3, 4), 2: Fraction(2, 3)},
            {1: 66, 2: 55},
        ),
        5: (
            654,
            654,
            124,
            Counter(
                {
                    12: 21,
                    14: 19,
                    10: 16,
                    16: 15,
                    15: 9,
                    20: 8,
                    11: 8,
                    13: 5,
                    18: 4,
                    8: 4,
                    19: 3,
                    9: 3,
                    22: 2,
                    25: 2,
                    17: 2,
                    33: 1,
                    26: 1,
                    24: 1,
                }
            ),
            {1: Fraction(2, 3), 2: Fraction(2, 5)},
            {1: 0, 2: 0},
        ),
    }

    canonical_hosts_checked = 0
    extendable_prescriptions = 0

    for side in range(2, 6):
        opposite = {(index, index) for index in range(side)}
        target = (0, 1)
        allowed = {
            (left, right)
            for left in range(side)
            for right in range(side)
        } - opposite - {target}

        raw_deletions = partial_matchings(allowed)
        executable: list[tuple[set[Edge], list[tuple[int, ...]]]] = []
        orbits: dict[
            tuple[Edge, ...], tuple[set[Edge], list[tuple[int, ...]]]
        ] = {}

        for deletion_tuple in raw_deletions:
            deletion = set(deletion_tuple)
            responses = perfect_matchings(side, opposite | {target} | deletion)
            if responses:
                executable.append((deletion, responses))
                orbits[canonical_deleted(side, deletion)] = (deletion, responses)

        denominator_distribution = Counter(
            len(responses) for _deletion, responses in orbits.values()
        )
        maximum_nonforced = {1: Fraction(0), 2: Fraction(0)}
        forced = {1: 0, 2: 0}

        for deletion, responses in orbits.values():
            forbidden = opposite | {target} | deletion
            remaining = {
                (left, right)
                for left in range(side)
                for right in range(side)
            } - forbidden

            for rank in (1, 2):
                for prescription in combinations(remaining, rank):
                    if len({left for left, _right in prescription}) < rank:
                        continue
                    if len({right for _left, right in prescription}) < rank:
                        continue

                    numerator = sum(
                        all(
                            permutation[left] == right
                            for left, right in prescription
                        )
                        for permutation in responses
                    )
                    if numerator == 0:
                        continue

                    extendable_prescriptions += 1
                    if numerator == len(responses):
                        forced[rank] += 1
                    else:
                        maximum_nonforced[rank] = max(
                            maximum_nonforced[rank],
                            Fraction(numerator, len(responses)),
                        )

        (
            expected_raw,
            expected_executable,
            expected_orbits,
            expected_distribution,
            expected_maximum,
            expected_forced,
        ) = expected[side]

        assert (
            len(raw_deletions),
            len(executable),
            len(orbits),
        ) == (
            expected_raw,
            expected_executable,
            expected_orbits,
        )
        assert denominator_distribution == expected_distribution
        if side >= 3:
            assert maximum_nonforced == expected_maximum
            assert forced == expected_forced

        canonical_hosts_checked += len(orbits)

    print(
        "verified normalized thin response census: "
        f"{canonical_hosts_checked} canonical hosts through side five, "
        f"{extendable_prescriptions} extendable rank-one/two prescriptions, "
        "exact denominator distributions, forced contractions and "
        "nonforced probability caps"
    )


if __name__ == "__main__":
    main()
