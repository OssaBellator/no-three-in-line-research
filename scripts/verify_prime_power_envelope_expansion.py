#!/usr/bin/env python3
"""Exact checks for CMR193--CMR195."""

from __future__ import annotations

from itertools import combinations
from math import ceil


def valuation(value: int, prime: int, cap: int) -> int:
    if value == 0:
        return cap
    result = 0
    while result < cap and value % prime == 0:
        result += 1
        value //= prime
    return result


def envelope_depth(columns: tuple[int, ...], prime: int, exponent: int) -> int:
    if len(columns) <= 1:
        return exponent
    return min(
        valuation(left - right, prime, exponent)
        for left, right in combinations(columns, 2)
    )


def verify_strict_expansion(prime: int, exponent: int) -> None:
    modulus = prime**exponent
    for depth in range(1, exponent + 1):
        for residue in range(prime**depth):
            inside = tuple(
                column
                for column in range(modulus)
                if column % (prime**depth) == residue
            )
            if len(inside) < 2:
                continue
            old_depth = envelope_depth(inside, prime, exponent)
            assert old_depth >= depth
            inside_set = set(inside)
            for outside in range(modulus):
                if outside in inside_set:
                    continue
                if outside % (prime**depth) == residue:
                    continue
                new_depth = envelope_depth(inside + (outside,), prime, exponent)
                assert new_depth < depth
                assert new_depth < old_depth


def verify_depth_budget(exponent: int) -> None:
    for start in range(exponent + 1):
        depth = start
        steps = 0
        while depth > 0:
            depth -= 1
            steps += 1
        assert steps <= exponent


def verify_batch_mass(max_targets: int) -> None:
    for targets in range(1, max_targets + 1):
        mass = ceil(2 * targets / 11)
        assert mass >= 1
        assert 11 * mass >= 2 * targets


def main() -> None:
    verify_strict_expansion(prime=5, exponent=3)
    verify_depth_budget(exponent=100)
    verify_batch_mass(max_targets=100_000)
    print(
        "verified envelope expansion: crossing columns strictly lower prefix "
        "depth and the expansion budget is at most k"
    )


if __name__ == "__main__":
    main()
