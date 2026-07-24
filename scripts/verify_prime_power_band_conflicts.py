#!/usr/bin/env python3
"""Exact small-grid checks for CMR223--CMR226."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import gcd


def primitive_height(
    first: tuple[int, int], second: tuple[int, int]
) -> int:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    divisor = gcd(abs(dx), abs(dy))
    return max(abs(dx // divisor), abs(dy // divisor))


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    third: tuple[int, int],
) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (third[0] - first[0]) * (second[1] - first[1])
    )


def band_floor(height: int) -> int:
    return 1 << (height.bit_length() - 1)


def verify_grid(t: int) -> None:
    points = [(column, row) for column in range(t) for row in range(t)]
    edge_degree: dict[int, Counter[tuple[int, int]]] = {
        1 << exponent: Counter()
        for exponent in range((t - 1).bit_length())
    }
    pair_degree: dict[int, Counter[tuple[tuple[int, int], tuple[int, int]]]] = {
        band: Counter() for band in edge_degree
    }

    for triple in combinations(points, 3):
        columns = {point[0] for point in triple}
        rows = {point[1] for point in triple}
        if len(columns) < 3 or len(rows) < 3:
            continue
        if not collinear(*triple):
            continue
        height = primitive_height(triple[0], triple[1])
        band = band_floor(height)
        for point in triple:
            edge_degree[band][point] += 1
        for pair in combinations(triple, 2):
            pair_degree[band][tuple(sorted(pair))] += 1

    for band in edge_degree:
        maximum_edge = max(edge_degree[band].values(), default=0)
        maximum_pair = max(pair_degree[band].values(), default=0)
        assert maximum_edge < 3 * t * t
        assert maximum_pair <= t / band


def verify_direction_count(max_h: int) -> None:
    for height in range(1, max_h + 1):
        vectors = []
        for u in range(-(2 * height - 1), 2 * height):
            for v in range(-(2 * height - 1), 2 * height):
                if u == 0 and v == 0:
                    continue
                maximum = max(abs(u), abs(v))
                if not (height <= maximum < 2 * height):
                    continue
                if gcd(abs(u), abs(v)) != 1:
                    continue
                if u < 0 or (u == 0 and v < 0):
                    continue
                vectors.append((u, v))
        assert len(vectors) < 6 * height * height


def main() -> None:
    for size in range(5, 13):
        verify_grid(size)
    verify_direction_count(max_h=100)
    print(
        "verified dyadic band conflicts on grids through t=12: "
        "edge degree below 3t^2 and pair codegree at most t/H"
    )


if __name__ == "__main__":
    main()
