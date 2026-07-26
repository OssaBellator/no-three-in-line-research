#!/usr/bin/env python3
"""Finite checks for SAS5q--SAS5t."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import gcd


def main() -> None:
    counts: Counter[str] = Counter()
    for order in range(3, 13):
        shapes: set[tuple[int, int]] = set()
        exact_addresses: set[tuple[int, int, int, int, int, int, int]] = set()

        for rows in combinations(range(order), 3):
            for fixed_position in range(3):
                other_positions = tuple(
                    position for position in range(3) if position != fixed_position
                )
                j, k = other_positions
                row_i = rows[fixed_position]
                gap_j = rows[j] - row_i
                gap_k = rows[k] - row_i
                common = gcd(abs(gap_j), abs(gap_k))
                reduced_j = gap_j // common
                reduced_k = gap_k // common
                assert gcd(abs(reduced_j), abs(reduced_k)) == 1
                assert reduced_j != 0 and reduced_k != 0 and reduced_j != reduced_k

                shapes.add((reduced_j, reduced_k))
                address = (
                    fixed_position,
                    j,
                    k,
                    reduced_j,
                    reduced_k,
                    common,
                    row_i,
                )
                exact_addresses.add(address)
                assert rows[j] == row_i + common * reduced_j
                assert rows[k] == row_i + common * reduced_k

                for fixed_column in range(order):
                    for column_j in range(order):
                        for column_k in range(order):
                            equation = (
                                gap_j * (column_k - fixed_column)
                                == gap_k * (column_j - fixed_column)
                            )
                            dilation = False
                            if (column_j - fixed_column) % reduced_j == 0:
                                parameter = (column_j - fixed_column) // reduced_j
                                dilation = (
                                    column_k
                                    == fixed_column + reduced_k * parameter
                                )
                            assert equation == dilation

                            if equation:
                                parameter = (column_j - fixed_column) // reduced_j
                                assert column_j == fixed_column + reduced_j * parameter
                                assert column_k == fixed_column + reduced_k * parameter
                                counts["integer dilation solutions"] += 1
                            else:
                                counts["nonsolutions"] += 1
                            counts["column-pair checks"] += 1

        assert len(shapes) <= 4 * (order - 1) ** 2
        assert len(exact_addresses) <= 4 * order * (order - 1) ** 3
        counts["orders"] += 1
        counts["primitive shapes"] += len(shapes)
        counts["exact row addresses"] += len(exact_addresses)

    print("SAS5q--SAS5t singleton-scope dilation audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
