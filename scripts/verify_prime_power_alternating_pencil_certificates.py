#!/usr/bin/env python3
"""Exact checks for CMR110--CMR112 alternating pencil certificates."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

Point = tuple[int, int]


def det(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def maximal_matching(edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    used: set[int] = set()
    result: list[tuple[int, int]] = []
    for u, v in edges:
        if u not in used and v not in used:
            used.add(u)
            used.add(v)
            result.append((u, v))
    return result


def verify_lll(max_t: int) -> None:
    x7 = Fraction(5, 19)
    assert x7 * (1 - x7) ** 2 >= Fraction(1, 7)
    assert (1 - x7) ** 14 > Fraction(1, 72)

    previous: Fraction | None = None
    for t in range(8, max_t + 1):
        x = Fraction(2, t + 1)
        assert x * (1 - x) ** 2 >= Fraction(1, t)
        probability = (1 - x) ** (2 * t)
        assert probability > Fraction(1, 72)
        if previous is not None:
            assert probability > previous
        previous = probability


def count_allowed(t: int, forbidden: set[tuple[int, int]]) -> int:
    return sum(
        all((i, permutation[i]) not in forbidden for i in range(t))
        for permutation in permutations(range(t))
    )


def verify_small_matching_banks(max_t: int) -> None:
    for t in range(7, min(max_t, 9) + 1):
        identity = {(i, i) for i in range(t)}
        shift = {(i, (i + 1) % t) for i in range(t)}
        forbidden = identity | shift
        count = count_allowed(t, forbidden)
        assert count * 72 >= factorial(t)

        allowed_permutations = [
            permutation
            for permutation in permutations(range(t))
            if all((i, permutation[i]) not in forbidden for i in range(t))
        ]
        prescribed = (0, 2 % t)
        if prescribed not in forbidden:
            containing = sum(
                prescribed[1] == permutation[prescribed[0]]
                for permutation in allowed_permutations
            )
            assert containing * t <= 72 * len(allowed_permutations)


def verify_quantitative_extraction(p: int, k: int, s: int) -> None:
    n = p**k
    child_size = p ** (k - s - 1)
    step = p**s
    high_step = p ** (s + 1)

    parent_columns = {x for x in range(n) if x % step == 0}
    fixed: list[Point] = []
    layers: list[int] = []
    for x in range(n):
        if x not in parent_columns:
            fixed.append((x, x))
            layers.append(0)
        fixed.append((x, (x + 1) % n))
        layers.append(1)

    v1 = 0
    v2 = 0
    best_t1 = 0
    best_t2 = 0
    profile_count = p * p

    for xi in range(p):
        for eta in range(p):
            child = [
                (step * xi + high_step * q, step * eta + high_step * q)
                for q in range(child_size)
            ]
            for z in child:
                edges = [
                    (i, j)
                    for i, j in combinations(range(len(fixed)), 2)
                    if det(z, fixed[i], fixed[j]) == 0
                ]
                v1 += len(edges)
                matching = maximal_matching(edges)
                represented = [
                    sum(layers[i] == ell or layers[j] == ell for i, j in matching)
                    for ell in (0, 1)
                ]
                best_t1 = max(best_t1, max(represented, default=0))

            for outside in fixed:
                edges = [
                    (i, j)
                    for i, j in combinations(range(child_size), 2)
                    if det(child[i], child[j], outside) == 0
                ]
                v2 += len(edges)
                best_t2 = max(best_t2, len(maximal_matching(edges)))

    lower_t1 = v1 // (4 * profile_count * child_size * (len(fixed) - 1))
    lower_t2 = v2 // (
        2 * profile_count * len(fixed) * max(child_size - 1, 1)
    )
    assert best_t1 >= lower_t1
    assert best_t2 >= lower_t2

    print(
        "verified quantitative extraction: "
        f"p={p}, N={n}, s={s}, V1={v1}, V2={v2}, "
        f"best-t1={best_t1}, lower-t1={lower_t1}, "
        f"best-t2={best_t2}, lower-t2={lower_t2}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-t", type=int, default=20)
    parser.add_argument("--prime", type=int, default=5)
    parser.add_argument("--exponent", type=int, default=3)
    parser.add_argument("--scale", type=int, default=1)
    args = parser.parse_args()

    verify_lll(args.max_t)
    verify_small_matching_banks(args.max_t)
    verify_quantitative_extraction(args.prime, args.exponent, args.scale)


if __name__ == "__main__":
    main()
