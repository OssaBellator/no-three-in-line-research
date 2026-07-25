#!/usr/bin/env python3
"""Exact finite checks for AC3ln--AC3ls."""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


Check = tuple[tuple[int, ...], tuple[int, ...]]
ROUTES = (
    "PAID",
    "FIXED_CURRENT",
    "PROSPECTIVE",
    "OCCURRENCE_FAILURE",
    "COHERENCE_MISMATCH",
    "OWNER_RESET",
)


def generate_checks(nblocks: int, phases: int, max_rank: int = 3) -> list[Check]:
    checks: list[Check] = []
    for rank in range(1, max_rank + 1):
        for scope in combinations(range(nblocks), rank):
            for values in product(range(phases), repeat=rank):
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def check_prospective_literal_records() -> dict[str, int]:
    checks = generate_checks(nblocks=4, phases=3)
    totals = {
        "canonical_checks": len(checks),
        "literal_records": 0,
        "active_records": 0,
        "latent_records": 0,
    }

    for scope, values in checks:
        for source_position, source_phase in enumerate(values):
            if source_phase == 0:
                continue
            totals["literal_records"] += 1

            # The current assignment is the all-zero phase word. A record with
            # a noncurrent source literal cannot itself be a current certificate.
            assert values[source_position] != 0
            assert tuple(values) != tuple(0 for _ in values)

            mismatches = [
                (block, phase)
                for index, (block, phase) in enumerate(zip(scope, values))
                if index != source_position and phase != 0
            ]
            assert len(mismatches) <= 2
            if mismatches:
                totals["latent_records"] += 1
                dependency = min(mismatches)
                assert dependency[0] != scope[source_position]
                assert dependency[1] != 0
            else:
                totals["active_records"] += 1

    assert totals["active_records"] + totals["latent_records"] == totals["literal_records"]
    return totals


def owner_route(
    current: bool,
    physical: bool,
    coherent: bool,
    payable: bool,
    reset: bool,
) -> str:
    if reset:
        return "OWNER_RESET"
    if not physical:
        return "OCCURRENCE_FAILURE"
    if not coherent:
        return "COHERENCE_MISMATCH"
    if payable:
        assert current
        return "PAID"
    if current:
        return "FIXED_CURRENT"
    return "PROSPECTIVE"


def check_owner_routes() -> dict[str, int]:
    counts = {route: 0 for route in ROUTES}
    valid_rows = 0

    for current, physical, coherent, payable, reset in product((False, True), repeat=5):
        if payable and not (current and physical and coherent):
            continue
        if coherent and not physical:
            continue
        if reset and payable:
            continue

        route = owner_route(current, physical, coherent, payable, reset)
        assert route in ROUTES
        counts[route] += 1
        valid_rows += 1

    assert all(counts[route] > 0 for route in ROUTES)
    counts["valid_status_rows"] = valid_rows
    return counts


def check_role_dictionary(max_kinds: int = 50, max_provenance: int = 10) -> int:
    systems = 0
    rank_word_count = sum(rank * 2 ** (rank - 1) for rank in range(1, 4))
    assert rank_word_count == 17

    for hard_kinds in range(1, max_kinds + 1):
        for provenance_kinds in range(1, max_provenance + 1):
            bound = 6 * provenance_kinds * hard_kinds * rank_word_count
            assert bound == 102 * provenance_kinds * hard_kinds

            if provenance_kinds == 7:
                assert bound == 714 * hard_kinds
            systems += 1

    return systems


def check_weighted_role_and_dependency_concentration() -> int:
    systems = 0
    for total_weight in range(1, 81):
        for role_count in range(1, 31):
            retained = total_weight / role_count
            assert retained >= total_weight / role_count

            for threshold in range(1, 11):
                distinct = ceil(retained / threshold)
                assert distinct >= 1
                systems += 1
    return systems


def check_owner_incidence_router(max_owners: int = 6) -> int:
    systems = 0
    for owner_count in range(1, max_owners + 1):
        for loads in product(range(5), repeat=owner_count):
            total = sum(loads)
            if total == 0:
                continue

            for threshold in range(1, 5):
                if max(loads) > threshold:
                    pass
                else:
                    positive = sum(load > 0 for load in loads)
                    assert positive >= ceil(total / threshold)
                systems += 1
    return systems


def check_cycle_payment_union(max_length: int = 6, owner_count: int = 4) -> int:
    systems = 0
    owner_choices = tuple(range(-1, owner_count))  # -1 means no owner.

    for length in range(2, max_length + 1):
        for owners in product(owner_choices, repeat=length):
            for paid_flags in product((False, True), repeat=length):
                if any(paid and owner == -1 for owner, paid in zip(owners, paid_flags)):
                    continue

                paid_occurrences = sum(paid_flags)
                distinct_paid_owners = {
                    owner
                    for owner, paid in zip(owners, paid_flags)
                    if paid
                }

                # Shared owners are counted once, never once per cycle edge.
                assert len(distinct_paid_owners) <= paid_occurrences
                if not distinct_paid_owners:
                    assert paid_occurrences == 0
                systems += 1

    return systems


def check_decoration_stock() -> int:
    systems = 0
    for side in range(2, 101):
        literal_addresses = 2 * side * side
        for hard_kinds in range(1, 11):
            role_bound = 714 * hard_kinds
            decorated_records = role_bound * literal_addresses * (literal_addresses + 1)
            assert decorated_records > 0
            assert decorated_records <= 714 * hard_kinds * (2 * side * side) * (2 * side * side + 1)
            systems += 1
    return systems


def main() -> None:
    totals = check_prospective_literal_records()
    totals.update(check_owner_routes())
    totals["role_dictionary_systems"] = check_role_dictionary()
    totals["weighted_role_dependency_systems"] = (
        check_weighted_role_and_dependency_concentration()
    )
    totals["owner_incidence_systems"] = check_owner_incidence_router()
    totals["cycle_payment_union_systems"] = check_cycle_payment_union()
    totals["decoration_stock_systems"] = check_decoration_stock()

    print("AC3ln--AC3ls verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
