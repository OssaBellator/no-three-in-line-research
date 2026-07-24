#!/usr/bin/env python3
"""Verify CMR19--CMR21 for finite prime powers."""
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


def completed_reciprocal_values(p: int, k: int, parameters: tuple[int, ...]) -> list[int]:
    n = p**k
    values = []
    for x in range(n):
        if x == 0:
            values.append(0)
            continue
        r = valuation(x, p)
        modulus = p ** (k - r)
        unit = x // (p**r)
        values.append(p**r * ((parameters[r] * pow(unit, -1, modulus)) % modulus))
    return values


def companion(y: int, p: int, k: int) -> int:
    n = p**k
    increment = p if p % 2 else 4
    return ((1 + increment) * y + 1) % n


def all_blocks(p: int, k: int):
    a = p ** (k - 1)
    blocks = []
    for r in range(k - 1):
        step_unit = p ** (k - r - 1)
        scale = p**r
        for xi in range(step_unit):
            if xi % p == 0:
                continue
            blocks.append([scale * (xi + j * step_unit) for j in range(p)])
    blocks.append([j * a for j in range(p)])
    return blocks


def verify_instance(p: int, k: int, parameters: tuple[int, ...]) -> tuple[int, int]:
    n = p**k
    a = p ** (k - 1)
    first = completed_reciprocal_values(p, k, parameters)
    blocks = all_blocks(p, k)
    assert len(blocks) == a
    assert sorted(x for block in blocks for x in block) == list(range(n))

    first_row_sets = []
    second_row_sets = []
    for columns in blocks:
        rows = [first[x] for x in columns]
        assert len(set(rows)) == p
        first_row_sets.append(set(rows))
        second = {companion(row, p, k) for row in rows}
        assert len(second) == p
        assert set(rows).isdisjoint(second)
        second_row_sets.append(second)

    assert sorted(row for rows in first_row_sets for row in rows) == list(range(n))
    assert sorted(row for rows in second_row_sets for row in rows) == list(range(n))

    local_states = 0
    perms = list(permutations(range(p)))
    for columns, first_rows, second_rows in zip(blocks, first_row_sets, second_row_sets):
        first_list = sorted(first_rows)
        second_list = sorted(second_rows)
        for pi in perms:
            for tau in perms:
                for j in range(p):
                    assert first_list[pi[j]] != second_list[tau[j]]
                local_states += 1

    layer0 = []
    layer1 = []
    for columns, first_rows, second_rows in zip(blocks, first_row_sets, second_row_sets):
        first_list = sorted(first_rows)
        second_list = sorted(second_rows)
        layer0.extend((columns[j], first_list[j]) for j in range(p))
        layer1.extend((columns[j], second_list[j]) for j in range(p))
    assert len({point for point in layer0 + layer1}) == 2 * n
    assert sorted(y for _, y in layer0) == list(range(n))
    assert sorted(y for _, y in layer1) == list(range(n))
    return len(blocks), local_states


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=125)
    args = parser.parse_args()
    if args.max_modulus < 8:
        parser.error("--max-modulus must be at least 8")

    instances = 0
    blocks = 0
    local_states = 0
    for p in (2, 3, 5):
        k = 2
        while p**k <= args.max_modulus:
            parameters = tuple(1 + p * r for r in range(k))
            parameters = tuple(c if gcd(c, p) == 1 else 1 for c in parameters)
            b, s = verify_instance(p, k, parameters)
            blocks += b
            local_states += s
            instances += 1
            k += 1

    print(
        f"verified all-stratum bank instances={instances}; "
        f"blocks={blocks}; local two-layer states={local_states}"
    )


if __name__ == "__main__":
    main()
