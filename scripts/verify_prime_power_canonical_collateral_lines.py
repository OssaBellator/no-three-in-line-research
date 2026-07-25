#!/usr/bin/env python3
"""Verify CMR558--CMR563 line decomposition and packing identities."""

from itertools import combinations
from math import ceil, comb, gcd, sqrt


Cell = tuple[int, int]


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def line_key(a: Cell, b: Cell) -> tuple[int, int, int]:
    x1, y1 = a
    x2, y2 = b
    aa = y2 - y1
    bb = x1 - x2
    cc = -(aa * x1 + bb * y1)
    g = gcd(gcd(abs(aa), abs(bb)), abs(cc))
    if g:
        aa //= g
        bb //= g
        cc //= g
    if aa < 0 or (aa == 0 and bb < 0) or (aa == bb == 0 and cc < 0):
        aa, bb, cc = -aa, -bb, -cc
    return aa, bb, cc


def canonical_allowed(m: int, z1: Cell, z2: Cell) -> list[Cell]:
    rows = [x for x in range(m) if x not in {z1[0], z2[0]}]
    cols = [y for y in range(m) if y not in {z1[1], z2[1]}]

    trace: list[Cell] = []
    used_rows: set[int] = set()
    used_cols: set[int] = set()
    for x in rows:
        for y in cols:
            w = (x, y)
            if collinear(z1, z2, w):
                trace.append(w)
                used_rows.add(x)
                used_cols.add(y)

    assert len(trace) == len(used_rows) == len(used_cols)
    rem_rows = [x for x in rows if x not in used_rows]
    rem_cols = [y for y in cols if y not in used_cols]
    forbidden = set(trace) | set(zip(rem_rows, rem_cols))
    return [(x, y) for x in rows for y in cols if (x, y) not in forbidden]


def compatible(points: tuple[Cell, ...]) -> bool:
    return (
        len({p[0] for p in points}) == len(points)
        and len({p[1] for p in points}) == len(points)
    )


def maximal_disjoint(triples: list[tuple[Cell, Cell, Cell]]) -> list[tuple[Cell, Cell, Cell]]:
    chosen: list[tuple[Cell, Cell, Cell]] = []
    used: set[Cell] = set()
    for triple in triples:
        if used.isdisjoint(triple):
            chosen.append(triple)
            used.update(triple)
    return chosen


def check_pair(m: int, z1: Cell, z2: Cell) -> None:
    n = m - 2
    allowed = canonical_allowed(m, z1, z2)
    paid_line = line_key(z1, z2)

    rank0: list[tuple[Cell, Cell, Cell]] = []
    for triple in combinations(allowed, 3):
        if compatible(triple) and collinear(*triple):
            rank0.append(triple)

    rank1: dict[Cell, list[tuple[Cell, Cell]]] = {z1: [], z2: []}
    for z in (z1, z2):
        for pair in combinations(allowed, 2):
            if compatible(pair) and collinear(z, *pair):
                rank1[z].append(pair)

    groups0: dict[tuple[int, int, int], list[tuple[Cell, Cell, Cell]]] = {}
    for triple in rank0:
        key = line_key(triple[0], triple[1])
        assert all(line_key(triple[0], p) == key for p in triple[1:])
        groups0.setdefault(key, []).append(triple)
    assert sum(len(v) for v in groups0.values()) == len(rank0)

    for triples in groups0.values():
        points = {p for triple in triples for p in triple}
        assert len(points) <= n
        assert len(triples) <= comb(len(points), 3)

    for z, pairs in rank1.items():
        groups1: dict[tuple[int, int, int], list[tuple[Cell, Cell]]] = {}
        for pair in pairs:
            key = line_key(z, pair[0])
            assert key != paid_line
            assert line_key(z, pair[1]) == key
            groups1.setdefault(key, []).append(pair)
        assert sum(len(v) for v in groups1.values()) == len(pairs)

        chosen_pairs: list[tuple[Cell, Cell]] = []
        for line_pairs in groups1.values():
            points = {p for pair in line_pairs for p in pair}
            assert len(points) <= n
            assert len(line_pairs) <= comb(len(points), 2)
            chosen_pairs.append(line_pairs[0])

        for a, b in combinations(chosen_pairs, 2):
            assert set(a).isdisjoint(b)

    selected = [triples[0] for triples in groups0.values()]
    for s in range(2, min(6, len(selected) + 2)):
        packing = maximal_disjoint(selected)
        if len(packing) < s and selected:
            cover = {p for triple in packing for p in triple}
            assert all(not cover.isdisjoint(triple) for triple in selected)
            maximum_degree = max(
                sum(p in triple for triple in selected)
                for p in cover
            )
            assert maximum_degree >= ceil(len(selected) / (3 * (s - 1)))

            heavy = max(
                cover,
                key=lambda p: sum(p in triple for triple in selected),
            )
            through = [triple for triple in selected if heavy in triple]
            for a, b in combinations(through, 2):
                assert (set(a) - {heavy}).isdisjoint(set(b) - {heavy})


def check_sqrt_extraction() -> None:
    for weight in range(1, 10000):
        h = ceil(sqrt(weight))
        if h >= 2:
            assert ceil(weight / (h - 1)) >= h


def main() -> None:
    total = 0
    for m in range(5, 8):
        cells = [(x, y) for x in range(m) for y in range(m)]
        for z1, z2 in combinations(cells, 2):
            if z1[0] == z2[0] or z1[1] == z2[1]:
                continue
            check_pair(m, z1, z2)
            total += 1

    check_sqrt_extraction()
    print(
        "verified canonical collateral line decomposition for "
        f"{total} compatible paid pairs through side seven"
    )


if __name__ == "__main__":
    main()
