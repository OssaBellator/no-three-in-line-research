#!/usr/bin/env python3
"""Finite checks for GC5a--GC5c's dense two-layer endpoint."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from math import prod

Cell = tuple[int, int]
State = tuple[tuple[int, ...], tuple[int, ...]]
LabelledCell = tuple[int, int, int]


def falling(value: int, rank: int) -> int:
    return prod(range(value - rank + 1, value + 1))


def collinear(a: Cell, b: Cell, c: Cell) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def host_states(size: int, holes: frozenset[Cell]) -> list[State]:
    perms = [
        perm
        for perm in permutations(range(size))
        if all((row, perm[row]) not in holes for row in range(size))
    ]
    return [
        (first, second)
        for first in perms
        for second in perms
        if all(first[row] != second[row] for row in range(size))
    ]


def minimum_degree(size: int, holes: frozenset[Cell]) -> int:
    row_degrees = [size - sum((row, col) in holes for col in range(size)) for row in range(size)]
    col_degrees = [size - sum((row, col) in holes for row in range(size)) for col in range(size)]
    return min(row_degrees + col_degrees)


def real_host_triples(size: int, holes: frozenset[Cell]) -> tuple[tuple[Cell, Cell, Cell], ...]:
    cells = [(row, col) for row in range(size) for col in range(size) if (row, col) not in holes]
    triples = []
    for triple in combinations(cells, 3):
        rows = {cell[0] for cell in triple}
        cols = {cell[1] for cell in triple}
        if len(rows) == 3 and len(cols) == 3 and collinear(*triple):
            triples.append(triple)
    return tuple(triples)


def state_labelled_edges(state: State) -> frozenset[LabelledCell]:
    size = len(state[0])
    return frozenset(
        (layer, row, state[layer][row])
        for layer in (0, 1)
        for row in range(size)
    )


def state_has_real_triple(state: State) -> bool:
    cells = {(row, state[layer][row]) for layer in (0, 1) for row in range(len(state[0]))}
    for triple in combinations(cells, 3):
        if len({cell[0] for cell in triple}) == 3 and len({cell[1] for cell in triple}) == 3:
            if collinear(*triple):
                return True
    return False


def host_samples(size: int) -> list[frozenset[Cell]]:
    cells = [(row, col) for row in range(size) for col in range(size)]
    samples = [frozenset()]
    samples.extend(frozenset({cell}) for cell in cells)
    if size <= 4:
        samples.extend(frozenset(pair) for pair in combinations(cells, 2))
    else:
        samples.extend(
            frozenset({cells[index], cells[-index - 1]})
            for index in range(min(12, len(cells) // 2))
        )
    return samples


def verify_host(size: int, holes: frozenset[Cell], counts: Counter[str]) -> None:
    omega = host_states(size, holes)
    if not omega:
        return
    d_min = minimum_degree(size, holes)
    lower = 2 * d_min - size - 3
    real_triples = real_host_triples(size, holes)
    labelled_counts: Counter[tuple[LabelledCell, ...]] = Counter()
    state_edges = [state_labelled_edges(state) for state in omega]

    for triple in real_triples:
        for layers in product((0, 1), repeat=3):
            labelled = tuple(sorted((layers[index],) + triple[index] for index in range(3)))
            compatible = True
            for layer in (0, 1):
                layer_cells = [(row, col) for assigned, row, col in labelled if assigned == layer]
                if len({row for row, _ in layer_cells}) != len(layer_cells):
                    compatible = False
                if len({col for _, col in layer_cells}) != len(layer_cells):
                    compatible = False
            if not compatible:
                continue
            multiplicity = sum(set(labelled).issubset(edges) for edges in state_edges)
            if multiplicity:
                labelled_counts[labelled] = multiplicity

    if lower >= 3:
        denominator = falling(lower + 1, 3)
        for multiplicity in labelled_counts.values():
            assert multiplicity * denominator <= len(omega)
            counts["rank-three cylinders"] += 1
        if 8 * len(real_triples) < denominator:
            assert any(not state_has_real_triple(state) for state in omega)
            counts["successful first-moment hosts"] += 1

    counts["hosts"] += 1
    counts["states"] += len(omega)


def verify_complete_order_six_rank_three(counts: Counter[str]) -> None:
    """Exercise the first nonvacuous rank-three switching denominator."""
    size = 6
    omega = host_states(size, frozenset())
    assert len(omega) == 190_800
    state_edges = [state_labelled_edges(state) for state in omega]
    triple = ((0, 0), (1, 1), (2, 2))
    assert collinear(*triple)
    lower = size - 3
    denominator = falling(lower + 1, 3)
    assert denominator == 24
    for layers in product((0, 1), repeat=3):
        labelled = tuple(sorted((layers[index],) + triple[index] for index in range(3)))
        multiplicity = sum(set(labelled).issubset(edges) for edges in state_edges)
        assert multiplicity * denominator <= len(omega)
        counts["order-six rank-three samples"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    for size in range(3, 6):
        for holes in host_samples(size):
            verify_host(size, holes, counts)
    verify_complete_order_six_rank_three(counts)
    print("GC5a--GC5c all-n endpoint audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
