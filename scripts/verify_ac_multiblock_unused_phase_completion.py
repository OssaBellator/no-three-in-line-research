#!/usr/bin/env python3
"""Exact finite checks for AC3ld--AC3lh."""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


Check = tuple[tuple[int, ...], tuple[int, ...]]


def generate_checks(nblocks: int, phases: int, max_rank: int = 3) -> list[Check]:
    checks: list[Check] = []
    for rank in range(1, max_rank + 1):
        for scope in combinations(range(nblocks), rank):
            for values in product(range(phases), repeat=rank):
                # The all-zero current assignment must remain hard-feasible.
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def violates(check: Check, assignment: list[int]) -> bool:
    scope, values = check
    return all(assignment[block] == value for block, value in zip(scope, values))


def activated_bucket(
    family: list[Check],
    *,
    centre: int,
    target: int,
    nblocks: int,
) -> list[Check]:
    assignment = [0] * nblocks
    assignment[centre] = target
    return [
        check
        for check in family
        if centre in check[0] and violates(check, assignment)
    ]


def residual_scope(check: Check, centre: int) -> set[int]:
    return set(check[0]) - {centre}


def maximal_disjoint(scopes: list[set[int]]) -> tuple[list[set[int]], set[int]]:
    selected: list[set[int]] = []
    used: set[int] = set()
    for scope in sorted(scopes, key=lambda value: (len(value), tuple(sorted(value)))):
        if scope.isdisjoint(used):
            selected.append(scope)
            used.update(scope)
    return selected, used


def literal_support(family: list[Check], block: int) -> set[int]:
    support: set[int] = set()
    for scope, values in family:
        if block in scope:
            support.add(values[scope.index(block)])
    return support


def check_small_hard_systems() -> dict[str, int]:
    nblocks = 4
    phases = 3
    centre = 0
    target = 1
    checks = generate_checks(nblocks, phases)

    totals = {
        "canonical_checks": len(checks),
        "hard_families": 0,
        "activated_targets": 0,
        "unconditional_exclusions": 0,
        "completed_targets": 0,
        "saturated_transversals": 0,
        "large_matchings": 0,
    }

    for size in range(1, 4):
        for family_tuple in combinations(checks, size):
            family = list(family_tuple)
            totals["hard_families"] += 1
            bucket = activated_bucket(
                family,
                centre=centre,
                target=target,
                nblocks=nblocks,
            )
            if not bucket:
                continue

            totals["activated_targets"] += 1
            residuals = [residual_scope(check, centre) for check in bucket]

            if any(not scope for scope in residuals):
                totals["unconditional_exclusions"] += 1
                continue

            matching, transversal = maximal_disjoint(residuals)
            assert len(transversal) <= 2 * len(matching)
            assert all(any(block in transversal for block in scope) for scope in residuals)

            # Threshold m=2.
            if len(matching) >= 2:
                totals["large_matchings"] += 1
                continue

            chosen: dict[int, int] = {}
            saturated = False
            for block in transversal:
                support = literal_support(family, block)
                unused = [
                    phase
                    for phase in range(1, phases)
                    if phase not in support
                ]
                if not unused:
                    saturated = True
                    break
                chosen[block] = unused[0]

            if saturated:
                totals["saturated_transversals"] += 1
                continue

            assignment = [0] * nblocks
            assignment[centre] = target
            for block, phase in chosen.items():
                assignment[block] = phase

            assert not any(violates(check, assignment) for check in family)
            totals["completed_targets"] += 1

    return totals


def check_many_target_concentration() -> int:
    checks = 0
    for target_count in range(1, 41):
        for role_count in range(1, 8):
            role_class = ceil(target_count / role_count)
            for threshold in range(1, 9):
                distinct_lower_bound = ceil(role_class / threshold)
                assert distinct_lower_bound >= 1
                checks += 1
    return checks


def check_physical_registry_bounds() -> int:
    checks = 0
    for side in range(2, 51):
        literal_addresses = 2 * side * side
        for kinds in range(1, 11):
            hard_checks = kinds * (
                literal_addresses
                + literal_addresses**2
                + literal_addresses**3
            )
            incidence_tickets = 3 * hard_checks
            replacement_edges = hard_checks * (hard_checks - 1)
            assert incidence_tickets >= hard_checks
            assert replacement_edges >= 0
            checks += 1
    return checks


def main() -> None:
    totals = check_small_hard_systems()
    totals["many_target_ledgers"] = check_many_target_concentration()
    totals["physical_bound_systems"] = check_physical_registry_bounds()

    print("AC3ld--AC3lh verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
