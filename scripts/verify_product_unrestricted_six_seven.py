#!/usr/bin/env python3
"""Exact unrestricted PX28 rectangle search at base sides six and seven."""
from __future__ import annotations

import argparse
import gc
from itertools import product

Point = tuple[int, int]
Edge = tuple[int, int, int, int]
ORIENTATIONS = ("cc", "cf", "fc", "ff")
EXPECTED_NODES = {
    (6, "cc"): 236651,
    (6, "cf"): 251708,
    (6, "fc"): 260521,
    (6, "ff"): 204824,
    (7, "cc"): 3185100,
    (7, "cf"): 3561372,
    (7, "ff"): 2761350,
}


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def compatible(first: Edge, second: Edge) -> bool:
    return all(a != b for a, b in zip(first, second))


def corners(n: int, edge: Edge, orientation: str) -> tuple[Point, ...]:
    u, p, t, r = edge
    x_0 = u if orientation[0] == "c" else 2 * u
    x_1 = n + p if orientation[0] == "c" else 2 * p + 1
    y_0 = t if orientation[1] == "c" else 2 * t
    y_1 = n + r if orientation[1] == "c" else 2 * r + 1
    return (x_0, y_0), (x_0, y_1), (x_1, y_0), (x_1, y_1)


def pair_conflict(first: tuple[Point, ...], second: tuple[Point, ...]) -> bool:
    for left, right in ((0, 3), (1, 2)):
        if any(determinant(first[left], first[right], point) == 0 for point in second):
            return True
        if any(determinant(second[left], second[right], point) == 0 for point in first):
            return True
    return False


def exact_search(n: int, orientation: str) -> tuple[tuple[Edge, ...] | None, int]:
    side = 2 * n
    edges = tuple(product(range(n), repeat=4))
    edge_count = len(edges)
    rectangles = tuple(corners(n, edge, orientation) for edge in edges)
    grid = tuple((x, y) for x in range(side) for y in range(side))
    grid_index = {point: index for index, point in enumerate(grid)}
    rectangle_points = tuple(
        tuple(grid_index[point] for point in rectangle)
        for rectangle in rectangles
    )
    all_edges = (1 << edge_count) - 1

    by_part = [[0] * n for _ in range(4)]
    by_u = [0] * n
    at_point = [0] * len(grid)
    for index, edge in enumerate(edges):
        bit = 1 << index
        for part, value in enumerate(edge):
            by_part[part][value] |= bit
        by_u[edge[0]] |= bit
        for point in rectangle_points[index]:
            at_point[point] |= bit

    line_masks: dict[tuple[int, int], int] = {}
    for first in range(len(grid)):
        for second in range(first + 1, len(grid)):
            mask = 0
            for third, point in enumerate(grid):
                if determinant(grid[first], grid[second], point) == 0:
                    mask |= 1 << third
            line_masks[(first, second)] = mask

    pair_bad = [0] * edge_count
    for first, edge in enumerate(edges):
        for second in range(first + 1, edge_count):
            if not compatible(edge, edges[second]):
                continue
            if pair_conflict(rectangles[first], rectangles[second]):
                pair_bad[first] |= 1 << second
                pair_bad[second] |= 1 << first

    compatibility = [all_edges] * edge_count
    for index, edge in enumerate(edges):
        mask = all_edges
        for part, value in enumerate(edge):
            mask &= ~by_part[part][value]
        compatibility[index] = mask

    transversal_cache: dict[tuple[int, int], int] = {}

    def transversal_completions(first: int, second: int) -> int:
        if first > second:
            first, second = second, first
        key = (first, second)
        cached = transversal_cache.get(key)
        if cached is not None:
            return cached

        dangerous_points = 0
        for first_point in rectangle_points[first]:
            for second_point in rectangle_points[second]:
                assert first_point != second_point
                pair = (
                    (first_point, second_point)
                    if first_point < second_point
                    else (second_point, first_point)
                )
                dangerous_points |= line_masks[pair]

        result = 0
        while dangerous_points:
            bit = dangerous_points & -dangerous_points
            point = bit.bit_length() - 1
            dangerous_points -= bit
            result |= at_point[point]
        result &= compatibility[first] & compatibility[second]
        transversal_cache[key] = result
        return result

    selected: list[int] = []
    nodes = 0

    def search(
        used_u: int,
        used_p: int,
        used_t: int,
        used_r: int,
        forbidden: int,
    ) -> tuple[int, ...] | None:
        nonlocal nodes
        nodes += 1
        if len(selected) == n:
            return tuple(selected)

        unavailable = 0
        for value in range(n):
            if used_p >> value & 1:
                unavailable |= by_part[1][value]
            if used_t >> value & 1:
                unavailable |= by_part[2][value]
            if used_r >> value & 1:
                unavailable |= by_part[3][value]

        best_candidates = 0
        best_count = edge_count + 1
        for u in range(n):
            if used_u >> u & 1:
                continue
            candidates = by_u[u] & ~unavailable & ~forbidden & all_edges
            count = candidates.bit_count()
            if count == 0:
                return None
            if count < best_count:
                best_candidates = candidates
                best_count = count

        ordered: list[int] = []
        while best_candidates:
            bit = best_candidates & -best_candidates
            index = bit.bit_length() - 1
            best_candidates -= bit
            ordered.append(index)
        ordered.sort(key=lambda index: pair_bad[index].bit_count())

        for index in ordered:
            edge = edges[index]
            next_forbidden = forbidden | pair_bad[index]
            for previous in selected:
                next_forbidden |= transversal_completions(index, previous)

            selected.append(index)
            result = search(
                used_u | 1 << edge[0],
                used_p | 1 << edge[1],
                used_t | 1 << edge[2],
                used_r | 1 << edge[3],
                next_forbidden,
            )
            if result is not None:
                return result
            selected.pop()
        return None

    solution = search(0, 0, 0, 0, 0)
    if solution is None:
        return None, nodes
    return tuple(edges[index] for index in solution), nodes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--side", type=int, choices=(6, 7), default=6)
    parser.add_argument("--orientation", choices=ORIENTATIONS)
    args = parser.parse_args()

    if args.orientation:
        orientations = (args.orientation,)
    elif args.side == 6:
        orientations = ORIENTATIONS
    else:
        orientations = ("cc", "cf", "ff")

    for orientation in orientations:
        solution, nodes = exact_search(args.side, orientation)
        assert solution is None, (args.side, orientation, solution)
        assert nodes == EXPECTED_NODES[(args.side, orientation)], (
            args.side,
            orientation,
            nodes,
            EXPECTED_NODES[(args.side, orientation)],
        )
        print(
            f"n={args.side}, orientation={orientation}: "
            f"no unrestricted PX28 template; nodes={nodes}"
        )
        gc.collect()

    if args.side == 7 and args.orientation is None:
        print("n=7, orientation=fc follows from cf by scalar transposition")


if __name__ == "__main__":
    main()
