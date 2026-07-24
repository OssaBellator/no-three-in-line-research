#!/usr/bin/env python3
"""Verify the two-coordinate protected affine-coset bank PX81--PX82."""
from __future__ import annotations

from collections import Counter
from math import gcd
import random

Point = tuple[int, int]
Direction = tuple[int, int]
LocalState = tuple[int, int, int, int]


def primitive_directions(height: int) -> tuple[Direction, ...]:
    result: list[Direction] = []
    for a in range(1, height + 1):
        for b in range(-height, height + 1):
            if b == 0 or max(a, abs(b)) > height:
                continue
            if gcd(a, abs(b)) == 1:
                result.append((a, b))
    return tuple(result)


def find_base_slope(n: int, directions: tuple[Direction, ...]) -> int:
    for slope in range(n):
        if gcd(slope, n) != 1:
            continue
        if all(gcd(b - a * slope, n) == 1 for a, b in directions):
            return slope
    raise AssertionError((n, directions))


def subgroup(n: int, order: int) -> tuple[int, ...]:
    assert n % order == 0
    step = n // order
    return tuple(step * index for index in range(order))


def admissible_pairs(
    order: int,
    slope: int,
    directions: tuple[Direction, ...],
) -> tuple[tuple[int, int], ...]:
    units = tuple(value for value in range(order) if gcd(value, order) == 1)
    return tuple(
        (row_slope, column_slope)
        for row_slope in units
        for column_slope in units
        if all(
            gcd(b - a * slope * column_slope, order) == 1
            and gcd(b * row_slope - a * slope * column_slope, order) == 1
            for a, b in directions
        )
    )


def rectangle_points(
    n: int,
    order: int,
    slope: int,
    choices: tuple[LocalState, ...],
    global_shift: int = 0,
) -> tuple[Point, ...]:
    coset_count = n // order
    assert len(choices) == coset_count
    group = set(subgroup(n, order))
    p_values: list[int] = []
    t_values: list[int] = []
    points: list[Point] = []

    for fine_row in range(n):
        representative = fine_row % coset_count
        group_coordinate = (fine_row - representative) % n
        row_slope, column_slope, row_shift, column_shift = choices[representative]
        assert row_shift in group and column_shift in group
        p_value = (
            representative + row_slope * group_coordinate + row_shift
        ) % n
        phi_value = (
            representative + column_slope * group_coordinate + column_shift
        ) % n
        t_value = (slope * phi_value + global_shift) % n
        p_values.append(p_value)
        t_values.append(t_value)
        points.extend(
            (
                (fine_row, t_value),
                (fine_row, n + t_value),
                (n + p_value, t_value),
                (n + p_value, n + t_value),
            )
        )

    assert sorted(p_values) == list(range(n))
    assert sorted(t_values) == list(range(n))
    return tuple(points)


def line_coordinate(direction: Direction, point: Point) -> int:
    a, b = direction
    x, y = point
    return b * x - a * y


def verify_state(
    n: int,
    order: int,
    slope: int,
    directions: tuple[Direction, ...],
    choices: tuple[LocalState, ...],
) -> None:
    points = rectangle_points(n, order, slope, choices, global_shift=3 % n)
    assert len(points) == 4 * n
    assert len(set(points)) == 4 * n
    assert all(sum(x == row for x, _ in points) == 2 for row in range(2 * n))
    assert all(sum(y == column for _, y in points) == 2 for column in range(2 * n))
    for direction in directions:
        occupancy = Counter(line_coordinate(direction, point) for point in points)
        assert max(occupancy.values(), default=0) <= 2


def exhaust_z25_local_states() -> None:
    n = 25
    order = 5
    directions = ((1, 1), (1, -1))
    slope = 2
    pairs = admissible_pairs(order, slope, directions)
    assert pairs == ((1, 1), (1, 4), (4, 1), (4, 4))
    group = subgroup(n, order)
    local_states = tuple(
        (row_slope, column_slope, row_shift, column_shift)
        for row_slope, column_slope in pairs
        for row_shift in group
        for column_shift in group
    )
    assert len(local_states) == 100

    base = (1, 1, 0, 0)
    coset_count = n // order
    for active_coset in range(coset_count):
        for local_state in local_states:
            choices = [base] * coset_count
            choices[active_coset] = local_state
            verify_state(n, order, slope, directions, tuple(choices))
    print("Z_25: all 100 local states checked in each of five cosets")


def verify_prime_order_lower_bound() -> None:
    examples = ((25, 5, 1), (49, 7, 1), (121, 11, 2), (169, 13, 2))
    rng = random.Random(8122)
    for n, order, height in examples:
        directions = primitive_directions(height)
        assert order > len(directions) + 1
        slope = find_base_slope(n, directions)
        pairs = admissible_pairs(order, slope, directions)
        lower_bound = (order - 1 - len(directions)) ** 2
        assert len(pairs) >= lower_bound

        group = subgroup(n, order)
        local_states = tuple(
            (row_slope, column_slope, row_shift, column_shift)
            for row_slope, column_slope in pairs
            for row_shift in group
            for column_shift in group
        )
        coset_count = n // order
        for _ in range(50):
            choices = tuple(rng.choice(local_states) for _ in range(coset_count))
            verify_state(n, order, slope, directions, choices)
        print(
            f"n={n}, order={order}, H={height}, slope={slope}, "
            f"slope_pairs={len(pairs)}, local_states={len(local_states)}"
        )


def main() -> None:
    exhaust_z25_local_states()
    verify_prime_order_lower_bound()
    print("two-coordinate protected coset bank verified")


if __name__ == "__main__":
    main()
