#!/usr/bin/env python3
"""Verify universal side-four closure from one normalized PX28 template."""
from __future__ import annotations

from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]

TARGET: Permutation = (1, 3, 0, 2)
EXPECTED_LAYERS = (
    (2, 3, 6, 7, 0, 1, 4, 5),
    (3, 2, 7, 6, 1, 0, 5, 4),
)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def compose(first: Permutation, second: Permutation) -> Permutation:
    return tuple(first[second[x]] for x in range(len(first)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for x, value in enumerate(permutation):
        result[value] = x
    return tuple(result)


def transported_state(tau: Permutation) -> tuple[Point, ...]:
    beta = compose(TARGET, inverse(tau))
    outer = ((0, 1), (1, 0))
    points: list[Point] = []
    for layer in (0, 1):
        for i in (0, 1):
            j = outer[layer][i]
            for u in range(4):
                v = tau[u]
                x = 2 * u + i
                y = 2 * beta[v] + j
                points.append((x, y))
    return tuple(sorted(points))


def expected_state() -> tuple[Point, ...]:
    return tuple(
        sorted(
            (x, EXPECTED_LAYERS[layer][x])
            for layer in (0, 1)
            for x in range(8)
        )
    )


def verify_saturation(points: tuple[Point, ...]) -> None:
    assert len(points) == 16
    assert len(set(points)) == 16
    assert all(sum(x == row for x, _ in points) == 2 for row in range(8))
    assert all(sum(y == column for _, y in points) == 2 for column in range(8))


def main() -> None:
    target_points = expected_state()
    verify_saturation(target_points)
    assert all(
        determinant(*triple) != 0
        for triple in combinations(target_points, 3)
    )

    for tau in permutations(range(4)):
        points = transported_state(tau)
        assert points == target_points

    print(
        "universal 2x4 closure verified: all 24 fine permutations transport "
        "to the same side-eight no-three state"
    )


if __name__ == "__main__":
    main()
