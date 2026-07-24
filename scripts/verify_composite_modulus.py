#!/usr/bin/env python3
"""Finite checks for the composite-modulus track.

The script verifies:
- affine channels are permutations and two offsets saturate rows/columns;
- every affine modular channel has an explicit real collinear triple for N >= 5;
- the exact affine carry-determinant identity;
- the alternating-cycle decomposition of two affine layers;
- the linear vertical-displacement multiplicity obstruction;
- squarefree and prime-power unit-hyperbola line collapses;
- real collinearity always implies modular collinearity, while the converse fails;
- the mixed-projection determinant obstruction for naive CRT product channels.

These checks support the proofs in docs/27-composite-modulus-obstructions.md.
They are finite sanity checks, not proofs for arbitrary modulus.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
from math import gcd, isqrt

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    """Twice the signed Euclidean area."""
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        - (c[0] - a[0]) * (b[1] - a[1])
    )


def affine_channel(n: int, m: int, c: int) -> list[Point]:
    return [(x, (m * x + c) % n) for x in range(n)]


def affine_carries(n: int, m: int, c: int) -> list[int]:
    return [(m * x + c) // n for x in range(n)]


def affine_triple_witness(n: int, m: int, c: int) -> tuple[int, int, int]:
    """Return the constructive witness used in Theorem CMA3."""
    if n < 5 or not (0 < m < n) or not (0 <= c < n):
        raise ValueError("requires n >= 5, 0 < m < n, and 0 <= c < n")
    pts = affine_channel(n, m, c)
    differences = [pts[x + 1][1] - pts[x][1] for x in range(n - 1)]
    for x in range(n - 2):
        if differences[x] == differences[x + 1]:
            return x, x + 1, x + 2
    return 0, 2, 4


def two_layer_cycle_lengths(n: int, m: int, c0: int, c1: int) -> list[int]:
    """Alternating cycle lengths in the row-column bipartite graph."""
    inv_m = pow(m, -1, n)
    step = (inv_m * (c0 - c1)) % n
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(n):
        if start in seen:
            continue
        x = start
        count = 0
        while x not in seen:
            seen.add(x)
            count += 1
            x = (x + step) % n
        lengths.append(2 * count)
    return sorted(lengths)


def vertical_displacements(n: int, m: int, c0: int, c1: int) -> Counter[Point]:
    p0 = affine_channel(n, m, c0)
    p1 = affine_channel(n, m, c1)
    return Counter((0, p1[x][1] - p0[x][1]) for x in range(n))


def unit_hyperbola(n: int, c: int) -> list[Point]:
    if gcd(c, n) != 1:
        raise ValueError("c must be a unit")
    return [(x, (c * pow(x, -1, n)) % n) for x in range(n) if gcd(x, n) == 1]


def distinct_prime_factors(n: int) -> list[int]:
    factors: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def is_squarefree(n: int) -> bool:
    for p in distinct_prime_factors(n):
        if n % (p * p) == 0:
            return False
    return True


def odd_prime_power(n: int) -> tuple[int, int] | None:
    if n < 9:
        return None
    factors = distinct_prime_factors(n)
    if len(factors) != 1 or factors[0] == 2:
        return None
    p = factors[0]
    k = 0
    value = n
    while value % p == 0:
        value //= p
        k += 1
    return (p, k) if value == 1 and k >= 2 else None


def crt_pair(a: int, b: int, u: int, v: int) -> int:
    """Standard representative modulo n=uv for coprime u,v."""
    n = u * v
    e_u = v * pow(v, -1, u)
    e_v = u * pow(u, -1, v)
    return (a * e_u + b * e_v) % n


def crt_product_permutation(
    u: int,
    v: int,
    a_u: int,
    b_u: int,
    a_v: int,
    b_v: int,
) -> list[int]:
    n = u * v
    return [
        crt_pair((a_u * (x % u) + b_u) % u, (a_v * (x % v) + b_v) % v, u, v)
        for x in range(n)
    ]


def verify_affine(max_modulus: int) -> int:
    checks = 0
    for n in range(2, max_modulus + 1):
        for m in range(1, n):
            if gcd(m, n) != 1:
                continue
            for c in range(n):
                channel = affine_channel(n, m, c)
                assert len({x for x, _ in channel}) == n
                assert len({y for _, y in channel}) == n
                checks += 1

            c0, c1 = 0, 1
            union = affine_channel(n, m, c0) + affine_channel(n, m, c1)
            assert set(Counter(x for x, _ in union).values()) == {2}
            assert set(Counter(y for _, y in union).values()) == {2}

            expected_g = gcd(c1 - c0, n)
            expected_lengths = [2 * n // expected_g] * expected_g
            assert two_layer_cycle_lengths(n, m, c0, c1) == expected_lengths

            displacement_counts = vertical_displacements(n, m, c0, c1)
            assert sorted(displacement_counts.values()) == sorted([1, n - 1])
            assert max(displacement_counts.values()) >= (n + 1) // 2

        if n >= 5:
            for m in range(1, n):
                for c in range(n):
                    channel = affine_channel(n, m, c)
                    i, j, k = affine_triple_witness(n, m, c)
                    assert determinant(channel[i], channel[j], channel[k]) == 0
                    checks += 1

        if n <= min(max_modulus, 12):
            for m in range(1, n):
                for c in range(n):
                    channel = affine_channel(n, m, c)
                    carries = affine_carries(n, m, c)
                    for i, j, k in combinations(range(n), 3):
                        left = determinant(channel[i], channel[j], channel[k])
                        carry_det = (
                            (j - i) * (carries[k] - carries[i])
                            - (k - i) * (carries[j] - carries[i])
                        )
                        assert left == -n * carry_det
                        checks += 1
    return checks


def verify_hyperbola_collapses(max_modulus: int) -> int:
    checks = 0
    for n in range(3, max_modulus + 1, 2):
        factors = distinct_prime_factors(n)
        if len(factors) >= 2 and is_squarefree(n):
            roots = [x for x in range(n) if (x * x - 1) % n == 0]
            assert len(roots) == 2 ** len(factors)
            points = [(x, x) for x in roots]
            assert all(point in unit_hyperbola(n, 1) for point in points)
            assert all(determinant(points[0], points[1], point) == 0 for point in points[2:])
            checks += 1

    for n in range(9, max_modulus + 1):
        data = odd_prime_power(n)
        if data is None:
            continue
        p, k = data
        a = (n - 1) // 2
        c = (a * a) % n
        q = p ** ((k + 1) // 2)
        roots = [x for x in range(n) if (x - a) % q == 0]
        assert len(roots) == p ** (k // 2)
        hyperbola = set(unit_hyperbola(n, c))
        points = [(x, n - 1 - x) for x in roots]
        assert all(point in hyperbola for point in points)
        assert all(determinant(points[0], points[1], point) == 0 for point in points[2:])
        checks += 1

    power = 8
    while power <= max_modulus:
        roots = [x for x in range(power) if (x * x - 1) % power == 0]
        assert len(roots) == 4
        points = [(x, x) for x in roots]
        hyperbola = set(unit_hyperbola(power, 1))
        assert all(point in hyperbola for point in points)
        assert all(determinant(points[0], points[1], point) == 0 for point in points[2:])
        checks += 1
        power *= 2
    return checks


def verify_lifting_and_crt(max_modulus: int) -> int:
    checks = 0
    for n in range(3, max_modulus + 1):
        if n % 2:
            points = ((0, 0), (1, 2), ((n + 1) // 2, 1))
        elif n >= 4:
            points = ((0, 0), (0, 2), (n // 2, 0))
        else:
            continue
        area = determinant(*points)
        assert area != 0 and area % n == 0
        checks += 1

    for u in range(2, isqrt(max_modulus) + 2):
        for v in range(2, max_modulus // u + 1):
            if gcd(u, v) != 1:
                continue
            n = u * v
            if n > max_modulus:
                continue
            for a_u in range(1, u):
                if gcd(a_u, u) != 1:
                    continue
                for a_v in range(1, v):
                    if gcd(a_v, v) != 1:
                        continue
                    values = crt_product_permutation(u, v, a_u, 1 % u, a_v, 1 % v)
                    assert len(set(values)) == n
                    p0 = (0, values[0])
                    pu = (u, values[u])
                    pv = (v, values[v])
                    area = determinant(p0, pu, pv)
                    assert area % n == 0
                    assert p0[0] != pu[0] and p0[0] != pv[0] and pu[0] != pv[0]
                    checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=40)
    args = parser.parse_args()
    if args.max_modulus < 9:
        parser.error("--max-modulus must be at least 9")

    affine_checks = verify_affine(args.max_modulus)
    hyperbola_checks = verify_hyperbola_collapses(args.max_modulus)
    lifting_checks = verify_lifting_and_crt(args.max_modulus)

    print(
        f"verified through N={args.max_modulus}: "
        f"affine={affine_checks}, "
        f"hyperbola={hyperbola_checks}, "
        f"lifting/CRT={lifting_checks}"
    )


if __name__ == "__main__":
    main()
