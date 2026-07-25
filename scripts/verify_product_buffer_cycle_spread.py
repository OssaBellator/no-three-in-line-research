#!/usr/bin/env python3
"""Finite checks for PX346--PX350."""

from __future__ import annotations

import random
from collections import Counter
from itertools import combinations


def det(p: tuple[int, int], q: tuple[int, int], r: tuple[int, int]) -> int:
    return (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1])


def no_internal_triple(cells: list[tuple[int, int]]) -> bool:
    return all(det(*triple) != 0 for triple in combinations(cells, 3))


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


def bank_one(
    x: list[int], y: list[int], forbidden: set[tuple[int, int]], u: int
) -> list[tuple[int, int]]:
    n = len(x)
    out = []
    for a in range(n):
        if (u, a) in forbidden:
            continue
        for b in range(n):
            if b in {u, a}:
                continue
            if (a, b) in forbidden or (b, u) in forbidden:
                continue
            cells = [(x[u], y[a]), (x[a], y[b]), (x[b], y[u])]
            if no_internal_triple(cells):
                out.append((a, b))
    return out


def bank_two(
    x: list[int],
    y: list[int],
    forbidden: set[tuple[int, int]],
    u: int,
    v: int,
) -> list[tuple[int, int]]:
    n = len(x)
    out = []
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
                out.append((a, b))
    return out


def check_spread(bank: list[tuple[int, int]]) -> None:
    assert bank
    first = Counter(a for a, _ in bank)
    second = Counter(b for _, b in bank)
    pair = Counter(bank)
    assert max(first.values()) <= len({b for _, b in bank})
    assert max(second.values()) <= len({a for a, _ in bank})
    assert max(pair.values()) == 1

    rng = random.Random(len(bank))
    wa = {a: rng.randrange(6) for a in first}
    wb = {b: rng.randrange(6) for b in second}
    wab = {p: rng.randrange(6) for p in pair}
    direct = sum(wa[a] + wb[b] + wab[(a, b)] for a, b in bank) / len(bank)
    expanded = (
        sum(wa[a] * count for a, count in first.items())
        + sum(wb[b] * count for b, count in second.items())
        + sum(wab[p] * count for p, count in pair.items())
    ) / len(bank)
    assert direct == expanded


def main() -> None:
    templates = {
        tuple(sorted(("P", "P"))),
        tuple(sorted(("P", "H"))),
    }
    assert len(templates) == 2

    rng = random.Random(350)
    for n in (20, 28, 36):
        x = list(range(n))
        for _ in range(20):
            y = list(range(n))
            rng.shuffle(y)
            forbidden = forbidden_union(n, 1, rng)
            u, v = rng.sample(range(n), 2)
            one = bank_one(x, y, forbidden, u)
            two = bank_two(x, y, forbidden, u, v)
            assert one and two
            check_spread(one)
            check_spread(two)

    for n in range(20, 101):
        delta = 3
        dcap = 1
        if n >= 4 * delta + 10 + 8 * dcap:
            assert (n - delta) * (n - 2 * delta - 2 - 2 * dcap) >= n * n // 4
            assert (n - 2 * delta - 2) * (
                n - 2 * delta - 5 - 4 * dcap
            ) >= n * n // 4

    print("PX346--PX350 buffer-cycle spread verifier: PASS")


if __name__ == "__main__":
    main()
