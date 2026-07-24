#!/usr/bin/env python3
"""Verify BDA5a--BDA5e radial rectangle decoding."""

from __future__ import annotations

from itertools import combinations, permutations
from math import factorial


Point = tuple[int, int]
Vector = tuple[int, int]


def add_scaled(anchor: Point, scale: int, direction: Vector) -> Point:
    return (
        anchor[0] + scale * direction[0],
        anchor[1] + scale * direction[1],
    )


def determinant(anchor: Point, first: Point, second: Point) -> int:
    return (
        (first[0] - anchor[0]) * (second[1] - anchor[1])
        - (first[1] - anchor[1]) * (second[0] - anchor[0])
    )


def rectangle(
    anchor: Point,
    h: int,
    q: int,
    direction: Vector,
    role: int,
) -> tuple[Point, Point, Point, Point]:
    first = add_scaled(anchor, h * role, direction)
    second = add_scaled(anchor, (h + q) * role, direction)
    cross_first = first[0], second[1]
    cross_second = second[0], first[1]
    return first, second, cross_first, cross_second


def is_matching(points: set[Point]) -> bool:
    return (
        len({point[0] for point in points}) == len(points)
        and len({point[1] for point in points}) == len(points)
    )


def verify_geometry() -> None:
    anchors = ((0, 0), (3, -2), (-4, 5))
    for anchor in anchors:
        for h in range(1, 7):
            for q in range(2, 7):
                for a in range(1, 5):
                    for b in range(-4, 5):
                        if b == 0:
                            continue
                        direction = a, b
                        for role in range(-4, 5):
                            if role == 0:
                                continue
                            first, second, cross_first, cross_second = (
                                rectangle(
                                    anchor,
                                    h,
                                    q,
                                    direction,
                                    role,
                                )
                            )
                            assert {first[0], second[0]} == {
                                cross_first[0],
                                cross_second[0],
                            }
                            assert {first[1], second[1]} == {
                                cross_first[1],
                                cross_second[1],
                            }
                            assert len({
                                first,
                                second,
                                cross_first,
                                cross_second,
                            }) == 4
                            expected = -a * b * role**2 * q * (2 * h + q)
                            assert determinant(
                                anchor,
                                cross_first,
                                cross_second,
                            ) == expected
                            assert expected != 0


def verify_blocker_patterns() -> None:
    anchor = 0, 0
    for h in range(1, 8):
        for q in range(2, 7):
            for direction in ((1, 1), (2, -1), (1, -2)):
                for roles in ((1, 2), (-1, 2), (2, -3)):
                    active = {anchor}
                    rectangles = {}
                    for role in roles:
                        data = rectangle(anchor, h, q, direction, role)
                        active.update(data[:2])
                        rectangles[role] = data
                    if len(active) != 5 or not is_matching(active):
                        continue

                    cross_cells = {
                        point
                        for data in rectangles.values()
                        for point in data[2:]
                    }
                    assert len(cross_cells) == 4
                    cross_tuple = tuple(cross_cells)
                    for size in range(len(cross_tuple) + 1):
                        for selected in combinations(cross_tuple, size):
                            blockers = set(selected)
                            if not is_matching(blockers):
                                continue
                            counts = {
                                role: len(set(data[2:]) & blockers)
                                for role, data in rectangles.items()
                            }
                            assert all(
                                count in (0, 1, 2)
                                for count in counts.values()
                            )
                            if all(
                                count not in (0, 2)
                                for count in counts.values()
                            ):
                                assert set(counts.values()) == {1}
                                blocker_sets = [
                                    set(rectangles[role][2:]) & blockers
                                    for role in roles
                                ]
                                assert all(
                                    len(blocker_set) == 1
                                    for blocker_set in blocker_sets
                                )
                                assert blocker_sets[0].isdisjoint(
                                    blocker_sets[1]
                                )
                                first_blocker = next(iter(blocker_sets[0]))
                                second_blocker = next(iter(blocker_sets[1]))
                                active_after = cross_cells
                                replacement = {
                                    (
                                        first_blocker[0],
                                        second_blocker[1],
                                    ),
                                    (
                                        second_blocker[0],
                                        first_blocker[1],
                                    ),
                                }
                                assert is_matching(replacement)
                                assert replacement.isdisjoint(active_after)
                                assert {
                                    point[0] for point in replacement
                                } == {
                                    first_blocker[0],
                                    second_blocker[0],
                                }
                                assert {
                                    point[1] for point in replacement
                                } == {
                                    first_blocker[1],
                                    second_blocker[1],
                                }

                            for role, count in counts.items():
                                first, second, cross_first, cross_second = (
                                    rectangles[role]
                                )
                                if count == 0:
                                    assert not (
                                        {cross_first, cross_second} & blockers
                                    )
                                elif count == 2:
                                    before_active = {first, second}
                                    before_blocker = {
                                        cross_first,
                                        cross_second,
                                    }
                                    assert is_matching(before_active)
                                    assert is_matching(before_blocker)
                                    assert {
                                        point[0] for point in before_active
                                    } == {
                                        point[0] for point in before_blocker
                                    }
                                    assert {
                                        point[1] for point in before_active
                                    } == {
                                        point[1] for point in before_blocker
                                    }


def verify_coupled_derangements(maximum_size: int = 8) -> None:
    for size in range(2, maximum_size + 1):
        active_after = {
            point
            for index in range(size)
            for point in (
                (2 * index, 2 * index + 1),
                (2 * index + 1, 2 * index),
            )
        }
        blockers = {
            (2 * index, 2 * index + 1)
            for index in range(size)
        }
        assert blockers <= active_after
        derangements = [
            permutation
            for permutation in permutations(range(size))
            if all(
                permutation[index] != index
                for index in range(size)
            )
        ]
        assert derangements
        for permutation in derangements:
            replacement = {
                (2 * index, 2 * permutation[index] + 1)
                for index in range(size)
            }
            assert is_matching(replacement)
            assert replacement.isdisjoint(active_after)

        if size >= 7:
            assert 128 * len(derangements) >= factorial(size)
            for rank in range(1, min(3, size) + 1):
                maximum_containing = factorial(size - rank)
                assert (
                    maximum_containing * falling(size, rank)
                    <= 128 * len(derangements)
                )


def falling(value: int, rank: int) -> int:
    result = 1
    for offset in range(rank):
        result *= value - offset
    return result


def main() -> None:
    verify_geometry()
    verify_blocker_patterns()
    verify_coupled_derangements()
    print("BDA radial rectangle decoder: verified")


if __name__ == "__main__":
    main()
