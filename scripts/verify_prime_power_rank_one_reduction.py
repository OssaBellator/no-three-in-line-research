#!/usr/bin/env python3
"""Verify CMR79--CMR81 on finite recursive p-adic states."""

from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd
from typing import Iterable, Sequence

Point = tuple[int, int]
Line = tuple[int, int, int]


def determinant(points: Sequence[Point]) -> int:
    (x1, y1), (x2, y2), (x3, y3) = points
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


def primitive_line(first: Point, second: Point) -> Line:
    x1, y1 = first
    x2, y2 = second
    a0 = y1 - y2
    b0 = x2 - x1
    divisor = gcd(abs(a0), abs(b0))
    assert divisor > 0
    a = a0 // divisor
    b = b0 // divisor
    c = (a0 * x1 + b0 * y1) // divisor
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def on_line(point: Point, line: Line) -> bool:
    x, y = point
    a, b, c = line
    return a * x + b * y == c


def build_recursive_state(n: int) -> tuple[list[int], list[int]]:
    """Two p-adic-compatible permutations with disjoint quotient images."""
    first = list(range(n))
    second = [(x + 1) % n for x in range(n)]
    assert sorted(first) == list(range(n))
    assert sorted(second) == list(range(n))
    assert all(first[x] != second[x] for x in range(n))
    return first, second


def quotient_permutation(layer: Sequence[int], modulus: int) -> list[int]:
    quotient = []
    for residue in range(modulus):
        values = {layer[x] % modulus for x in range(residue, len(layer), modulus)}
        assert len(values) == 1
        quotient.append(values.pop())
    assert sorted(quotient) == list(range(modulus))
    return quotient


def quotient_incidence(line: Line, quotient: Sequence[int], modulus: int) -> int:
    a, b, c = line
    return sum(
        (a * x + b * quotient[x] - c) % modulus == 0
        for x in range(modulus)
    )


def lifted_channel_cells(quotient: Sequence[int], n: int, modulus: int) -> set[Point]:
    return {
        (x, y)
        for x in range(n)
        for y in range(n)
        if y % modulus == quotient[x % modulus]
    }


def verify_line_lift_bound(
    state: set[Point], quotient_layers: Sequence[Sequence[int]], n: int, modulus: int
) -> int:
    t = n // modulus
    channels = [lifted_channel_cells(q, n, modulus) for q in quotient_layers]
    checks = 0
    for first, second in combinations(state, 2):
        line = primitive_line(first, second)
        for quotient, channel in zip(quotient_layers, channels):
            actual = sum(on_line(point, line) for point in channel)
            incidence = quotient_incidence(line, quotient, modulus)
            assert actual <= t * incidence
            checks += 1
    return checks


def block_rank_one_count(
    first: Sequence[int],
    second: Sequence[int],
    layer_index: int,
    modulus: int,
    residue: int,
) -> int:
    layers = (first, second)
    active = layers[layer_index]
    opposite = layers[1 - layer_index]
    columns = [x for x in range(len(first)) if x % modulus == residue]
    row_residue = active[columns[0]] % modulus
    rows = [y for y in range(len(first)) if y % modulus == row_residue]

    anchor = {(x, active[x]) for x in columns}
    state = {(x, first[x]) for x in range(len(first))} | {
        (x, second[x]) for x in range(len(second))
    }
    fixed = state - anchor
    candidates = {
        (x, y)
        for x in columns
        for y in rows
        if y != active[x] and y != opposite[x]
    }

    count = 0
    fixed_pairs = tuple(combinations(fixed, 2))
    for candidate in candidates:
        for pair in fixed_pairs:
            if determinant((pair[0], pair[1], candidate)) == 0:
                count += 1
    return count


def quotient_secant_energy(
    state: set[Point], quotient_layers: Sequence[Sequence[int]], modulus: int
) -> int:
    energy = 0
    for first, second in combinations(state, 2):
        line = primitive_line(first, second)
        energy += sum(
            quotient_incidence(line, quotient, modulus)
            for quotient in quotient_layers
        )
    return energy


def verify_rank_one_sum(p: int, k: int, s: int) -> tuple[int, int, int]:
    n = p**k
    modulus = p**s
    t = n // modulus
    first, second = build_recursive_state(n)
    quotient_layers = [
        quotient_permutation(first, modulus),
        quotient_permutation(second, modulus),
    ]
    state = {(x, first[x]) for x in range(n)} | {(x, second[x]) for x in range(n)}

    checks = verify_line_lift_bound(state, quotient_layers, n, modulus)

    rank_one_total = 0
    for layer in range(2):
        for residue in range(modulus):
            rank_one_total += block_rank_one_count(
                first, second, layer, modulus, residue
            )

    energy = quotient_secant_energy(state, quotient_layers, modulus)
    assert rank_one_total <= t * energy
    checks += 2 * modulus
    return checks, rank_one_total, energy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=25)
    args = parser.parse_args()

    total_checks = 0
    summaries: list[str] = []
    for p, k in ((5, 2), (5, 3)):
        n = p**k
        if n > args.max_modulus:
            continue
        for s in range(k):
            checks, rank_one, energy = verify_rank_one_sum(p, k, s)
            total_checks += checks
            summaries.append(
                f"N={n},s={s},T1={rank_one},J={energy}"
            )

    print(
        "verified rank-one quotient reduction: "
        + "; ".join(summaries)
        + f"; checks={total_checks}"
    )


if __name__ == "__main__":
    main()
