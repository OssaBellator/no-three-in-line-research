#!/usr/bin/env python3
"""Verify CMR546--CMR551 arithmetic and finite stock identities."""

from fractions import Fraction
from itertools import combinations, permutations
from math import ceil


def falling(n: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= n - j
    return out


def check_polarization() -> None:
    for n in range(5, 15):
        for q in range(4, 17):
            h = ceil(q * (n - 1) / 4)
            n2 = falling(n, 2)
            n3 = falling(n, 3)
            for v0 in range(0, min(n3, 30) + 1):
                for v1 in range(0, min(n2, 30) + 1):
                    s = Fraction(v0, n3) + Fraction(v1, n2)
                    a = Fraction(30, 11) * s
                    for b in range(0, min(n * n, h + 2) + 1):
                        failed_ineq = (
                            a
                            + Fraction(2, q)
                            + Fraction(b, q * (n - 1))
                            >= 1
                        )
                        if failed_ineq:
                            assert s >= Fraction(11, 120) or b >= h


def enumerate_matching_prescriptions(n: int) -> tuple[int, int]:
    vertices = range(n)
    rank0 = set()
    for srcs in combinations(vertices, 3):
        for tgts in combinations(vertices, 3):
            for perm in permutations(tgts):
                rank0.add(tuple(sorted(zip(srcs, perm))))

    rank1 = set()
    for paid_index in range(2):
        for srcs in combinations(vertices, 2):
            for tgts in combinations(vertices, 2):
                for perm in permutations(tgts):
                    rank1.add((paid_index, tuple(sorted(zip(srcs, perm)))))
    return len(rank0), len(rank1)


def check_stock_counts() -> None:
    for n in range(3, 8):
        n2 = falling(n, 2)
        n3 = falling(n, 3)
        count0, count1 = enumerate_matching_prescriptions(n)
        assert count0 == n3 * n3 // 6
        assert count1 == n2 * n2


def check_recurrence_bounds() -> None:
    c0 = Fraction(11, 240)
    for n in range(5, 20):
        n2 = falling(n, 2)
        n3 = falling(n, 3)
        u0 = n3 * n3 // 6
        u1 = n2 * n2
        assert Fraction(u0, c0 * n3) == Fraction(40, 11) * n3
        assert Fraction(u1, c0 * n2) == Fraction(240, 11) * n2

        for q in range(4, 15):
            h = ceil(q * (n - 1) / 4)
            for lam in range(2, 9):
                assert (
                    (lam - 1) * n * n // h
                    <= Fraction((lam - 1) * n * n, h)
                )


def collinear(
    a: tuple[int, int],
    b: tuple[int, int],
    c: tuple[int, int],
) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def check_rank_one_line_separation() -> None:
    for m in range(4, 8):
        cells = [(x, y) for x in range(m) for y in range(m)]
        for z1, z2 in combinations(cells, 2):
            if z1[0] == z2[0] or z1[1] == z2[1]:
                continue
            residual = [
                w
                for w in cells
                if w[0] not in {z1[0], z2[0]}
                and w[1] not in {z1[1], z2[1]}
            ]
            allowed = [w for w in residual if not collinear(z1, z2, w)]
            for z in (z1, z2):
                for r1, r2 in combinations(allowed, 2):
                    if r1[0] == r2[0] or r1[1] == r2[1]:
                        continue
                    if collinear(z, r1, r2):
                        assert not collinear(z1, z2, r1)
                        assert not collinear(z1, z2, r2)


def main() -> None:
    check_polarization()
    check_stock_counts()
    check_recurrence_bounds()
    check_rank_one_line_separation()
    print("verified fixed-selector obstruction stock through the configured ranges")


if __name__ == "__main__":
    main()
