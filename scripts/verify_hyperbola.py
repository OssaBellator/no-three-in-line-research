#!/usr/bin/env python3
"""Small-instance checks for modular-hyperbola claims.

This script verifies, for a chosen prime p:
- H_c is a permutation graph;
- H_a union H_b has exactly two points per row/column;
- each real line meets one H_c in at most two points;
- each real line meets H_a union H_b in at most four points;
- exact displacement multiplicity between H_c and H_d is at most two;
- triple syndrome counts for all channel pairs.

This is a finite sanity check, not a proof for arbitrary p.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations
from math import gcd

Point = tuple[int, int]


def inv(x: int, p: int) -> int:
    return pow(x, p - 2, p)


def hyperbola(c: int, p: int) -> list[Point]:
    return [(x, (c * inv(x, p)) % p) for x in range(1, p)]


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = A * x1 + B * y1
    g = gcd(gcd(abs(A), abs(B)), abs(C))
    if g:
        A, B, C = A // g, B // g, C // g
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def line_occupancies(points: list[Point]) -> dict[tuple[int, int, int], set[Point]]:
    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for a, b in combinations(points, 2):
        k = line_key(a, b)
        lines[k].add(a)
        lines[k].add(b)
    return lines


def displacement_multiplicity(P: list[Point], Q: list[Point]) -> Counter[tuple[int, int]]:
    out: Counter[tuple[int, int]] = Counter()
    qset = set(Q)
    for x, y in P:
        for u, v in Q:
            if (x, y) != (u, v):
                out[(u - x, v - y)] += 1
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--prime', type=int, default=17)
    args = ap.parse_args()
    p = args.prime
    channels = {c: hyperbola(c, p) for c in range(1, p)}

    for c, pts in channels.items():
        assert len({x for x, _ in pts}) == p - 1
        assert len({y for _, y in pts}) == p - 1
        mx = max((len(v) for v in line_occupancies(pts).values()), default=1)
        assert mx <= 2, (c, mx)

    best = None
    for a in range(1, p):
        for b in range(a + 1, p):
            pts = channels[a] + channels[b]
            rows = Counter(y for _, y in pts)
            cols = Counter(x for x, _ in pts)
            assert set(rows.values()) == {2}
            assert set(cols.values()) == {2}
            lines = line_occupancies(pts)
            max_line = max((len(v) for v in lines.values()), default=1)
            assert max_line <= 4, (a, b, max_line)
            syndrome = sum(len(v) * (len(v)-1) * (len(v)-2) // 6 for v in lines.values())
            if best is None or syndrome < best[0]:
                best = (syndrome, a, b, max_line)

    for c in range(1, p):
        for d in range(1, p):
            mult = displacement_multiplicity(channels[c], channels[d])
            if mult:
                assert max(mult.values()) <= 2, (c, d, max(mult.values()))

    print(f'p={p}; best pair syndrome={best[0]} at a={best[1]}, b={best[2]}; max line={best[3]}')


if __name__ == '__main__':
    main()
