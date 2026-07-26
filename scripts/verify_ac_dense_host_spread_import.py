#!/usr/bin/env python3
"""Finite checks for AC5u--AC5x on complete and hole-deleted hosts."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import prod

Edge = tuple[int, int]
State = tuple[tuple[int, ...], tuple[int, ...]]
LabelledEdge = tuple[int, int, int]


def falling(value: int, rank: int) -> int:
    return prod(range(value - rank + 1, value + 1)) if rank else 1


def states(size: int, holes: frozenset[Edge]) -> list[State]:
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


def minimum_degree(size: int, holes: frozenset[Edge]) -> int:
    row_degrees = [size - sum((row, col) in holes for col in range(size)) for row in range(size)]
    col_degrees = [size - sum((row, col) in holes for row in range(size)) for col in range(size)]
    return min(row_degrees + col_degrees)


def switch(first: tuple[int, ...], i: int, u: int) -> tuple[int, ...]:
    out = list(first)
    out[i], out[u] = out[u], out[i]
    return tuple(out)


def valid_switch_rows(
    size: int,
    holes: frozenset[Edge],
    state: State,
    layer: int,
    row: int,
) -> list[int]:
    active = state[layer]
    other = state[1 - layer]
    target_col = active[row]
    rows: list[int] = []
    for partner in range(size):
        if partner == row:
            continue
        moved = switch(active, row, partner)
        if (row, moved[row]) in holes or (partner, moved[partner]) in holes:
            continue
        if any(moved[r] == other[r] for r in range(size)):
            continue
        assert moved[row] != target_col
        rows.append(partner)
    return rows


def verify_switching(
    size: int,
    holes: frozenset[Edge],
    omega: list[State],
    counts: Counter[str],
) -> None:
    d_min = minimum_degree(size, holes)
    lower = 2 * d_min - size - 3
    omega_set = set(omega)
    for state in omega:
        for layer in (0, 1):
            active = state[layer]
            for row in range(size):
                rows = valid_switch_rows(size, holes, state, layer, row)
                if lower > 0:
                    assert len(rows) >= lower
                for partner in rows:
                    moved = switch(active, row, partner)
                    child = (moved, state[1]) if layer == 0 else (state[0], moved)
                    assert child in omega_set
                    target_col = active[row]
                    assert child[layer][row] != target_col
                    reverse_rows = [
                        u
                        for u in range(size)
                        if u != row
                        and switch(child[layer], row, u)[row] == target_col
                    ]
                    assert reverse_rows == [partner]
                    counts["valid switches"] += 1


def labelled_edges(state: State) -> tuple[LabelledEdge, ...]:
    return tuple(
        (layer, row, state[layer][row])
        for layer in (0, 1)
        for row in range(len(state[0]))
    )


def verify_cylinders(
    size: int,
    holes: frozenset[Edge],
    omega: list[State],
    counts: Counter[str],
) -> None:
    d_min = minimum_degree(size, holes)
    lower = 2 * d_min - size - 3
    if lower < 1:
        return
    cylinder_counts: Counter[tuple[LabelledEdge, ...]] = Counter()
    max_rank = min(3, lower)
    for state in omega:
        edges = labelled_edges(state)
        for rank in range(1, max_rank + 1):
            for cylinder in combinations(edges, rank):
                cylinder_counts[tuple(sorted(cylinder))] += 1
    total = len(omega)
    for cylinder, multiplicity in cylinder_counts.items():
        rank = len(cylinder)
        assert multiplicity * falling(lower + 1, rank) <= total
        if lower >= 2:
            assert multiplicity * (lower - 1) ** rank <= total
        counts[f"rank-{rank} cylinders"] += 1


def host_samples(size: int) -> list[frozenset[Edge]]:
    edges = [(row, col) for row in range(size) for col in range(size)]
    samples = [frozenset()]
    samples.extend(frozenset({edge}) for edge in edges)
    if size <= 4:
        samples.extend(frozenset(pair) for pair in combinations(edges, 2))
    else:
        samples.extend(
            frozenset({edges[index], edges[-index - 1]})
            for index in range(min(12, len(edges) // 2))
        )
    return samples


def main() -> None:
    counts: Counter[str] = Counter()
    for size in range(3, 6):
        for holes in host_samples(size):
            omega = states(size, holes)
            if not omega:
                continue
            verify_switching(size, holes, omega, counts)
            verify_cylinders(size, holes, omega, counts)
            counts["hosts"] += 1
    print("AC5u--AC5x dense-host spread audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
