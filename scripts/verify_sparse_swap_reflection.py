#!/usr/bin/env python3
"""Finite checks for SAS5z--SAS5ad."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

Point = tuple[int, int]


def collinear(points: tuple[Point, Point, Point]) -> bool:
    a, b, c = points
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def reflect(column: int, x: int, y: int) -> int:
    return x + y - column


def swap_labels(labels: tuple[int, ...], x: int, y: int) -> tuple[int, ...]:
    out = list(labels)
    out[x], out[y] = out[y], out[x]
    return tuple(out)


def verify_double_scope(counts: Counter[str]) -> None:
    for size in range(3, 9):
        for rows in combinations(range(size), 3):
            for i, j in permutations(range(3), 2):
                k = next(pos for pos in range(3) if pos not in {i, j})
                for x, y in permutations(range(size), 2):
                    ratio = Fraction(rows[k] - rows[i], rows[j] - rows[i])
                    z = Fraction(x) + ratio * (y - x)
                    z_star = Fraction(y) + ratio * (x - y)
                    assert z + z_star == x + y
                    assert (z.denominator == 1) == (z_star.denominator == 1)
                    if z.denominator != 1:
                        counts["rational double addresses"] += 1
                        continue
                    z_int = int(z)
                    z_star_int = int(z_star)
                    destruction = [None, None, None]
                    repair = [None, None, None]
                    destruction[i], destruction[j], destruction[k] = x, y, z_int
                    repair[i], repair[j], repair[k] = y, x, z_star_int
                    assert collinear(tuple(zip(rows, destruction)))
                    assert collinear(tuple(zip(rows, repair)))
                    if len(set(destruction)) == 3:
                        assert len(set(repair)) == 3
                    assert z_star_int - reflect(z_int, x, y) == 0
                    counts["integral double addresses"] += 1

                    if size <= 5 and all(0 <= c < size for c in destruction + repair):
                        for labels in product(range(3), repeat=size):
                            a, b = labels[x], labels[y]
                            if a == b:
                                continue
                            required = [0, 0, 0]
                            required[i], required[j], required[k] = a, b, labels[z_int]
                            if not all(labels[destruction[p]] == required[p] for p in range(3)):
                                continue
                            after = swap_labels(labels, x, y)
                            repaired = all(after[repair[p]] == required[p] for p in range(3))
                            assert repaired == (labels[z_star_int] == required[k])
                            counts["double label tests"] += 1


def verify_single_scope(counts: Counter[str]) -> None:
    for size in range(3, 7):
        for rows in combinations(range(size), 3):
            for i in range(3):
                others = [p for p in range(3) if p != i]
                j, k = others
                for x, y in permutations(range(size), 2):
                    available = [c for c in range(size) if c not in {x, y}]
                    for cj, ck in permutations(available, 2):
                        destruction = [None, None, None]
                        destruction[i], destruction[j], destruction[k] = x, cj, ck
                        points = tuple(zip(rows, destruction))
                        if not collinear(points):
                            continue
                        repair = [reflect(c, x, y) for c in destruction]
                        assert repair[i] == y
                        assert collinear(tuple(zip(rows, repair)))
                        assert len(set(repair)) == 3
                        assert x not in repair[1:] if i == 0 else True
                        counts["singleton geometries"] += 1

                        if all(0 <= c < size for c in repair) and size <= 5:
                            for labels in product(range(3), repeat=size):
                                a, b = labels[x], labels[y]
                                if a == b:
                                    continue
                                required = [labels[c] for c in destruction]
                                if not all(labels[destruction[p]] == required[p] for p in range(3)):
                                    continue
                                after = swap_labels(labels, x, y)
                                repaired = all(after[repair[p]] == required[p] for p in range(3))
                                expected = all(
                                    labels[repair[p]] == required[p]
                                    for p in range(3)
                                    if p != i
                                )
                                assert repaired == expected
                                counts["singleton label tests"] += 1


def verify_increment_reversal(counts: Counter[str]) -> None:
    for x, y, base, step in product(range(-3, 4), repeat=4):
        for s in range(-3, 4):
            z0 = base + s * step
            z1 = base + (s + 1) * step
            assert reflect(z1, x, y) - reflect(z0, x, y) == -step
            counts["increment checks"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_double_scope(counts)
    verify_single_scope(counts)
    verify_increment_reversal(counts)
    print("SAS5z--SAS5ad swap-reflection audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
