#!/usr/bin/env python3
"""Verify PX161 anchored affine-triangle tuple-weight counts."""
from __future__ import annotations

from collections import Counter
from itertools import combinations

Edge = tuple[int, int, int, int]
Shape = tuple[int, int, int]


def edge(prime: int, row: int, column: int) -> Edge:
    return row, column, (row - column) % prime, (row + column) % prime


def compatible(prime: int, shape: Shape) -> bool:
    slope, row_ratio, image_ratio = shape
    if slope in (0, 1, prime - 1):
        return False
    if row_ratio in (0, 1) or image_ratio in (0, 1):
        return False
    return all(
        value % prime != 0
        for value in (
            row_ratio - slope * image_ratio,
            row_ratio - 1 - slope * (image_ratio - 1),
            row_ratio + slope * image_ratio,
            row_ratio - 1 + slope * (image_ratio - 1),
        )
    )


def occurrence_with_anchor(
    prime: int,
    anchor: Edge,
    shape: Shape,
    role: int,
    step: int,
) -> tuple[Edge, Edge, Edge]:
    slope, row_ratio, image_ratio = shape
    row, image = anchor[0], anchor[1]

    if role == 0:
        base_row, base_image = row, image
    elif role == 1:
        base_row = (row - step) % prime
        base_image = (image - slope * step) % prime
    elif role == 2:
        base_row = (row - row_ratio * step) % prime
        base_image = (image - image_ratio * slope * step) % prime
    else:
        raise ValueError("role must be zero, one, or two")

    return (
        edge(prime, base_row, base_image),
        edge(
            prime,
            (base_row + step) % prime,
            (base_image + slope * step) % prime,
        ),
        edge(
            prime,
            (base_row + row_ratio * step) % prime,
            (base_image + image_ratio * slope * step) % prime,
        ),
    )


def is_matching(items: tuple[Edge, ...]) -> bool:
    return all(
        len({item[part] for item in items}) == len(items)
        for part in range(4)
    )


def verify_prime(prime: int) -> None:
    host = [
        edge(prime, row, column)
        for row in range(prime)
        for column in range(prime)
    ]
    shapes = [
        (slope, row_ratio, image_ratio)
        for slope in range(prime)
        for row_ratio in range(prime)
        for image_ratio in range(prime)
        if compatible(prime, (slope, row_ratio, image_ratio))
    ]
    assert len(shapes) >= (prime - 3) * (prime - 2) * max(0, prime - 6)

    maximum_pair_multiplicity = 0
    maximum_link_weight = 0
    anchors = host if prime <= 7 else host[: min(prime, len(host))]
    for anchor in anchors:
        for shape in shapes:
            for role in range(3):
                pair_weights: Counter[tuple[Edge, Edge]] = Counter()
                for step in range(1, prime):
                    occurrence = occurrence_with_anchor(
                        prime, anchor, shape, role, step
                    )
                    assert occurrence[role] == anchor
                    assert is_matching(occurrence)
                    other_pair = tuple(
                        sorted(
                            occurrence[index]
                            for index in range(3)
                            if index != role
                        )
                    )
                    pair_weights[other_pair] += 1

                assert sum(pair_weights.values()) == prime - 1
                maximum_pair_multiplicity = max(
                    maximum_pair_multiplicity,
                    max(pair_weights.values()),
                )
                links: Counter[Edge] = Counter()
                for pair, weight in pair_weights.items():
                    for item in pair:
                        links[item] += weight
                maximum_link_weight = max(
                    maximum_link_weight,
                    max(links.values()),
                )

    assert maximum_pair_multiplicity <= 2
    assert maximum_link_weight <= 2

    anchor = edge(prime, 0, 0)
    disjoint = [
        item
        for item in host
        if all(item[part] != anchor[part] for part in range(4))
    ]
    assert len(disjoint) == (prime - 1) * (prime - 3)

    clean_pairs = 0
    maximum_clean_link = 0
    clean_links: Counter[Edge] = Counter()
    for first, second in combinations(disjoint, 2):
        if is_matching((first, second)):
            clean_pairs += 1
            clean_links[first] += 1
            clean_links[second] += 1
    maximum_clean_link = max(clean_links.values(), default=0)

    assert clean_pairs >= prime**4 // 100
    assert maximum_clean_link <= prime**2

    print(
        f"p={prime}: shapes={len(shapes)}, anchored mass={prime - 1}, "
        f"theta link<={maximum_link_weight}, clean pairs={clean_pairs}"
    )


def main() -> None:
    for prime in (7, 11, 13):
        verify_prime(prime)
    print("PX161 anchored triangle weights verified")


if __name__ == "__main__":
    main()
