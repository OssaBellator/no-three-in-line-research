#!/usr/bin/env python3
"""Verify protected affine cylinder laws PX83--PX84."""
from __future__ import annotations

from collections import Counter
from math import gcd

DIRECTIONS = ((1, 1), (1, -1))
SLOPE = 2
EXPECTED_PAIR_COUNTS = {5: 4, 7: 16, 11: 68}


def admissible_pairs(order: int) -> tuple[tuple[int, int], ...]:
    units = tuple(value for value in range(order) if gcd(value, order) == 1)
    return tuple(
        (row_slope, column_slope)
        for row_slope in units
        for column_slope in units
        if all(
            gcd(b - a * SLOPE * column_slope, order) == 1
            and gcd(b * row_slope - a * SLOPE * column_slope, order) == 1
            for a, b in DIRECTIONS
        )
    )


def local_states(order: int) -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        (row_slope, column_slope, row_shift, column_shift)
        for row_slope, column_slope in admissible_pairs(order)
        for row_shift in range(order)
        for column_shift in range(order)
    )


def images(
    order: int,
    state: tuple[int, int, int, int],
    index: int,
) -> tuple[int, int]:
    row_slope, column_slope, row_shift, column_shift = state
    return (
        (row_slope * index + row_shift) % order,
        (column_slope * index + column_shift) % order,
    )


def verify_order(order: int) -> None:
    pairs = admissible_pairs(order)
    assert len(pairs) == EXPECTED_PAIR_COUNTS[order]
    states = local_states(order)
    state_count = len(pairs) * order**2
    assert len(states) == state_count

    for index in range(order):
        one = Counter(images(order, state, index) for state in states)
        assert len(one) == order**2
        assert set(one.values()) == {len(pairs)}

    for first in range(order):
        for second in range(first + 1, order):
            two = Counter(
                images(order, state, first) + images(order, state, second)
                for state in states
            )
            assert set(two.values()) == {1}
            assert len(two) == state_count

    first, second, third = 0, 1, 2
    two_keys = Counter(
        images(order, state, first) + images(order, state, second)
        for state in states
    )
    three_keys = Counter(
        images(order, state, first)
        + images(order, state, second)
        + images(order, state, third)
        for state in states
    )
    assert set(two_keys.values()) == {1}
    assert set(three_keys.values()) == {1}
    assert len(two_keys) == len(three_keys) == state_count

    lower_bound = (order - 1 - len(DIRECTIONS)) ** 2
    assert len(pairs) >= lower_bound
    print(
        f"ell={order}: slope_pairs={len(pairs)}, local_states={state_count}, "
        f"one-point count={len(pairs)}, two/three-point count=1"
    )


def main() -> None:
    for order in EXPECTED_PAIR_COUNTS:
        verify_order(order)
    print("protected affine cylinder bounds and rank-two barrier verified")


if __name__ == "__main__":
    main()
