#!/usr/bin/env python3
"""Finite checks for the incidence geometry of the hyperbola pencil.

For every ratio r != 1 and every opposite-channel anchor z, this checks:
- the projective secant map is an involution on P^1(F_p);
- the two affine exceptions are paired with the points at infinity;
- the tangent count is 1 + chi(1-r);
- the affine secant-pair count is (p - 4 - chi(1-r)) / 2.

This is a finite sanity check, not a proof for arbitrary p.
"""
from __future__ import annotations

import argparse
from math import isqrt

ProjectiveParameter = int | None
INFINITY: ProjectiveParameter = None


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def inv(x: int, p: int) -> int:
    if x % p == 0:
        raise ZeroDivisionError("zero has no inverse modulo p")
    return pow(x, p - 2, p)


def quadratic_character(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def secant_involution(
    x: ProjectiveParameter,
    z: int,
    ratio: int,
    p: int,
) -> ProjectiveParameter:
    """Apply T_z(x) = z(x-z)/(ratio*x-z) on P^1(F_p)."""
    if x is INFINITY:
        return z * inv(ratio, p) % p

    numerator = z * (x - z) % p
    denominator = ratio * x - z
    if denominator % p == 0:
        return INFINITY
    return numerator * inv(denominator, p) % p


def conic_point(x: ProjectiveParameter, p: int) -> tuple[int, int, int]:
    """Parameterise XY=Z^2 by P^1(F_p)."""
    if x is INFINITY:
        return (1, 0, 0)
    if x == 0:
        return (0, 1, 0)
    return (x, inv(x, p), 1)


def determinant3(
    a: tuple[int, int, int],
    b: tuple[int, int, int],
    c: tuple[int, int, int],
    p: int,
) -> int:
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    ) % p


def check_prime(p: int) -> None:
    parameters: list[ProjectiveParameter] = list(range(p)) + [INFINITY]

    for ratio in range(2, p):
        character = quadratic_character(1 - ratio, p)
        expected_fixed = 1 + character
        expected_secants = (p - 4 - character) // 2

        for z in range(1, p):
            image = {
                x: secant_involution(x, z, ratio, p)
                for x in parameters
            }
            anchor = (z, ratio * inv(z, p) % p, 1)
            assert all(
                determinant3(
                    anchor,
                    conic_point(x, p),
                    conic_point(image[x], p),
                    p,
                ) == 0
                for x in parameters
            ), (p, ratio, z, "secant formula is not collinear")
            assert set(image.values()) == set(parameters), (p, ratio, z, "not bijective")
            assert all(image[image[x]] == x for x in parameters), (
                p,
                ratio,
                z,
                "not involutive",
            )

            horizontal_parameter = z * inv(ratio, p) % p
            assert image[0] == z and image[z] == 0
            assert image[INFINITY] == horizontal_parameter
            assert image[horizontal_parameter] is INFINITY

            affine = set(range(1, p))
            exceptional = {z, horizontal_parameter}
            fixed = {x for x in affine if image[x] == x}
            assert len(fixed) == expected_fixed, (
                p,
                ratio,
                z,
                len(fixed),
                expected_fixed,
            )
            assert fixed.isdisjoint(exceptional)

            remaining = affine - exceptional - fixed
            seen: set[int] = set()
            secant_pairs = 0
            for x in remaining:
                if x in seen:
                    continue
                y = image[x]
                assert isinstance(y, int) and y in remaining and y != x
                assert image[y] == x
                seen.add(x)
                seen.add(y)
                secant_pairs += 1

            assert seen == remaining
            assert secant_pairs == expected_secants, (
                p,
                ratio,
                z,
                secant_pairs,
                expected_secants,
            )

    print(f"p={p}: all conic-incidence checks passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=17)
    args = parser.parse_args()

    if not is_prime(args.prime) or args.prime == 2:
        parser.error("--prime must be an odd prime")
    check_prime(args.prime)


if __name__ == "__main__":
    main()
