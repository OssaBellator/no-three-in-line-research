#!/usr/bin/env python3
"""Finite checks for AC3ns--AC3nw."""

from __future__ import annotations

from collections import Counter
from itertools import combinations


def edge_list(size: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(size), 2))


def independent(mask: int, graph_mask: int, edges: tuple[tuple[int, int], ...]) -> bool:
    for index, (u, v) in enumerate(edges):
        if graph_mask >> index & 1 and mask >> u & 1 and mask >> v & 1:
            return False
    return True


def canonical_set(size: int, available: int, graph_mask: int) -> int:
    edges = edge_list(size)
    feasible = [
        mask
        for mask in range(1 << size)
        if mask & ~available == 0 and independent(mask, graph_mask, edges)
    ]
    maximum = max(mask.bit_count() for mask in feasible)
    # Integer mask order is the lexicographic order of the membership word read
    # from the highest candidate to the lowest.  Only determinism is needed.
    return min(mask for mask in feasible if mask.bit_count() == maximum)


def blocker_fibres(
    size: int,
    available: int,
    graph_mask: int,
    selected: int,
) -> dict[int, list[int]]:
    edges = edge_list(size)
    adjacency = [set() for _ in range(size)]
    for index, (u, v) in enumerate(edges):
        if graph_mask >> index & 1:
            adjacency[u].add(v)
            adjacency[v].add(u)
    fibres = {u: [] for u in range(size) if selected >> u & 1}
    for v in range(size):
        if not (available >> v & 1) or selected >> v & 1:
            continue
        neighbours = sorted(u for u in adjacency[v] if selected >> u & 1)
        assert neighbours
        fibres[neighbours[0]].append(v)
    return fibres


def verify_reconstruction_and_blockers(counts: Counter[str]) -> None:
    for size in range(1, 6):
        edges = edge_list(size)
        for graph_mask in range(1 << len(edges)):
            for available in range(1 << size):
                selected = canonical_set(size, available, graph_mask)
                alpha = selected.bit_count()
                assert selected & ~available == 0
                assert independent(selected, graph_mask, edges)

                for candidate in range(1 << size):
                    if candidate & ~available == 0 and independent(candidate, graph_mask, edges):
                        assert candidate.bit_count() <= alpha

                if available:
                    assert alpha >= 1
                    fibres = blocker_fibres(size, available, graph_mask, selected)
                    blocked = sum(len(values) for values in fibres.values())
                    assert blocked == available.bit_count() - alpha
                    maximum_fibre = max((len(values) for values in fibres.values()), default=0)
                    assert maximum_fibre * alpha >= blocked
                    delta = max((len(values) for values in fibres.values()), default=0)
                    assert available.bit_count() <= (delta + 1) * alpha
                counts["candidate systems"] += 1


def verify_atomic_rank_sensitivity(counts: Counter[str]) -> None:
    rotation_example = False
    for size in range(1, 6):
        edges = edge_list(size)
        for graph_mask in range(1 << len(edges)):
            for available in range(1 << size):
                selected = canonical_set(size, available, graph_mask)
                alpha = selected.bit_count()

                for vertex in range(size):
                    updated_available = available ^ (1 << vertex)
                    updated = canonical_set(size, updated_available, graph_mask)
                    assert abs(updated.bit_count() - alpha) <= 1
                    if (selected ^ updated).bit_count() >= 3:
                        rotation_example = True
                    counts["vertex updates"] += 1

                for edge_index in range(len(edges)):
                    updated_graph = graph_mask ^ (1 << edge_index)
                    updated = canonical_set(size, available, updated_graph)
                    assert abs(updated.bit_count() - alpha) <= 1
                    if (selected ^ updated).bit_count() >= 3:
                        rotation_example = True
                    counts["edge updates"] += 1
    assert rotation_example


def verify_consumption(counts: Counter[str]) -> None:
    for size in range(1, 6):
        edges = edge_list(size)
        for graph_mask in range(1 << len(edges)):
            available0 = (1 << size) - 1
            spent = 0
            steps = 0
            while True:
                available = available0 & ~spent
                selected = canonical_set(size, available, graph_mask)
                if selected == 0:
                    break
                chosen = (selected & -selected).bit_length() - 1
                old = spent.bit_count()
                spent |= 1 << chosen
                assert spent.bit_count() == old + 1
                steps += 1
            assert steps <= size
            assert spent.bit_count() == steps
            counts["consumption epochs"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_reconstruction_and_blockers(counts)
    verify_atomic_rank_sensitivity(counts)
    verify_consumption(counts)
    print("AC3ns--AC3nw compatible-subbank audit passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
