#!/usr/bin/env python3
"""Verify BDA3k/BDA4c projective lift separation and radial chains."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import ceil, gcd


Vector = tuple[int, int]


def units(modulus: int) -> tuple[int, ...]:
    return tuple(
        value for value in range(modulus) if gcd(value, modulus) == 1
    )


def projective_class(vector: Vector, modulus: int) -> Vector:
    return min(
        (
            unit * vector[0] % modulus,
            unit * vector[1] % modulus,
        )
        for unit in units(modulus)
    )


def normalized_vectors(bound: int) -> tuple[Vector, ...]:
    return tuple(
        (first, second)
        for first in range(1, bound + 1)
        for second in range(-bound, bound + 1)
        if second != 0 and gcd(first, abs(second)) == 1
    )


def signed_primitive_vectors(bound: int) -> tuple[Vector, ...]:
    return tuple(
        (first, second)
        for first in range(-bound, bound + 1)
        for second in range(-bound, bound + 1)
        if first != 0
        and second != 0
        and gcd(abs(first), abs(second)) == 1
    )


def orient(vector: Vector) -> Vector:
    sign = 1 if vector[0] > 0 else -1
    return sign * vector[0], sign * vector[1]


def outer_product(
    scalar: int,
    direction: Vector,
    scale: Vector,
    modulus: int,
) -> tuple[int, int, int, int]:
    return (
        scalar * direction[0] * scale[0] % modulus,
        scalar * direction[0] * scale[1] % modulus,
        scalar * direction[1] * scale[0] % modulus,
        scalar * direction[1] * scale[1] % modulus,
    )


def verify_separation(maximum_q: int = 12, bound: int = 8) -> None:
    vectors = normalized_vectors(bound)
    for modulus in range(2, maximum_q + 1):
        classes: dict[Vector, list[Vector]] = {}
        for vector in vectors:
            key = projective_class(vector, modulus)
            classes.setdefault(key, []).append(vector)

        for members in classes.values():
            ordered = sorted(members, key=lambda vector: Fraction(
                vector[1],
                vector[0],
            ))
            for first, second in combinations(ordered, 2):
                determinant = (
                    first[0] * second[1]
                    - first[1] * second[0]
                )
                assert determinant % modulus == 0
                assert abs(determinant) >= modulus
                gap = abs(
                    Fraction(first[1], first[0])
                    - Fraction(second[1], second[0])
                )
                assert gap == Fraction(
                    abs(determinant),
                    first[0] * second[0],
                )
                assert gap >= Fraction(modulus, bound**2)

            for left in range(len(ordered)):
                for right in range(left, len(ordered)):
                    window = ordered[left:right + 1]
                    width = (
                        Fraction(window[-1][1], window[-1][0])
                        - Fraction(window[0][1], window[0][0])
                    )
                    packing_bound = width * bound**2 // modulus + 1
                    assert len(window) <= packing_bound


def verify_orientation(maximum_q: int = 12, bound: int = 7) -> None:
    for vector in signed_primitive_vectors(bound):
        oriented = orient(vector)
        assert oriented[0] > 0
        assert max(map(abs, oriented)) == max(map(abs, vector))
        assert Fraction(oriented[1], oriented[0]) == Fraction(
            vector[1],
            vector[0],
        )
        for modulus in range(2, maximum_q + 1):
            assert projective_class(oriented, modulus) == (
                projective_class(vector, modulus)
            )


def verify_scalar_faithfulness(
    maximum_q: int = 12,
    bound: int = 3,
) -> None:
    vectors = signed_primitive_vectors(bound)
    for modulus in range(2, maximum_q + 1):
        for direction in vectors:
            for scale in vectors:
                matrices = {
                    outer_product(
                        scalar,
                        direction,
                        scale,
                        modulus,
                    )
                    for scalar in range(modulus)
                }
                assert len(matrices) == modulus


def verify_radial_spacing(maximum_q: int = 20, maximum_h: int = 80) -> None:
    for modulus in range(2, maximum_q + 1):
        for height in range(1, maximum_h + 1):
            for residue in range(modulus):
                members = [
                    value
                    for value in range(1, height + 1)
                    if value % modulus == residue
                ]
                assert len(members) <= ceil(height / modulus)
                assert all(
                    second - first >= modulus
                    for first, second in zip(members, members[1:])
                )


def main() -> None:
    verify_separation()
    verify_orientation()
    verify_scalar_faithfulness()
    verify_radial_spacing()
    print("BDA projective lift separation: verified")


if __name__ == "__main__":
    main()
