#!/usr/bin/env python3
"""Verify the protected coset local-load census PX76--PX77."""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product

Point = tuple[int, int]
Label = tuple[int, int]

N = 25
H = 5
SLOPE = 2
SUBGROUP = (0, 5, 10, 15, 20)
EXPECTED_EVENT_COUNTS = {1: 1_150, 2: 20_614, 3: 25_484}
EXPECTED_WEIGHTED_TOTALS = {1: 48_500, 2: 253_300, 3: 94_268}
EXPECTED_LOAD_NUMERATORS = (167_688, 167_429, 167_462, 167_670, 167_655)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def coset_index(fine_row: int) -> int:
    return fine_row % 5


def scalar_point(label: Label, shifts: list[int]) -> Point:
    fine_row, corner_type = label
    delta = shifts[coset_index(fine_row)]
    fine_column = SLOPE * ((fine_row + delta) % N) % N
    scalar_row = fine_row if corner_type < 2 else N + fine_row
    scalar_column = fine_column if corner_type % 2 == 0 else N + fine_column
    return scalar_row, scalar_column


def main() -> None:
    labels = tuple((fine_row, corner_type) for fine_row in range(N) for corner_type in range(4))
    event_counts = defaultdict(int)
    weighted_totals = defaultdict(int)
    load_numerators = [0] * 5
    certain_events = 0

    for triple in combinations(labels, 3):
        support = tuple(sorted({coset_index(label[0]) for label in triple}))
        support_size = len(support)
        assert 1 <= support_size <= 3

        realization_count = 0
        for values in product(SUBGROUP, repeat=support_size):
            shifts = [0] * 5
            for variable, value in zip(support, values):
                shifts[variable] = value
            points = tuple(scalar_point(label, shifts) for label in triple)
            realization_count += determinant(*points) == 0

        if realization_count == 0:
            continue
        if realization_count == H**support_size:
            certain_events += 1

        integer_weight = realization_count * H ** (3 - support_size)
        event_counts[support_size] += 1
        weighted_totals[support_size] += integer_weight
        for variable in support:
            load_numerators[variable] += integer_weight

    assert dict(event_counts) == EXPECTED_EVENT_COUNTS
    assert dict(weighted_totals) == EXPECTED_WEIGHTED_TOTALS
    assert tuple(load_numerators) == EXPECTED_LOAD_NUMERATORS
    assert certain_events == 0

    denominator = H**3
    maximum_numerator = max(load_numerators)
    assert 12 * maximum_numerator > 16_000 * denominator

    print(f"event counts by support: {dict(event_counts)}")
    print(f"integer probability masses by support: {dict(weighted_totals)}")
    print(f"load numerators: {tuple(load_numerators)} / {denominator}")
    print(f"maximum load: {maximum_numerator / denominator:.3f}")
    print(f"LLL threshold ratio: {12 * maximum_numerator / denominator:.3f}")
    print("certain bad events: 0")
    print("protected coset local-load barrier verified")


if __name__ == "__main__":
    main()
