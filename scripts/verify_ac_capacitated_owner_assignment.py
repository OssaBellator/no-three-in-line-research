#!/usr/bin/env python3
"""Exhaustive checks for AC3ni--AC3nm on small capacitated graphs."""

from __future__ import annotations

from itertools import product
from typing import Iterable

Assignment = tuple[int, ...]
Edge = tuple[int, int]


def feasible_assignments(
    demand_count: int,
    owner_count: int,
    edges: set[Edge],
    residual: tuple[int, ...],
) -> Iterable[Assignment]:
    sentinel = owner_count
    for assignment in product(range(owner_count + 1), repeat=demand_count):
        degree = [0] * owner_count
        valid = True
        for demand, owner in enumerate(assignment):
            if owner == sentinel:
                continue
            if (demand, owner) not in edges:
                valid = False
                break
            degree[owner] += 1
            if degree[owner] > residual[owner]:
                valid = False
                break
        if valid:
            yield assignment


def rank(assignment: Assignment, owner_count: int) -> int:
    return sum(owner < owner_count for owner in assignment)


def canonical_assignment(
    demand_count: int,
    owner_count: int,
    edges: set[Edge],
    residual: tuple[int, ...],
) -> Assignment:
    assignments = list(
        feasible_assignments(demand_count, owner_count, edges, residual)
    )
    best_rank = max(rank(assignment, owner_count) for assignment in assignments)
    return min(
        assignment
        for assignment in assignments
        if rank(assignment, owner_count) == best_rank
    )


def has_capacitated_hall_defect(
    demand_count: int,
    owner_count: int,
    edges: set[Edge],
    residual: tuple[int, ...],
) -> bool:
    for mask in range(1, 1 << demand_count):
        demands = [d for d in range(demand_count) if mask & (1 << d)]
        neighbours = {
            owner
            for demand in demands
            for owner in range(owner_count)
            if (demand, owner) in edges
        }
        if sum(residual[owner] for owner in neighbours) < len(demands):
            return True
    return False


def edge_set(all_edges: list[Edge], mask: int) -> set[Edge]:
    return {
        edge for index, edge in enumerate(all_edges) if mask & (1 << index)
    }


def symmetric_difference_size(
    left: Assignment, right: Assignment, owner_count: int
) -> int:
    return sum(
        a != b and (a < owner_count or b < owner_count)
        for a, b in zip(left, right)
    )


def verify() -> None:
    checked_states = 0
    checked_updates = 0
    largest_rotation = 0
    rotation_witness: tuple[object, ...] | None = None

    for demand_count in range(1, 4):
        for owner_count in range(1, 4):
            all_edges = [
                (demand, owner)
                for demand in range(demand_count)
                for owner in range(owner_count)
            ]
            for mask in range(1 << len(all_edges)):
                edges = edge_set(all_edges, mask)
                for residual in product(range(3), repeat=owner_count):
                    canonical = canonical_assignment(
                        demand_count, owner_count, edges, residual
                    )
                    maximum_rank = rank(canonical, owner_count)
                    assert (maximum_rank < demand_count) == (
                        has_capacitated_hall_defect(
                            demand_count, owner_count, edges, residual
                        )
                    )
                    checked_states += 1

                    for edge in all_edges:
                        changed_edges = set(edges)
                        if edge in changed_edges:
                            changed_edges.remove(edge)
                        else:
                            changed_edges.add(edge)
                        changed = canonical_assignment(
                            demand_count,
                            owner_count,
                            changed_edges,
                            residual,
                        )
                        changed_rank = rank(changed, owner_count)
                        assert abs(changed_rank - maximum_rank) <= 1
                        rotation = symmetric_difference_size(
                            canonical, changed, owner_count
                        )
                        if rotation > largest_rotation:
                            largest_rotation = rotation
                            rotation_witness = (
                                demand_count,
                                owner_count,
                                edges,
                                residual,
                                edge,
                                canonical,
                                changed,
                            )
                        checked_updates += 1

                    for owner in range(owner_count):
                        for delta in (-1, 1):
                            new_capacity = residual[owner] + delta
                            if not 0 <= new_capacity <= 2:
                                continue
                            changed_residual = list(residual)
                            changed_residual[owner] = new_capacity
                            changed = canonical_assignment(
                                demand_count,
                                owner_count,
                                edges,
                                tuple(changed_residual),
                            )
                            changed_rank = rank(changed, owner_count)
                            assert abs(changed_rank - maximum_rank) <= 1
                            rotation = symmetric_difference_size(
                                canonical, changed, owner_count
                            )
                            if rotation > largest_rotation:
                                largest_rotation = rotation
                                rotation_witness = (
                                    demand_count,
                                    owner_count,
                                    edges,
                                    residual,
                                    (owner, delta),
                                    canonical,
                                    changed,
                                )
                            checked_updates += 1

    assert largest_rotation >= 2
    print(
        "verified",
        checked_states,
        "states and",
        checked_updates,
        "atomic updates;",
        "largest canonical rotation =",
        largest_rotation,
    )
    print("rotation witness:", rotation_witness)


if __name__ == "__main__":
    verify()
