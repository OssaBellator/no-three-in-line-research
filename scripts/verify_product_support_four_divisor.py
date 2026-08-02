#!/usr/bin/env python3
"""Verify PX207--PX209 ambient divisor control of support-four collateral."""
from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import isqrt
from random import Random


def divisor_count(value: int) -> int:
    assert value >= 1
    total = 0
    for divisor in range(1, isqrt(value) + 1):
        if value % divisor == 0:
            total += 1 if divisor * divisor == value else 2
    return total


def divisor_envelope(side: int) -> int:
    assert side >= 2
    return max(
        divisor_count(value)
        for value in range(1, (side - 1) ** 2 + 1)
    )


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def support_four_count(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    anchor: tuple[int, int],
) -> int:
    """Count unordered diagonal-free support-four candidate pairs through anchor."""
    cells = tuple(
        (row_index, column_index, (row, column))
        for row_index, row in enumerate(rows)
        for column_index, column in enumerate(columns)
        if row_index != column_index
    )
    total = 0
    for first, second in combinations(cells, 2):
        i, j, first_cell = first
        k, ell, second_cell = second
        if i == k or j == ell or len({i, j, k, ell}) != 4:
            continue
        if collinear(anchor, first_cell, second_cell):
            total += 1
    return total


def crossed_product_energy(
    rows: tuple[int, ...],
    columns: tuple[int, ...],
    anchor: tuple[int, int],
) -> int:
    """Upper-count candidate pairs by equal crossed products."""
    representations: Counter[int] = Counter()
    for row in rows:
        row_difference = row - anchor[0]
        if row_difference == 0:
            continue
        for column in columns:
            column_difference = column - anchor[1]
            if column_difference == 0:
                continue
            representations[row_difference * column_difference] += 1
    return sum(
        multiplicity * (multiplicity - 1) // 2
        for multiplicity in representations.values()
    )


def verify_random_fixed_anchor_bounds() -> None:
    random = Random(207208209)
    for side in range(7, 14):
        envelope = divisor_envelope(side)
        order = min(5, side - 2)
        for _ in range(100):
            rows = tuple(random.sample(range(side), order))
            columns = tuple(random.sample(range(side), order))
            grid = {(row, column) for row in rows for column in columns}
            anchors = tuple(
                (row, column)
                for row in range(side)
                for column in range(side)
                if (row, column) not in grid
            )
            anchor = random.choice(anchors)
            actual = support_four_count(rows, columns, anchor)
            energy = crossed_product_energy(rows, columns, anchor)
            assert actual <= energy
            assert energy <= envelope * order**2
        print(
            f"N={side}, t={order}: fixed-anchor divisor bound verified "
            f"with envelope {envelope}"
        )


def geometric_progression_formula(order: int) -> int:
    return 2 * sum(
        (order - difference) * (order - difference - 1) // 2
        - max(order - 2 * difference, 0)
        for difference in range(1, order)
    )


def verify_geometric_progression_sharpness() -> None:
    for order in range(4, 15):
        coordinates = tuple(1 << index for index in range(order))
        actual = support_four_count(coordinates, coordinates, (0, 0))
        formula = geometric_progression_formula(order)
        assert actual == formula
        if order >= 6:
            assert actual >= order**3 // 10
        print(
            f"geometric t={order}: support-four pairs={actual}, "
            f"ratio={actual / order**3:.6f}"
        )


def verify_large_block_exponent() -> None:
    # If t=N^(2/3+epsilon), then N/t^(3/2)=N^(-3epsilon/2).
    for numerator, denominator in ((1, 20), (1, 10), (1, 5)):
        epsilon = numerator / denominator
        exponent = 1 - 1.5 * (2 / 3 + epsilon)
        assert abs(exponent + 1.5 * epsilon) < 1e-15
        assert exponent < 0
    print("large-block N^(2/3+epsilon) exponent saving verified")


def main() -> None:
    verify_random_fixed_anchor_bounds()
    verify_geometric_progression_sharpness()
    verify_large_block_exponent()
    print("PX207--PX209 verified")


if __name__ == "__main__":
    main()
