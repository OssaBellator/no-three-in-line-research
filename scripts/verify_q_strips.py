#!/usr/bin/env python3
"""Exhaustively verify the arithmetic identities used in BDA1."""

from __future__ import annotations

from math import gcd


def primes_through(limit: int) -> list[int]:
    return [
        n
        for n in range(3, limit + 1, 2)
        if all(n % d for d in range(2, int(n**0.5) + 1))
    ]


def rep(value: int, p: int) -> int:
    value %= p
    assert value
    return value


def carry_interval(p: int, multiplier: int, carry: int) -> set[int]:
    """Return the exact integer interval with the prescribed carry."""
    lower = (carry * p + multiplier - 1) // multiplier
    upper = ((carry + 1) * p + multiplier - 1) // multiplier - 1
    return set(range(max(1, lower), min(p - 1, upper) + 1))


def verify_strip_partition(p: int, multiplier: int, q: int) -> None:
    classes: list[set[int]] = []
    for residue in range(q):
        by_intervals: set[int] = set()
        for carry in range(multiplier):
            if carry % q == residue:
                by_intervals |= carry_interval(p, multiplier, carry)
        directly = {
            z
            for z in range(1, p)
            if (multiplier * z // p) % q == residue
        }
        assert by_intervals == directly
        classes.append(directly)

    assert set().union(*classes) == set(range(1, p))
    assert sum(map(len, classes)) == p - 1


def verify_interpolation(p: int, g: int, t: int, d: int) -> None:
    h = pow(g, -1, p)
    q = d // gcd(t, d)
    lam = 1 + t * (g - 1) // d
    m = h - t * (h - 1) // d

    for x in range(1, p):
        target = rep(g * x, p)
        carry = g * x // p
        numerator = d * x + t * (target - x)
        integral = numerator % d == 0
        assert integral == (carry % q == 0)
        if integral:
            assert numerator // d == rep(lam * x, p)

    for y in range(1, p):
        target = rep(h * y, p)
        carry = h * y // p
        numerator = d * target + t * (y - target)
        integral = numerator % d == 0
        assert integral == (carry % q == 0)
        if integral:
            assert numerator // d == rep(m * y, p)


def verify(limit: int = 43) -> None:
    for p in primes_through(limit):
        for multiplier in range(1, p):
            for q in range(2, min(8, p)):
                verify_strip_partition(p, multiplier, q)

        for g in range(2, p):
            h = pow(g, -1, p)
            mu = (g * h - 1) // p
            d = gcd(mu, g - 1)
            assert (h - 1) % d == 0
            for t in range(1, d):
                verify_interpolation(p, g, t, d)


def main() -> None:
    verify()
    print("BDA1 q-strip decomposition: verified through p=43")


if __name__ == "__main__":
    main()
