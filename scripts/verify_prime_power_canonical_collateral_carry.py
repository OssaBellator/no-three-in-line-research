#!/usr/bin/env python3
"""Verify CMR574--CMR580 energy, height, and carry-splice arithmetic."""

from itertools import combinations
from math import ceil, comb, floor, gcd, log2


Cell = tuple[int, int]
Line = tuple[int, int, int]


def falling(n: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= n - j
    return out


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def line_key(a: Cell, b: Cell) -> Line:
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


def primitive_height(line: Line) -> int:
    aa, bb, _ = line
    return max(abs(aa), abs(bb))


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


def check_profile(m: int, z1: Cell, z2: Cell) -> None:
    n = m - 2
    allowed = canonical_allowed(m, z1, z2)
    paid_line = line_key(z1, z2)

    rank0: dict[Line, int] = {}
    cells0: dict[Line, set[Cell]] = {}
    for triple in combinations(allowed, 3):
        if compatible(triple) and collinear(*triple):
            line = line_key(triple[0], triple[1])
            rank0[line] = rank0.get(line, 0) + 1
            cells0.setdefault(line, set()).update(triple)

    rank1: dict[Cell, dict[Line, int]] = {z1: {}, z2: {}}
    cells1: dict[Cell, dict[Line, set[Cell]]] = {z1: {}, z2: {}}
    for z in (z1, z2):
        for pair in combinations(allowed, 2):
            if compatible(pair) and collinear(z, *pair):
                line = line_key(z, pair[0])
                assert line != paid_line
                rank1[z][line] = rank1[z].get(line, 0) + 1
                cells1[z].setdefault(line, set()).update(pair)

    v0 = sum(rank0.values())
    energy0 = sum(falling(len(cells0[line]), 3) for line in rank0)
    assert energy0 >= 6 * v0

    for z in (z1, z2):
        v1 = sum(rank1[z].values())
        energy1 = sum(falling(len(cells1[z][line]), 2) for line in rank1[z])
        assert energy1 >= 2 * v1

    band_count = ceil(log2(m))
    if v0:
        band_mass: dict[int, int] = {}
        for line, atoms in rank0.items():
            height = primitive_height(line)
            band = 1 << (height.bit_length() - 1)
            band_mass[band] = band_mass.get(band, 0) + atoms
            qh = 1 + floor((m - 1) / band)
            assert len(cells0[line]) <= qh
        assert max(band_mass.values()) * band_count >= v0

    for z in (z1, z2):
        v1 = sum(rank1[z].values())
        if not v1:
            continue
        band_mass: dict[int, int] = {}
        for line, atoms in rank1[z].items():
            height = primitive_height(line)
            band = 1 << (height.bit_length() - 1)
            band_mass[band] = band_mass.get(band, 0) + atoms
            qh = 1 + floor((m - 1) / band)
            assert len(cells1[z][line]) <= qh
        assert max(band_mass.values()) * band_count >= v1

    for line, points in cells0.items():
        r = len(points)
        if r >= 2:
            assert primitive_height(line) * (r - 1) <= m - 1
    for z in (z1, z2):
        for line, points in cells1[z].items():
            r = len(points)
            if r >= 2:
                assert primitive_height(line) * (r - 1) <= m - 1


def check_occupancy_constants() -> None:
    for m in range(20, 250):
        n = m - 2
        h = 1
        while h < m:
            qh = 1 + floor((m - 1) / h)
            if qh >= 3:
                assert (
                    comb(qh, 3) / falling(n, 3)
                    < 11 / (10 * h**3)
                )
            h *= 2

    for m in range(7, 250):
        n = m - 2
        h = 1
        while h < m:
            qh = 1 + floor((m - 1) / h)
            if qh >= 2:
                assert comb(qh, 2) / falling(n, 2) <= 4 / h**2
            h *= 2


def check_threshold_arithmetic() -> None:
    for q in range(4, 30):
        cq = 11 / 30 * (1 - 2 / q)
        assert cq >= 11 / 60
        for n in range(5, 100):
            rank0 = cq * falling(n, 3) / 2
            rank1 = cq * falling(n, 2) / 4
            assert 6 * rank0 >= 3 * cq * falling(n, 3)
            assert 2 * rank1 >= cq * falling(n, 2) / 2


def main() -> None:
    total = 0
    for m in range(5, 8):
        cells = [(x, y) for x in range(m) for y in range(m)]
        for z1, z2 in combinations(cells, 2):
            if z1[0] == z2[0] or z1[1] == z2[1]:
                continue
            check_profile(m, z1, z2)
            total += 1

    check_occupancy_constants()
    check_threshold_arithmetic()
    print(
        "verified canonical collateral carry splice for "
        f"{total} compatible paid pairs and the configured arithmetic ranges"
    )


if __name__ == "__main__":
    main()
