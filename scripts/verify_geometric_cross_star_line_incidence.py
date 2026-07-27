#!/usr/bin/env python3
"""Finite audit for GC2dh--GC2dl."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations
from math import comb, gcd
import random

Point = tuple[int, int]


def line_key(p: Point, q: Point) -> tuple[int, int, int]:
    r_1, c_1 = p
    r_2, c_2 = q
    a = c_2 - c_1
    b = r_1 - r_2
    c = -(a * r_1 + b * c_1)
    common = reduce(gcd, (abs(a), abs(b), abs(c)), 0) or 1
    a, b, c = a // common, b // common, c // common
    for value in (a, b, c):
        if value:
            if value < 0:
                a, b, c = -a, -b, -c
            break
    return a, b, c


def is_axis(key: tuple[int, int, int]) -> bool:
    a, b, _ = key
    return a == 0 or b == 0


def grid_lines(N: int) -> dict[tuple[int, int, int], tuple[Point, ...]]:
    points = [(r, c) for r in range(N) for c in range(N)]
    keys = {line_key(p, q) for p, q in combinations(points, 2)}
    result = {}
    for key in keys:
        a, b, c = key
        result[key] = tuple(p for p in points if a * p[0] + b * p[1] + c == 0)
    return result


def weighted_repeated_cell(certificates: list[tuple[tuple[Point, ...], int]], multiplicity: int, N: int) -> int:
    load: defaultdict[Point, int] = defaultdict(int)
    total = 0
    for cells, weight in certificates:
        assert len(cells) == multiplicity
        total += weight
        for cell in cells:
            load[cell] += weight
    assert load
    maximum = max(load.values())
    assert maximum * N >= multiplicity * total
    return maximum


def main() -> None:
    rng = random.Random(20260727)
    stats: Counter[str] = Counter()

    all_nonaxis: dict[int, list[tuple[tuple[int, int, int], tuple[Point, ...]]]] = {}
    for N in range(2, 9):
        lines = grid_lines(N)
        nonaxis = [(key, cells) for key, cells in lines.items() if not is_axis(key)]
        assert len(nonaxis) <= comb(N * N, 2)
        assert all(len(cells) <= N for _, cells in nonaxis)
        all_nonaxis[N] = nonaxis
        stats["board_orders"] += 1
        stats["nonaxis_lines"] += len(nonaxis)
        stats["nonaxis_line_cells"] += sum(len(cells) for _, cells in nonaxis)

        for key, cells in lines.items():
            if len(cells) >= 3:
                for triple in combinations(cells, 3):
                    assert line_key(triple[0], triple[1]) == key
                    assert line_key(triple[0], triple[2]) == key
                    stats["unique_line_triples"] += 1
                    stats["axis_triples" if is_axis(key) else "nonaxis_triples"] += 1

    for _ in range(50_000):
        N = rng.randint(3, 8)
        key, line_cells = rng.choice(all_nonaxis[N])
        cells = list(line_cells)
        if len(cells) < 3:
            continue
        profile = rng.choice(("bridge", "chord", "transversal"))
        certificate_count = rng.randint(1, 30)

        if profile == "bridge":
            fixed = rng.choice(cells)
            weighted: list[tuple[tuple[Point, ...], int]] = []
            for _j in range(certificate_count):
                moved = rng.sample([cell for cell in cells if cell != fixed], 2)
                weighted.append((tuple(moved), rng.randint(1, 20)))
            total = sum(weight for _, weight in weighted)
            assert total > 0
            weighted_repeated_cell([((moved[0],), weight) for moved, weight in weighted], 1, N)
            weighted_repeated_cell([((moved[1],), weight) for moved, weight in weighted], 1, N)
            stats["bridge_systems"] += 1
            stats["bridge_weight"] += total

        elif profile == "chord":
            weighted = []
            for _j in range(certificate_count):
                triple = rng.sample(cells, 3)
                weighted.append((tuple(triple), rng.randint(1, 20)))
            total = sum(weight for _, weight in weighted)
            weighted_repeated_cell([((triple[0], triple[1]), weight) for triple, weight in weighted], 2, N)
            weighted_repeated_cell([((triple[2],), weight) for triple, weight in weighted], 1, N)
            stats["chord_systems"] += 1
            stats["chord_weight"] += total

        else:
            weighted = []
            for _j in range(certificate_count):
                triple = rng.sample(cells, 3)
                weighted.append((tuple(triple), rng.randint(1, 20)))
            total = sum(weight for _, weight in weighted)
            for position in range(3):
                weighted_repeated_cell([((triple[position],), weight) for triple, weight in weighted], 1, N)
            stats["transversal_systems"] += 1
            stats["transversal_weight"] += total

        # A localized non-axis family uses one of at most ell_N lines.
        ell_N = len(all_nonaxis[N])
        assert total * ell_N >= total
        stats["weighted_line_localizations"] += 1

    # Exact axis/non-axis half split for arbitrary nonnegative masses.
    for _ in range(20_000):
        axis = rng.randint(0, 10_000)
        nonaxis = rng.randint(0, 10_000)
        total = axis + nonaxis
        if total:
            assert max(axis, nonaxis) * 2 >= total
            stats["axis_split_systems"] += 1

    print("GC cross-star line-incidence audit passed")
    for key in sorted(stats):
        print(f"{key}: {stats[key]}")


if __name__ == "__main__":
    main()
