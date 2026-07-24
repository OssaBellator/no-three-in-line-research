#!/usr/bin/env python3
"""Exact checks for CMR116--CMR119 prime-seven balanced bank."""

from __future__ import annotations

from itertools import combinations

Point = tuple[int, int]

FAMILY: tuple[tuple[int, ...], ...] = (
    (0, 3, 2, 4, 1, 6, 5),
    (1, 4, 3, 6, 2, 5, 0),
    (2, 6, 1, 5, 4, 0, 3),
    (3, 5, 6, 1, 0, 4, 2),
    (4, 2, 5, 0, 3, 1, 6),
    (5, 0, 4, 2, 6, 3, 1),
    (6, 1, 0, 3, 5, 2, 4),
)


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def verify_local() -> None:
    for mapping in FAMILY:
        assert sorted(mapping) == list(range(7))
        points = [(x, mapping[x]) for x in range(7)]
        assert all(det(*triple) != 0 for triple in combinations(points, 3))

    for x in range(7):
        assert sorted(mapping[x] for mapping in FAMILY) == list(range(7))

    for first in range(7):
        for second in range(7):
            if first == second:
                continue
            points = {
                *((x, FAMILY[first][x]) for x in range(7)),
                *((x, FAMILY[second][x]) for x in range(7)),
            }
            assert len(points) == 14
            row_counts = [sum(y == row for _, y in points) for row in range(7)]
            column_counts = [
                sum(x == column for x, _ in points) for column in range(7)
            ]
            assert row_counts == [2] * 7
            assert column_counts == [2] * 7


def digits(x: int, k: int) -> list[int]:
    result = []
    for _ in range(k):
        result.append(x % 7)
        x //= 7
    return result


def recursive_permutation(layer: int, root_index: int, k: int) -> tuple[int, ...]:
    n = 7**k
    values: list[int] = []
    for x in range(n):
        x_digits = digits(x, k)
        y_digits = [FAMILY[root_index][x_digits[0]]]
        prefix = x_digits[0]
        power = 7
        for depth in range(1, k):
            map_index = (layer + depth + prefix) % 7
            y_digits.append(FAMILY[map_index][x_digits[depth]])
            prefix += power * x_digits[depth]
            power *= 7
        values.append(
            sum(digit * (7**index) for index, digit in enumerate(y_digits))
        )
    return tuple(values)


def verify_recursive(max_exponent: int = 3) -> None:
    for k in range(1, max_exponent + 1):
        n = 7**k
        first = recursive_permutation(0, 0, k)
        second = recursive_permutation(1, 1, k)
        assert sorted(first) == list(range(n))
        assert sorted(second) == list(range(n))
        assert all(first[x] != second[x] for x in range(n))

        points = {(x, first[x]) for x in range(n)} | {
            (x, second[x]) for x in range(n)
        }
        assert len(points) == 2 * n
        assert all(sum(y == row for _, y in points) == 2 for row in range(n))
        assert all(
            sum(x == column for x, _ in points) == 2 for column in range(n)
        )

        node_count = 2 * sum(7**depth for depth in range(1, k))
        assert node_count == (n - 7) // 3


def main() -> None:
    verify_local()
    verify_recursive()
    print(
        "verified prime-seven bank: "
        "local triples=245, root pairs=42, recursive N=7,49,343"
    )


if __name__ == "__main__":
    main()
