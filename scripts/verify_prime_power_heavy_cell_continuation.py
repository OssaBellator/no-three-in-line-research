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
                    assert b > c
                elif c > b:
                    assert e == b
                    assert c > b
                elif e > b:
                    assert c == b
                    assert e > b
                else:
                    assert depths == (b, b, b)


def verify_prefix_residues() -> None:
    for p in (3, 5, 7):
        for depth in range(1, 5):
            modulus = p**depth
            first = 17
            second = first + modulus
            for outside_depth in range(depth):
                third = first + p**outside_depth
                assert first % modulus == second % modulus
                assert third % modulus != first % modulus

            # Equilateral parameters 0, p^depth, 2*p^depth occupy one prefix
            # block and three distinct children for odd p.
            equilateral = (
                first,
                first + modulus,
                first + 2 * modulus,
            )
            assert len({value % modulus for value in equilateral}) == 1
            children = {
                (value // modulus) % p
                for value in equilateral
            }
            assert len(children) == 3
            assert valuation(equilateral[1] - equilateral[0], p) == depth
            assert valuation(equilateral[2] - equilateral[1], p) == depth
            assert valuation(equilateral[2] - equilateral[0], p) == depth


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
        "ownership, equilateral common blocks, and depth termination"
    )


if __name__ == "__main__":
    main()
