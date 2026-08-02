#!/usr/bin/env python3
"""Verify the protected rectangle coset absorber theorem PX75."""
from __future__ import annotations

from collections import Counter
from itertools import product
from math import gcd
import random

Point = tuple[int, int]
Direction = tuple[int, int]


def primitive_directions(height: int) -> tuple[Direction, ...]:
    result: list[Direction] = []
    for a in range(1, height + 1):
        for b in range(-height, height + 1):
            if b == 0 or max(a, abs(b)) > height:
                continue
            if gcd(a, abs(b)) == 1:
                result.append((a, b))
    return tuple(result)


def find_slope(n: int, directions: tuple[Direction, ...]) -> int:
    for slope in range(n):
        if gcd(slope, n) != 1:
            continue
        if all(gcd(b - a * slope, n) == 1 for a, b in directions):
            return slope
    raise AssertionError((n, directions))


def subgroup(n: int, order: int) -> tuple[int, ...]:
    assert n % order == 0
    step = n // order
    return tuple((step * index) % n for index in range(order))


def coset_index(n: int, order: int, value: int) -> int:
    return value % (n // order)


def rectangle_points(
    n: int,
    order: int,
    shifts: tuple[int, ...],
    slope: int,
    column_shift: int,
    row_shift: int,
) -> tuple[Point, ...]:
    expected_cosets = n // order
    assert len(shifts) == expected_cosets
    group = set(subgroup(n, order))
    assert all(shift in group for shift in shifts)

    points: list[Point] = []
    t_values: list[int] = []
    for u in range(n):
        delta = shifts[coset_index(n, order, u)]
        phi = (u + delta) % n
        p = (u + row_shift) % n
        t = (slope * phi + column_shift) % n
        t_values.append(t)
        points.extend(((u, t), (u, n + t), (n + p, t), (n + p, n + t)))

    assert sorted(t_values) == list(range(n))
    return tuple(points)


def line_coordinate(direction: Direction, point: Point) -> int:
    a, b = direction
    x, y = point
    return b * x - a * y


def verify_state(
    n: int,
    order: int,
    shifts: tuple[int, ...],
    slope: int,
    directions: tuple[Direction, ...],
) -> None:
    points = rectangle_points(n, order, shifts, slope, 3 % n, 2 % n)
    assert len(points) == 4 * n
    assert len(set(points)) == 4 * n
    assert all(sum(x == row for x, _ in points) == 2 for row in range(2 * n))
    assert all(sum(y == column for _, y in points) == 2 for column in range(2 * n))
    for direction in directions:
        occupancy = Counter(line_coordinate(direction, point) for point in points)
        assert max(occupancy.values(), default=0) <= 2


def exhaust_order_five_bank() -> None:
    n = 25
    order = 5
    directions = primitive_directions(1)
    slope = find_slope(n, directions)
    group = subgroup(n, order)
    state_count = 0
    for shifts in product(group, repeat=n // order):
        verify_state(n, order, shifts, slope, directions)
        state_count += 1
    assert state_count == order ** (n // order) == 3125
    print(f"Z_{n}, subgroup order {order}: exhausted {state_count} states")


def verify_random_banks() -> None:
    rng = random.Random(7501)
    examples = ((35, 5, 1), (49, 7, 1), (77, 7, 1), (121, 11, 2))
    for n, order, height in examples:
        directions = primitive_directions(height)
        slope = find_slope(n, directions)
        group = subgroup(n, order)
        coset_count = n // order
        for _ in range(80):
            shifts = tuple(rng.choice(group) for _ in range(coset_count))
            verify_state(n, order, shifts, slope, directions)
        print(
            f"Z_{n}, subgroup order {order}, H={height}: "
            f"checked 80 of {order ** coset_count} states"
        )


def verify_local_support() -> None:
    n = 25
    order = 5
    directions = primitive_directions(1)
    slope = find_slope(n, directions)
    zero = tuple(0 for _ in range(n // order))
    group = subgroup(n, order)
    base = set(rectangle_points(n, order, zero, slope, 0, 0))
    changed = list(zero)
    changed[2] = group[1]
    moved = set(rectangle_points(n, order, tuple(changed), slope, 0, 0))
    symmetric_difference = base ^ moved
    assert len(symmetric_difference) <= 8 * order
    affected_rows = {x for x, _ in symmetric_difference}
    expected_rows = set()
    step = n // order
    for u in range(n):
        if u % step == 2:
            expected_rows.add(u)
            expected_rows.add(n + u)
    assert affected_rows.issubset(expected_rows)
    verify_state(n, order, tuple(changed), slope, directions)
    print("single-coset support and protected saturation checked")


def main() -> None:
    exhaust_order_five_bank()
    verify_random_banks()
    verify_local_support()
    print("protected rectangle coset absorbers verified")


if __name__ == "__main__":
    main()
