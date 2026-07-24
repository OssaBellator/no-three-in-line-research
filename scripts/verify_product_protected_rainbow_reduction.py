#!/usr/bin/env python3
"""Verify the protected simultaneous-rainbow reduction PX85--PX86."""
from __future__ import annotations

from itertools import permutations

Direction = tuple[int, int]
Permutation = tuple[int, ...]
DIRECTIONS = ((1, 1), (1, -1))
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


def check_proper_colours(order: int) -> None:
    for a, b in DIRECTIONS:
        for x in range(order):
            colours = [(b * x - a * SLOPE * y) % order for y in range(order)]
            assert is_permutation(colours, order)
        for y in range(order):
            colours = [(b * x - a * SLOPE * y) % order for x in range(order)]
            assert is_permutation(colours, order)

    sample_phi = tuple(range(order))
    for a, b in DIRECTIONS:
        for x in range(order):
            colours = [
                (b * w - a * SLOPE * sample_phi[x]) % order
                for w in range(order)
            ]
            assert is_permutation(colours, order)
        for w in range(order):
            colours = [
                (b * w - a * SLOPE * sample_phi[x]) % order
                for x in range(order)
            ]
            assert is_permutation(colours, order)
    print(f"order {order}: all protected colourings are proper")


def exhaust_order_five() -> None:
    order = 5
    all_permutations = tuple(permutations(range(order)))
    first_stage = tuple(
        phi for phi in all_permutations if first_stage_rainbow(phi, order)
    )
    assert len(first_stage) == 10

    protected_pairs = 0
    for phi in all_permutations:
        top_maps = [
            [(b * x - a * SLOPE * phi[x]) % order for x in range(order)]
            for a, b in DIRECTIONS
        ]
        top_protected = all(is_permutation(values, order) for values in top_maps)
        assert top_protected == first_stage_rainbow(phi, order)
        if not top_protected:
            continue

        for row_permutation in all_permutations:
            bottom_maps = [
                [
                    (b * row_permutation[x] - a * SLOPE * phi[x]) % order
                    for x in range(order)
                ]
                for a, b in DIRECTIONS
            ]
            direct_protection = all(
                is_permutation(values, order) for values in bottom_maps
            )
            rainbow = second_stage_rainbow(row_permutation, phi, order)
            assert direct_protection == rainbow
            protected_pairs += rainbow

    assert protected_pairs == 100
    print("order 5: first-stage matchings=10, protected pairs=100")


def count_order_seven_first_stage() -> None:
    order = 7
    count = sum(
        first_stage_rainbow(phi, order)
        for phi in permutations(range(order))
    )
    assert count == 28
    print("order 7: first-stage common-rainbow matchings=28")


def main() -> None:
    check_proper_colours(5)
    check_proper_colours(7)
    exhaust_order_five()
    count_order_seven_first_stage()
    print("protected simultaneous-rainbow reduction verified")


if __name__ == "__main__":
    main()
