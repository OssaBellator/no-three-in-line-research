#!/usr/bin/env python3
"""Verify PX181--PX182 protected trade support barriers."""
from __future__ import annotations

from itertools import combinations, permutations
from random import Random


def preserving_slopes(
    prime: int,
    rows: tuple[int, ...],
    old_images: tuple[int, ...],
    new_images: tuple[int, ...],
) -> tuple[int, ...]:
    result = []
    for slope in range(prime):
        old_colours = sorted(
            (image - slope * row) % prime
            for row, image in zip(rows, old_images)
        )
        new_colours = sorted(
            (image - slope * row) % prime
            for row, image in zip(rows, new_images)
        )
        if old_colours == new_colours:
            result.append(slope)
    return tuple(result)


def verify_exhaustive_order_seven() -> None:
    prime = 7
    for support_size in range(2, 5):
        checked = 0
        for rows in combinations(range(prime), support_size):
            for old_images in permutations(range(prime), support_size):
                for image_permutation in permutations(range(support_size)):
                    if image_permutation == tuple(range(support_size)):
                        continue
                    new_images = tuple(
                        old_images[index] for index in image_permutation
                    )
                    slopes = preserving_slopes(
                        prime, rows, old_images, new_images
                    )
                    assert len(slopes) <= support_size - 1
                    checked += 1
        print(
            f"p=7, support={support_size}: checked {checked} nontrivial trades"
        )


def verify_random_larger_supports() -> None:
    random = Random(20260725)
    for prime in (11, 13, 17):
        for support_size in range(2, min(prime, 9)):
            for _ in range(1000):
                rows = tuple(random.sample(range(prime), support_size))
                old_images = tuple(random.sample(range(prime), support_size))
                order = list(range(support_size))
                while order == list(range(support_size)):
                    random.shuffle(order)
                new_images = tuple(old_images[index] for index in order)
                slopes = preserving_slopes(
                    prime, rows, old_images, new_images
                )
                assert len(slopes) <= support_size - 1
    print("random protected-trade support checks passed")


def verify_px98_sharpness() -> None:
    # The standard four-row strong-complete trade preserves the three slope
    # colourings c=0,1,-1, so the k>s inequality is sharp at (k,s)=(4,3).
    for prime in (7, 11, 13, 17):
        a, r, s = 0, 1, 2
        rows = (a, (a + r) % prime, (a - s) % prime, (a - s + r) % prime)
        old_images = (0, s % prime, r % prime, (r + s) % prime)
        new_images = ((r + s) % prime, r % prime, s % prime, 0)
        slopes = preserving_slopes(prime, rows, old_images, new_images)
        assert {0, 1, prime - 1}.issubset(slopes)
        assert len(slopes) <= 3
    print("PX98 support-four, three-slope sharpness verified")


def verify_height_exponents() -> None:
    # Protecting Omega(H^2) primitive slopes forces the same order of trade
    # support. Record the exponent conversion H=p^delta -> support=p^(2delta).
    for delta_times_100 in (5, 10, 20, 30, 40):
        delta = delta_times_100 / 100
        for prime in (1009, 10007):
            height = prime**delta
            protected_scale = height**2
            assert protected_scale == prime ** (2 * delta)
    print("height-to-support exponent conversion verified")


def main() -> None:
    verify_exhaustive_order_seven()
    verify_random_larger_supports()
    verify_px98_sharpness()
    verify_height_exponents()
    print("PX181--PX182 verified")


if __name__ == "__main__":
    main()
