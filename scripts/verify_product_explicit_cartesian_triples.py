#!/usr/bin/env python3
"""Finite checks for PX456--PX460 explicit Cartesian triple bounds."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, log
import random


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def check_crossing_algebra() -> None:
    for vertices in range(1, 200):
        for edges in range(4 * vertices, 8 * vertices + 1):
            p = Fraction(4 * vertices, edges)
            rhs = p * p * edges - 3 * p * vertices
            assert rhs == Fraction(4 * vertices * vertices, edges)
            lower = rhs / (p**4)
            assert lower == Fraction(edges**3, 64 * vertices**2)


def check_rich_line_case_split() -> None:
    rng = random.Random(458)
    for _ in range(10000):
        points = rng.randint(1, 10_000)
        k = rng.randint(2, 100)
        rich_lines = rng.randint(0, 100_000)
        lhs = (k - 1) * rich_lines
        first = 4 * (points ** (2 / 3)) * (rich_lines ** (2 / 3))
        second = 4 * points
        if lhs <= first + second + 1e-9:
            bound = (
                Fraction(512 * points * points, (k - 1) ** 3)
                + Fraction(8 * points, k - 1)
            )
            assert rich_lines <= float(bound) + 1e-6


def check_constant_320() -> None:
    for order in range(2, 100_000):
        lhs = 256 * (1 + log(order)) + 2
        rhs = 320 * log(2 * order)
        assert lhs <= rhs


def count_cartesian_triples(rows: list[int], columns: list[int]) -> int:
    points = [(x, y) for x in rows for y in columns]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def check_small_cartesian_grids() -> None:
    rng = random.Random(459)
    for order in range(2, 7):
        for _ in range(100):
            rows = sorted(rng.sample(range(-20, 21), order))
            columns = sorted(rng.sample(range(-20, 21), order))
            triples = count_cartesian_triples(rows, columns)
            bound = 320 * order**4 * log(2 * order)
            assert triples <= bound

        # Consecutive grids give a denser deterministic test.
        rows = list(range(order))
        columns = list(range(order))
        triples = count_cartesian_triples(rows, columns)
        assert triples <= 320 * order**4 * log(2 * order)


def check_harmonic_decomposition() -> None:
    for line_size in range(3, 100):
        assert comb(line_size, 3) == sum(
            comb(k - 1, 2) for k in range(3, line_size + 1)
        )


def main() -> None:
    check_crossing_algebra()
    check_rich_line_case_split()
    check_constant_320()
    check_small_cartesian_grids()
    check_harmonic_decomposition()
    print("PX456--PX460 explicit Cartesian triple verifier: PASS")


if __name__ == "__main__":
    main()
