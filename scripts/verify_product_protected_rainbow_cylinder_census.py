#!/usr/bin/env python3
"""Exact rank-three cylinder census for protected simultaneous-rainbow families."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import prod

Direction = tuple[int, int]
Permutation = tuple[int, ...]
DIRECTIONS: tuple[Direction, ...] = ((1, 1), (1, -1))
SLOPE = 2


def is_permutation(values: list[int], order: int) -> bool:
    return sorted(values) == list(range(order))


def first_stage_rainbow(phi: Permutation, order: int) -> bool:
    return all(
        is_permutation(
            [(b * x - a * SLOPE * phi[x]) % order for x in range(order)],
            order,
        )
        for a, b in DIRECTIONS
    )


def second_stage_rainbow(
    row_permutation: Permutation,
    phi: Permutation,
    order: int,
) -> bool:
    return all(
        is_permutation(
            [
                (b * row_permutation[x] - a * SLOPE * phi[x]) % order
                for x in range(order)
            ],
            order,
        )
        for a, b in DIRECTIONS
    )


def falling(order: int, rank: int) -> int:
    return prod(range(order - rank + 1, order + 1))


def cylinder_histogram(
    family: tuple[Permutation, ...],
    order: int,
    rank: int,
) -> Counter[int]:
    counts: Counter[tuple[tuple[int, int], ...]] = Counter()
    for permutation in family:
        for domain in combinations(range(order), rank):
            counts[tuple((x, permutation[x]) for x in domain)] += 1
    return Counter(counts.values())


def check_order(order: int, expected_size: int, expected_rank_constants: tuple[float, ...]) -> None:
    all_permutations = tuple(permutations(range(order)))
    first_family = tuple(
        permutation
        for permutation in all_permutations
        if first_stage_rainbow(permutation, order)
    )
    assert len(first_family) == expected_size

    for rank, expected_constant in enumerate(expected_rank_constants, start=1):
        histogram = cylinder_histogram(first_family, order, rank)
        maximum_count = max(histogram)
        constant = maximum_count * falling(order, rank) / len(first_family)
        assert constant == expected_constant
        if rank >= 2:
            assert maximum_count == 1

    conditional_sizes: Counter[int] = Counter()
    conditional_constants: list[tuple[float, float, float]] = []
    for phi in first_family:
        second_family = tuple(
            permutation
            for permutation in all_permutations
            if second_stage_rainbow(permutation, phi, order)
        )
        conditional_sizes[len(second_family)] += 1
        constants = []
        for rank in range(1, 4):
            histogram = cylinder_histogram(second_family, order, rank)
            maximum_count = max(histogram)
            constants.append(
                maximum_count * falling(order, rank) / len(second_family)
            )
            if rank >= 2:
                assert maximum_count == 1
        conditional_constants.append(tuple(constants))

    assert conditional_sizes == Counter({expected_size: expected_size})
    assert set(conditional_constants) == {expected_rank_constants}
    print(
        f"order={order} family={expected_size} "
        f"rank_constants={expected_rank_constants} "
        f"conditional_families={expected_size} PASS"
    )


def main() -> None:
    check_order(5, 10, (1.0, 2.0, 6.0))
    check_order(7, 28, (1.0, 1.5, 7.5))
    print("PX1033--PX1035 protected rainbow cylinder census: PASS")


if __name__ == "__main__":
    main()
