#!/usr/bin/env python3
"""Exact first-stage protected-rainbow cylinder censuses at orders 11 and 13."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import prod

Permutation = tuple[int, ...]
SLOPE = 2


def rainbow_family(order: int) -> tuple[Permutation, ...]:
    permutation = [-1] * order
    result: list[Permutation] = []

    def search(row: int, used_values: int, used_plus: int, used_minus: int) -> None:
        if row == order:
            result.append(tuple(permutation))
            return
        for value in range(order):
            value_bit = 1 << value
            if used_values & value_bit:
                continue
            plus = (row - SLOPE * value) % order
            minus = (-row - SLOPE * value) % order
            plus_bit = 1 << plus
            minus_bit = 1 << minus
            if used_plus & plus_bit or used_minus & minus_bit:
                continue
            permutation[row] = value
            search(
                row + 1,
                used_values | value_bit,
                used_plus | plus_bit,
                used_minus | minus_bit,
            )

    search(0, 0, 0, 0)
    return tuple(result)


def cylinder_histogram(
    family: tuple[Permutation, ...], order: int, rank: int
) -> Counter[int]:
    counts: Counter[tuple[tuple[int, int], ...]] = Counter()
    for permutation in family:
        for domain in combinations(range(order), rank):
            counts[tuple((x, permutation[x]) for x in domain)] += 1
    return Counter(counts.values())


def falling(order: int, rank: int) -> int:
    return prod(range(order - rank + 1, order + 1))


def check_order(
    order: int,
    expected_size: int,
    expected_histograms: tuple[Counter[int], Counter[int], Counter[int]],
    expected_constants: tuple[Fraction, Fraction, Fraction],
) -> None:
    family = rainbow_family(order)
    assert len(family) == expected_size
    constants: list[Fraction] = []
    for rank, expected_histogram in enumerate(expected_histograms, start=1):
        histogram = cylinder_histogram(family, order, rank)
        assert histogram == expected_histogram
        maximum = max(histogram)
        constants.append(Fraction(maximum * falling(order, rank), len(family)))
    assert tuple(constants) == expected_constants
    print(
        f"order={order} family={len(family)} "
        f"constants={','.join(map(str, constants))} PASS"
    )


def main() -> None:
    check_order(
        11,
        88,
        (
            Counter({8: 121}),
            Counter({1: 4_840}),
            Counter({1: 14_520}),
        ),
        (Fraction(1), Fraction(5, 4), Fraction(45, 4)),
    )
    check_order(
        13,
        4_524,
        (
            Counter({348: 169}),
            Counter({29: 8_112, 58: 2_028}),
            Counter({
                2: 97_344,
                4: 32_448,
                5: 29_744,
                6: 48_672,
                8: 48_672,
                16: 1_352,
                18: 2_028,
                20: 4_056,
            }),
        ),
        (Fraction(1), Fraction(2), Fraction(220, 29)),
    )
    assert 88 < 11**3
    assert 4_524 > 13**3
    print("PX1139--PX1142 protected rainbow orders 11 and 13 census: PASS")


if __name__ == "__main__":
    main()
