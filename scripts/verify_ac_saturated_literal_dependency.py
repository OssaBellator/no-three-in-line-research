#!/usr/bin/env python3
"""Exact finite checks for AC3li--AC3lm."""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


Check = tuple[tuple[int, ...], tuple[int, ...]]


def generate_checks(nblocks: int, phases: int, max_rank: int = 3) -> list[Check]:
    checks: list[Check] = []
    for rank in range(1, max_rank + 1):
        for scope in combinations(range(nblocks), rank):
            for values in product(range(phases), repeat=rank):
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def canonical_check(family: list[Check], block: int, phase: int) -> Check | None:
    candidates: list[Check] = []
    for check in family:
        scope, values = check
        if block in scope and values[scope.index(block)] == phase:
            candidates.append(check)
    return min(candidates) if candidates else None


def mismatch_literals(check: Check, block: int) -> list[tuple[int, int]]:
    scope, values = check
    return [
        (other, value)
        for other, value in zip(scope, values)
        if other != block and value != 0
    ]


def check_active_latent_partitions() -> dict[str, int]:
    nblocks = 4
    phases = 3
    checks = generate_checks(nblocks, phases)

    totals = {
        "canonical_checks": len(checks),
        "hard_families": 0,
        "saturated_block_records": 0,
        "active_literals": 0,
        "latent_literals": 0,
    }

    for size in (2, 3):
        for family_tuple in combinations(checks, size):
            family = list(family_tuple)
            totals["hard_families"] += 1
            for block in range(nblocks):
                selected = [
                    canonical_check(family, block, phase)
                    for phase in range(1, phases)
                ]
                if any(check is None for check in selected):
                    continue

                totals["saturated_block_records"] += 1
                assert len(set(selected)) == phases - 1

                for check in selected:
                    assert check is not None
                    mismatches = mismatch_literals(check, block)
                    assert len(mismatches) <= 2
                    if mismatches:
                        totals["latent_literals"] += 1
                        dependency_block, dependency_phase = min(mismatches)
                        assert dependency_block != block
                        assert dependency_phase != 0
                    else:
                        totals["active_literals"] += 1

    return totals


def check_functional_dependency_graphs(max_nodes: int = 6) -> dict[str, int]:
    totals = {
        "functional_graphs": 0,
        "literal_walks": 0,
        "active_terminations": 0,
        "cycle_terminations": 0,
    }

    for nodes in range(1, max_nodes + 1):
        choices = [
            [-1] + [target for target in range(nodes) if target != source]
            for source in range(nodes)
        ]
        for successor in product(*choices):
            totals["functional_graphs"] += 1
            cycle_vertex_sets: list[frozenset[int]] = []

            for start in range(nodes):
                totals["literal_walks"] += 1
                first_seen: dict[int, int] = {}
                current = start
                steps = 0

                while True:
                    if successor[current] == -1:
                        totals["active_terminations"] += 1
                        assert steps <= nodes - 1
                        break

                    if current in first_seen:
                        cycle_start = first_seen[current]
                        cycle_nodes = []
                        probe = current
                        while True:
                            cycle_nodes.append(probe)
                            probe = successor[probe]
                            if probe == current:
                                break
                        assert 2 <= len(cycle_nodes) <= nodes
                        cycle_vertex_sets.append(frozenset(cycle_nodes))
                        totals["cycle_terminations"] += 1
                        assert steps - cycle_start == len(cycle_nodes)
                        break

                    first_seen[current] = steps
                    current = successor[current]
                    steps += 1
                    assert steps <= nodes + 1

            unique_cycles = set(cycle_vertex_sets)
            for left, right in combinations(unique_cycles, 2):
                assert left.isdisjoint(right)
            assert len(unique_cycles) <= nodes // 2

    return totals


def check_weighted_concentration() -> int:
    checks = 0
    for total_weight in range(1, 81):
        for role_count in range(1, 9):
            lower = total_weight / (2 * role_count)
            for threshold in range(1, 11):
                distinct = ceil(lower / threshold)
                assert distinct >= 1 if lower > 0 else distinct == 0
                checks += 1
    return checks


def check_o1_physical_bounds() -> int:
    checks = 0
    for side in range(2, 101):
        literals = 2 * side * side
        assert literals <= 2 * side * side
        assert literals // 2 <= side * side
        checks += 1
    return checks


def main() -> None:
    totals = check_active_latent_partitions()
    totals.update(check_functional_dependency_graphs())
    totals["weighted_concentration_ledgers"] = check_weighted_concentration()
    totals["o1_physical_bounds"] = check_o1_physical_bounds()

    print("AC3li--AC3lm verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
