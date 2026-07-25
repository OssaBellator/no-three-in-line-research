#!/usr/bin/env python3
"""Verify PX183--PX184 uniform rematching logarithmic barrier ingredients."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import gcd, log


def collinear(first, second, third) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def forbidden_cells(size: int) -> set[tuple[int, int]]:
    # Union of two disjoint partial permutations: identity and cyclic shift.
    return {
        (row, column)
        for row in range(size)
        for column in (row, (row + 1) % size)
    }


def candidate_triples(size: int, forbidden: set[tuple[int, int]]):
    cells = [
        (row, column)
        for row in range(size)
        for column in range(size)
        if (row, column) not in forbidden
    ]
    for triple in combinations(cells, 3):
        if len({cell[0] for cell in triple}) < 3:
            continue
        if len({cell[1] for cell in triple}) < 3:
            continue
        if collinear(*triple):
            yield triple


def count_matchings(size: int, forbidden: set[tuple[int, int]]) -> int:
    allowed_masks = []
    full = (1 << size) - 1
    for row in range(size):
        mask = full
        for column in range(size):
            if (row, column) in forbidden:
                mask &= ~(1 << column)
        allowed_masks.append(mask)

    @lru_cache(None)
    def dynamic(row: int, used: int) -> int:
        if row == size:
            return 1
        available = allowed_masks[row] & ~used
        total = 0
        while available:
            bit = available & -available
            available -= bit
            total += dynamic(row + 1, used | bit)
        return total

    return dynamic(0, 0)


def count_extensions(
    size: int,
    forbidden: set[tuple[int, int]],
    triple: tuple[tuple[int, int], ...],
) -> int:
    fixed = dict(triple)
    fixed_columns = {column for _, column in triple}
    if len(fixed) != 3 or len(fixed_columns) != 3:
        return 0
    if any(cell in forbidden for cell in triple):
        return 0

    free_rows = [row for row in range(size) if row not in fixed]
    free_columns = [
        column for column in range(size) if column not in fixed_columns
    ]
    column_index = {column: index for index, column in enumerate(free_columns)}
    allowed_masks = []
    full = (1 << len(free_columns)) - 1
    for row in free_rows:
        mask = full
        for column in free_columns:
            if (row, column) in forbidden:
                mask &= ~(1 << column_index[column])
        allowed_masks.append(mask)

    @lru_cache(None)
    def dynamic(position: int, used: int) -> int:
        if position == len(free_rows):
            return 1
        available = allowed_masks[position] & ~used
        total = 0
        while available:
            bit = available & -available
            available -= bit
            total += dynamic(position + 1, used | bit)
        return total

    return dynamic(0, 0)


def verify_exact_small_sizes() -> None:
    for size in range(8, 13):
        forbidden = forbidden_cells(size)
        triples = list(candidate_triples(size, forbidden))
        total_matchings = count_matchings(size, forbidden)
        assert total_matchings >= 1

        # Exact expected number of internal collinear triples under the uniform
        # allowed matching. At size twelve the complete sum is still small.
        extension_sum = 0
        minimum_probability = 1.0
        sample_step = max(1, len(triples) // 300)
        for index, triple in enumerate(triples):
            extensions = count_extensions(size, forbidden, triple)
            extension_sum += extensions
            if index % sample_step == 0:
                probability = extensions / total_matchings
                minimum_probability = min(minimum_probability, probability)
                # The asymptotic theorem uses the weaker 1/(128(t)_3) bound.
                falling = size * (size - 1) * (size - 2)
                assert probability >= 1 / (128 * falling)

        expectation = extension_sum / total_matchings
        print(
            f"t={size}: candidates={len(triples)}, matchings={total_matchings}, "
            f"E[internal triples]={expectation:.6f}, "
            f"E/(t log t)={expectation/(size*log(size)):.6f}"
        )


def primitive_direction_sum(limit: int) -> float:
    total = 0.0
    for first in range(1, limit + 1):
        for second in range(1, limit + 1):
            if gcd(first, second) == 1:
                height = max(first, second)
                total += 1 / (height * height)
    return total


def verify_direction_harmonic_growth() -> None:
    ratios = []
    for limit in (20, 40, 80, 160, 320):
        value = primitive_direction_sum(limit)
        ratio = value / log(limit)
        ratios.append(ratio)
        print(
            f"H={limit}: primitive weighted sum={value:.6f}, "
            f"ratio/log(H)={ratio:.6f}"
        )
    assert min(ratios[-3:]) > 0.8


def main() -> None:
    verify_exact_small_sizes()
    verify_direction_harmonic_growth()
    print("PX183--PX184 verified")


if __name__ == "__main__":
    main()
