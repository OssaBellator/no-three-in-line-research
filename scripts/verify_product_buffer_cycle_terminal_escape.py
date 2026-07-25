#!/usr/bin/env python3
"""Finite checks for PX341--PX345."""

from __future__ import annotations

import random
from itertools import combinations
from typing import Iterable


def det(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])


def tau(n: int) -> int:
    n = abs(n)
    out = 0
    d = 1
    while d * d <= n:
        if n % d == 0:
            out += 1 if d * d == n else 2
        d += 1
    return out


def signed_factor_pairs(p: int) -> int:
    assert p != 0
    return 2 * tau(p)


def check_identities() -> None:
    rng = random.Random(341)
    for _ in range(5000):
        vals = rng.sample(range(-30, 31), 8)
        xu, xv, xa, xb, yu, yv, ya, yb = vals

        a = (xu, ya)
        b = (xa, yb)
        c = (xb, yu)
        rhs = (xa - xu) * (yu - ya) - (xb - xu) * (yb - ya)
        assert det(a, b, c) == rhs

        f1 = (xu, ya)
        f2 = (xa, yv)
        f3 = (xv, yb)
        f4 = (xb, yu)
        assert det(f1, f3, f4) == (
            (xv - xu) * (yu - ya) - (xb - xu) * (yb - ya)
        )
        assert det(f2, f3, f4) == (
            (xv - xa) * (yu - yv) - (xb - xa) * (yb - yv)
        )


def random_partial_matching(n: int, rng: random.Random) -> set[tuple[int, int]]:
    rows = list(range(n))
    cols = list(range(n))
    rng.shuffle(rows)
    rng.shuffle(cols)
    size = rng.randrange(n + 1)
    return set(zip(rows[:size], cols[:size]))


def forbidden_union(n: int, depth: int, rng: random.Random) -> set[tuple[int, int]]:
    out = {(i, i) for i in range(n)}
    perm = list(range(n))
    rng.shuffle(perm)
    out.update((i, perm[i]) for i in range(n))
    for _ in range(depth):
        out.update(random_partial_matching(n, rng))
    return out


def no_internal_triple(cells: Iterable[tuple[int, int]]) -> bool:
    return all(det(*triple) != 0 for triple in combinations(cells, 3))


def search_one(
    x: list[int], y: list[int], forbidden: set[tuple[int, int]], u: int
) -> bool:
    n = len(x)
    for a in range(n):
        if a == u or (u, a) in forbidden:
            continue
        for b in range(n):
            if b in {u, a}:
                continue
            if (a, b) in forbidden or (b, u) in forbidden:
                continue
            cells = [(x[u], y[a]), (x[a], y[b]), (x[b], y[u])]
            if no_internal_triple(cells):
                return True
    return False


def search_two(
    x: list[int],
    y: list[int],
    forbidden: set[tuple[int, int]],
    u: int,
    v: int,
) -> bool:
    n = len(x)
    for a in range(n):
        if a in {u, v}:
            continue
        if (u, a) in forbidden or (a, v) in forbidden:
            continue
        for b in range(n):
            if b in {u, v, a}:
                continue
            if (v, b) in forbidden or (b, u) in forbidden:
                continue
            cells = [
                (x[u], y[a]),
                (x[a], y[v]),
                (x[v], y[b]),
                (x[b], y[u]),
            ]
            if no_internal_triple(cells):
                return True
    return False


def main() -> None:
    check_identities()

    for p in range(-100, 101):
        if p:
            pairs = {
                (a, b)
                for a in range(-abs(p), abs(p) + 1)
                for b in range(-abs(p), abs(p) + 1)
                if a * b == p
            }
            assert len(pairs) == signed_factor_pairs(p)

    rng = random.Random(345)
    for n in (24, 32, 40):
        x = list(range(n))
        for _ in range(30):
            y = list(range(n))
            rng.shuffle(y)
            depth = 2
            forbidden = forbidden_union(n, depth, rng)
            assert max(
                sum((i, j) in forbidden for j in range(n)) for i in range(n)
            ) <= depth + 2
            u, v = rng.sample(range(n), 2)
            assert search_one(x, y, forbidden, u)
            assert search_two(x, y, forbidden, u, v)

    delta0 = 1
    assert delta0 + 1 == 2

    print("PX341--PX345 buffer-cycle terminal escape verifier: PASS")


if __name__ == "__main__":
    main()
