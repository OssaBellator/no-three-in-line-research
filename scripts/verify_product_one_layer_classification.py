#!/usr/bin/env python3
"""Classify simultaneous-reversal one-inner-layer products through base side 8."""
from __future__ import annotations

from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def one_layer_state(tau: Permutation, orientation: str) -> tuple[Point, ...]:
    n = len(tau)
    identity = tuple(range(n))
    reversal = tuple(reversed(range(n)))
    outer = ((0, 1), (1, 0))
    points: list[Point] = []
    for r in (0, 1):
        for i in range(2):
            j = outer[r][i]
            for u in range(n):
                v = tau[u]
                row_digit = (identity, reversal)[i][u]
                column_digit = (identity, reversal)[j][v]
                x = n * i + row_digit if orientation[0] == "c" else 2 * row_digit + i
                y = n * j + column_digit if orientation[1] == "c" else 2 * column_digit + j
                points.append((x, y))
    return tuple(points)


def is_no_three(points: tuple[Point, ...]) -> bool:
    for index, third in enumerate(points):
        for first, second in combinations(points[:index], 2):
            if determinant(first, second, third) == 0:
                return False
    return True


def verify_saturation(points: tuple[Point, ...]) -> None:
    side = len(points) // 2
    assert len(set(points)) == 2 * side
    assert all(sum(x == row for x, _ in points) == 2 for row in range(side))
    assert all(sum(y == column for _, y in points) == 2 for column in range(side))


def main() -> None:
    expected: dict[int, dict[str, tuple[int, Permutation | None]]] = {
        2: {orientation: (1, (1, 0)) for orientation in ("cc", "cf", "fc", "ff")},
        3: {orientation: (0, None) for orientation in ("cc", "cf", "fc", "ff")},
        4: {orientation: (0, None) for orientation in ("cc", "cf", "fc", "ff")},
        5: {
            "cc": (1, (4, 2, 1, 3, 0)),
            "cf": (1, (2, 1, 4, 3, 0)),
            "fc": (1, (4, 1, 0, 3, 2)),
            "ff": (1, (2, 4, 0, 3, 1)),
        },
        6: {orientation: (0, None) for orientation in ("cc", "cf", "fc", "ff")},
        7: {orientation: (0, None) for orientation in ("cc", "cf", "fc", "ff")},
        8: {orientation: (0, None) for orientation in ("cc", "cf", "fc", "ff")},
    }

    for n in range(2, 9):
        for orientation in ("cc", "cf", "fc", "ff"):
            count = 0
            first: Permutation | None = None
            for tau in permutations(range(n)):
                points = one_layer_state(tau, orientation)
                verify_saturation(points)
                if is_no_three(points):
                    count += 1
                    if first is None:
                        first = tau
            assert (count, first) == expected[n][orientation]
            print(
                f"n={n}, orientation={orientation}: "
                f"no-three permutations={count}, first={first}"
            )


if __name__ == "__main__":
    main()
