#!/usr/bin/env python3
"""Verify hybrid-resonance bounds and alternating-cycle repair traps.

This script checks:
- ordered secants of one fixed direction have multiplicity at most the size of
  a no-three factor set;
- after fixing three coarse projections and two fine projections, at most two
  fine third points can complete a product collinearity;
- the canonical 2 x 3 crossed product host contains exact alternating-cycle
  local minima for both triple count and a natural pair-line refinement.

The finite searches are sanity checks and counterexample certificates, not an
asymptotic closure theorem.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from heapq import heappop, heappush
from itertools import combinations, permutations
from math import comb, gcd, inf

Point = tuple[int, int]
Permutation = tuple[int, ...]
FactorPair = tuple[Permutation, Permutation]


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


def factor_points(pair: FactorPair) -> tuple[Point, ...]:
    n = len(pair[0])
    return tuple(
        (x, pair[layer][x])
        for layer in (0, 1)
        for x in range(n)
    )


def primitive_direction(a: Point, b: Point) -> Point:
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    divisor = gcd(abs(dx), abs(dy))
    dx //= divisor
    dy //= divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx = -dx
        dy = -dy
    return dx, dy


def verify_direction_bound() -> None:
    for n in range(2, 6):
        maximum = 0
        for pair in valid_factor_pairs(n):
            points = factor_points(pair)
            counts = Counter(
                primitive_direction(a, b)
                for a in points
                for b in points
                if a != b
            )
            maximum = max(maximum, max(counts.values(), default=0))
            assert max(counts.values(), default=0) <= len(points)
        print(
            f"direction bound n={n}: pairs={len(valid_factor_pairs(n))}, "
            f"maximum ordered multiplicity={maximum}, cap={2 * n}"
        )


def flatten(
    m: int,
    n: int,
    i: int,
    j: int,
    u: int,
    v: int,
    orientation: str,
) -> Point:
    x = n * i + u if orientation[0] == "c" else m * u + i
    y = n * j + v if orientation[1] == "c" else m * v + j
    return x, y


def product_host(
    outer: FactorPair,
    inner: FactorPair,
    orientation: str,
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


def enumerate_degree_two_states(
    host: tuple[Point, ...],
) -> tuple[tuple[Point, ...], ...]:
    side = len(host) // 4
    rows = tuple(
        tuple(y for x, y in host if x == row)
        for row in range(side)
    )
    remaining = [[0] * side for _ in range(side + 1)]
    for row in range(side - 1, -1, -1):
        remaining[row] = remaining[row + 1].copy()
        for y in rows[row]:
            remaining[row][y] += 1

    states: list[tuple[Point, ...]] = []
    selected: list[Point] = []
    column_degree = [0] * side

    def search(row: int) -> None:
        if row == side:
            if column_degree == [2] * side:
                states.append(tuple(sorted(selected)))
            return

        for selected_columns in combinations(rows[row], 2):
            if any(column_degree[y] == 2 for y in selected_columns):
                continue
            for y in selected_columns:
                column_degree[y] += 1
            feasible = all(
                column_degree[y] <= 2
                and column_degree[y] + remaining[row + 1][y] >= 2
                for y in range(side)
            )
            if feasible:
                selected.extend(
                    ((row, selected_columns[0]), (row, selected_columns[1]))
                )
                search(row + 1)
                selected.pop()
                selected.pop()
            for y in selected_columns:
                column_degree[y] -= 1

    search(0)
    return tuple(states)


def single_cycle_neighbours(
    first: tuple[Point, ...],
    second: tuple[Point, ...],
) -> bool:
    difference = set(first) ^ set(second)
    if not difference:
        return False

    adjacency: dict[tuple[str, int], list[tuple[str, int]]] = defaultdict(list)
    for x, y in difference:
        row = ("r", x)
        column = ("c", y)
        adjacency[row].append(column)
        adjacency[column].append(row)
    if any(len(values) != 2 for values in adjacency.values()):
        return False

    start = next(iter(adjacency))
    seen = {start}
    stack = [start]
    while stack:
        vertex = stack.pop()
        for neighbour in adjacency[vertex]:
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return len(seen) == len(adjacency)


def line_key(a: Point, b: Point) -> tuple[int, int, int]:
    x_1, y_1 = a
    x_2, y_2 = b
    coefficient_x = y_2 - y_1
    coefficient_y = x_1 - x_2
    constant = -(coefficient_x * x_1 + coefficient_y * y_1)
    divisor = gcd(
        gcd(abs(coefficient_x), abs(coefficient_y)),
        abs(constant),
    )
    if divisor:
        coefficient_x //= divisor
        coefficient_y //= divisor
        constant //= divisor
    if coefficient_x < 0 or (
        coefficient_x == 0 and coefficient_y < 0
    ):
        coefficient_x = -coefficient_x
        coefficient_y = -coefficient_y
        constant = -constant
    return coefficient_x, coefficient_y, constant


def triple_potential(state: tuple[Point, ...]) -> int:
    return sum(
        determinant(*triple) == 0
        for triple in combinations(state, 3)
    )


def pair_line_energy(
    state: tuple[Point, ...],
    long_lines: tuple[frozenset[Point], ...],
) -> int:
    chosen = set(state)
    return sum(comb(len(chosen & line), 2) for line in long_lines)


def decompose(state: tuple[Point, ...]) -> FactorPair:
    side = len(state) // 2
    row_neighbours = {x: [] for x in range(side)}
    column_neighbours = {y: [] for y in range(side)}
    for x, y in state:
        row_neighbours[x].append(y)
        column_neighbours[y].append(x)

    colour: dict[Point, int] = {}
    for start in state:
        if start in colour:
            continue
        edge = start
        value = 0
        while edge not in colour:
            colour[edge] = value
            x, y = edge
            value ^= 1
            other_x = (
                column_neighbours[y][0]
                if column_neighbours[y][1] == x
                else column_neighbours[y][1]
            )
            column_edge = (other_x, y)
            if column_edge in colour:
                break
            colour[column_edge] = value
            value ^= 1
            other_y = (
                row_neighbours[other_x][0]
                if row_neighbours[other_x][1] == y
                else row_neighbours[other_x][1]
            )
            edge = (other_x, other_y)

    layers = [[-1] * side for _ in range(2)]
    for (x, y), value in colour.items():
        layers[value][x] = y
    return tuple(tuple(layer) for layer in layers)  # type: ignore[return-value]


def verify_repair_trap() -> None:
    outer: FactorPair = ((0, 1), (1, 0))
    inner: FactorPair = ((0, 2, 1), (1, 0, 2))
    host = product_host(outer, inner, "cf")
    states = enumerate_degree_two_states(host)
    assert len(states) == 546

    potentials = tuple(triple_potential(state) for state in states)
    assert Counter(potentials)[0] == 2

    neighbours: list[list[int]] = [[] for _ in states]
    for first in range(len(states)):
        for second in range(first + 1, len(states)):
            if single_cycle_neighbours(states[first], states[second]):
                neighbours[first].append(second)
                neighbours[second].append(first)
    assert sum(map(len, neighbours)) // 2 == 20944

    traps = [
        index
        for index, value in enumerate(potentials)
        if value > 0
        and all(potentials[neighbour] >= value for neighbour in neighbours[index])
    ]
    assert len(traps) == 10
    assert {potentials[index] for index in traps} == {1}

    barriers: list[int] = []
    for start in traps:
        distance = [inf] * len(states)
        distance[start] = potentials[start]
        queue: list[tuple[int, int]] = [(potentials[start], start)]
        while queue:
            barrier, vertex = heappop(queue)
            if barrier != distance[vertex]:
                continue
            if potentials[vertex] == 0:
                barriers.append(int(barrier))
                break
            for neighbour in neighbours[vertex]:
                candidate = max(barrier, potentials[neighbour])
                if candidate < distance[neighbour]:
                    distance[neighbour] = candidate
                    heappush(queue, (candidate, neighbour))
    assert barriers == [2] * 10

    lines: dict[tuple[int, int, int], set[Point]] = defaultdict(set)
    for first, second in combinations(host, 2):
        key = line_key(first, second)
        lines[key].update((first, second))
    long_lines = tuple(
        frozenset(points)
        for points in lines.values()
        if len(points) >= 3
    )
    pair_energy = tuple(
        pair_line_energy(state, long_lines)
        for state in states
    )
    lexicographic_traps = [
        index
        for index in range(len(states))
        if potentials[index] > 0
        and all(
            (potentials[neighbour], pair_energy[neighbour])
            >= (potentials[index], pair_energy[index])
            for neighbour in neighbours[index]
        )
    ]
    assert len(lexicographic_traps) == 4

    certificate = states[lexicographic_traps[0]]
    assert decompose(certificate) == (
        (1, 0, 2, 3, 5, 4),
        (2, 4, 5, 1, 0, 3),
    )
    bad_triples = tuple(
        triple
        for triple in combinations(certificate, 3)
        if determinant(*triple) == 0
    )
    assert bad_triples == (((2, 2), (3, 1), (4, 0)),)

    print(
        "2x3 cf repair graph: states=546, edges=20944, solutions=2, "
        "one-defect traps=10, barrier=2, lexicographic pair-energy traps=4"
    )
    print(
        f"explicit lexicographic trap layers={decompose(certificate)}, "
        f"bad={bad_triples[0]}"
    )


def verify_joint_fibre_bound() -> None:
    for m, n in ((2, 3), (3, 2), (3, 3)):
        maxima = {
            orientation: 0
            for orientation in ("cc", "cf", "fc", "ff")
        }
        for outer in valid_factor_pairs(m):
            coarse = factor_points(outer)
            for inner in valid_factor_pairs(n):
                fine = factor_points(inner)
                for orientation in maxima:
                    for coarse_0 in coarse:
                        for coarse_1 in coarse:
                            for coarse_2 in coarse:
                                for fine_0 in fine:
                                    for fine_1 in fine:
                                        point_0 = flatten(
                                            m,
                                            n,
                                            coarse_0[0],
                                            coarse_0[1],
                                            fine_0[0],
                                            fine_0[1],
                                            orientation,
                                        )
                                        point_1 = flatten(
                                            m,
                                            n,
                                            coarse_1[0],
                                            coarse_1[1],
                                            fine_1[0],
                                            fine_1[1],
                                            orientation,
                                        )
                                        if point_0 == point_1:
                                            continue
                                        count = 0
                                        for fine_2 in fine:
                                            point_2 = flatten(
                                                m,
                                                n,
                                                coarse_2[0],
                                                coarse_2[1],
                                                fine_2[0],
                                                fine_2[1],
                                                orientation,
                                            )
                                            if (
                                                point_2 not in (point_0, point_1)
                                                and determinant(
                                                    point_0,
                                                    point_1,
                                                    point_2,
                                                )
                                                == 0
                                            ):
                                                count += 1
                                        maxima[orientation] = max(
                                            maxima[orientation],
                                            count,
                                        )
                                        assert count <= 2
        print(f"joint fibre bound {m}x{n}: {maxima}")


def main() -> None:
    verify_direction_bound()
    verify_joint_fibre_bound()
    verify_repair_trap()


if __name__ == "__main__":
    main()
