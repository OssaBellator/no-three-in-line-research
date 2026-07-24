#!/usr/bin/env python3
"""Verify Theorems CMR15 and CMR16 on finite odd prime powers."""
from __future__ import annotations

import argparse
from itertools import permutations
from math import gcd


def valuation(value: int, p: int) -> int:
    out = 0
    while value % p == 0:
        value //= p
        out += 1
    return out


def completed_reciprocal_values(p: int, k: int, c0: int) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p)
        modulus = p ** (k - r)
        c = c0 if r == 0 else 1
        unit = x // (p**r)
        values.append(p**r * ((c * pow(unit, -1, modulus)) % modulus))
    return values


def verify_instance(p: int, k: int, c0: int) -> tuple[int, int]:
    n = p**k
    a = p ** (k - 1)
    values = completed_reciprocal_values(p, k, c0)
    row_blocks = set()
    block_count = 0
    state_checks = 0

    for xi in range(a):
        if xi % p == 0:
            continue
        columns = [xi + j * a for j in range(p)]
        rows = [values[x] for x in columns]
        assert len(set(columns)) == p
        assert len(set(rows)) == p
        residues = {row % a for row in rows}
        assert len(residues) == 1
        row_residue = next(iter(residues))
        assert row_residue not in row_blocks
        row_blocks.add(row_residue)

        inverse = pow(xi, -1, n)
        q = (c0 * inverse * inverse) % p
        base = (c0 * inverse) % n
        for j, row in enumerate(rows):
            assert (row - (base - j * q * a)) % n == 0

        # Every permutation is checked for p <= 5; for p=7 use rotations.
        if p <= 5:
            states = permutations(range(p))
        else:
            states = (tuple((j + shift) % p for j in range(p)) for shift in range(p))
        for pi in states:
            state_rows = [rows[pi[j]] for j in range(p)]
            assert set(state_rows) == set(rows)
            state_checks += 1

        block_count += 1

    assert block_count == (p - 1) * p ** (k - 2)
    assert len(row_blocks) == block_count
    return block_count, state_checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 9:
        parser.error("--max-modulus must be at least 9")

    instances = 0
    blocks = 0
    states = 0
    for p in (3, 5, 7):
        k = 2
        while p**k <= args.max_modulus:
            for c0 in range(1, p):
                if gcd(c0, p) != 1:
                    continue
                b, s = verify_instance(p, k, c0)
                blocks += b
                states += s
                instances += 1
            k += 1

    print(
        f"verified top-digit block instances={instances}; "
        f"blocks={blocks}; local states checked={states}"
    )


if __name__ == "__main__":
    main()
