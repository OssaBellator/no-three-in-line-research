#!/usr/bin/env python3
"""Arithmetic checks for CMR741--CMR747."""

from functools import lru_cache
from math import comb


@lru_cache(maxsize=None)
def maximum_splits(side):
    if side == 0:
        return 0
    return max(
        1 + maximum_splits(left) + maximum_splits(right)
        for left in range(side)
        for right in (side - 1 - left,)
    )


@lru_cache(maxsize=None)
def maximum_created_nodes(side):
    if side == 0:
        return 1
    return max(
        1 + maximum_created_nodes(left) + maximum_created_nodes(right)
        for left in range(side)
        for right in (side - 1 - left,)
    )


@lru_cache(maxsize=None)
def maximum_square_stock(side):
    if side == 0:
        return 0
    return side * side + max(
        maximum_square_stock(left) + maximum_square_stock(right)
        for left in range(side)
        for right in (side - 1 - left,)
    )


@lru_cache(maxsize=None)
def maximum_certificate_stock(side):
    if side == 0:
        return 0
    local = comb(side * side, 3) if side * side >= 3 else 0
    return local + max(
        maximum_certificate_stock(left)
        + maximum_certificate_stock(right)
        for left in range(side)
        for right in (side - 1 - left,)
    )


def main():
    checked = 0
    for side in range(1, 160):
        square_sum = sum(index * index for index in range(1, side + 1))
        certificate_sum = sum(
            comb(index * index, 3) if index * index >= 3 else 0
            for index in range(1, side + 1)
        )

        assert maximum_splits(side) == side
        assert maximum_created_nodes(side) == 2 * side + 1
        assert maximum_square_stock(side) == square_sum
        assert maximum_certificate_stock(side) == certificate_sum

        for left in range(side + 1):
            right = side - left
            left_square_sum = sum(
                index * index for index in range(1, left + 1)
            )
            right_square_sum = sum(
                index * index for index in range(1, right + 1)
            )
            assert left_square_sum + right_square_sum <= square_sum

        for prime in (3, 5, 7, 11):
            for height in range(1, 8):
                token_stock = (
                    (prime + 1) * (height - 1) * square_sum
                )
                assert token_stock >= 0

        for recurrence_threshold in range(2, 12):
            for witnesses_per_episode in range(1, 10):
                episode_bound = (
                    (recurrence_threshold - 1)
                    * square_sum
                    // witnesses_per_episode
                )
                assert episode_bound * witnesses_per_episode <= (
                    recurrence_threshold - 1
                ) * square_sum

        checked += 1

    print(
        "verified unit Hall wall factor-tree stock:",
        checked,
        "initial sides",
    )


if __name__ == "__main__":
    main()
