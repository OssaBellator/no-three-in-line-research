#!/usr/bin/env python3
"""Exhaust the simplest blockwise reversal patterns over all side-five factors."""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations

from verify_product_blockwise_digits import (
    FactorPair,
    Point,
    determinant,
    is_no_three,
    local_product_host,
    verify_four_regular,
)


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    for first in permutations(range(n)):
        for second in permutations(range(n)):
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = [(x, first[x]) for x in range(n)]
            points.extend((x, second[x]) for x in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def canonical_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    result: list[FactorPair] = []
    for pair in valid_factor_pairs(n):
        key = tuple(sorted(pair))
        if key not in seen:
            seen.add(key)
            result.append(pair)
    return tuple(result)


def first_no_three_degree_two_state(
    host: tuple[Point, ...],
) -> tuple[Point, ...] | None:
    side = len(host) // 4
    rows = tuple(tuple(y for x, y in host if x == row) for row in range(side))
    remaining = [[0] * side for _ in range(side + 1)]
    for row in range(side - 1, -1, -1):
        remaining[row] = remaining[row + 1].copy()
        for y in rows[row]:
            remaining[row][y] += 1

    index = {point: bit for bit, point in enumerate(host)}
    forbidden_pairs: dict[Point, tuple[int, ...]] = {}
    for point in host:
        prior = [cell for cell in host if cell[0] < point[0]]
        forbidden_pairs[point] = tuple(
            (1 << index[first]) | (1 << index[second])
            for first, second in combinations(prior, 2)
            if determinant(first, second, point) == 0
        )

    selected: list[Point] = []
    selected_mask = 0
    column_degree = [0] * side

    def search(row: int) -> tuple[Point, ...] | None:
        nonlocal selected_mask
        if row == side:
            return tuple(selected) if column_degree == [2] * side else None

        for columns in combinations(rows[row], 2):
            if any(column_degree[y] >= 2 for y in columns):
                continue
            new_points = ((row, columns[0]), (row, columns[1]))
            if any(
                selected_mask & pair_mask == pair_mask
                for point in new_points
                for pair_mask in forbidden_pairs[point]
            ):
                continue

            for y in columns:
                column_degree[y] += 1
            feasible = all(
                column_degree[y] <= 2
                and column_degree[y] + remaining[row + 1][y] >= 2
                for y in range(side)
            )
            if feasible:
                selected.extend(new_points)
                added = (1 << index[new_points[0]]) | (1 << index[new_points[1]])
                selected_mask |= added
                result = search(row + 1)
                if result is not None:
                    return result
                selected_mask ^= added
                selected.pop()
                selected.pop()
            for y in columns:
                column_degree[y] -= 1
        return None

    return search(0)


def main() -> None:
    outer: FactorPair = ((0, 1), (1, 0))
    identity = (0, 1, 2, 3, 4)
    reversal = (4, 3, 2, 1, 0)
    factors = canonical_factor_pairs(5)
    assert len(factors) == 32

    patterns = {
        "both": ((identity, reversal), (identity, reversal)),
        "row-only": ((identity, reversal), (identity, identity)),
        "column-only": ((identity, identity), (identity, reversal)),
    }
    expected = {
        "both": {"cc": 2, "cf": 2, "fc": 2, "ff": 7},
        "row-only": {"cc": 0, "cf": 0, "fc": 0, "ff": 0},
        "column-only": {"cc": 0, "cf": 0, "fc": 0, "ff": 0},
    }

    for name, (row_maps, column_maps) in patterns.items():
        for orientation in ("cc", "cf", "fc", "ff"):
            successes = 0
            for factor in factors:
                host = local_product_host(
                    outer,
                    factor,
                    row_maps,
                    column_maps,
                    orientation,
                )
                verify_four_regular(host)
                successes += int(first_no_three_degree_two_state(host) is not None)
            assert successes == expected[name][orientation]
            print(
                f"{name} {orientation}: successful side-five hosts="
                f"{successes}/32"
            )


if __name__ == "__main__":
    main()
