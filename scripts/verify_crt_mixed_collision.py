#!/usr/bin/env python3
"""Verify CMCRT2 and CMCRT3 on finite coprime moduli."""
from __future__ import annotations

import argparse
from itertools import combinations
from math import gcd


def crt_pair(a: int, b: int, u: int, v: int) -> int:
    n = u * v
    return (
        a * v * pow(v, -1, u)
        + b * u * pow(u, -1, v)
    ) % n


def crt_permutation(u: int, v: int, fu: list[int], fv: list[int]) -> list[int]:
    n = u * v
    return [crt_pair(fu[x % u], fv[x % v], u, v) for x in range(n)]


def determinant(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])


def vector_det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def verify_pair(u: int, v: int) -> tuple[int, int]:
    assert gcd(u, v) == 1
    n = u * v
    fu0 = [(x + 1) % u for x in range(u)]
    fu1 = [(x + 2) % u for x in range(u)]
    fv0 = [(2 * x + 1) % v for x in range(v)]
    # Choose a unit slope distinct from the first layer at every column.
    slope = next(s for s in range(1, v) if gcd(s, v) == 1 and s != 2 % v)
    fv1 = [(slope * x + 2) % v for x in range(v)]
    # Repair the rare accidental local equality by using two translations when needed.
    if any(fv0[x] == fv1[x] for x in range(v)):
        fv1 = [(2 * x + 2) % v for x in range(v)]
    assert sorted(fu0) == list(range(u))
    assert sorted(fu1) == list(range(u))
    assert sorted(fv0) == list(range(v))
    assert sorted(fv1) == list(range(v))
    assert all(fu0[x] != fu1[x] for x in range(u))
    assert all(fv0[x] != fv1[x] for x in range(v))

    f0 = crt_permutation(u, v, fu0, fv0)
    f1 = crt_permutation(u, v, fu1, fv1)
    assert sorted(f0) == list(range(n))
    assert sorted(f1) == list(range(n))
    assert all(f0[x] != f1[x] for x in range(n))

    points = [(x, f0[x]) for x in range(n)] + [(x, f1[x]) for x in range(n)]
    factor_checks = 0
    real_mixed = 0
    for p0, p1, p2 in combinations(points, 3):
        # Check every orientation that has a u-collision and a v-collision at p0.
        for base, pu, pv in ((p0, p1, p2), (p1, p0, p2), (p2, p0, p1)):
            if not all((pu[i] - base[i]) % u == 0 for i in (0, 1)):
                continue
            if not all((pv[i] - base[i]) % v == 0 for i in (0, 1)):
                continue
            avec = ((pu[0] - base[0]) // u, (pu[1] - base[1]) // u)
            bvec = ((pv[0] - base[0]) // v, (pv[1] - base[1]) // v)
            full = determinant(base, pu, pv)
            assert full == n * vector_det(avec, bvec)
            if full == 0:
                assert vector_det(avec, bvec) == 0
                real_mixed += 1
            factor_checks += 1
    return factor_checks, real_mixed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-modulus", type=int, default=60)
    args = parser.parse_args()

    instances = 0
    factors = 0
    real_mixed = 0
    for u in range(3, args.max_modulus + 1):
        for v in range(3, args.max_modulus // u + 1):
            if gcd(u, v) != 1 or u * v > args.max_modulus:
                continue
            # The affine test pairs require 2 to be a unit modulo v.
            if gcd(2, v) != 1:
                continue
            f, r = verify_pair(u, v)
            factors += f
            real_mixed += r
            instances += 1
    print(
        f"verified CRT instances={instances}; mixed factorizations={factors}; "
        f"real mixed triples={real_mixed}"
    )


if __name__ == "__main__":
    main()
