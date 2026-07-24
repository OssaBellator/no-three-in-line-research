#!/usr/bin/env python3
"""Verify BDA3h prime-power valuation-pivot classification."""

from __future__ import annotations

from math import gcd


def truncated_valuation(value: int, prime: int, exponent: int) -> int:
    modulus = prime**exponent
    if value % modulus == 0:
        return exponent
    valuation = 0
    while value % prime == 0:
        value //= prime
        valuation += 1
    return valuation


def verify() -> None:
    for prime in (2, 3, 5):
        for exponent in range(1, 4):
            prime_power = prime**exponent
            for a in range(1, 8):
                for b in range(-7, 8):
                    if b == 0 or gcd(a, abs(b)) != 1:
                        continue
                    for m in range(-18, 19):
                        for n in range(-18, 19):
                            if m == 0 or n == 0 or m == n:
                                continue
                            matrix = (
                                (a * m, a * n),
                                (b * m, b * n),
                            )
                            kappa = min(
                                exponent,
                                truncated_valuation(m, prime, exponent),
                                truncated_valuation(n, prime, exponent),
                            )
                            entry_kappa = min(
                                truncated_valuation(
                                    entry,
                                    prime,
                                    exponent,
                                )
                                for row in matrix
                                for entry in row
                            )
                            assert entry_kappa == kappa

                            residues = tuple(
                                tuple(entry % prime_power for entry in row)
                                for row in matrix
                            )
                            if kappa == exponent:
                                assert all(
                                    entry == 0
                                    for row in residues
                                    for entry in row
                                )
                                assert m % prime_power == 0
                                assert n % prime_power == 0
                                continue

                            divisor = prime**kappa
                            modulus = prime ** (exponent - kappa)
                            normalized = tuple(
                                tuple((entry // divisor) % modulus for entry in row)
                                for row in matrix
                            )
                            unit_pivots = [
                                (row, column)
                                for row in range(2)
                                for column in range(2)
                                if normalized[row][column] % prime != 0
                            ]
                            assert unit_pivots

                            direction = (a, b)
                            scales = (m // divisor, n // divisor)
                            for row, column in unit_pivots:
                                pivot_inverse = pow(
                                    normalized[row][column],
                                    -1,
                                    modulus,
                                )
                                other_row = 1 - row
                                other_column = 1 - column
                                recovered_direction_ratio = (
                                    normalized[other_row][column]
                                    * pivot_inverse
                                ) % modulus
                                recovered_scale_ratio = (
                                    normalized[row][other_column]
                                    * pivot_inverse
                                ) % modulus
                                assert direction[row] % prime != 0
                                assert scales[column] % prime != 0
                                assert recovered_direction_ratio == (
                                    direction[other_row]
                                    * pow(direction[row], -1, modulus)
                                ) % modulus
                                assert recovered_scale_ratio == (
                                    scales[other_column]
                                    * pow(scales[column], -1, modulus)
                                ) % modulus


def main() -> None:
    verify()
    print("BDA valuation-pivot charts: verified")


if __name__ == "__main__":
    main()
