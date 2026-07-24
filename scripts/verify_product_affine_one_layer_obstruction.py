#!/usr/bin/env python3
"""Exhaust blockwise-affine one-inner-layer products at base side 6 or 7."""
from __future__ import annotations

import argparse
from itertools import combinations, permutations
from math import gcd
from multiprocessing import Pool

Point = tuple[int, int]
Permutation = tuple[int, ...]
ORIENTATIONS = ("cc", "cf", "fc", "ff")


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def affine_group(n: int) -> tuple[Permutation, ...]:
    return tuple(
        tuple((a * x + b) % n for x in range(n))
        for a in range(n)
        if gcd(a, n) == 1
        for b in range(n)
    )


def one_layer_state(
    tau: Permutation,
    orientation: str,
    alpha_1: Permutation,
    beta_1: Permutation,
) -> tuple[Point, ...]:
    n = len(tau)
    identity = tuple(range(n))
    row_maps = (identity, alpha_1)
    column_maps = (identity, beta_1)
    outer = ((0, 1), (1, 0))
    points: list[Point] = []
    for r in (0, 1):
        for i in range(2):
            j = outer[r][i]
            for u in range(n):
                v = tau[u]
                row_digit = row_maps[i][u]
                column_digit = column_maps[j][v]
                x = n * i + row_digit if orientation[0] == "c" else 2 * row_digit + i
                y = n * j + column_digit if orientation[1] == "c" else 2 * column_digit + j
                points.append((x, y))
    return tuple(points)


def is_no_three(points: tuple[Point, ...]) -> bool:
    for index, third in enumerate(points):
        for first, second in combinations(points[:index], 2):
            if determinant(first, second, third) == 0:
                return False
    return True


def _worker(arguments: tuple[Permutation, tuple[Permutation, ...]]) -> bool:
    tau, group = arguments
    for orientation in ORIENTATIONS:
        for alpha_1 in group:
            for beta_1 in group:
                if is_no_three(one_layer_state(tau, orientation, alpha_1, beta_1)):
                    return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", type=int, choices=(6, 7), default=6)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    n = args.side
    group = affine_group(n)
    expected_group_size = {6: 12, 7: 42}[n]
    expected_states = {6: 414_720, 7: 35_562_240}[n]
    assert len(group) == expected_group_size

    tasks = ((tau, group) for tau in permutations(range(n)))
    with Pool(args.workers) as pool:
        successes = sum(pool.imap_unordered(_worker, tasks, chunksize=1))

    assert successes == 0
    tested = 1
    for factor in (len(tuple(permutations(range(n)))), 4, len(group), len(group)):
        tested *= factor
    assert tested == expected_states
    print(
        f"normalized affine one-layer obstruction n={n}: "
        f"tested_states={tested}, no_three_states={successes}"
    )


if __name__ == "__main__":
    main()
