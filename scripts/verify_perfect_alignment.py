#!/usr/bin/env python3
"""Finite checks for perfect-alignment parameter arithmetic.

Checks:
- eta=0 parameter classification;
- reduced-denominator wrap-index criterion;
- denominator-sensitive population bound.

This is a finite sanity check, not a proof for arbitrary p.
"""
from __future__ import annotations

import argparse
from math import ceil, gcd, isqrt


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


def check_prime(p: int, all_a: bool) -> None:
    a_values = list(range(1, p)) if all_a else sorted({1, 2 % p, p - 1})
    checked_parameters = 0
    checked_points = 0

    for g in range(2, p):
        h = inv(g, p)
        mu = (g * h - 1) // p
        d = gcd(mu, g - 1)

        actual: set[int] = set()
        for lam in range(1, p):
            m = lam * h % p
            rho = (h * lam - m) // p
            nu = (g * m - lam) // p
            eta = -mu + nu + rho
            assert eta == mu * (lam - 1) - (g - 1) * rho
            if eta == 0:
                actual.add(lam)

        expected = {
            1 + t * ((g - 1) // d)
            for t in range(d + 1)
        }
        assert actual == expected, (p, g, actual, expected)

        for t in range(1, d):
            lam = 1 + t * ((g - 1) // d)
            m = lam * h % p
            e = gcd(t, d)
            q = d // e
            checked_parameters += 1

            for a in a_values:
                population = 0
                for x in range(1, p):
                    y = a * inv(x, p) % p
                    A = g * x // p
                    B = h * y // p
                    D = lam * x // p
                    C = m * y // p

                    rho = (h * lam - m) // p
                    nu = (g * m - lam) // p
                    eta = -mu + nu + rho

                    R_x = (lam - 1) * A - (g - 1) * D
                    R_y = eta * y + (g - lam) * B - (g - 1) * C
                    aligned = R_x == 0 and R_y == 0
                    striped = A % q == 0 and B % q == 0
                    assert aligned == striped, (
                        p,
                        a,
                        g,
                        lam,
                        x,
                        q,
                        A,
                        B,
                        R_x,
                        R_y,
                    )
                    population += int(aligned)
                    checked_points += 1

                bound = min(
                    ceil(g / q) * ceil(p / g),
                    ceil(h / q) * ceil(p / h),
                )
                assert population <= bound, (
                    p,
                    a,
                    g,
                    lam,
                    q,
                    population,
                    bound,
                )
                assert population <= 4 * p / q

    print(
        f"p={p}: checked {checked_parameters} interior parameters "
        f"and {checked_points} base points"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=17)
    parser.add_argument("--all-a", action="store_true")
    args = parser.parse_args()

    if not is_prime(args.prime) or args.prime == 2:
        parser.error("--prime must be an odd prime")

    check_prime(args.prime, args.all_a)


if __name__ == "__main__":
    main()
