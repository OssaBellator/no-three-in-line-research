#!/usr/bin/env python3
"""Verify blockwise digit permutations and the parity-reflection lift.

The script checks the exact side-10 witness obtained from a locally permuted
2 x 5 product host, then exhausts the parity-reflection subfamily through
base side eight.
"""
from __future__ import annotations

from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


def local_product_host(
    outer: FactorPair,
    inner: FactorPair,
    row_maps: tuple[Permutation, ...],
    column_maps: tuple[Permutation, ...],
    orientation: str,
) -> tuple[Point, ...]:
    m = len(outer[0])
    n = len(inner[0])
    cells: set[Point] = set()
    for r in (0, 1):
        for s in (0, 1):
            for i in range(m):
                j = outer[r][i]
                for u in range(n):
                    v = inner[s][u]
                    row_digit = row_maps[i][u]
                    column_digit = column_maps[j][v]
                    x = n * i + row_digit if orientation[0] == "c" else m * row_digit + i
                    y = n * j + column_digit if orientation[1] == "c" else m * column_digit + j
                    cells.add((x, y))
    assert len(cells) == 4 * m * n
    return tuple(sorted(cells))


def verify_four_regular(host: tuple[Point, ...]) -> None:
    side = len(host) // 4
    assert len(host) == 4 * side
    assert all(sum(x == row for x, _ in host) == 4 for row in range(side))
    assert all(sum(y == column for _, y in host) == 4 for column in range(side))


def verify_degree_two_state(
    host: tuple[Point, ...],
    layers: FactorPair,
) -> None:
    side = len(layers[0])
    assert len(layers[1]) == side
    assert all(sorted(layer) == list(range(side)) for layer in layers)
    assert all(layers[0][x] != layers[1][x] for x in range(side))
    points = tuple(
        (x, layers[layer][x])
        for layer in (0, 1)
        for x in range(side)
    )
    assert set(points).issubset(host)
    assert is_no_three(points)


def reflection_lift(tau: Permutation) -> tuple[Point, ...]:
    n = len(tau)
    side = 2 * n
    return tuple(
        (x, y)
        for u, v in enumerate(tau)
        for x in (2 * u, side - 1 - 2 * u)
        for y in (2 * v, side - 1 - 2 * v)
    )


def verify_reflection_saturation(tau: Permutation) -> None:
    points = reflection_lift(tau)
    side = 2 * len(tau)
    assert len(points) == 2 * side
    assert len(set(points)) == 2 * side
    assert all(sum(x == row for x, _ in points) == 2 for row in range(side))
    assert all(sum(y == column for _, y in points) == 2 for column in range(side))


def main() -> None:
    outer: FactorPair = ((0, 1), (1, 0))
    inner: FactorPair = ((0, 2, 1, 4, 3), (2, 4, 0, 3, 1))
    identity = (0, 1, 2, 3, 4)
    reversal = (4, 3, 2, 1, 0)
    host = local_product_host(
        outer,
        inner,
        (identity, reversal),
        (identity, reversal),
        "ff",
    )
    verify_four_regular(host)

    side_ten: FactorPair = (
        (4, 2, 1, 3, 0, 9, 6, 8, 7, 5),
        (5, 7, 8, 6, 9, 0, 3, 1, 2, 4),
    )
    verify_degree_two_state(host, side_ten)

    tau = inner[1]
    assert set(reflection_lift(tau)) == {
        (x, side_ten[layer][x])
        for layer in (0, 1)
        for x in range(10)
    }
    print("side 10 blockwise-reversal product witness verified")

    expected: dict[int, tuple[int, Permutation | None]] = {
        2: (1, (1, 0)),
        3: (0, None),
        4: (0, None),
        5: (1, (2, 4, 0, 3, 1)),
        6: (0, None),
        7: (0, None),
        8: (0, None),
    }
    for n in range(2, 9):
        count = 0
        first: Permutation | None = None
        for candidate in permutations(range(n)):
            verify_reflection_saturation(candidate)
            if is_no_three(reflection_lift(candidate)):
                count += 1
                if first is None:
                    first = candidate
        assert (count, first) == expected[n]
        print(f"reflection lift n={n}: no-three permutations={count}, first={first}")


if __name__ == "__main__":
    main()
