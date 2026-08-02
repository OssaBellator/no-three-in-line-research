#!/usr/bin/env python3
"""Checks for PX330--PX335."""

from itertools import combinations, permutations
from math import log
import random


def falling(n: int, r: int) -> int:
    out = 1
    for k in range(r):
        out *= n - k
    return out


def support_shape(arcs: tuple[tuple[int, int], ...]) -> str:
    vertices = set()
    out = {}
    indeg = {}
    for u, v in arcs:
        vertices.update((u, v))
        out[u] = v
        indeg[v] = u
    assert len(vertices) == 4
    two_cycles = sum(out.get(v) == u for u, v in arcs) // 2
    if two_cycles == 1:
        return "two_cycle_arc"
    starts = [v for v in vertices if v not in indeg and v in out]
    assert len(starts) == 1
    u = starts[0]
    length = 0
    while u in out:
        u = out[u]
        length += 1
    assert length == 3
    return "path"


def classify(n: int) -> None:
    counts = {"path": 0, "two_cycle_arc": 0}
    labels = range(n)
    for rows in combinations(labels, 3):
        for cols in combinations(labels, 3):
            for perm in permutations(cols):
                arcs = tuple(zip(rows, perm))
                if any(u == v for u, v in arcs):
                    continue
                support = {x for arc in arcs for x in arc}
                if len(support) == 4:
                    counts[support_shape(arcs)] += 1
    assert counts["path"] == falling(n, 4)
    assert counts["two_cycle_arc"] == falling(n, 4) // 2


def collinear(p, q, r) -> bool:
    return (q[0] - p[0]) * (r[1] - p[1]) == (q[1] - p[1]) * (r[0] - p[0])


def geometric_check(n: int, rng: random.Random) -> None:
    xs = sorted(rng.sample(range(1, 100), n))
    ys = sorted(rng.sample(range(101, 250), n))
    count = 0
    labels = range(n)
    for rows in combinations(labels, 3):
        for cols in combinations(labels, 3):
            for perm in permutations(cols):
                arcs = tuple(zip(rows, perm))
                if any(u == v for u, v in arcs):
                    continue
                if len({x for arc in arcs for x in arc}) != 4:
                    continue
                pts = [(xs[u], ys[v]) for u, v in arcs]
                if collinear(*pts):
                    count += 1
    assert 2 * count <= 3 * falling(n, 3)


def hybrid_check() -> None:
    for exponent in (6, 9, 12, 15):
        x = 10.0 ** exponent
        bound = x ** (-1.0 / 3.0) * log(2.0 * x)
        for k in range(1001):
            t = 1.0 + (x - 1.0) * k / 1000.0
            q = min(t ** -0.5, t / x)
            assert q * log(2.0 * t) <= 1.000001 * bound
            assert q * q * log(2.0 * t) <= q * log(2.0 * t)


def main() -> None:
    for n in range(4, 9):
        classify(n)
    rng = random.Random(141)
    for n in range(4, 9):
        for _ in range(100):
            geometric_check(n, rng)
    hybrid_check()
    print("PX330--PX335 rank-three support-four verifier: PASS")


if __name__ == "__main__":
    main()
