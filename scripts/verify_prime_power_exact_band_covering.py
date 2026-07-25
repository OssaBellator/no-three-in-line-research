#!/usr/bin/env python3
"""Finite checks for CMR372--CMR377's duplicated-row model."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from math import gcd

Cell = tuple[int, int]
Edge = tuple[str, int, int]


def primitive_height(first: Cell, second: Cell) -> int:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    common = gcd(abs(dx), abs(dy))
    return max(abs(dx // common), abs(dy // common))


def collinear(triple: tuple[Cell, Cell, Cell]) -> bool:
    (x1, y1), (x2, y2), (x3, y3) = triple
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def band_triples(t: int, height: int) -> list[tuple[Cell, Cell, Cell]]:
    cells = [(x, y) for x in range(t) for y in range(t)]
    result = []
    for triple in combinations(cells, 3):
        if len({x for x, _ in triple}) < 3 or len({y for _, y in triple}) < 3:
            continue
        if not collinear(triple):
            continue
        level = primitive_height(triple[0], triple[1])
        assert level == primitive_height(triple[0], triple[2])
        if height <= level < 2 * height:
            result.append(triple)
    return result


def verify_host_degrees(t: int, target: Cell) -> None:
    for _copy_name in ("Q", "R"):
        source_degree = Counter()
        row_degree = Counter()
        for x in range(t):
            for y in range(t):
                if (x, y) == target:
                    continue
                source_degree[x] += 1
                row_degree[y] += 1
        assert min(source_degree.values()) == t - 1
        assert max(source_degree.values()) == t
        assert min(row_degree.values()) == t - 1
        assert max(row_degree.values()) == t


def verify_main_band_bounds(t: int, height: int) -> None:
    triples = band_triples(t, height)
    degree = Counter()
    pair_degree = Counter()
    for triple in triples:
        edges = tuple(("Q", x, y) for x, y in triple)
        for edge in edges:
            degree[edge] += 1
        for pair in combinations(edges, 2):
            pair_degree[frozenset(pair)] += 1

    assert max(degree.values(), default=0) < 3 * t * t
    assert all(value * height < t for value in pair_degree.values())


def verify_mixed_copy_counts(t: int, height: int) -> None:
    triples = band_triples(t, height)
    by_type_edge_degree: dict[tuple[int, int], Counter[Edge]] = defaultdict(Counter)
    by_type_pair_degree: dict[
        tuple[int, int], Counter[frozenset[Edge]]
    ] = defaultdict(Counter)

    for triple in triples:
        for copies in product(("Q", "R"), repeat=3):
            reserve_count = copies.count("R")
            if reserve_count == 0:
                continue
            main_count = 3 - reserve_count
            edges = tuple(
                (copy_name, cell[0], cell[1])
                for copy_name, cell in zip(copies, triple)
            )
            key = (main_count, reserve_count)
            for edge in edges:
                by_type_edge_degree[key][edge] += 1
            for pair in combinations(edges, 2):
                by_type_pair_degree[key][frozenset(pair)] += 1

    reserve_degrees = [
        count
        for edge, count in by_type_edge_degree[(2, 1)].items()
        if edge[0] == "R"
    ]
    assert max(reserve_degrees, default=0) < 3 * t * t

    for pair, count in by_type_pair_degree[(2, 1)].items():
        if {edge[0] for edge in pair} == {"Q", "R"}:
            assert count * height < t

    for counter in by_type_pair_degree.values():
        for pair, count in counter.items():
            represented = {(edge[1], edge[2]) for edge in pair}
            if len(represented) == 2:
                assert count * height < t


def verify_row_copy_conflicts(t: int) -> None:
    for reserve_source in range(t):
        conflicts = []
        for row in range(t):
            reserve = ("R", reserve_source, row)
            for main_source in range(t):
                if main_source == reserve_source:
                    continue
                main = ("Q", main_source, row)
                conflicts.append((main, reserve))
        assert len(conflicts) == t * (t - 1)

        fixed_reserve_degree = Counter(reserve for _, reserve in conflicts)
        fixed_main_degree = Counter(main for main, _ in conflicts)
        assert max(fixed_reserve_degree.values()) == t - 1
        assert max(fixed_main_degree.values()) == 1


def verify_decoding(t: int, target: Cell) -> None:
    options = [
        (copy_name, row)
        for copy_name in ("Q", "R")
        for row in range(t)
    ]
    checked = 0
    for assignment in product(options, repeat=t):
        if any((x, choice[1]) == target for x, choice in enumerate(assignment)):
            continue
        main_rows = [row for copy_name, row in assignment if copy_name == "Q"]
        reserve_rows = [row for copy_name, row in assignment if copy_name == "R"]
        if len(main_rows) != len(set(main_rows)):
            continue
        if len(reserve_rows) != len(set(reserve_rows)):
            continue
        if set(main_rows) & set(reserve_rows):
            continue
        rows = [row for _, row in assignment]
        assert len(set(rows)) == t
        assert set(rows) == set(range(t))
        checked += 1
    assert checked > 0


def main() -> None:
    for t in (5, 7, 9):
        target = (0, 0)
        verify_host_degrees(t, target)
        verify_row_copy_conflicts(t)
        for height in range(1, (t + 1) // 2):
            verify_main_band_bounds(t, height)
            verify_mixed_copy_counts(t, height)

    verify_decoding(4, (0, 0))
    print(
        "verified exact-band covering model: duplicated hosts, row decoding, "
        "main/mixed band degrees, and reserve-copy conflict patterns"
    )


if __name__ == "__main__":
    main()
