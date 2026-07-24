#!/usr/bin/env python3
"""Exact checks for CMR106--CMR109 child-pencil dichotomy."""

from __future__ import annotations

import argparse
from itertools import combinations

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
    size = p ** (k - s - 1)
    return [
        (a + step * xi + high_step * q, step * eta + high_step * q)
        for q in range(size)
    ]


def build_fixed_set(
    p: int, k: int, s: int, a: int
) -> tuple[list[Point], list[int]]:
    """Two disjoint permutation layers with one layer-zero parent node removed."""
    modulus = p**s
    n = p**k
    parent_columns = {x for x in range(n) if x % modulus == a}
    points: list[Point] = []
    layers: list[int] = []
    for x in range(n):
        if x not in parent_columns:
            points.append((x, x))
            layers.append(0)
        points.append((x, (x + 1) % n))
        layers.append(1)
    assert len(points) == len(set(points))
    return points, layers


def maximal_matching(edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    used: set[int] = set()
    result: list[tuple[int, int]] = []
    for u, v in edges:
        if u not in used and v not in used:
            used.add(u)
            used.add(v)
            result.append((u, v))
    return result


def profile_counts(points: list[Point], fixed: list[Point]) -> tuple[int, int]:
    w1 = sum(
        det(z, p1, p2) == 0
        for z in points
        for p1, p2 in combinations(fixed, 2)
    )
    w2 = sum(
        det(z1, z2, p0) == 0
        for z1, z2 in combinations(points, 2)
        for p0 in fixed
    )
    return w1, w2


def verify(p: int, k: int, s: int) -> None:
    if p < 5 or p % 2 == 0:
        raise ValueError("use an odd prime p>=5")
    if not (1 <= s < k):
        raise ValueError("require 1 <= s < k")

    n = p**k
    a = 0
    child_size = p ** (k - s - 1)
    fixed, layers = build_fixed_set(p, k, s, a)
    z_size = len(fixed)

    all_maps = [
        local_map(b, c, p)
        for c in nonsquares(p)
        for b in range(p)
    ]
    current = all_maps[0]
    target_inputs = (0, 1)
    omega = [
        mapping
        for mapping in all_maps
        if all(mapping[xi] != current[xi] for xi in target_inputs)
    ]
    h = (p - 1) // 2
    expected_bank_size = h * (p - 2) + 1
    assert len(omega) == expected_bank_size

    support = {(xi, mapping[xi]) for mapping in omega for xi in range(p)}
    cell_multiplicity = {
        cell: sum(mapping[cell[0]] == cell[1] for mapping in omega)
        for cell in support
    }
    assert max(cell_multiplicity.values(), default=0) <= h

    profiles: dict[tuple[int, int], tuple[int, int]] = {}
    v1 = 0
    v2 = 0
    has_w1_absorber = False
    has_w2_absorber = False

    for xi, eta in sorted(support):
        points = child_set(p, k, s, a, xi, eta)
        w1, w2 = profile_counts(points, fixed)
        profiles[(xi, eta)] = (w1, w2)
        v1 += w1
        v2 += w2

        for z in points:
            edges = [
                (i, j)
                for i, j in combinations(range(z_size), 2)
                if det(z, fixed[i], fixed[j]) == 0
            ]
            matching = maximal_matching(edges)
            assert len(edges) <= 2 * len(matching) * (z_size - 1)
            if len(matching) >= 13:
                represented = [
                    sum(layers[i] == ell or layers[j] == ell for i, j in matching)
                    for ell in (0, 1)
                ]
                assert max(represented) >= 7
                has_w1_absorber = True

        for outside in fixed:
            edges = [
                (i, j)
                for i, j in combinations(range(child_size), 2)
                if det(points[i], points[j], outside) == 0
            ]
            matching = maximal_matching(edges)
            assert len(edges) <= 2 * len(matching) * max(child_size - 1, 0)
            if len(matching) >= 7:
                has_w2_absorber = True

    v_support = v1 + v2
    expected_rank_one = sum(
        sum(
            profiles[(xi, mapping[xi])][0]
            + profiles[(xi, mapping[xi])][1]
            for xi in range(p)
        )
        for mapping in omega
    ) / len(omega)
    assert expected_rank_one <= h * v_support / len(omega)

    diffuse_bound = (
        24 * p * p * child_size * (z_size - 1)
        + 12 * p * p * z_size * max(child_size - 1, 0)
    )
    assert has_w1_absorber or has_w2_absorber or v_support <= diffuse_bound

    parent_size = p * child_size
    if not has_w1_absorber and not has_w2_absorber:
        coarse = 120 * parent_size * n
        assert h * v_support / len(omega) < coarse

    print(
        "verified child-pencil dichotomy: "
        f"p={p}, N={n}, s={s}, support={len(support)}, "
        f"bank={len(omega)}, V1={v1}, V2={v2}, "
        f"W1-absorber={has_w1_absorber}, W2-absorber={has_w2_absorber}"
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
