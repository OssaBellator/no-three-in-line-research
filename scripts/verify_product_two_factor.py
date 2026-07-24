#!/usr/bin/env python3
"""Exact search for no-three degree-two states in factor-product hosts.

The search enlarges the cycle-phase family to every spanning degree-two
subgraph of the four-regular product host.  It also constructs the equivalent
width-three CNF and checks small exact model counts.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations, permutations

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]
Orientation = str

ORIENTATIONS: tuple[Orientation, ...] = ("cc", "cf", "fc", "ff")

EXPECTED: dict[tuple[int, int], dict[Orientation, tuple[int, int]]] = {
    (2, 2): {"cc": (4, 44), "cf": (4, 44), "fc": (4, 44), "ff": (4, 44)},
    (2, 3): {"cc": (0, 0), "cf": (8, 16), "fc": (8, 16), "ff": (0, 0)},
    (3, 2): {"cc": (0, 0), "cf": (8, 16), "fc": (8, 16), "ff": (0, 0)},
    (3, 3): {"cc": (0, 0), "cf": (8, 16), "fc": (8, 16), "ff": (0, 0)},
    (2, 4): {"cc": (0, 0), "cf": (32, 64), "fc": (32, 64), "ff": (40, 96)},
    (4, 2): {"cc": (40, 96), "cf": (32, 64), "fc": (32, 64), "ff": (0, 0)},
    (2, 5): {"cc": (0, 0), "cf": (0, 0), "fc": (0, 0), "ff": (0, 0)},
    (5, 2): {"cc": (0, 0), "cf": (0, 0), "fc": (0, 0), "ff": (0, 0)},
}


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def is_no_three(points: list[Point] | tuple[Point, ...]) -> bool:
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
    orientation: Orientation,
) -> Point:
    row_mode, column_mode = orientation
    x = n * i + u if row_mode == "c" else m * u + i
    y = n * j + v if column_mode == "c" else m * v + j
    return x, y


def product_host(
    outer: FactorPair,
    inner: FactorPair,
    orientation: Orientation,
) -> tuple[Point, ...]:
    m = len(outer[0])
    n = len(inner[0])
    cells = {
        flatten(m, n, i, outer[r][i], u, inner[s][u], orientation)
        for r in (0, 1)
        for s in (0, 1)
        for i in range(m)
        for u in range(n)
    }
    assert len(cells) == 4 * m * n
    return tuple(sorted(cells))


def verify_host(host: tuple[Point, ...]) -> None:
    side = len(host) // 4
    assert len(host) == 4 * side
    for x in range(side):
        assert sum(px == x for px, _ in host) == 4
    for y in range(side):
        assert sum(py == y for _, py in host) == 4


def count_no_three_two_factors(
    host: tuple[Point, ...],
) -> tuple[int, tuple[Point, ...] | None, int]:
    side = len(host) // 4
    rows = tuple(tuple(y for x, y in host if x == row) for row in range(side))
    assert all(len(row) == 4 for row in rows)

    remaining_incidence = [[0] * side for _ in range(side + 1)]
    for row in range(side - 1, -1, -1):
        remaining_incidence[row] = remaining_incidence[row + 1].copy()
        for y in rows[row]:
            remaining_incidence[row][y] += 1

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
    model_count = 0
    first_model: tuple[Point, ...] | None = None
    nodes = 0

    def search(row: int) -> None:
        nonlocal model_count, first_model, nodes, chosen_mask
        nodes += 1
        if row == side:
            if column_degree == [2] * side:
                model_count += 1
                if first_model is None:
                    first_model = tuple(chosen)
            return

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
            chosen.extend(new_points)
            added_mask = (1 << index[new_points[0]]) | (1 << index[new_points[1]])
            chosen_mask |= added_mask

            feasible = all(
                column_degree[y] <= 2
                and column_degree[y] + remaining_incidence[row + 1][y] >= 2
                for y in range(side)
            )
            if feasible:
                search(row + 1)

            chosen.pop()
            chosen.pop()
            chosen_mask ^= added_mask
            for y in selected_columns:
                column_degree[y] -= 1

    search(0)
    return model_count, first_model, nodes


def verify_two_factor(
    host: tuple[Point, ...],
    selected: tuple[Point, ...],
) -> None:
    side = len(host) // 4
    assert set(selected).issubset(host)
    assert len(selected) == 2 * side
    for x in range(side):
        assert sum(px == x for px, _ in selected) == 2
    for y in range(side):
        assert sum(py == y for _, py in selected) == 2
    assert is_no_three(selected)


def decompose_two_factor(selected: tuple[Point, ...]) -> FactorPair:
    side = len(selected) // 2
    row_neighbors = {x: [] for x in range(side)}
    column_neighbors = {y: [] for y in range(side)}
    for x, y in selected:
        row_neighbors[x].append(y)
        column_neighbors[y].append(x)
    assert all(len(values) == 2 for values in row_neighbors.values())
    assert all(len(values) == 2 for values in column_neighbors.values())

    edge_colour: dict[Point, int] = {}
    for start in selected:
        if start in edge_colour:
            continue
        edge = start
        colour = 0
        while edge not in edge_colour:
            edge_colour[edge] = colour
            x, y = edge
            colour ^= 1
            other_x = (
                column_neighbors[y][0]
                if column_neighbors[y][1] == x
                else column_neighbors[y][1]
            )
            column_edge = (other_x, y)
            if column_edge in edge_colour:
                break
            edge_colour[column_edge] = colour
            colour ^= 1
            other_y = (
                row_neighbors[other_x][0]
                if row_neighbors[other_x][1] == y
                else row_neighbors[other_x][1]
            )
            edge = (other_x, other_y)

    layers = [[-1] * side for _ in range(2)]
    for (x, y), colour in edge_colour.items():
        layers[colour][x] = y
    pair = (tuple(layers[0]), tuple(layers[1]))
    assert all(sorted(layer) == list(range(side)) for layer in pair)
    assert all(pair[0][x] != pair[1][x] for x in range(side))
    return pair


def exact_two_cnf(host: tuple[Point, ...]) -> tuple[tuple[int, ...], ...]:
    """Return the exact degree-two plus no-three 3-CNF for the product host."""
    side = len(host) // 4
    variable = {cell: index + 1 for index, cell in enumerate(host)}
    clauses: set[tuple[int, ...]] = set()

    for coordinate in (0, 1):
        for value in range(side):
            incident = [
                variable[cell]
                for cell in host
                if cell[coordinate] == value
            ]
            assert len(incident) == 4
            for triple in combinations(incident, 3):
                clauses.add(tuple(sorted(triple)))
                clauses.add(tuple(sorted((-literal for literal in triple))))

    for triple in combinations(host, 3):
        if determinant(*triple) == 0:
            clauses.add(tuple(sorted((-variable[cell] for cell in triple))))

    assert all(1 <= len(clause) <= 3 for clause in clauses)
    return tuple(sorted(clauses))


def count_cnf_models(
    variable_count: int,
    clauses: tuple[tuple[int, ...], ...],
) -> int:
    count = 0
    for mask in range(1 << variable_count):
        if all(
            any(
                bool(mask & (1 << (abs(literal) - 1))) == (literal > 0)
                for literal in clause
            )
            for clause in clauses
        ):
            count += 1
    return count


def verify_cnf_equivalence() -> None:
    outer = valid_factor_pairs(2)[0]
    inner = valid_factor_pairs(2)[0]
    for orientation in ORIENTATIONS:
        host = product_host(outer, inner, orientation)
        direct_count, _, _ = count_no_three_two_factors(host)
        clauses = exact_two_cnf(host)
        cnf_count = count_cnf_models(len(host), clauses)
        assert direct_count == cnf_count == 11
    print("2x2 CNF equivalence: 11 models in every orientation")


def run_case(m: int, n: int, build_cnf: bool = False) -> None:
    instance_count = len(valid_factor_pairs(m)) * len(valid_factor_pairs(n))
    totals = {orientation: [0, 0, 0] for orientation in ORIENTATIONS}
    witnesses: dict[Orientation, FactorPair] = {}

    for outer in valid_factor_pairs(m):
        for inner in valid_factor_pairs(n):
            for orientation in ORIENTATIONS:
                host = product_host(outer, inner, orientation)
                verify_host(host)
                count, first, nodes = count_no_three_two_factors(host)
                totals[orientation][0] += int(count > 0)
                totals[orientation][1] += count
                totals[orientation][2] += nodes
                if first is not None:
                    verify_two_factor(host, first)
                    witnesses.setdefault(
                        orientation,
                        decompose_two_factor(first),
                    )
                if build_cnf:
                    clauses = exact_two_cnf(host)
                    assert clauses

    expected = EXPECTED[(m, n)]
    for orientation, values in totals.items():
        assert (values[0], values[1]) == expected[orientation], (
            m,
            n,
            orientation,
            values,
            expected[orientation],
        )

    summary = ", ".join(
        f"{orientation}: instances={values[0]}/{instance_count}, "
        f"models={values[1]}, nodes={values[2]}"
        for orientation, values in totals.items()
    )
    print(f"m={m}, n={n}: {summary}")
    for orientation, pair in witnesses.items():
        print(f"  first {orientation} witness: {pair}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    parser.add_argument("--cnf", action="store_true")
    args = parser.parse_args()

    verify_cnf_equivalence()

    cases = [(2, 2), (2, 3), (3, 2), (3, 3)]
    if args.extended:
        cases.extend([(2, 4), (4, 2), (2, 5), (5, 2)])
    for m, n in cases:
        run_case(m, n, build_cnf=args.cnf)


if __name__ == "__main__":
    main()
