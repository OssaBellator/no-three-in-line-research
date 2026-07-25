#!/usr/bin/env python3
"""Finite checks for PX267--PX269."""

from __future__ import annotations

import itertools
import math


def extends_partial(permutation: tuple[int, ...], partial: dict[int, int]) -> bool:
    return all(permutation[row] == column for row, column in partial.items())


def is_derangement(permutation: tuple[int, ...]) -> bool:
    return all(row != column for row, column in enumerate(permutation))


def complete_partial(partial: dict[int, int], order: int):
    for permutation in itertools.permutations(range(order)):
        if is_derangement(permutation) and extends_partial(permutation, partial):
            return permutation
    return None


def check_partial_completion(max_order: int = 6) -> None:
    for order in range(2, max_order + 1):
        # Enumerate partial matchings by restricting full permutations to subsets.
        partials: set[tuple[tuple[int, int], ...]] = set()
        for permutation in itertools.permutations(range(order)):
            for mask in range(1 << order):
                partial = tuple(
                    (row, permutation[row])
                    for row in range(order)
                    if mask & (1 << row) and permutation[row] != row
                )
                if len({column for _row, column in partial}) == len(partial):
                    partials.add(partial)
        for partial_tuple in partials:
            partial = dict(partial_tuple)
            if complete_partial(partial, order) is not None:
                continue
            # PX267 says the only obstruction is one common unmatched label and
            # deleting it leaves a complete partial derangement.
            unmatched_rows = set(range(order)) - set(partial)
            unused_columns = set(range(order)) - set(partial.values())
            assert len(unmatched_rows) == len(unused_columns) == 1
            assert unmatched_rows == unused_columns
            deleted = next(iter(unmatched_rows))
            remaining = [label for label in range(order) if label != deleted]
            assert len(partial) == order - 1
            assert set(partial) == set(remaining)
            assert set(partial.values()) == set(remaining)


def allowed_count(opposite: tuple[int, ...]) -> int:
    order = len(opposite)
    return sum(
        all(permutation[row] not in (row, opposite[row]) for row in range(order))
        for permutation in itertools.permutations(range(order))
    )


def partitions_without_ones(total: int, minimum: int = 2):
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for rest in partitions_without_ones(total - first, first):
            yield (first,) + rest


def representative(cycle_lengths: tuple[int, ...]) -> tuple[int, ...]:
    order = sum(cycle_lengths)
    permutation = list(range(order))
    start = 0
    for length in cycle_lengths:
        for offset in range(length):
            permutation[start + offset] = start + (offset + 1) % length
        start += length
    return tuple(permutation)


def check_regular_permanent(max_order: int = 9) -> None:
    for order in range(3, max_order + 1):
        lower = math.factorial(order) * (1 - 2 / order) ** order
        for cycle_lengths in partitions_without_ones(order):
            opposite = representative(cycle_lengths)
            assert is_derangement(opposite)
            count = allowed_count(opposite)
            assert count + 1e-12 >= lower
            factor = (1 - 2 / order) ** (-order)
            for rank in range(1, min(3, order) + 1):
                assert math.factorial(order - rank) / count <= factor / math.prod(
                    range(order - rank + 1, order + 1)
                ) + 1e-12


def check_numeric_envelope() -> None:
    assert (7 / 5) ** 7 < 11
    for order in range(8, 10000):
        factor = (1 - 2 / order) ** (-order)
        assert factor < math.e**3


def main() -> None:
    check_partial_completion()
    check_regular_permanent()
    check_numeric_envelope()
    print("PX267--PX269 two-layer regular spread checks passed")


if __name__ == "__main__":
    main()
