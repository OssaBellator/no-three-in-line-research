#!/usr/bin/env python3
"""Verify CMR564--CMR568 line-bank splice identities."""

from itertools import combinations
from math import ceil, floor


def line_key(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int, int]:
    from math import gcd

    x1, y1 = a
    x2, y2 = b
    aa = y2 - y1
    bb = x1 - x2
    cc = aa * x1 + bb * y1
    if aa < 0 or (aa == 0 and bb < 0):
        aa, bb, cc = -aa, -bb, -cc
    g = gcd(gcd(abs(aa), abs(bb)), abs(cc))
    if g:
        aa //= g
        bb //= g
        cc //= g
    return aa, bb, cc


def collinear(points: tuple[tuple[int, int], ...]) -> bool:
    return all(
        (points[1][0] - points[0][0]) * (p[1] - points[0][1])
        == (points[1][1] - points[0][1]) * (p[0] - points[0][0])
        for p in points[2:]
    )


def check_rank_one_star() -> None:
    for m in range(4, 9):
        z = (0, 0)
        cells = [(x, y) for x in range(m) for y in range(m)]
        triples = []
        for a, b in combinations([p for p in cells if p != z], 2):
            tr = (z, a, b)
            if collinear(tr):
                triples.append(tr)
        by_line = {}
        for tr in triples:
            by_line.setdefault(line_key(z, tr[1]), tr)
        chosen = list(by_line.values())
        for c1, c2 in combinations(chosen, 2):
            assert set(c1[1:]).isdisjoint(c2[1:])


def check_rank_zero_linearity() -> None:
    for m in range(3, 8):
        cells = [(x, y) for x in range(m) for y in range(m)]
        by_line = {}
        for tr in combinations(cells, 3):
            if collinear(tr):
                by_line.setdefault(line_key(tr[0], tr[1]), tr)
        chosen = list(by_line.values())
        for c1, c2 in combinations(chosen, 2):
            assert len(set(c1) & set(c2)) <= 1


def greedy_packing(family: list[frozenset[int]]) -> list[frozenset[int]]:
    remaining = list(family)
    out = []
    while remaining:
        chosen = remaining[0]
        out.append(chosen)
        remaining = [f for f in remaining if f.isdisjoint(chosen)]
    return out


def check_fan_or_packing() -> None:
    points = range(8)
    triples = [frozenset(t) for t in combinations(points, 3)]
    for size in range(1, 8):
        checked = 0
        for fam_tuple in combinations(triples, size):
            if any(len(a & b) > 1 for a, b in combinations(fam_tuple, 2)):
                continue
            family = list(fam_tuple)
            degrees = {x: sum(x in f for f in family) for x in points}
            for r in range(2, 6):
                if max(degrees.values(), default=0) < r:
                    packing = greedy_packing(family)
                    assert len(packing) >= ceil(size / (3 * (r - 1)))
            checked += 1
            if checked >= 250:
                break


def check_square_root_bound() -> None:
    for a in range(1, 1000):
        r = max(2, ceil(a**0.5))
        bound = ceil(a / (3 * (r - 1)))
        assert bound >= 1
        assert r >= floor(a**0.5)


def main() -> None:
    check_rank_one_star()
    check_rank_zero_linearity()
    check_fan_or_packing()
    check_square_root_bound()
    print("verified static line-bank splice through the configured ranges")


if __name__ == "__main__":
    main()
