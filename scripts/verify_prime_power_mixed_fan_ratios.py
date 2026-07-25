#!/usr/bin/env python3
"""Exact checks for CMR306--CMR309."""

from __future__ import annotations

from collections import Counter
from math import ceil, gcd


def determinant(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> int:
    x1, y1 = first
    x2, y2 = second
    x3, y3 = third
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def verify_exact_factorization(max_t: int = 9) -> None:
    for t in range(4, max_t + 1):
        for x1 in range(t):
            for x2 in range(x1 + 1, t):
                d = x2 - x1
                for y3 in range(t):
                    for a in range(t):
                        for b in range(t):
                            if a == b:
                                continue
                            for c in range(t):
                                s = c - x1
                                alpha = y3 - a
                                beta = b - y3
                                exact = determinant(
                                    (x1, a), (x2, b), (c, y3)
                                ) == 0
                                factor = (d - s) * alpha == s * beta
                                assert exact == factor

                                if exact and s not in (0, d):
                                    common = gcd(abs(s), abs(d - s))
                                    primitive_left = s // common
                                    primitive_right = (d - s) // common
                                    assert gcd(
                                        abs(primitive_left), abs(primitive_right)
                                    ) == 1
                                    assert alpha % primitive_left == 0
                                    parameter = alpha // primitive_left
                                    assert beta == parameter * primitive_right
                                    assert parameter != 0

                                if exact and s == 0:
                                    assert a == y3
                                if exact and s == d:
                                    assert b == y3


def check_ratio_census(p: int, t: int, x1: int, x2: int) -> None:
    assert 0 <= x1 < x2 < t
    d = x2 - x1
    ratios: Counter[int] = Counter()
    good = 0
    for c in range(t):
        s = c - x1
        if s in (0, d):
            continue
        if s % p == 0 or (d - s) % p == 0:
            continue
        rho = (s % p) * pow((d - s) % p, -1, p) % p
        assert rho != 0
        ratios[rho] += 1
        good += 1
        if d % p != 0:
            assert rho != p - 1
            recovered = rho * (d % p) * pow(1 + rho, -1, p) % p
            assert recovered == s % p

    assert good >= t - 2 - 2 * (t // p)
    if ratios:
        assert max(ratios.values()) >= ceil(good / (p - 1))


def verify_unit_ratio_counts() -> None:
    # Exhaustive slice pairs on the small prime-power boards.
    for p, h in ((3, 3), (5, 2), (7, 2)):
        t = p**h
        for x1 in range(t):
            for x2 in range(x1 + 1, t):
                check_ratio_census(p, t, x1, x2)

    # Representative unit, singular, central, and long gaps on larger boards.
    for p, h in ((3, 5), (5, 4), (7, 3), (11, 3)):
        t = p**h
        pairs = {
            (0, 1),
            (0, p),
            (0, t - 1),
            (t // 3, min(t - 1, t // 3 + p)),
            (max(0, t // 2 - 1), min(t - 1, t // 2 + 1)),
        }
        for x1, x2 in pairs:
            if x1 < x2:
                check_ratio_census(p, t, x1, x2)


def verify_recycled_bound() -> None:
    for p, h in ((5, 2), (5, 3), (7, 2), (7, 3), (11, 2)):
        t = p**h
        numerator = max(0, t - 3 - 2 * (t // p))
        bound = ceil(numerator / (p - 1))
        assert bound >= 0
        assert bound * (p - 1) >= numerator


def main() -> None:
    verify_exact_factorization()
    verify_unit_ratio_counts()
    verify_recycled_bound()
    print(
        "verified mixed-fan ratios: determinant factorization, primitive "
        "parameters, degeneracies, and linear unit-ratio extraction"
    )


if __name__ == "__main__":
    main()
