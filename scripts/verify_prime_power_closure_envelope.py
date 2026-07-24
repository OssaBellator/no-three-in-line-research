#!/usr/bin/env python3
"""Finite checks for CMR172--CMR175."""

from __future__ import annotations

from itertools import combinations


def valuation(value: int, p: int, k: int) -> int:
    if value == 0:
        return k
    result = 0
    while result < k and value % p == 0:
        value //= p
        result += 1
    return result


def envelope_depth(columns: set[int], p: int, k: int) -> int:
    if len(columns) <= 1:
        return k
    return min(
        valuation(first - second, p, k)
        for first, second in combinations(sorted(columns), 2)
    )


def envelope_columns(columns: set[int], p: int, k: int) -> set[int]:
    depth = envelope_depth(columns, p, k)
    modulus = p**depth
    residue = next(iter(columns)) % modulus
    return {value for value in range(p**k) if value % modulus == residue}


def cycle_rows(rows: list[int], columns: list[int]) -> None:
    old = [rows[column] for column in columns]
    for index, column in enumerate(columns):
        rows[column] = old[(index + 1) % len(old)]


def verify_depth_monotonicity() -> None:
    p, k = 5, 2
    columns = list(range(p**k))
    for first_size in (1, 2, 3):
        for first in combinations(columns, first_size):
            current = set(first)
            old_depth = envelope_depth(current, p, k)
            old_envelope = envelope_columns(current, p, k)
            for new_column in columns:
                enlarged = current | {new_column}
                new_depth = envelope_depth(enlarged, p, k)
                assert new_depth <= old_depth
                if new_column not in old_envelope:
                    assert new_depth < old_depth


def verify_row_set_invariance() -> None:
    p, k = 5, 2
    n = p**k
    initial_zero = list(range(n))
    # Distinct root row digit: add one modulo the lower digit, leaving the upper
    # digit fixed.
    initial_one = [
        (value // p) * p + ((value + 1) % p)
        for value in range(n)
    ]
    rows_zero = initial_zero.copy()
    rows_one = initial_one.copy()

    moves = [
        (0, [0, 5, 10, 15]),
        (1, [1, 6, 11, 16]),
        (0, [0, 1, 5, 6]),
        (1, [2, 7, 12, 17]),
        (0, [0, 2, 10, 12]),
    ]

    moved_columns: set[int] = set()
    for layer, selected in moves:
        moved_columns.update(selected)
        if layer == 0:
            cycle_rows(rows_zero, selected)
        else:
            cycle_rows(rows_one, selected)

        envelope = envelope_columns(moved_columns, p, k)
        assert {rows_zero[column] for column in envelope} == {
            initial_zero[column] for column in envelope
        }
        assert {rows_one[column] for column in envelope} == {
            initial_one[column] for column in envelope
        }

        depth = envelope_depth(moved_columns, p, k)
        if depth >= 1:
            assert {
                rows_zero[column] for column in envelope
            }.isdisjoint({rows_one[column] for column in envelope})


def main() -> None:
    verify_depth_monotonicity()
    verify_row_set_invariance()
    print(
        "verified closure envelopes: monotone prefix depth, strict expansion, "
        "row-set invariance, and nonroot disjointness"
    )


if __name__ == "__main__":
    main()
