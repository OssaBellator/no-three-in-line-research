#!/usr/bin/env python3
"""Verify PX176 protected-slope rigidity on small prime fields."""
from __future__ import annotations

from math import gcd


def protected_slopes(prime: int, height: int) -> set[int]:
    slopes: set[int] = set()
    for a in range(1, height + 1):
        for b in range(1, height + 1):
            if gcd(a, b) != 1:
                continue
            slope = b * pow(a, -1, prime) % prime
            slopes.add(slope)
            slopes.add((-slope) % prime)
    return slopes


def is_affine(mapping: tuple[int, ...]) -> bool:
    prime = len(mapping)
    slope = (mapping[1] - mapping[0]) % prime
    intercept = mapping[0]
    return all(
        mapping[x] == (slope * x + intercept) % prime
        for x in range(prime)
    )


def determined_slopes(mapping: tuple[int, ...]) -> set[int]:
    prime = len(mapping)
    slopes = set()
    for first in range(prime):
        for second in range(first + 1, prime):
            slopes.add(
                (mapping[second] - mapping[first])
                * pow(second - first, -1, prime)
                % prime
            )
    return slopes


def enumerate_avoiding(prime: int, forbidden: set[int]) -> list[tuple[int, ...]]:
    mapping = [-1] * prime
    used_images = 0
    result: list[tuple[int, ...]] = []

    def search(row: int, used: int) -> None:
        if row == prime:
            result.append(tuple(mapping))
            return
        for image in range(prime):
            if used & (1 << image):
                continue
            valid = True
            for previous in range(row):
                slope = (
                    (image - mapping[previous])
                    * pow(row - previous, -1, prime)
                    % prime
                )
                if slope in forbidden:
                    valid = False
                    break
            if not valid:
                continue
            mapping[row] = image
            search(row + 1, used | (1 << image))

    search(0, used_images)
    return result


def verify_prime(prime: int, height: int) -> None:
    forbidden = protected_slopes(prime, height)
    mappings = enumerate_avoiding(prime, forbidden)
    allowed_affine_slopes = set(range(1, prime)) - forbidden
    assert len(mappings) == prime * len(allowed_affine_slopes)
    assert all(is_affine(mapping) for mapping in mappings)
    assert all(determined_slopes(mapping).isdisjoint(forbidden) for mapping in mappings)
    assert len(forbidden) > (prime - 5) // 2
    print(
        f"p={prime}, H={height}: protected={len(forbidden)}, "
        f"solutions={len(mappings)}, all affine"
    )


def main() -> None:
    verify_prime(5, 1)
    verify_prime(7, 2)
    verify_prime(11, 2)
    print("PX176 finite protected-slope rigidity verified")


if __name__ == "__main__":
    main()
