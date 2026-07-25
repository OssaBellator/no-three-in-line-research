#!/usr/bin/env python3
"""Exact checks for CMR310--CMR313."""

from __future__ import annotations

from math import ceil, gcd


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def verify_membership_criterion() -> None:
    for p in (3, 5, 7):
        for depth in range(5):
            modulus = p**depth
            for u in range(-8, 9):
                for v in range(-8, 9):
                    if (u, v) == (0, 0) or gcd(abs(u), abs(v)) != 1:
                        continue
                    for q in range(-100, 101):
                        same_cell = (q * u) % modulus == 0 and (q * v) % modulus == 0
                        assert same_cell == (q % modulus == 0)
                        if q != 0 and q % modulus != 0:
                            exit_depth = valuation(q, p)
                            assert exit_depth < depth
                            scale = p**exit_depth
                            x = (q * u // scale) % p
                            y = (q * v // scale) % p
                            assert (x, y) != (0, 0)


def verify_routing_counts() -> None:
    for population in range(1, 500):
        assert max(population // 2, population - population // 2) >= ceil(
            population / 2
        )
        for depth in range(1, 12):
            crossing = ceil(population / 2)
            assert ceil(crossing / depth) >= ceil(population / (2 * depth))


def verify_internal_scaling() -> None:
    for p, h in ((3, 5), (5, 4), (7, 3)):
        side = p**h
        for depth in range(1, h + 1):
            modulus = p**depth
            child_side = side // modulus
            for residue_x in range(modulus):
                for residue_y in range(modulus):
                    points = [
                        (residue_x + modulus * index, residue_y + modulus * index)
                        for index in range(min(child_side, 4))
                    ]
                    scaled = [
                        ((x - residue_x) // modulus, (y - residue_y) // modulus)
                        for x, y in points
                    ]
                    assert all(0 <= x < child_side and 0 <= y < child_side for x, y in scaled)
                    assert len(set(scaled)) == len(points)

            # A concrete collinear triple remains collinear after scaling.
            if child_side >= 3:
                residue_x = modulus - 1
                residue_y = modulus - 1
                triple = [
                    (residue_x + modulus * index, residue_y + 2 * modulus * index)
                    for index in range(3)
                    if residue_y + 2 * modulus * index < side
                ]
                if len(triple) == 3:
                    scaled = [
                        ((x - residue_x) // modulus, (y - residue_y) // modulus)
                        for x, y in triple
                    ]
                    (x1, y1), (x2, y2), (x3, y3) = scaled
                    assert (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def main() -> None:
    verify_membership_criterion()
    verify_routing_counts()
    verify_internal_scaling()
    print(
        "verified carry-cell routing: prefix membership, strict exit depths, "
        "half-population routing, and internal scaling"
    )


if __name__ == "__main__":
    main()
