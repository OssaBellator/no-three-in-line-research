#!/usr/bin/env python3
"""Finite checks for carry-filtered alternating-closure lemmas.

Checks:
- same-channel cross-carry factorization and divisor bounds;
- scalar-lift wrap determinant criterion;
- nondegenerate carry cells contain at most two hyperbola points;
- degenerate cells have the claimed common rational center.

This is a finite sanity check, not a proof for arbitrary p.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from math import gcd, isqrt

Point = tuple[int, int]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def inv(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def hpoint(c: int, x: int, p: int) -> Point:
    return (x, c * inv(x, p) % p)


def det3(p0: Point, p1: Point, p2: Point) -> int:
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (
        p2[0] - p0[0]
    ) * (p1[1] - p0[1])


def tau(n: int) -> int:
    n = abs(n)
    if n == 0:
        raise ValueError("tau(0) is undefined")
    count = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            count += 1 if d * d == n else 2
        d += 1
    return count


def secant_involution(x: int, z: int, ratio: int, p: int) -> int | None:
    denominator = (ratio * x - z) % p
    if denominator == 0:
        return None
    return z * (x - z) * inv(denominator, p) % p


def carry_vector(alpha: int, point: Point, p: int) -> Point:
    return (alpha * point[0] // p, alpha * point[1] // p)


def lifted_multiple(alpha: int, point: Point, p: int) -> Point:
    return (alpha * point[0] % p, alpha * point[1] % p)


def det2(a: Point, b: Point) -> int:
    return a[0] * b[1] - a[1] * b[0]


def check_same_channel(p: int) -> None:
    for a in range(1, p):
        for b in range(1, p):
            if a == b:
                continue
            ratio = b * inv(a, p) % p
            for z in range(1, p):
                anchor = hpoint(b, z, p)
                oriented: dict[int, list[int]] = defaultdict(list)
                real_edges: dict[int, set[tuple[int, int]]] = defaultdict(set)

                for x in range(1, p):
                    u = secant_involution(x, z, ratio, p)
                    if u is None or u == 0 or u == x:
                        continue

                    partner_row = hpoint(a, u, p)[1]
                    cross_product = (x - z) * (partner_row - anchor[1])
                    assert (cross_product - (b - a)) % p == 0
                    carry = (cross_product - (b - a)) // p
                    oriented[carry].append(x)

                    if det3(anchor, hpoint(a, x, p), hpoint(a, u, p)) == 0:
                        reverse_product = (u - z) * (
                            hpoint(a, x, p)[1] - anchor[1]
                        )
                        assert reverse_product == cross_product
                        real_edges[carry].add(tuple(sorted((x, u))))

                for carry, parameters in oriented.items():
                    level = b - a + p * carry
                    assert level != 0
                    assert len(parameters) <= 2 * tau(level)

                for carry, edges in real_edges.items():
                    level = b - a + p * carry
                    assert len(edges) <= tau(level)


def check_wrap_cells(p: int) -> None:
    for c in range(1, p):
        channel = [hpoint(c, x, p) for x in range(1, p)]

        for alpha in range(2, p):
            for beta in range(2, p):
                if beta == alpha:
                    continue

                groups: dict[
                    tuple[Point, Point], list[tuple[Point, bool]]
                ] = defaultdict(list)

                for point in channel:
                    carry_a = carry_vector(alpha, point, p)
                    carry_b = carry_vector(beta, point, p)
                    point_a = lifted_multiple(alpha, point, p)
                    point_b = lifted_multiple(beta, point, p)

                    left = p * det2(carry_a, carry_b)
                    right = (alpha - 1) * det2(point, carry_b) - (
                        beta - 1
                    ) * det2(point, carry_a)
                    collinear = det3(point, point_a, point_b) == 0
                    assert collinear == (left == right)
                    groups[(carry_a, carry_b)].append((point, collinear))

                common_divisor = gcd(alpha - 1, beta - 1)
                alpha_reduced = (alpha - 1) // common_divisor
                beta_reduced = (beta - 1) // common_divisor

                for (carry_a, carry_b), items in groups.items():
                    coefficient = (
                        (alpha - 1) * carry_b[0]
                        - (beta - 1) * carry_a[0],
                        (alpha - 1) * carry_b[1]
                        - (beta - 1) * carry_a[1],
                    )
                    degenerate = coefficient == (0, 0)

                    if not degenerate:
                        assert sum(collinear for _, collinear in items) <= 2
                        continue

                    assert det2(carry_a, carry_b) == 0
                    assert all(collinear for _, collinear in items)
                    assert carry_a[0] % alpha_reduced == 0
                    assert carry_a[1] % alpha_reduced == 0
                    center_index = (
                        carry_a[0] // alpha_reduced,
                        carry_a[1] // alpha_reduced,
                    )
                    assert carry_b == (
                        beta_reduced * center_index[0],
                        beta_reduced * center_index[1],
                    )
                    assert 0 <= center_index[0] <= common_divisor
                    assert 0 <= center_index[1] <= common_divisor

                    for point, _ in items:
                        point_a = lifted_multiple(alpha, point, p)
                        point_b = lifted_multiple(beta, point, p)
                        base = (
                            common_divisor * point[0]
                            - p * center_index[0],
                            common_divisor * point[1]
                            - p * center_index[1],
                        )
                        vector_a = (
                            common_divisor * (point_a[0] - point[0]),
                            common_divisor * (point_a[1] - point[1]),
                        )
                        vector_b = (
                            common_divisor * (point_b[0] - point[0]),
                            common_divisor * (point_b[1] - point[1]),
                        )
                        assert vector_a == (
                            (alpha - 1) * base[0],
                            (alpha - 1) * base[1],
                        )
                        assert vector_b == (
                            (beta - 1) * base[0],
                            (beta - 1) * base[1],
                        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=17)
    args = parser.parse_args()

    if not is_prime(args.prime) or args.prime == 2:
        parser.error("--prime must be an odd prime")

    check_same_channel(args.prime)
    check_wrap_cells(args.prime)
    print(f"p={args.prime}: carry-closure checks passed")


if __name__ == "__main__":
    main()
