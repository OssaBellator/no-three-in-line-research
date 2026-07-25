#!/usr/bin/env python3
"""Exact side-seven saturated-graph and relative-cycle census."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def census(n: int) -> tuple[int, Counter[tuple[int, ...]], int]:
    pair_options = tuple(combinations(range(n), 2))
    column_degree = [0] * n
    selected: list[Point] = []
    row_columns: list[tuple[int, int] | None] = [None] * n
    type_counts: Counter[tuple[int, ...]] = Counter()
    configurations = 0
    nodes = 0

    def component_partition() -> tuple[int, ...]:
        row_neighbours = [tuple(pair) for pair in row_columns]
        column_neighbours: list[list[int]] = [[] for _ in range(n)]
        for row, pair in enumerate(row_neighbours):
            for column in pair:
                column_neighbours[column].append(row)
        assert all(len(neighbours) == 2 for neighbours in column_neighbours)

        seen: set[int] = set()
        half_lengths: list[int] = []
        for start in range(n):
            if start in seen:
                continue
            current = start
            previous: int | None = None
            edge_count = 0
            while current not in seen:
                seen.add(current)
                if current < n:
                    neighbours = tuple(n + column for column in row_neighbours[current])
                else:
                    neighbours = tuple(column_neighbours[current - n])
                next_vertex = neighbours[0] if neighbours[0] != previous else neighbours[1]
                previous, current = current, next_vertex
                edge_count += 1
            assert edge_count % 2 == 0
            half_lengths.append(edge_count // 2)
        return tuple(sorted(half_lengths, reverse=True))

    def search(row: int) -> None:
        nonlocal configurations, nodes
        nodes += 1
        if row == n:
            if all(degree == 2 for degree in column_degree):
                configurations += 1
                type_counts[component_partition()] += 1
            return

        rows_left = n - row - 1
        for first, second in pair_options:
            if column_degree[first] >= 2 or column_degree[second] >= 2:
                continue

            column_degree[first] += 1
            column_degree[second] += 1
            if any(
                degree > 2 or degree + rows_left < 2
                for degree in column_degree
            ):
                column_degree[first] -= 1
                column_degree[second] -= 1
                continue

            new_points = ((row, first), (row, second))
            bad = False
            for point in new_points:
                if any(
                    determinant(left, right, point) == 0
                    for left, right in combinations(selected, 2)
                ):
                    bad = True
                    break

            if not bad:
                selected.extend(new_points)
                row_columns[row] = (first, second)
                search(row + 1)
                row_columns[row] = None
                del selected[-2:]

            column_degree[first] -= 1
            column_degree[second] -= 1

    search(0)
    return configurations, type_counts, nodes


def main() -> None:
    configurations, type_counts, nodes = census(7)
    expected = Counter({
        (7,): 60,
        (5, 2): 32,
        (4, 3): 20,
        (3, 2, 2): 20,
    })
    assert configurations == 132
    assert type_counts == expected
    assert nodes == 51_967

    ordered = sum(count * 2 ** len(cycle_type) for cycle_type, count in type_counts.items())
    assert ordered == 488
    assert {
        cycle_type: count * 2 ** len(cycle_type)
        for cycle_type, count in type_counts.items()
    } == {
        (7,): 120,
        (5, 2): 128,
        (4, 3): 80,
        (3, 2, 2): 160,
    }

    print("side-seven relative-class census: PASS")
    print(f"configurations={configurations}, ordered_factors={ordered}, nodes={nodes}")
    print(dict(sorted(type_counts.items(), reverse=True)))


if __name__ == "__main__":
    main()
