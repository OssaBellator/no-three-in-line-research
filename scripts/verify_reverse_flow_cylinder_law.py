#!/usr/bin/env python3
"""Exhaustive finite checks for SRR2c--SRR2e."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product


def subsets(items: range):
    seq = list(items)
    for size in range(1, len(seq) + 1):
        yield from combinations(seq, size)


def check_matrix(rows: int, cols: int, entries: tuple[int, ...]) -> None:
    w = [
        [Fraction(entries[i * cols + j], 2) for j in range(cols)]
        for i in range(rows)
    ]
    if any(sum(row) != 1 for row in w):
        return
    column_loads = [sum(w[i][j] for i in range(rows)) for j in range(cols)]
    if any(load > 1 for load in column_loads):
        return

    direct = [sum(w[i][j] for i in range(rows)) / rows for j in range(cols)]
    q_bar_b = sum(column_loads) / cols
    assert q_bar_b == Fraction(rows, cols)

    for subset in subsets(range(cols)):
        probability = sum(direct[j] for j in subset)
        q_bar_c = sum(column_loads[j] for j in subset) / len(subset)
        formula = Fraction(len(subset), rows) * q_bar_c
        conditional_uniform = Fraction(len(subset), cols)
        ratio_formula = conditional_uniform * q_bar_c / q_bar_b
        assert probability == formula == ratio_formula

        if q_bar_c == q_bar_b:
            assert probability == conditional_uniform


def main() -> None:
    checked = 0
    for rows in (1, 2):
        for cols in range(rows, 4):
            for entries in product(range(3), repeat=rows * cols):
                w = [
                    [Fraction(entries[i * cols + j], 2) for j in range(cols)]
                    for i in range(rows)
                ]
                if all(sum(row) == 1 for row in w) and all(
                    sum(w[i][j] for i in range(rows)) <= 1 for j in range(cols)
                ):
                    checked += 1
                check_matrix(rows, cols, entries)
    assert checked > 0
    print(f"Reverse-flow cylinder checks passed on {checked} feasible matrices")


if __name__ == "__main__":
    main()
