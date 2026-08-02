#!/usr/bin/env python3
"""Verify blockwise digit relabelling and the exact side-ten product witness.

The script proves finite statements only.  It exhausts all side-five saturated
no-three permutation pairs, all four radix orientations, and all sixteen ways
to assign identity/reversal maps to the two coarse row and two coarse column
blocks.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations, product

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]
BlockMaps = tuple[Permutation, ...]

ORIENTATIONS = ("cc", "cf", "fc", "ff")
OUTER: FactorPair = ((0, 1), (1, 0))
IDENTITY = tuple(range(5))
REVERSAL = tuple(reversed(range(5)))
SIDE_TEN_INNER: FactorPair = (
    (0, 2, 1, 4, 3),
    (2, 4, 0, 3, 1),
)
SIDE_TEN_WITNESS: FactorPair = (
    (4, 2, 1, 3, 0, 9, 6, 8, 7, 5),
    (5, 7, 8, 6, 9, 0, 3, 1, 2, 4),
)


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def is_no_three(points: tuple[Point, ...] | list[Point]) -> bool:
    return all(determinant(*triple) != 0 for triple in combinations(points, 3))


@lru_cache(maxsize=None)
def valid_factor_pairs(n: int) -> tuple[FactorPair, ...]:
    result: list[FactorPair] = []
    all_permutations = tuple(permutations(range(n)))
    for first in all_permutations:
        for second in all_permutations:
            if any(first[x] == second[x] for x in range(n)):
                continue
            points = [(x, first[x]) for x in range(n)]
            points.extend((x, second[x]) for x in range(n))
            if is_no_three(points):
                result.append((first, second))
    return tuple(result)


def flatten(
    m: int,
    n: int,
    i: int,
    j: int,
    u: int,
    v: int,
    orientation: str,
    row_maps: BlockMaps,
    column_maps: BlockMaps,
) -> Point:
    row_digit = row_maps[i][u]
    column_digit = column_maps[j][v]
    x = n * i + row_digit if orientation[0] == "c" else m * row_digit + i
    y = n * j + column_digit if orientation[1] == "c" else m * column_digit + j
    return x, y


def blockwise_host(
    outer: FactorPair,
    inner: FactorPair,
    orientation: str,
    row_maps: BlockMaps,
    column_maps: BlockMaps,
) -> tuple[Point, ...]:
    m = len(outer[0])
    n = len(inner[0])
    cells = {
        flatten(
            m,
            n,
            i,
            outer[r][i],
            u,
            inner[s][u],
            orientation,
            row_maps,
            column_maps,
        )
        for r in (0, 1)
        for s in (0, 1)
        for i in range(m)
        for u in range(n)
    }
    assert len(cells) == 4 * m * n
    return tuple(sorted(cells))


def verify_regular(host: tuple[Point, ...], degree: int) -> None:
    side = len(host) // degree
    assert len(host) == degree * side
    for x in range(side):
        assert sum(px == x for px, _ in host) == degree
    for y in range(side):
        assert sum(py == y for _, py in host) == degree


def one_inner_layer_state(
    outer: FactorPair,
    inner: FactorPair,
    inner_layer: int,
    orientation: str,
    row_maps: BlockMaps,
    column_maps: BlockMaps,
) -> tuple[Point, ...]:
    m = len(outer[0])
    n = len(inner[0])
    cells = {
        flatten(
            m,
            n,
            i,
            outer[r][i],
            u,
            inner[inner_layer][u],
            orientation,
            row_maps,
            column_maps,
        )
        for r in (0, 1)
        for i in range(m)
        for u in range(n)
    }
    assert len(cells) == 2 * m * n
    result = tuple(sorted(cells))
    verify_regular(result, degree=2)
    return result


def first_no_three_degree_two(
    host: tuple[Point, ...],
) -> tuple[Point, ...] | None:
    side = len(host) // 4
    rows = tuple(tuple(y for x, y in host if x == row) for row in range(side))
    assert all(len(row) == 4 for row in rows)

    remaining = [[0] * side for _ in range(side + 1)]
    for row in range(side - 1, -1, -1):
        remaining[row] = remaining[row + 1].copy()
        for y in rows[row]:
            remaining[row][y] += 1

    index = {cell: bit for bit, cell in enumerate(host)}
    forbidden_pairs: dict[Point, tuple[int, ...]] = {}
    for point in host:
        prior = [cell for cell in host if cell[0] < point[0]]
        forbidden_pairs[point] = tuple(
            (1 << index[first]) | (1 << index[second])
            for first, second in combinations(prior, 2)
            if determinant(first, second, point) == 0
        )

    chosen: list[Point] = []
    chosen_mask = 0
    column_degree = [0] * side

    def search(row: int) -> tuple[Point, ...] | None:
        nonlocal chosen_mask
        if row == side:
            return tuple(chosen) if column_degree == [2] * side else None

        for selected_columns in combinations(rows[row], 2):
            if any(column_degree[y] == 2 for y in selected_columns):
                continue
            new_points = ((row, selected_columns[0]), (row, selected_columns[1]))
            if any(
                chosen_mask & pair_mask == pair_mask
                for point in new_points
                for pair_mask in forbidden_pairs[point]
            ):
                continue

            for y in selected_columns:
                column_degree[y] += 1
            feasible = all(
                column_degree[y] <= 2
                and column_degree[y] + remaining[row + 1][y] >= 2
                for y in range(side)
            )
            if feasible:
                chosen.extend(new_points)
                added_mask = (
                    (1 << index[new_points[0]]) | (1 << index[new_points[1]])
                )
                chosen_mask |= added_mask
                model = search(row + 1)
                if model is not None:
                    return model
                chosen_mask ^= added_mask
                chosen.pop()
                chosen.pop()
            for y in selected_columns:
                column_degree[y] -= 1
        return None

    return search(0)


def graph_points(pair: FactorPair) -> tuple[Point, ...]:
    return tuple(
        sorted(
            (x, pair[layer][x])
            for layer in (0, 1)
            for x in range(len(pair[0]))
        )
    )


def verify_side_ten_witness() -> None:
    row_maps = (IDENTITY, REVERSAL)
    column_maps = (IDENTITY, REVERSAL)
    selected = one_inner_layer_state(
        OUTER,
        SIDE_TEN_INNER,
        inner_layer=1,
        orientation="ff",
        row_maps=row_maps,
        column_maps=column_maps,
    )
    assert selected == graph_points(SIDE_TEN_WITNESS)
    assert is_no_three(selected)
    print("side ten blockwise-reversal witness: verified 20 no-three points")


def exhaustive_reversal_census() -> None:
    ordered_pairs = valid_factor_pairs(5)
    assert len(ordered_pairs) == 64
    inner_factors = tuple(pair for pair in ordered_pairs if pair[0] < pair[1])
    assert len(inner_factors) == 32

    maps = (IDENTITY, REVERSAL)
    successful_patterns = {
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
    }

    for bits in product((0, 1), repeat=4):
        row_maps = (maps[bits[0]], maps[bits[1]])
        column_maps = (maps[bits[2]], maps[bits[3]])
        successful_hosts = 0
        successful_factors: set[FactorPair] = set()
        simple_hosts = 0
        simple_factors: set[FactorPair] = set()

        for inner in inner_factors:
            for orientation in ORIENTATIONS:
                host = blockwise_host(
                    OUTER,
                    inner,
                    orientation,
                    row_maps,
                    column_maps,
                )
                verify_regular(host, degree=4)
                if first_no_three_degree_two(host) is not None:
                    successful_hosts += 1
                    successful_factors.add(inner)

                simple = any(
                    is_no_three(
                        one_inner_layer_state(
                            OUTER,
                            inner,
                            inner_layer,
                            orientation,
                            row_maps,
                            column_maps,
                        )
                    )
                    for inner_layer in (0, 1)
                )
                if simple:
                    simple_hosts += 1
                    simple_factors.add(inner)

        if bits in successful_patterns:
            assert successful_hosts == 13
            assert len(successful_factors) == 9
            assert simple_hosts == 7
            assert len(simple_factors) == 7
        else:
            assert successful_hosts == 0
            assert not successful_factors
            assert simple_hosts == 0
            assert not simple_factors

        print(
            f"pattern={bits}: full_hosts={successful_hosts}, "
            f"full_factors={len(successful_factors)}, "
            f"one_layer_hosts={simple_hosts}, "
            f"one_layer_factors={len(simple_factors)}"
        )


def main() -> None:
    verify_side_ten_witness()
    exhaustive_reversal_census()


if __name__ == "__main__":
    main()
