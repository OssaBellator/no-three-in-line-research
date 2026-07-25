#!/usr/bin/env python3
"""Exact checks for CMR340--CMR343."""

from __future__ import annotations


def valuation(n: int, p: int) -> int:
    assert n != 0
    n = abs(n)
    value = 0
    while n % p == 0:
        n //= p
        value += 1
    return value


def verify_assignments() -> None:
    for p in (3, 5, 7, 11):
        for first in range(1, 400):
            for third in range(1, 400):
                if third == first:
                    continue
                b = valuation(first, p)
                c = valuation(third, p)
                e = valuation(third - first, p)
                depths = (b, c, e)

                if c < b:
                    assert e == c
                    closest = b
                    outside = c
                    assert closest > outside
                elif c > b:
                    assert e == b
                    closest = c
                    outside = b
                    assert closest > outside
                elif e > b:
                    assert c == b
                    closest = e
                    outside = b
                    assert closest > outside
                else:
                    assert depths == (b, b, b)


def verify_prefix_residues() -> None:
    for p in (3, 5, 7):
        for closest_depth in range(1, 5):
            modulus = p**closest_depth
            first = 17
            second = first + modulus
            for outside_depth in range(closest_depth):
                third = first + p**outside_depth
                assert first % modulus == second % modulus
                assert third % modulus != first % modulus


def verify_depth_termination() -> None:
    for height in range(1, 30):
        for start in range(height):
            current = start
            steps = 0
            while current < height - 1:
                current += 1
                steps += 1
            assert steps == height - 1 - start


def main() -> None:
    verify_assignments()
    verify_prefix_residues()
    verify_depth_termination()
    print(
        "verified heavy-cell continuation: external and deeper closest-pair "
        "ownership, prefix exclusion, equilateral cases, and depth termination"
    )


if __name__ == "__main__":
    main()
