#!/usr/bin/env python3
"""Verify BDA3k/BDA4c--BDA4d projective lift and radial structure."""

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


def integer_outer_product(
    scalar: int,
    direction: Vector,
    scale: Vector,
) -> tuple[int, int, int, int]:
    return (
        scalar * direction[0] * scale[0],
        scalar * direction[0] * scale[1],
        scalar * direction[1] * scale[0],
        scalar * direction[1] * scale[1],
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


def verify_radial_density(
    maximum_q: int = 8,
    maximum_h: int = 24,
) -> None:
    direction = (2, -1)
    scale = (-1, 3)
    for modulus in range(2, maximum_q + 1):
        increment = integer_outer_product(
            modulus,
            direction,
            scale,
        )
        for height in range(1, maximum_h + 1):
            for residue in range(modulus):
                available = tuple(
                    value
                    for value in range(1, height + 1)
                    if value % modulus == residue
                )
                slot_count = len(available)
                for mask in range(1 << slot_count):
                    occupied = {
                        value
                        for index, value in enumerate(available)
                        if mask & (1 << index)
                    }
                    count = len(occupied)
                    if count:
                        assert max(occupied) >= (
                            1 + modulus * (count - 1)
                        )

                    adjacent = {
                        value
                        for value in occupied
                        if value + modulus in occupied
                    }
                    lower_bound = max(
                        0,
                        2 * count - slot_count - 1,
                    )
                    assert len(adjacent) >= lower_bound

                    unused = set(occupied)
                    matching = 0
                    for value in available:
                        if (
                            value in unused
                            and value + modulus in unused
                        ):
                            unused.remove(value)
                            unused.remove(value + modulus)
                            matching += 1
                            first = integer_outer_product(
                                value,
                                direction,
                                scale,
                            )
                            second = integer_outer_product(
                                value + modulus,
                                direction,
                                scale,
                            )
                            assert tuple(
                                right - left
                                for left, right in zip(first, second)
                            ) == increment
                    assert matching >= ceil(lower_bound / 2)


def verify_linear_density_shape(
    maximum_q: int = 8,
    maximum_n: int = 80,
    maximum_norm: int = 8,
) -> None:
    densities = (
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(1, 4),
        Fraction(1, 5),
    )
    for modulus in range(2, maximum_q + 1):
        for norm_a in range(1, maximum_norm + 1):
            for norm_b in range(1, maximum_norm + 1):
                shape = norm_a * norm_b
                for box_height in range(1, maximum_n + 1):
                    radial_height = box_height // shape
                    for residue in range(modulus):
                        chain_length = sum(
                            value % modulus == residue
                            for value in range(1, radial_height + 1)
                        )
                        for density in densities:
                            if (
                                box_height * density.numerator
                                < 2 * density.denominator
                            ):
                                continue
                            if (
                                chain_length * density.denominator
                                < box_height * density.numerator
                            ):
                                continue
                            assert Fraction(shape) <= (
                                Fraction(2, modulus) / density
                            )


def verify_factor_library(maximum_norm: int = 8) -> None:
    for norm_bound in range(1, maximum_norm + 1):
        directions = normalized_vectors(norm_bound)
        scales = signed_primitive_vectors(norm_bound)
        pairs = {
            (direction, scale)
            for direction in directions
            for scale in scales
            if (
                max(map(abs, direction))
                * max(map(abs, scale))
                <= norm_bound
            )
        }
        assert len(pairs) <= 8 * norm_bound**4


def main() -> None:
    verify_separation()
    verify_orientation()
    verify_scalar_faithfulness()
    verify_radial_spacing()
    verify_radial_density()
    verify_linear_density_shape()
    verify_factor_library()
    print("BDA projective lift separation: verified")


if __name__ == "__main__":
    main()
