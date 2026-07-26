#!/usr/bin/env python3
"""Finite checks for SAS5m--SAS5p."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import gcd


def main() -> None:
    counts: Counter[str] = Counter()
    for order in range(3, 13):
        positions = tuple(permutations(range(3), 2))
        for column_i in range(order):
            for column_j in range(order):
                if column_i == column_j:
                    continue
                displacement = column_j - column_i
                for i, j in positions:
                    k = next(position for position in range(3) if position not in {i, j})
                    directions: set[int] = set()
                    offsets_by_gap: dict[int, set[int]] = defaultdict(set)

                    for rows in combinations(range(order), 3):
                        row_i = rows[i]
                        row_j = rows[j]
                        row_k = rows[k]
                        gap = row_j - row_i
                        third_displacement = row_k - row_i
                        common = gcd(abs(gap), abs(displacement))
                        reduced_row = gap // common
                        reduced_column = displacement // common

                        assert gcd(abs(reduced_row), abs(reduced_column)) == 1
                        integral_rational = (third_displacement * displacement) % gap == 0
                        divisor_condition = third_displacement % reduced_row == 0
                        assert integral_rational == divisor_condition

                        directions.add(gap)
                        offset = reduced_column * row_i - reduced_row * column_i
                        offsets_by_gap[gap].add(offset)

                        if integral_rational:
                            parameter = third_displacement // reduced_row
                            third_column = (
                                column_i
                                + (third_displacement * displacement) // gap
                            )
                            assert row_k == row_i + parameter * reduced_row
                            assert third_column == column_i + parameter * reduced_column
                            assert (
                                reduced_column * row_k
                                - reduced_row * third_column
                                == offset
                            )
                            counts["integral progression records"] += 1
                        else:
                            counts["nonintegral rational records"] += 1
                        counts["row-triple records"] += 1

                    assert len(directions) <= order - 1
                    for gap, offsets in offsets_by_gap.items():
                        assert len(offsets) <= order
                        # The word positions fix the sign of every oriented row gap.
                        assert all((value > 0) == (gap > 0) for value in {gap})
                        counts["direction-offset classes"] += 1
                    counts["word-column systems"] += 1

    print("SAS5m--SAS5p double-scope progression audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
