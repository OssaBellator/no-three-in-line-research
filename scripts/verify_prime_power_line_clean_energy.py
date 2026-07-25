#!/usr/bin/env python3
"""Exact and arithmetic checks for CMR351--CMR354."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import comb


def line_key(points: tuple[tuple[int, int], ...]) -> tuple[int, int, int]:
    (x1, y1), (x2, y2) = points[:2]
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    from math import gcd

    common = gcd(gcd(abs(a), abs(b)), abs(c))
    if common:
        a //= common
        b //= common
        c //= common
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def extend_matching(
    sources: tuple[int, ...],
    rows: tuple[int, ...],
    partial: set[tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    fixed_sources = {x for x, _ in partial}
    fixed_rows = {y for _, y in partial}
    free_sources = [x for x in sources if x not in fixed_sources]
    free_rows = [y for y in rows if y not in fixed_rows]
    assert len(free_sources) == len(free_rows)
    extension = set(partial)
    extension.update(zip(free_sources, free_rows))
    assert len({x for x, _ in extension}) == len(sources)
    assert len({y for _, y in extension}) == len(rows)
    return tuple(sorted(extension))


def cylinder_states(t: int, offset: int) -> set[tuple[int, ...]]:
    target = (0, t - 1)
    paid = {(0, offset), (1, offset + 1)}
    assert target not in paid
    sources = tuple(x for x in range(t) if x not in {0, 1})
    rows = tuple(y for y in range(t) if y not in {offset, offset + 1})

    residual_line = {
        (x, x + offset)
        for x in range(t)
        if 0 <= x + offset < t and x not in {0, 1}
    }
    forbidden = extend_matching(sources, rows, residual_line)
    forbidden_map = dict(forbidden)

    result: set[tuple[int, ...]] = set()
    for image in permutations(rows):
        state = dict(paid)
        state.update(zip(sources, image))
        if any(state[x] == forbidden_map[x] for x in sources):
            continue
        vector = tuple(state[x] for x in range(t))
        assert vector[0] != target[1]
        result.add(vector)
    return result


def verify_exact_line_atoms() -> None:
    t = 7
    offsets = (0, 1, 2)
    cylinders = [cylinder_states(t, offset) for offset in offsets]
    assert all(len(cylinder) == 44 for cylinder in cylinders)
    assert all(
        cylinders[i].isdisjoint(cylinders[j])
        for i in range(len(cylinders))
        for j in range(i + 1, len(cylinders))
    )
    bank = set().union(*cylinders)
    m = len(offsets)
    n = t - 2
    target = (0, t - 1)

    cells_by_line: dict[tuple[int, int, int], set[tuple[int, int]]] = defaultdict(set)
    grid = [(x, y) for x in range(t) for y in range(t) if (x, y) != target]
    for first, second in combinations(grid, 2):
        if first[0] == second[0] or first[1] == second[1]:
            continue
        key = line_key((first, second))
        for cell in grid:
            a, b, c = key
            if a * cell[0] + b * cell[1] == c:
                cells_by_line[key].add(cell)

    for cells in cells_by_line.values():
        if len(cells) < 3:
            continue
        hits = 0
        for state in bank:
            selected = {(x, state[x]) for x in range(t)}
            if len(selected & cells) >= 3:
                hits += 1
        actual = Fraction(hits, len(bank))
        s = len(cells)
        bound = Fraction(30, 11) * (
            Fraction(comb(s, 3), n * (n - 1) * (n - 2))
            + Fraction(2 * comb(s - 1, 2), m * n * (n - 1))
        )
        assert actual <= bound


def verify_cubic_height_bound(max_t: int = 20_000) -> None:
    for t in range(20, max_t + 1):
        n = t - 2
        m = t - 9
        bands = (t - 1).bit_length()
        assert bands >= 1
        for height in range(1, t):
            q = 1 + (t - 1) // height
            atom = Fraction(comb(q, 3), n * (n - 1) * (n - 2))
            atom += Fraction(2 * comb(q - 1, 2), m * n * (n - 1))
            assert atom * height**3 <= 3

            if atom:
                lower = Fraction(11 * height**3, 90 * bands)
                # CMR354 is the rearrangement J * atom >= 11/(30B).
                assert lower * atom <= Fraction(11, 30 * bands)


def main() -> None:
    verify_exact_line_atoms()
    verify_cubic_height_bound()
    print(
        "verified line-clean line energy: exact two-slice atoms on t=7, "
        "dyadic occupancy bounds, and the cubic height-signature inequality"
    )


if __name__ == "__main__":
    main()
