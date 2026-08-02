#!/usr/bin/env python3
"""Verify the PX28 rectangle normal form and bad-triple classification."""
from __future__ import annotations

from itertools import combinations, permutations, product

Point = tuple[int, int]
LabelledPoint = tuple[Point, int, int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def rectangle_state(
    n: int,
    row_permutation: tuple[int, ...],
    first_column_permutation: tuple[int, ...],
    second_column_permutation: tuple[int, ...],
    orientation: str,
) -> tuple[LabelledPoint, ...]:
    result: list[LabelledPoint] = []
    for u in range(n):
        row_digits = (u, row_permutation[u])
        column_digits = (
            first_column_permutation[u],
            second_column_permutation[u],
        )
        for row_block, column_block in product((0, 1), repeat=2):
            row_digit = row_digits[row_block]
            column_digit = column_digits[column_block]
            x = n * row_block + row_digit if orientation[0] == "c" else 2 * row_digit + row_block
            y = n * column_block + column_digit if orientation[1] == "c" else 2 * column_digit + column_block
            result.append(((x, y), u, row_block, column_block))
    return tuple(result)


def verify_state(points: tuple[LabelledPoint, ...], n: int) -> None:
    scalar = tuple(point for point, _, _, _ in points)
    assert len(scalar) == len(set(scalar)) == 4 * n
    assert all(sum(x == row for x, _ in scalar) == 2 for row in range(2 * n))
    assert all(sum(y == column for _, y in scalar) == 2 for column in range(2 * n))

    for triple in combinations(points, 3):
        scalar_triple = tuple(item[0] for item in triple)
        if determinant(*scalar_triple) != 0:
            continue
        rectangle_counts: dict[int, list[LabelledPoint]] = {}
        for item in triple:
            rectangle_counts.setdefault(item[1], []).append(item)
        multiplicities = sorted(map(len, rectangle_counts.values()), reverse=True)
        assert multiplicities in ([2, 1], [1, 1, 1])
        if multiplicities == [2, 1]:
            repeated = next(items for items in rectangle_counts.values() if len(items) == 2)
            assert repeated[0][2] != repeated[1][2]
            assert repeated[0][3] != repeated[1][3]


def main() -> None:
    for n in range(2, 5):
        maps = tuple(permutations(range(n)))
        state_count = 0
        for row_permutation in maps:
            for first_column_permutation in maps:
                for second_column_permutation in maps:
                    for orientation in ORIENTATIONS:
                        points = rectangle_state(
                            n,
                            row_permutation,
                            first_column_permutation,
                            second_column_permutation,
                            orientation,
                        )
                        verify_state(points, n)
                        state_count += 1
        assert state_count == len(maps) ** 3 * 4
        print(f"n={n}: verified {state_count} rectangle matching states")

    print("PX28 rectangle normal form and conflict classification verified")


if __name__ == "__main__":
    main()
