#!/usr/bin/env python3
"""Exhaust BDA5w--BDA5x on small primitive direction pairs."""

from itertools import product
from math import gcd


def primitive_vectors(bound):
    return [
        (x, y)
        for x in range(1, bound + 1)
        for y in range(-bound, bound + 1)
        if y != 0 and gcd(x, abs(y)) == 1
    ]


def complement(vector):
    a, b = vector
    for c in range(-abs(a) - abs(b) - 1, abs(a) + abs(b) + 2):
        for d in range(-abs(a) - abs(b) - 1, abs(a) + abs(b) + 2):
            if a * d - b * c == 1:
                return c, d
    raise AssertionError("missing unimodular complement")


def verify(bound=7, maximum_q=12):
    vectors = primitive_vectors(bound)
    decomposition_checks = 0
    congruence_checks = 0
    dense_checks = 0

    for radial, context in product(vectors, repeat=2):
        a, b = radial
        r, s = context
        determinant = a * s - b * r
        if determinant == 0:
            continue

        c, d = complement(radial)
        alpha = r * d - s * c
        assert (
            alpha * a + determinant * c,
            alpha * b + determinant * d,
        ) == context
        decomposition_checks += 1

        norm_radial = max(abs(a), abs(b))
        norm_context = max(abs(r), abs(s))

        for q in range(2, maximum_q + 1):
            common = gcd(abs(determinant), q)
            residual = determinant // common
            modulus = q // common

            assert gcd(abs(residual), modulus) == 1
            assert gcd(alpha, common) == 1
            assert abs(residual) * common <= 2 * norm_radial * norm_context

            for residue in range(q):
                original = [
                    h
                    for h in range(0, 3 * q + 1)
                    if (h * determinant - residue) % q == 0
                ]
                if residue % common:
                    assert not original
                    continue
                reduced_residue = residue // common
                reduced = [
                    h
                    for h in range(0, 3 * q + 1)
                    if (h * residual - reduced_residue) % modulus == 0
                ]
                assert original == reduced
                congruence_checks += 1

            for numerator, denominator in ((1, 4), (1, 3), (1, 2)):
                density = numerator / denominator
                # Test the theorem at the extremal lower bound on g.
                if common + 1e-12 >= density * q / 2:
                    assert abs(residual) <= (
                        4 * norm_radial * norm_context / (density * q)
                        + 1e-12
                    )
                    increment = q * residual
                    assert increment == (q // common) * determinant
                    dense_checks += 1

    return decomposition_checks, congruence_checks, dense_checks


def main():
    decompositions, congruences, dense = verify()
    print(
        "BDA residual determinant: verified "
        f"{decompositions} decompositions, {congruences} congruences, "
        f"and {dense} dense bounds"
    )


if __name__ == "__main__":
    main()
