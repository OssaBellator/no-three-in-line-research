#!/usr/bin/env python3
"""Finite checks for OP4p--OP4s."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def inv(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def primitive_root(p: int) -> int:
    factors: set[int] = set()
    n = p - 1
    d = 2
    m = n
    while d * d <= m:
        if m % d == 0:
            factors.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        factors.add(m)
    for g in range(2, p):
        if all(pow(g, n // q, p) != 1 for q in factors):
            return g
    raise AssertionError("no primitive root")


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def coset_index(x: int, p: int, h: int, gamma: int) -> int:
    k = (p - 1) // h
    cur = 1
    logs: dict[int, int] = {}
    for j in range(p - 1):
        logs[cur] = j
        cur = cur * gamma % p
    return logs[x] % k


def check_field(p: int) -> None:
    gamma = primitive_root(p)
    for a in range(1, p):
        for b in range(1, p):
            if a == b:
                continue
            r = b * inv(a, p) % p
            for x in range(1, p):
                for z in range(1, p):
                    c = z * inv(x, p) % p
                    if c in (1, r):
                        continue
                    g = c * (1 - c) * inv((r - c) % p, p) % p
                    if g == 0:
                        continue
                    u = g * x % p
                    cdag = r * (c - 1) * inv((c - r) % p, p) % p
                    assert c * cdag % p == r * g % p
                    g2 = cdag * (1 - cdag) * inv((r - cdag) % p, p) % p
                    assert g2 == g
                    for h in divisors(p - 1):
                        k = (p - 1) // h
                        A = coset_index(c, p, h, gamma)
                        B = coset_index(cdag, p, h, gamma)
                        C = coset_index(g, p, h, gamma)
                        R = coset_index(r, p, h, gamma)
                        S = coset_index(x, p, h, gamma)
                        assert B == (R + C - A) % k
                        assert coset_index(u, p, h, gamma) == (C + S) % k
                        assert coset_index(z, p, h, gamma) == (A + S) % k


def check_pairing_tables() -> None:
    for a_values in product(range(4), repeat=4):
        for b_values in product(range(4), repeat=4):
            total = sum(a_values) + sum(b_values)
            matched = sum(min(a, b) for a, b in zip(a_values, b_values))
            excess = sum(abs(a - b) for a, b in zip(a_values, b_values))
            assert total == 2 * matched + excess
            if matched * 4 < total:
                assert excess * 2 > total
                positive = sum(max(a - b, 0) for a, b in zip(a_values, b_values))
                negative = sum(max(b - a, 0) for a, b in zip(a_values, b_values))
                assert max(positive, negative) * 4 > total

    for w_num in range(1, 10):
        w = Fraction(w_num, 17)
        for pcount in range(1, 5):
            complete = w / (2 * pcount)
            paired = complete / 4
            assert paired == w / (8 * pcount)


def main() -> None:
    for p in (5, 7, 11, 13):
        check_field(p)
        print(f"p={p}: physical RI identities passed")
    check_pairing_tables()
    print("Orbit-phase RI physical-lift checks passed")


if __name__ == "__main__":
    main()
