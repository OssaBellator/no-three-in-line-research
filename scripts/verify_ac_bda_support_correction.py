#!/usr/bin/env python3
"""Finite audit for AC3hq--AC3ht."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def det(p, q):
    return p[0] * q[1] - p[1] * q[0]


def verify_ordinary():
    records = 0
    collisions = 0
    clean = 0
    for h in range(1, 13):
        for q in range(1, 8):
            H = h + q
            for u, v in product(range(-6, 7), repeat=2):
                if u == 0 or v == 0 or u == v:
                    continue
                records += 1
                scalars = [0, h * u, h * v, H * u, H * v]
                mixed = (h * u == H * v) or (h * v == H * u)
                if mixed:
                    collisions += 1
                else:
                    clean += 1
                    assert len(set(scalars)) == 5
                    for a, b in product(range(-4, 5), repeat=2):
                        if a == 0 or b == 0:
                            continue
                        cells = [(s * a, s * b) for s in scalars]
                        assert len({x for x, _ in cells}) == 5
                        assert len({y for _, y in cells}) == 5
    return records, collisions, clean


def verify_reflected():
    records = 0
    determinant_checks = 0
    accidental_radial = 0
    for h in range(1, 13):
        for q in range(1, 8):
            for w, a, b in product(range(-5, 6), repeat=3):
                if w == 0 or a == 0 or b == 0:
                    continue
                C = (w * h * a, w * (h + q) * b)
                D = (w * (h + q) * a, w * h * b)
                lhs = det(C, D)
                rhs = -(w * w) * a * b * q * (2 * h + q)
                assert lhs == rhs
                assert lhs != 0
                determinant_checks += 1
                records += 1
                if lhs == 0:
                    accidental_radial += 1
    assert accidental_radial == 0
    return records, determinant_checks


def verify_routers():
    scope_cases = 0
    constants = 0
    for n in range(1, 9):
        weights = list(range(1, n + 1))
        V = sum(weights)
        for K in range(1, 9):
            retained = Fraction(V, K)
            assert retained * K == V
            scope_cases += 1
        for T in range(1, 100):
            for K in range(1, 10):
                assert Fraction(T, K) / 3 == Fraction(T, 3 * K)
                constants += 1
    return scope_cases, constants


def main():
    ordinary = verify_ordinary()
    reflected = verify_reflected()
    routers = verify_routers()
    print("AC BDA support correction audit passed")
    print(f"ordinary adjacent records: {ordinary[0]}")
    print(f"mixed collisions: {ordinary[1]}")
    print(f"clean five-cell supports: {ordinary[2]}")
    print(f"reflected CD records: {reflected[0]}")
    print(f"nonzero determinant checks: {reflected[1]}")
    print(f"scope arithmetic cases: {routers[0]}")
    print(f"pivot composition constants: {routers[1]}")


if __name__ == "__main__":
    main()
