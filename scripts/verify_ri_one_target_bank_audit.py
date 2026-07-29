#!/usr/bin/env python3
"""Finite checks for RI5bd--RI5bg."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


def i6_states(m: int, h: int):
    for sigma in permutations(range(m)):
        for shifts in product(range(h), repeat=m):
            yield sigma, shifts


def check_cylinders() -> int:
    checked = 0
    for m in range(1, 5):
        for h in range(1, 5):
            states = list(i6_states(m, h))
            total = len(states)
            for alpha in range(m):
                for beta in range(m):
                    for shift in range(h):
                        count = sum(
                            1
                            for sigma, shifts in states
                            if sigma[alpha] == beta and shifts[alpha] == shift
                        )
                        assert Fraction(count, total) == Fraction(1, m * h)
                        checked += 1

            records = []
            weight = 1
            for alpha in range(m):
                for beta in range(m):
                    for shift in range(h):
                        records.append((alpha, beta, shift, weight))
                        weight = weight % 7 + 1
            q1 = sum(w for *_rest, w in records)
            explicit = Fraction(0, 1)
            for sigma, shifts in states:
                load = sum(
                    w
                    for alpha, beta, shift, w in records
                    if sigma[alpha] == beta and shifts[alpha] == shift
                )
                explicit += Fraction(load, total)
            assert explicit == Fraction(q1, m * h)
    return checked


def inv(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def line_contains(P, Q, R, p: int) -> bool:
    return ((Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])) % p == 0


def check_hyperbola_intersections() -> int:
    checked = 0
    for p in (5, 7, 11):
        for a in range(1, p):
            hyperbola = [(x, a * inv(x, p) % p) for x in range(1, p)]
            plane = [(x, y) for x in range(p) for y in range(p)]
            for P, Q in combinations(plane, 2):
                hits = [R for R in hyperbola if line_contains(P, Q, R, p)]
                assert len(hits) <= 2, (p, a, P, Q, hits)
                checked += 1
    return checked


def main() -> None:
    cylinders = check_cylinders()
    lines = check_hyperbola_intersections()
    print(f"verified {cylinders} I6 prescriptions and {lines} finite-field lines")


if __name__ == "__main__":
    main()
