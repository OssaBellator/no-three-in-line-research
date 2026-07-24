#!/usr/bin/env python3
"""Exact checks for CMR102--CMR105 child-translation pencils."""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
from math import comb

Point = tuple[int, int]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def nonsquares(p: int) -> list[int]:
    squares = {x * x % p for x in range(1, p)}
    return [x for x in range(1, p) if x not in squares]


def tau(x: int, p: int) -> int:
    return 0 if x == 0 else pow(x, -1, p)


def local_map(b: int, c: int, p: int) -> tuple[int, ...]:
    return tuple((b + c * tau(x, p)) % p for x in range(p))


def child_set(p: int, k: int, s: int, a: int, xi: int, eta: int) -> list[Point]:
    step = p**s
    high_step = p ** (s + 1)
    L = p ** (k - s - 1)
    return [
        (a + step * xi + high_step * q, step * eta + high_step * q)
        for q in range(L)
    ]


def build_fixed_set(p: int, k: int, s: int, a: int) -> tuple[list[Point], set[int]]:
    """A simple disjoint two-layer host; remove the old layer-zero parent node."""
    N = p**k
    modulus = p**s
    parent_columns = {x for x in range(N) if x % modulus == a}
    fixed: list[Point] = []
    for x in range(N):
        if x not in parent_columns:
            fixed.append((x, x))
        fixed.append((x, (x + 1) % N))
    assert len(fixed) == 2 * N - len(parent_columns)
    assert len(set(fixed)) == len(fixed)
    return fixed, parent_columns


def profile_counts(points: list[Point], fixed: list[Point]) -> tuple[int, int, int]:
    w1 = 0
    for z in points:
        for p1, p2 in combinations(fixed, 2):
            w1 += det(z, p1, p2) == 0

    w2 = 0
    for z1, z2 in combinations(points, 2):
        for p0 in fixed:
            w2 += det(z1, z2, p0) == 0

    internal = sum(det(*triple) == 0 for triple in combinations(points, 3))
    return w1, w2, internal


def direct_rank_one_count(
    replacement: list[tuple[Point, int]], fixed: list[Point]
) -> tuple[int, int]:
    total = 0
    internal = 0
    all_points = [(point, xi, True) for point, xi in replacement]
    all_points.extend((point, -1, False) for point in fixed)

    for triple in combinations(all_points, 3):
        if det(triple[0][0], triple[1][0], triple[2][0]) != 0:
            continue
        moved = [item for item in triple if item[2]]
        if not moved:
            continue
        child_keys = {item[1] for item in moved}
        if len(child_keys) != 1:
            continue
        if len(moved) == 3:
            internal += 1
        else:
            total += 1
    return total, internal


def verify(p: int, k: int, s: int) -> None:
    if p < 5 or p % 2 == 0:
        raise ValueError("use an odd prime p>=5")
    if not (1 <= s < k):
        raise ValueError("require 1 <= s < k")

    N = p**k
    a = 0
    L = p ** (k - s - 1)
    parent_size = p * L
    fixed, _ = build_fixed_set(p, k, s, a)

    profiles: dict[tuple[int, int], tuple[int, int, int]] = {}
    for xi in range(p):
        internal_values = set()
        sum_w1 = 0
        sum_w2 = 0
        for eta in range(p):
            points = child_set(p, k, s, a, xi, eta)
            w1, w2, internal = profile_counts(points, fixed)
            profiles[(xi, eta)] = (w1, w2, internal)
            internal_values.add(internal)
            sum_w1 += w1
            sum_w2 += w2

            old_residue = (p**s * xi) % (p ** (s + 1))
            new_residue = (p**s * eta) % (p ** (s + 1))
            if eta != xi:
                assert new_residue != old_residue

        assert len(internal_values) == 1
        assert sum_w1 <= L * comb(len(fixed), 2)
        assert sum_w2 <= len(fixed) * comb(L, 2)

    V = sum(w1 + w2 for w1, w2, _ in profiles.values())
    coarse = 2 * parent_size * N * N + N * parent_size * parent_size // p
    assert V < coarse

    maps = [local_map(b, c, p) for c in nonsquares(p) for b in range(p)]
    for mapping in maps[: min(4, len(maps))]:
        replacement: list[tuple[Point, int]] = []
        expected_external = 0
        expected_internal = 0
        for xi, eta in enumerate(mapping):
            replacement.extend((point, xi) for point in child_set(p, k, s, a, xi, eta))
            w1, w2, internal = profiles[(xi, eta)]
            expected_external += w1 + w2
            expected_internal += internal

        direct_external, direct_internal = direct_rank_one_count(replacement, fixed)
        assert direct_external == expected_external
        assert direct_internal == expected_internal

    print(
        "verified child pencils: "
        f"p={p}, N={N}, s={s}, child-size={L}, profiles={p*p}, V={V}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=5)
    parser.add_argument("--exponent", type=int, default=3)
    parser.add_argument("--scale", type=int, default=1)
    args = parser.parse_args()
    verify(args.prime, args.exponent, args.scale)


if __name__ == "__main__":
    main()
