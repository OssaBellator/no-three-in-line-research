#!/usr/bin/env python3
"""Verify the affine rectangle finite-direction theorems PX72--PX74."""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd

Point = tuple[int, int]
Direction = tuple[int, int]


def primitive_directions(height: int) -> tuple[Direction, ...]:
    result: list[Direction] = []
    for a in range(-height, height + 1):
        for b in range(-height, height + 1):
            if a == 0 or b == 0:
                continue
            if max(abs(a), abs(b)) > height or gcd(abs(a), abs(b)) != 1:
                continue
            if a < 0 or (a == 0 and b < 0):
                continue
            result.append((a, b))
    return tuple(result)


def rectangle_points(n: int, slope: int, column_shift: int, row_shift: int) -> tuple[Point, ...]:
    result: list[Point] = []
    for u in range(n):
        p = (u + row_shift) % n
        t = (slope * u + column_shift) % n
        result.extend(((u, t), (u, n + t), (n + p, t), (n + p, n + t)))
    return tuple(result)


def line_coordinate(direction: Direction, point: Point) -> int:
    a, b = direction
    x, y = point
    return b * x - a * y


def find_slope(n: int, directions: tuple[Direction, ...]) -> int | None:
    for slope in range(n):
        if gcd(slope, n) != 1:
            continue
        if all(gcd(b - a * slope, n) == 1 for a, b in directions):
            return slope
    return None


def verify_state(n: int, slope: int, directions: tuple[Direction, ...]) -> None:
    assert gcd(slope, n) == 1
    assert all(gcd(b - a * slope, n) == 1 for a, b in directions)
    for column_shift in range(min(n, 4)):
        for row_shift in range(min(n, 4)):
            points = rectangle_points(n, slope, column_shift, row_shift)
            assert len(points) == 4 * n
            assert len(set(points)) == 4 * n
            assert all(sum(x == row for x, _ in points) == 2 for row in range(2 * n))
            assert all(sum(y == column for _, y in points) == 2 for column in range(2 * n))
            for direction in directions:
                occupancy = Counter(line_coordinate(direction, point) for point in points)
                assert max(occupancy.values(), default=0) <= 2


def verify_arithmetic_examples() -> None:
    examples = ((5, 1), (7, 1), (11, 2), (13, 2), (17, 2), (25, 1), (49, 1))
    for n, height in examples:
        directions = primitive_directions(height)
        assert len(directions) <= 2 * height * (height + 1)
        least_prime = next(divisor for divisor in range(2, n + 1) if n % divisor == 0)
        assert least_prime > len(directions) + 1
        slope = find_slope(n, directions)
        assert slope is not None
        verify_state(n, slope, directions)
        print(
            f"n={n}, H={height}, directions={len(directions)}, "
            f"least_prime={least_prime}, slope={slope}"
        )


def verify_all_small_admissible_cases() -> None:
    for n in range(3, 31):
        least_prime = next(divisor for divisor in range(2, n + 1) if n % divisor == 0)
        for height in range(1, 5):
            directions = primitive_directions(height)
            if least_prime <= len(directions) + 1:
                continue
            slope = find_slope(n, directions)
            assert slope is not None, (n, height, directions)
            verify_state(n, slope, directions)
    print("all admissible cases through modulus 30 checked")


def verify_no_protected_triples() -> None:
    n = 17
    height = 2
    directions = primitive_directions(height)
    slope = find_slope(n, directions)
    assert slope is not None
    points = rectangle_points(n, slope, 3, 5)
    direction_set = set(directions)
    for first, second, third in combinations(points, 3):
        determinant = (second[0] - first[0]) * (third[1] - first[1]) - (
            second[1] - first[1]
        ) * (third[0] - first[0])
        if determinant != 0:
            continue
        dx = second[0] - first[0]
        dy = second[1] - first[1]
        divisor = gcd(abs(dx), abs(dy))
        primitive = (dx // divisor, dy // divisor)
        if primitive[0] < 0 or (primitive[0] == 0 and primitive[1] < 0):
            primitive = (-primitive[0], -primitive[1])
        assert primitive not in direction_set
    print("explicit triple scan confirms protected-direction avoidance")


def main() -> None:
    verify_arithmetic_examples()
    verify_all_small_admissible_cases()
    verify_no_protected_triples()
    print("affine rectangle direction protection verified")


if __name__ == "__main__":
    main()
