#!/usr/bin/env python3
"""Exhaust normalized non-affine PX28 products for side-five factors."""
from __future__ import annotations

from itertools import permutations

from verify_product_two_factor import FactorPair, Permutation, is_no_three, valid_factor_pairs

Point = tuple[int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")
IDENTITY: Permutation = (0, 1, 2, 3, 4)
OUTER: FactorPair = ((0, 1), (1, 0))
EXPECTED = (
    ((1, 3, 0, 4, 2), (3, 4, 1, 2, 0), IDENTITY, "cf"),
    ((2, 0, 4, 1, 3), IDENTITY, (3, 4, 1, 2, 0), "fc"),
    ((2, 1, 4, 3, 0), (4, 3, 2, 1, 0), (4, 3, 2, 1, 0), "cf"),
    ((2, 4, 0, 3, 1), (4, 3, 2, 1, 0), (4, 3, 2, 1, 0), "ff"),
    ((3, 1, 4, 0, 2), IDENTITY, (3, 4, 1, 2, 0), "fc"),
    ((3, 1, 4, 0, 2), (3, 4, 1, 2, 0), IDENTITY, "cf"),
    ((4, 1, 0, 3, 2), (4, 3, 2, 1, 0), (4, 3, 2, 1, 0), "fc"),
)
CANONICAL_LAYERS: FactorPair = (
    (2, 6, 0, 8, 4, 5, 1, 9, 3, 7),
    (6, 2, 8, 0, 5, 4, 9, 1, 7, 3),
)


def unordered_factors() -> tuple[FactorPair, ...]:
    seen: set[tuple[Permutation, Permutation]] = set()
    result: list[FactorPair] = []
    for first, second in valid_factor_pairs(5):
        key = tuple(sorted((first, second)))
        if key not in seen:
            seen.add(key)
            result.append((first, second))
    assert len(result) == 32
    return tuple(result)


def flatten(
    i: int,
    j: int,
    u: int,
    v: int,
    row_map: Permutation,
    column_map: Permutation,
    orientation: str,
) -> Point:
    row_digit = u if i == 0 else row_map[u]
    column_digit = v if j == 0 else column_map[v]
    x = 5 * i + row_digit if orientation[0] == "c" else 2 * row_digit + i
    y = 5 * j + column_digit if orientation[1] == "c" else 2 * column_digit + j
    return x, y


def state(
    tau: Permutation,
    row_map: Permutation,
    column_map: Permutation,
    orientation: str,
) -> tuple[Point, ...]:
    return tuple(
        flatten(i, OUTER[layer][i], u, tau[u], row_map, column_map, orientation)
        for layer in (0, 1)
        for i in (0, 1)
        for u in range(5)
    )


def outer_layers(
    tau: Permutation,
    row_map: Permutation,
    column_map: Permutation,
    orientation: str,
) -> FactorPair:
    layers: list[Permutation] = []
    for layer in (0, 1):
        values = [-1] * 10
        for i in (0, 1):
            j = OUTER[layer][i]
            for u in range(5):
                x, y = flatten(i, j, u, tau[u], row_map, column_map, orientation)
                values[x] = y
        assert sorted(values) == list(range(10))
        layers.append(tuple(values))
    return layers[0], layers[1]


def main() -> None:
    factors = unordered_factors()
    fine_layers = tuple(sorted({layer for pair in factors for layer in pair}))
    maps = tuple(permutations(range(5)))
    assert len(fine_layers) == 44

    successes: list[tuple[Permutation, Permutation, Permutation, str]] = []
    configurations: set[tuple[Point, ...]] = set()
    for tau in fine_layers:
        for row_map in maps:
            for column_map in maps:
                for orientation in ORIENTATIONS:
                    points = state(tau, row_map, column_map, orientation)
                    if is_no_three(points):
                        assert len(set(points)) == 20
                        successes.append((tau, row_map, column_map, orientation))
                        configurations.add(tuple(sorted(points)))

    assert tuple(sorted(successes)) == EXPECTED
    assert len(configurations) == 5
    successful_layers = {record[0] for record in successes}
    rescued = [pair for pair in factors if any(tau in successful_layers for tau in pair)]
    assert len(successful_layers) == 6
    assert len(rescued) == 22
    assert all(sum(tau in successful_layers for tau in pair) == 1 for pair in rescued)

    non_affine = (3, 4, 1, 2, 0)
    canonical_tau = (2, 0, 4, 1, 3)
    assert outer_layers(canonical_tau, IDENTITY, non_affine, "fc") == CANONICAL_LAYERS
    assert len({(non_affine[(u + 1) % 5] - non_affine[u]) % 5 for u in range(5)}) > 1

    print("normalized non-affine PX28 census verified")
    print("successes=7, fine layers=6, configurations=5, factors=22/32")
    print("canonical non-affine side-ten witness verified")


if __name__ == "__main__":
    main()
