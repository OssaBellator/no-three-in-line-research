#!/usr/bin/env python3
"""Verify the exact high-load peeling certificate for small hypergraphs."""

from __future__ import annotations

from itertools import combinations

Conflict = frozenset[int]


def peel(
    size: int, conflicts: tuple[Conflict, ...], threshold: int
) -> tuple[list[int], tuple[Conflict, ...], list[tuple[int, tuple[Conflict, ...]]]]:
    active = set(conflicts)
    deleted: list[int] = []
    charges: list[tuple[int, tuple[Conflict, ...]]] = []

    while True:
        loads = [
            sum(vertex in conflict for conflict in active)
            if vertex not in deleted
            else 0
            for vertex in range(size)
        ]
        vertex = next(
            (
                candidate
                for candidate in range(size)
                if candidate not in deleted and loads[candidate] > threshold
            ),
            None,
        )
        if vertex is None:
            break
        removed = tuple(
            conflict for conflict in active if vertex in conflict
        )
        assert len(removed) > threshold
        charges.append((vertex, removed))
        active.difference_update(removed)
        deleted.append(vertex)

    return deleted, tuple(active), charges


def verify_instance(
    size: int, conflicts: tuple[Conflict, ...], threshold: int
) -> None:
    deleted, residual, charges = peel(size, conflicts, threshold)
    assert all(
        sum(vertex in conflict for conflict in residual) <= threshold
        for vertex in range(size)
        if vertex not in deleted
    )
    charged = [conflict for _, batch in charges for conflict in batch]
    assert len(charged) == len(set(charged))
    assert set(charged).isdisjoint(residual)
    assert set(charged) | set(residual) == set(conflicts)
    if deleted:
        assert len(deleted) * threshold < len(charged) <= len(conflicts)


def verify(max_size: int = 4) -> None:
    for size in range(2, max_size + 1):
        possible = tuple(
            frozenset(scope)
            for rank in range(2, min(3, size) + 1)
            for scope in combinations(range(size), rank)
        )
        for mask in range(1 << len(possible)):
            conflicts = tuple(
                conflict
                for index, conflict in enumerate(possible)
                if mask & (1 << index)
            )
            for threshold in range(1, len(conflicts) + 2):
                verify_instance(size, conflicts, threshold)

    size = 5
    triples = tuple(
        frozenset(scope) for scope in combinations(range(size), 3)
    )
    for mask in range(1 << len(triples)):
        conflicts = tuple(
            conflict
            for index, conflict in enumerate(triples)
            if mask & (1 << index)
        )
        for threshold in range(1, 5):
            verify_instance(size, conflicts, threshold)


def main() -> None:
    verify()
    print("candidate-conflict peeling: verified on small pair/triple hypergraphs")


if __name__ == "__main__":
    main()
