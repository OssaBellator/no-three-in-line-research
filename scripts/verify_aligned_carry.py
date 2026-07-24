#!/usr/bin/env python3
"""Finite checks for aligned-anchor carry-cell identities.

For selected channel parameters this checks:
- the exact determinant carry formula;
- the factorisation inside a fixed carry signature;
- the affine interpolation residual identities;
- degenerate signatures are perfectly aligned.

This is a finite sanity check, not a proof for arbitrary p.
"""
from __future__ import annotations

import argparse
from math import isqrt


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


def determinant(
    u: tuple[int, int],
    v: tuple[int, int],
    w: tuple[int, int],
) -> int:
    return (v[0] - u[0]) * (w[1] - u[1]) - (v[1] - u[1]) * (w[0] - u[0])


def check_prime(p: int, all_a: bool) -> None:
    if all_a:
        a_values = list(range(1, p))
    else:
        a_values = sorted({1, 2 % p, p - 1})

    checked = 0
    real_aligned = 0
    degenerate = 0

    for a in a_values:
        if a == 0:
            continue
        for g in range(2, p):
            h = inv(g, p)
            mu = (g * h - 1) // p

            for lam in range(1, p):
                m = lam * h % p
                nu = (g * m - lam) // p
                rho = (h * lam - m) // p
                eta = -mu + nu + rho

                for x in range(1, p):
                    y = a * inv(x, p) % p

                    A = g * x // p
                    D = lam * x // p
                    B = h * y // p
                    C = m * y // p

                    u = (x, h * y % p)
                    v = (g * x % p, y)
                    w = (lam * x % p, m * y % p)

                    alpha = B * (g - lam) + C * (1 - g)
                    beta = A * (h - m) + D * (1 - h)
                    gamma = -A * B + A * C + B * D

                    carry_value = eta * x * y + alpha * x + beta * y + p * gamma
                    det = determinant(u, v, w)
                    assert det == p * carry_value, (
                        p,
                        a,
                        g,
                        lam,
                        x,
                        "determinant formula",
                        det,
                        p * carry_value,
                    )

                    N = alpha * beta - eta * p * gamma
                    if eta != 0:
                        assert (eta * x + beta) * (eta * y + alpha) == (
                            eta * carry_value + N
                        )

                    R_x = (lam - 1) * A - (g - 1) * D
                    R_y = eta * y + (g - lam) * B - (g - 1) * C

                    assert (
                        (g - 1) * w[0]
                        - (g - lam) * u[0]
                        - (lam - 1) * v[0]
                        == p * R_x
                    )
                    assert (
                        (g - 1) * w[1]
                        - (g - lam) * u[1]
                        - (lam - 1) * v[1]
                        == p * R_y
                    )

                    assert (g - 1) * carry_value == (
                        ((g - 1) * x - p * A) * R_y
                        - ((1 - h) * y + p * B) * R_x
                    )

                    if carry_value == 0:
                        real_aligned += 1

                    if eta == alpha == beta == gamma == 0:
                        degenerate += 1
                        assert R_x == 0 and R_y == 0
                        assert det == 0

                    checked += 1

    print(
        f"p={p}: checked {checked} aligned triples; "
        f"real={real_aligned}, degenerate={degenerate}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=17)
    parser.add_argument(
        "--all-a",
        action="store_true",
        help="check every nonzero base channel instead of three representatives",
    )
    args = parser.parse_args()

    if not is_prime(args.prime) or args.prime == 2:
        parser.error("--prime must be an odd prime")

    check_prime(args.prime, args.all_a)


if __name__ == "__main__":
    main()
