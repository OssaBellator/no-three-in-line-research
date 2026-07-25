#!/usr/bin/env python3
"""Finite checks for PX249--PX252."""

from __future__ import annotations

import itertools
import math
import random
from collections import Counter


def maximum_degree(edges: set[tuple[int, int]], order: int) -> int:
    row_degree = [0] * order
    column_degree = [0] * order
    for row, column in edges:
        row_degree[row] += 1
        column_degree[column] += 1
    return max(row_degree + column_degree, default=0)


def has_perfect_matching(order: int, edges: set[tuple[int, int]]) -> bool:
    return any(
        all((row, permutation[row]) in edges for row in range(order))
        for permutation in itertools.permutations(range(order))
    )


def maximum_rectangle_matching(
    rows: set[int],
    columns: set[int],
    edges: set[tuple[int, int]],
) -> int:
    row_list = list(rows)
    column_list = list(columns)
    best = 0
    for size in range(1, min(len(row_list), len(column_list)) + 1):
        found = False
        for chosen_rows in itertools.combinations(row_list, size):
            for chosen_columns in itertools.combinations(column_list, size):
                for permutation in itertools.permutations(chosen_columns):
                    if all(
                        (chosen_rows[index], permutation[index]) in edges
                        for index in range(size)
                    ):
                        best = size
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return best


def check_hall_rectangles(seed: int = 249) -> None:
    rng = random.Random(seed)
    for order in range(3, 9):
        for _ in range(300):
            forbidden: set[tuple[int, int]] = set()
            for _layer in range(rng.randint(0, 2)):
                permutation = list(range(order))
                rng.shuffle(permutation)
                for row in range(order):
                    if rng.random() < 0.6:
                        forbidden.add((row, permutation[row]))

            delta = maximum_degree(forbidden, order)
            threshold = rng.randint(1, 3)
            weights = {
                (row, column): rng.randint(0, 3)
                for row in range(order)
                for column in range(order)
            }
            light = {
                (row, column)
                for row in range(order)
                for column in range(order)
                if (row, column) not in forbidden and weights[(row, column)] < threshold
            }
            if has_perfect_matching(order, light):
                continue

            witness_rows: set[int] | None = None
            witness_neighbours: set[int] | None = None
            for size in range(1, order + 1):
                for row_tuple in itertools.combinations(range(order), size):
                    rows = set(row_tuple)
                    neighbours = {
                        column
                        for row in rows
                        for column in range(order)
                        if (row, column) in light
                    }
                    if len(neighbours) < len(rows):
                        witness_rows = rows
                        witness_neighbours = neighbours
                        break
                if witness_rows is not None:
                    break

            assert witness_rows is not None
            assert witness_neighbours is not None
            columns = set(range(order)) - witness_neighbours
            assert len(witness_rows) + len(columns) >= order + 1

            heavy = {
                (row, column)
                for row in witness_rows
                for column in columns
                if (row, column) not in forbidden and weights[(row, column)] >= threshold
            }
            assert all(
                (row, column) in forbidden or (row, column) in heavy
                for row in witness_rows
                for column in columns
            )

            matching_size = maximum_rectangle_matching(witness_rows, columns, heavy)
            assert matching_size >= min(len(witness_rows), len(columns)) - delta


def random_matching(rng: random.Random, vertex_count: int, edge_count: int) -> list[tuple[int, int]]:
    vertices = list(range(vertex_count))
    rng.shuffle(vertices)
    return [
        tuple(sorted((vertices[2 * index], vertices[2 * index + 1])))
        for index in range(edge_count)
    ]


def maximum_coloured_matching(edges: list[tuple[int, int, int]]) -> int:
    best = 0

    def search(index: int, used: set[int], count: int) -> None:
        nonlocal best
        if index == len(edges):
            best = max(best, count)
            return
        if count + len(edges) - index <= best:
            return

        search(index + 1, used, count)
        _colour, first, second = edges[index]
        if first not in used and second not in used:
            search(index + 1, used | {first, second}, count + 1)

    search(0, set(), 0)
    return best


def check_coloured_star_overlap(seed: int = 250) -> None:
    rng = random.Random(seed)
    for vertex_count in range(4, 11):
        for colour_count in range(1, 5):
            for star_order in range(1, vertex_count // 2 + 1):
                for _ in range(30):
                    coloured_edges: list[tuple[int, int, int]] = []
                    for colour in range(colour_count):
                        for first, second in random_matching(rng, vertex_count, star_order):
                            coloured_edges.append((colour, first, second))

                    degree: Counter[int] = Counter()
                    for _colour, first, second in coloured_edges:
                        degree[first] += 1
                        degree[second] += 1
                    rho = max(degree.values(), default=0)
                    matching_size = maximum_coloured_matching(coloured_edges)
                    assert matching_size + 1e-12 >= len(coloured_edges) / (2 * rho)

                    loaded_vertex = max(degree, key=degree.get)
                    incident = [
                        edge for edge in coloured_edges if loaded_vertex in edge[1:]
                    ]
                    assert len(incident) == rho
                    for line_threshold in range(1, rho + 1):
                        partners = Counter(
                            second if first == loaded_vertex else first
                            for _colour, first, second in incident
                        )
                        if max(partners.values()) < line_threshold:
                            assert len(partners) >= rho / line_threshold


def check_type_extraction(seed: int = 251) -> None:
    rng = random.Random(seed)
    for pair_count in range(1, 100):
        for channel_count in range(1, 10):
            types = [rng.randrange(2 * channel_count) for _ in range(2 * pair_count)]
            incidence = Counter(types)
            chosen_type = max(incidence, key=incidence.get)
            represented_pairs = sum(
                types[2 * index] == chosen_type or types[2 * index + 1] == chosen_type
                for index in range(pair_count)
            )
            assert represented_pairs + 1e-12 >= pair_count / (2 * channel_count)


def check_residual_thresholds() -> None:
    for delta in range(1, 20):
        for residual_order in range(2 * delta, 10 * delta + 1):
            assert residual_order >= 2 * delta
        for residual_order in range(8 * delta, 10 * delta + 1):
            witness = 1 / (residual_order - 4 * delta)
            assert 1 / residual_order <= witness * (1 - witness) ** (2 * delta) + 1e-15


def main() -> None:
    check_hall_rectangles()
    check_coloured_star_overlap()
    check_type_extraction()
    check_residual_thresholds()
    print("PX249--PX252 coordinate star-field checks passed")


if __name__ == "__main__":
    main()
