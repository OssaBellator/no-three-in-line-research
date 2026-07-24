#!/usr/bin/env python3
"""Verify CMR47--CMR49 by exact enumeration."""
from __future__ import annotations

import argparse
from math import gcd


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def root_count(modulus: int, value: int) -> int:
    value %= modulus
    return sum(1 for z in range(modulus) if (z * z - value) % modulus == 0)


def legendre_square(value: int, p: int) -> bool:
    return pow(value % p, (p - 1) // 2, p) == 1


def verify_instance(p: int, m: int, R: int, S: int, c: int) -> int:
    modulus = p**m
    assert gcd(R * S * c, p) == 1
    inverse_s = pow(S, -1, modulus)
    constant = (-4 * c * R * inverse_s) % modulus

    all_sum = 0
    unit_sum = 0
    checks = 0
    for scalar in range(modulus):
        discriminant = (scalar * scalar * R * R + constant) % modulus
        count = root_count(modulus, discriminant)
        all_sum += count
        if scalar % p:
            unit_sum += count
        checks += 1

    phi = modulus - modulus // p
    assert all_sum == phi
    expected_units = (
        phi - 2 * p ** (m - 1)
        if legendre_square(constant, p)
        else phi
    )
    assert unit_sum == expected_units
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-prime", type=int, default=11)
    parser.add_argument("--max-exponent", type=int, default=3)
    args = parser.parse_args()

    checks = 0
    instances = 0
    for p in range(3, args.max_prime + 1, 2):
        if not is_prime(p):
            continue
        for m in range(1, args.max_exponent + 1):
            modulus = p**m
            units = [value for value in range(1, min(modulus, 8)) if value % p]
            for R in units:
                for S in units:
                    for c in units:
                        checks += verify_instance(p, m, R, S, c)
                        instances += 1

    print(
        f"verified average-root instances={instances}; scalar-residues={checks}"
    )


if __name__ == "__main__":
    main()
