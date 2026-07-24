#!/usr/bin/env python3
"""Exact finite checks for CMR90--CMR92."""
from __future__ import annotations

import argparse
import random
from itertools import combinations


def determinant(
    a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]
) -> int:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def saturated_state(n: int, seed: int) -> list[list[int]]:
    rng = random.Random(seed)
    first = list(range(n))
    rng.shuffle(first)
    shift = rng.randrange(1, n)
    second = [(value + shift) % n for value in first]
    assert sorted(first) == list(range(n))
    assert sorted(second) == list(range(n))
    assert all(first[x] != second[x] for x in range(n))
    return [first, second]


def selected_points(values: list[list[int]]) -> list[tuple[int, int, int]]:
    n = len(values[0])
    return [
        (x, values[layer][x], layer)
        for layer in range(2)
        for x in range(n)
    ]


def block_data(
    values: list[list[int]], modulus: int, residue: int, layer: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int, int]]]:
    n = len(values[0])
    columns = [x for x in range(n) if x % modulus == residue]
    rows = {values[layer][x] for x in columns}
    moved = {(x, values[layer][x], layer) for x in columns}
    fixed = [point for point in selected_points(values) if point not in moved]

    allowed = []
    for x in columns:
        for y in rows:
            if y == values[layer][x]:
                continue
            if y == values[1 - layer][x]:
                continue
            allowed.append((x, y))

    return allowed, fixed


def compatible(cells: tuple[tuple[int, int], ...]) -> bool:
    return (
        len({cell[0] for cell in cells}) == len(cells)
        and len({cell[1] for cell in cells}) == len(cells)
    )


def block_counts(
    values: list[list[int]], modulus: int, residue: int, layer: int
) -> tuple[int, int, int]:
    allowed, fixed = block_data(values, modulus, residue, layer)
    t2 = 0
    t3 = 0

    compatible_pairs = []
    for first, second in combinations(allowed, 2):
        if not compatible((first, second)):
            continue
        compatible_pairs.append((first, second))
        for point in fixed:
            if determinant(first, second, point[:2]) == 0:
                t2 += 1

    for first, second, third in combinations(allowed, 3):
        if not compatible((first, second, third)):
            continue
        if determinant(first, second, third) == 0:
            t3 += 1

    return t2, t3, len(compatible_pairs)


def verify_instance(n: int, modulus: int, seed: int) -> tuple[int, int, int]:
    values = saturated_state(n, seed)
    t = n // modulus
    assert t >= 3

    total_t2 = 0
    total_t3 = 0
    compatible_pairs = 0
    for layer in range(2):
        for residue in range(modulus):
            t2, t3, pairs = block_counts(values, modulus, residue, layer)
            total_t2 += t2
            total_t3 += t3
            compatible_pairs += pairs

    falling2 = t * (t - 1)
    falling3 = t * (t - 1) * (t - 2)

    rank_two_bound = modulus * (2 * n - t) * (t - 1)
    assert total_t2 <= falling2 * rank_two_bound

    # total_t3/falling3 <= modulus*(t-1)^2/3
    assert 3 * total_t3 <= modulus * (t - 1) ** 2 * falling3

    assert rank_two_bound < 2 * n * n
    assert modulus * (t - 1) ** 2 * n < n * n * n

    return total_t2, total_t3, compatible_pairs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=4)
    args = parser.parse_args()

    instances = 0
    rank_two = 0
    rank_three = 0
    compatible_pairs = 0
    for seed in range(args.seeds):
        for n, modulus in ((25, 5), (49, 7)):
            t2, t3, pairs = verify_instance(n, modulus, seed)
            instances += 1
            rank_two += t2
            rank_three += t3
            compatible_pairs += pairs

    print(
        "verified higher-rank prefix collateral "
        f"instances={instances}; rank-two-certificates={rank_two}; "
        f"rank-three-certificates={rank_three}; "
        f"compatible-pairs={compatible_pairs}"
    )


if __name__ == "__main__":
    main()
