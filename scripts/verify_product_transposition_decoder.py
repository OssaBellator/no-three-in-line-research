#!/usr/bin/env python3
"""Verify the rectangle transposition decoder and shadow coverage identities."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from random import Random

Point = tuple[int, int]
TaggedPoint = tuple[int, int, int, int, int]
Permutation = tuple[int, ...]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def flatten(n: int, coarse: int, fine: int, mode: str) -> int:
    return n * coarse + fine if mode == "c" else 2 * fine + coarse


def rectangle_state(
    p: Permutation,
    t: Permutation,
    r: Permutation,
    orientation: str,
) -> tuple[TaggedPoint, ...]:
    n = len(p)
    points: list[TaggedPoint] = []
    for rectangle in range(n):
        for coarse_row, coarse_column in product((0, 1), repeat=2):
            row_digit = rectangle if coarse_row == 0 else p[rectangle]
            column_digit = (
                t[rectangle] if coarse_column == 0 else r[rectangle]
            )
            points.append(
                (
                    flatten(n, coarse_row, row_digit, orientation[0]),
                    flatten(n, coarse_column, column_digit, orientation[1]),
                    rectangle,
                    coarse_row,
                    coarse_column,
                )
            )
    return tuple(points)


def bad_triples(points: tuple[TaggedPoint, ...]) -> set[frozenset[Point]]:
    result: set[frozenset[Point]] = set()
    for triple in combinations(points, 3):
        if determinant(triple[0][:2], triple[1][:2], triple[2][:2]) == 0:
            result.add(frozenset(point[:2] for point in triple))
    return result


def swapped_state(
    p: Permutation,
    t: Permutation,
    r: Permutation,
    family: str,
    first: int,
    second: int,
    orientation: str,
) -> tuple[TaggedPoint, ...]:
    new_t = list(t)
    new_r = list(r)
    target = new_t if family == "t" else new_r
    target[first], target[second] = target[second], target[first]
    return rectangle_state(p, tuple(new_t), tuple(new_r), orientation)


def verify_state(
    n: int,
    orientation: str,
    random: Random,
) -> tuple[int, int, int]:
    values = list(range(n))
    random.shuffle(values)
    p = tuple(values)
    values = list(range(n))
    random.shuffle(values)
    t = tuple(values)
    values = list(range(n))
    random.shuffle(values)
    r = tuple(values)

    current = rectangle_state(p, t, r, orientation)
    current_points = {point[:2] for point in current}
    current_bad = bad_triples(current)

    inserted_occurrences: Counter[Point] = Counter()
    pair_occurrences: Counter[frozenset[Point]] = Counter()
    total_destroyed = 0
    total_created = 0

    for family in ("t", "r"):
        for first, second in combinations(range(n), 2):
            updated = swapped_state(
                p, t, r, family, first, second, orientation
            )
            updated_points = {point[:2] for point in updated}
            updated_bad = bad_triples(updated)
            inserted = updated_points - current_points
            removed = current_points - updated_points
            assert len(inserted) == len(removed) == 4

            inserted_occurrences.update(inserted)
            total_destroyed += len(current_bad - updated_bad)
            total_created += len(updated_bad - current_bad)

            for left, right in combinations(sorted(inserted), 2):
                if left[1] == right[1]:
                    # The old two selected points in this scalar column were
                    # removed, and saturation leaves no background point.
                    assert not any(
                        point[1] == left[1]
                        for point in current_points - removed
                    )
                else:
                    pair_occurrences[frozenset((left, right))] += 1

    side = 2 * n
    complement = set(product(range(side), repeat=2)) - current_points
    assert set(inserted_occurrences) == complement
    assert set(inserted_occurrences.values()) == {1}
    assert len(pair_occurrences) == 4 * n * (n - 1)
    assert set(pair_occurrences.values()) == {1}
    assert total_destroyed >= 3 * (n - 4) * len(current_bad)

    return len(current_bad), total_destroyed, total_created


def main() -> None:
    random = Random(26072026)
    for n in range(5, 9):
        summaries: list[tuple[int, int, int]] = []
        for orientation in ORIENTATIONS:
            for _ in range(8):
                summaries.append(verify_state(n, orientation, random))
        print(
            f"n={n}: checked {len(summaries)} states; "
            f"defect range={min(value[0] for value in summaries)}.."
            f"{max(value[0] for value in summaries)}"
        )

    print("rectangle transposition decoder checks passed")


if __name__ == "__main__":
    main()
