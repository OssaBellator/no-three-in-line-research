#!/usr/bin/env python3
"""Exact conditional slice-entropy profile for protected rainbow families."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import prod

from verify_product_protected_rainbow_cylinder_census import (
    first_stage_rainbow,
    second_stage_rainbow,
)

Permutation = tuple[int, ...]


def falling(order: int, rank: int) -> int:
    return prod(range(order - rank + 1, order + 1))


def slice_histogram(
    family: tuple[Permutation, ...], order: int, rank: int
) -> Counter[int]:
    slices: Counter[tuple[tuple[int, int], ...]] = Counter()
    for permutation in family:
        for domain in combinations(range(order), rank):
            slices[tuple((x, permutation[x]) for x in domain)] += 1
    return Counter(slices.values())


def check_order(
    order: int,
    expected_size: int,
    expected_histograms: tuple[Counter[int], Counter[int], Counter[int]],
) -> None:
    all_permutations = tuple(permutations(range(order)))
    first_family = tuple(
        permutation
        for permutation in all_permutations
        if first_stage_rainbow(permutation, order)
    )
    assert len(first_family) == expected_size

    observed = tuple(
        slice_histogram(first_family, order, rank) for rank in range(1, 4)
    )
    assert observed == expected_histograms

    for phi in first_family:
        second_family = tuple(
            permutation
            for permutation in all_permutations
            if second_stage_rainbow(permutation, phi, order)
        )
        assert len(second_family) == expected_size
        conditional = tuple(
            slice_histogram(second_family, order, rank) for rank in range(1, 4)
        )
        assert conditional == expected_histograms

    # General necessity: a rank-three cylinder bound K after an r-edge
    # conditioning requires every nonempty slice to have at least
    # (order-r)_3/K members.  The exact small families collapse to one member
    # already at rank two, so no uniform residual cubic entropy is present.
    for rank in (2, 3):
        assert max(observed[rank - 1]) == 1
    print(
        f"order={order} family={expected_size} "
        f"rank1={dict(observed[0])} rank2={dict(observed[1])} "
        f"rank3={dict(observed[2])} PASS"
    )


def main() -> None:
    check_order(
        5,
        10,
        (Counter({2: 25}), Counter({1: 100}), Counter({1: 100})),
    )
    check_order(
        7,
        28,
        (Counter({4: 49}), Counter({1: 588}), Counter({1: 980})),
    )
    assert falling(7 - 2, 3) == 60
    print("PX1101--PX1104 protected rainbow slice entropy: PASS")


if __name__ == "__main__":
    main()
