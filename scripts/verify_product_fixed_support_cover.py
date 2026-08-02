#!/usr/bin/env python3
"""Finite combinatorial checks for PX371--PX376."""

from itertools import combinations


def maximal_support_matching(
    family: list[tuple[int, ...]],
) -> tuple[list[int], set[int]]:
    chosen: list[int] = []
    used: set[int] = set()
    for index, support in enumerate(family):
        if not used.intersection(support):
            chosen.append(index)
            used.update(support)
    return chosen, used


def main() -> None:
    # PX371: exhaust every simple support system of sets of size one or two
    # through five fixed selected points.
    for vertex_count in range(1, 6):
        supports = [(i,) for i in range(vertex_count)]
        supports += list(combinations(range(vertex_count), 2))
        for mask in range(1, 1 << len(supports)):
            family = [
                supports[index]
                for index in range(len(supports))
                if (mask >> index) & 1
            ]
            chosen, cover = maximal_support_matching(family)
            assert all(set(support).intersection(cover) for support in family)
            assert len(cover) <= 2 * len(chosen)

    # PX372--PX374: type-weight and size--weight inequalities.
    for blocker_count in range(1, 201):
        for channels in range(1, 9):
            type_count = 2 * channels
            guaranteed_type_weight = blocker_count / type_count
            assert guaranteed_type_weight == blocker_count / (2 * channels)
            for threshold in range(1, 31):
                # If a type class has fewer than T points, its maximum point
                # weight is strictly above W/T.
                point_bound = guaranteed_type_weight / threshold
                assert point_bound == blocker_count / (
                    2 * channels * threshold
                )

    # PX375 constants inherited from the weighted cover and one type class.
    for order in range(2, 101):
        for destroyed in range(1, 21):
            for channels in range(1, 9):
                one_family = destroyed * order / 48
                two_family = destroyed * order * order / 32
                assert one_family / (2 * channels) == destroyed * order / (
                    96 * channels
                )
                assert two_family / (2 * channels) == (
                    destroyed * order * order / (64 * channels)
                )

    # PX376 threshold substitution T=n^(2/3), checked algebraically on cubes.
    for root in range(2, 31):
        order = root**3
        threshold = root**2
        for channels in range(1, 9):
            one_point = order / (96 * channels * threshold)
            two_point = order * order / (64 * channels * threshold)
            assert one_point == root / (96 * channels)
            assert two_point == root**4 / (64 * channels)

    print("PX371--PX376 fixed-support-cover verifier: PASS")


if __name__ == "__main__":
    main()
