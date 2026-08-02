#!/usr/bin/env python3
"""Verify PX179--PX180 direction omission versus triangle spread."""
from __future__ import annotations

from collections import Counter

Permutation = tuple[int, ...]

EXPECTED_ORDER_13 = Counter(
    {
        (3, 8): 2028,
        (5, 24): 1352,
        (3, 48): 1014,
        (12, 156): 130,
    }
)

SEED_17: Permutation = (
    0, 12, 7, 5, 14, 2, 9, 16, 6,
    13, 1, 10, 8, 3, 15, 4, 11,
)
EXPECTED_OMITTED_17 = (0, 1, 2, 3, 8, 11, 16)


def strong_complete_mappings(prime: int) -> tuple[Permutation, ...]:
    mapping = [-1] * prime
    result: list[Permutation] = []

    def search(row: int, used_images: int, used_minus: int, used_plus: int) -> None:
        if row == prime:
            result.append(tuple(mapping))
            return
        for image in range(prime):
            image_bit = 1 << image
            minus = (row - image) % prime
            plus = (row + image) % prime
            if (
                used_images & image_bit
                or used_minus & (1 << minus)
                or used_plus & (1 << plus)
            ):
                continue
            mapping[row] = image
            search(
                row + 1,
                used_images | image_bit,
                used_minus | (1 << minus),
                used_plus | (1 << plus),
            )

    search(0, 0, 0, 0)
    return tuple(result)


def is_strong(mapping: Permutation) -> bool:
    prime = len(mapping)
    target = list(range(prime))
    return (
        sorted(mapping) == target
        and sorted((x - mapping[x]) % prime for x in range(prime)) == target
        and sorted((x + mapping[x]) % prime for x in range(prime)) == target
    )


def slope_counts(mapping: Permutation) -> Counter[int]:
    prime = len(mapping)
    inverse = [0] + [pow(value, -1, prime) for value in range(1, prime)]
    counts: Counter[int] = Counter()
    for first in range(prime):
        for second in range(prime):
            if first == second:
                continue
            slope = (
                (mapping[second] - mapping[first])
                * inverse[(second - first) % prime]
                % prime
            )
            counts[slope] += 1
    return counts


def omitted_slopes(mapping: Permutation) -> tuple[int, ...]:
    counts = slope_counts(mapping)
    return tuple(slope for slope in range(len(mapping)) if counts[slope] == 0)


def triangle_multiplicity(mapping: Permutation) -> int:
    prime = len(mapping)
    inverse = [0] + [pow(value, -1, prime) for value in range(1, prime)]
    counts: Counter[tuple[int, int, int]] = Counter()
    for first in range(prime):
        for second in range(prime):
            if first == second:
                continue
            row_difference = (second - first) % prime
            image_difference = (mapping[second] - mapping[first]) % prime
            slope = image_difference * inverse[row_difference] % prime
            for row_ratio in range(2, prime):
                third = (first + row_ratio * row_difference) % prime
                image_ratio = (
                    (mapping[third] - mapping[first])
                    * inverse[image_difference]
                    % prime
                )
                counts[(slope, row_ratio, image_ratio)] += 1
    return max(counts.values())


def affine_parameters(mapping: Permutation) -> tuple[int, int] | None:
    prime = len(mapping)
    intercept = mapping[0]
    slope = (mapping[1] - intercept) % prime
    if all(mapping[x] == (slope * x + intercept) % prime for x in range(prime)):
        return slope, intercept
    return None


def verify_order_thirteen() -> None:
    mappings = strong_complete_mappings(13)
    assert len(mappings) == 4524
    census: Counter[tuple[int, int]] = Counter()
    extra_direction_extremals = 0
    for mapping in mappings:
        omitted = omitted_slopes(mapping)
        triangle = triangle_multiplicity(mapping)
        census[(len(omitted), triangle)] += 1
        if affine_parameters(mapping) is None and len(omitted) > 3:
            # p-len(omitted) is the number of finite directions determined by
            # the graph. Equality with (p+3)/2 is the Redei lower bound.
            assert 13 - len(omitted) == (13 + 3) // 2
            extra_direction_extremals += 1
    assert census == EXPECTED_ORDER_13
    assert extra_direction_extremals == 1352
    print(f"p=13 census: {dict(census)}")


def verify_order_seventeen() -> None:
    assert is_strong(SEED_17)
    omitted = omitted_slopes(SEED_17)
    triangle = triangle_multiplicity(SEED_17)
    assert omitted == EXPECTED_OMITTED_17
    assert triangle == 40
    assert affine_parameters(SEED_17) is None
    assert 17 - len(omitted) == (17 + 3) // 2
    print(f"p=17: omitted={omitted}, tau={triangle}")


def main() -> None:
    verify_order_thirteen()
    verify_order_seventeen()
    print("PX179--PX180 verified")


if __name__ == "__main__":
    main()
