#!/usr/bin/env python3
"""Exact finite checks for CMR93--CMR95."""
from __future__ import annotations

import argparse
import random
from itertools import permutations


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def reciprocal_permutation(p: int, b: int, c: int) -> tuple[int, ...]:
    return tuple(
        b if x == 0 else (b + c * pow(x, -1, p)) % p
        for x in range(p)
    )


def balanced_recursive_state(p: int, k: int, seed: int) -> list[list[int]]:
    rng = random.Random(seed)
    ns = nonsquares(p)
    c = rng.choice(ns)
    b0, b1 = rng.sample(range(p), 2)
    values = [
        list(reciprocal_permutation(p, b0, c)),
        list(reciprocal_permutation(p, b1, c)),
    ]
    modulus = p

    for _depth in range(1, k):
        lifted_layers = []
        for layer in range(2):
            local = [
                reciprocal_permutation(p, rng.randrange(p), rng.choice(ns))
                for _ in range(modulus)
            ]
            lifted = [0] * (p * modulus)
            for prefix in range(modulus):
                for digit in range(p):
                    column = prefix + modulus * digit
                    lifted[column] = values[layer][prefix] + modulus * local[prefix][digit]
            lifted_layers.append(lifted)
        values = lifted_layers
        modulus *= p

    assert all(sorted(layer) == list(range(modulus)) for layer in values)
    assert all(values[0][x] != values[1][x] for x in range(modulus))
    return values


def block_columns(n: int, modulus: int, residue: int) -> list[int]:
    return [x for x in range(n) if x % modulus == residue]


def row_sets(values: list[list[int]], modulus: int) -> list[list[frozenset[int]]]:
    n = len(values[0])
    return [
        [
            frozenset(values[layer][x] for x in block_columns(n, modulus, residue))
            for residue in range(modulus)
        ]
        for layer in range(2)
    ]


def quotient_maps(values: list[list[int]], modulus: int) -> list[tuple[int, ...]]:
    n = len(values[0])
    maps = []
    for layer in range(2):
        quotient = []
        for residue in range(modulus):
            rows = {
                values[layer][x] % modulus
                for x in block_columns(n, modulus, residue)
            }
            assert len(rows) == 1
            quotient.append(next(iter(rows)))
        maps.append(tuple(quotient))
    return maps


def allowed_rematching(
    values: list[list[int]], modulus: int, residue: int, layer: int
) -> tuple[list[int], tuple[int, ...]]:
    n = len(values[0])
    columns = block_columns(n, modulus, residue)
    rows = [values[layer][x] for x in columns]
    row_index = {row: index for index, row in enumerate(rows)}

    opposite_forbidden = {}
    for index, column in enumerate(columns):
        opposite_row = values[1 - layer][column]
        if opposite_row in row_index:
            opposite_forbidden[index] = row_index[opposite_row]

    for permutation in permutations(range(len(rows))):
        if any(permutation[index] == index for index in range(len(rows))):
            continue
        if any(
            permutation[index] == forbidden
            for index, forbidden in opposite_forbidden.items()
        ):
            continue
        return columns, permutation
    raise AssertionError("no allowed rematching")


def apply_rematching(
    values: list[list[int]], modulus: int, residue: int, layer: int
) -> None:
    columns, permutation = allowed_rematching(values, modulus, residue, layer)
    old_rows = [values[layer][x] for x in columns]
    for index, column in enumerate(columns):
        values[layer][column] = old_rows[permutation[index]]

    n = len(values[0])
    assert sorted(values[layer]) == list(range(n))
    assert all(values[0][x] != values[1][x] for x in range(n))


def verify_instance(seed: int) -> tuple[int, int]:
    p = 5
    k = 3
    n = p**k
    values = balanced_recursive_state(p, k, seed)

    coarse_modulus = p
    fine_modulus = p**2
    initial_coarse_rows = row_sets(values, coarse_modulus)
    initial_coarse_maps = quotient_maps(values, coarse_modulus)
    initial_fine_maps = quotient_maps(values, fine_modulus)

    repairs = 0
    for layer in range(2):
        for residue in range(fine_modulus):
            apply_rematching(values, fine_modulus, residue, layer)
            repairs += 1

    assert row_sets(values, coarse_modulus) == initial_coarse_rows
    assert quotient_maps(values, coarse_modulus) == initial_coarse_maps
    assert quotient_maps(values, fine_modulus) == initial_fine_maps

    # Every coarse block still has an allowed degree-two-forbidden rematching.
    admissible = 0
    for layer in range(2):
        for residue in range(coarse_modulus):
            allowed_rematching(values, coarse_modulus, residue, layer)
            admissible += 1

    assert all(sorted(layer) == list(range(n)) for layer in values)
    assert all(values[0][x] != values[1][x] for x in range(n))
    return repairs, admissible


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=4)
    args = parser.parse_args()

    repairs = 0
    admissible = 0
    for seed in range(args.seeds):
        local_repairs, local_admissible = verify_instance(seed)
        repairs += local_repairs
        admissible += local_admissible

    print(
        "verified descending prefix invariance "
        f"instances={args.seeds}; fine-repairs={repairs}; "
        f"coarse-banks={admissible}"
    )


if __name__ == "__main__":
    main()
