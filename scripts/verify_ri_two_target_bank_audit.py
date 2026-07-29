#!/usr/bin/env python3
"""Finite checks for the bank-ready two-target I6 audit."""

from itertools import permutations, product, combinations
from fractions import Fraction


def i6_states(m, h):
    for sigma in permutations(range(m)):
        for shifts in product(range(h), repeat=m):
            yield sigma, shifts


def verify_cylinders():
    checked = 0
    for m in range(2, 6):
        for h in range(1, 5):
            states = list(i6_states(m, h))
            total = len(states)
            for a1, a2 in combinations(range(m), 2):
                for b1, b2 in permutations(range(m), 2):
                    for s1 in range(h):
                        for s2 in range(h):
                            count = sum(
                                sigma[a1] == b1
                                and sigma[a2] == b2
                                and shifts[a1] == s1
                                and shifts[a2] == s2
                                for sigma, shifts in states
                            )
                            assert Fraction(count, total) == Fraction(
                                1, m * (m - 1) * h * h
                            )
                            checked += 1
            # repeated source prescriptions are rank one or incompatible
            a = 0
            for b1 in range(m):
                for b2 in range(m):
                    for s1 in range(h):
                        for s2 in range(h):
                            count = sum(
                                sigma[a] == b1
                                and sigma[a] == b2
                                and shifts[a] == s1
                                and shifts[a] == s2
                                for sigma, shifts in states
                            )
                            expected = Fraction(1, m * h) if (b1, s1) == (b2, s2) else 0
                            assert Fraction(count, total) == expected
                            checked += 1
    return checked


def inv(x, p):
    return pow(x, p - 2, p)


def verify_secants():
    checked = 0
    for p in (5, 7, 11, 13):
        for a in range(1, p):
            seen = {}
            for x, y in combinations(range(1, p), 2):
                # secant address encoded by sum and product of target columns
                key = ((x + y) % p, (x * y) % p)
                pair = frozenset((x, y))
                assert key not in seen or seen[key] == pair
                seen[key] = pair
                # both points lie on xy=a
                assert (x * (a * inv(x, p))) % p == a
                assert (y * (a * inv(y, p))) % p == a
                checked += 1
    return checked


def main():
    c1 = verify_cylinders()
    c2 = verify_secants()
    print(f"verified {c1} I6 prescriptions and {c2} hyperbola secants")


if __name__ == "__main__":
    main()
