#!/usr/bin/env python3
"""Exact finite audit for AC3nc--AC3nh.

The general matching arguments are in
``docs/alternating-core-canonical-owner-assignment.md``.  This script exhausts
all bipartite demand--owner graphs through 3 x 3, every spent mask, canonical
maximum assignments, Hall cores, one-atom updates and capacity-consumption steps.
"""

from __future__ import annotations

from itertools import combinations, product


def subsets(n: int):
    for mask in range(1 << n):
        yield tuple(i for i in range(n) if (mask >> i) & 1)


def assignments(
    demand_count: int,
    owner_count: int,
    edges: set[tuple[int, int]],
    available: set[int],
):
    sentinel = owner_count
    for assignment in product(range(owner_count + 1), repeat=demand_count):
        used = [owner for owner in assignment if owner < owner_count]
        if len(set(used)) != len(used):
            continue
        if all(
            owner == sentinel
            or (owner in available and (demand, owner) in edges)
            for demand, owner in enumerate(assignment)
        ):
            yield assignment


def canonical_matching(
    demand_count: int,
    owner_count: int,
    edges: set[tuple[int, int]],
    available: set[int],
) -> tuple[tuple[int, ...], int]:
    candidates = list(assignments(demand_count, owner_count, edges, available))
    maximum = max(
        sum(owner < owner_count for owner in assignment)
        for assignment in candidates
    )
    best = min(
        assignment
        for assignment in candidates
        if sum(owner < owner_count for owner in assignment) == maximum
    )
    return best, maximum


def canonical_hall_core(
    demand_count: int,
    owner_count: int,
    edges: set[tuple[int, int]],
    available: set[int],
) -> tuple[int, ...] | None:
    deficient: list[tuple[int, ...]] = []
    for demand_set in subsets(demand_count):
        if not demand_set:
            continue
        neighbourhood = {
            owner
            for demand in demand_set
            for owner in available
            if (demand, owner) in edges
        }
        if len(neighbourhood) >= len(demand_set):
            continue

        inclusion_minimal = True
        for size in range(1, len(demand_set)):
            for smaller in combinations(demand_set, size):
                smaller_neighbourhood = {
                    owner
                    for demand in smaller
                    for owner in available
                    if (demand, owner) in edges
                }
                if len(smaller_neighbourhood) < len(smaller):
                    inclusion_minimal = False
                    break
            if not inclusion_minimal:
                break
        if inclusion_minimal:
            deficient.append(demand_set)

    if not deficient:
        return None
    return min(deficient, key=lambda item: (len(item), item))


def edge_set(all_edges: list[tuple[int, int]], mask: int) -> set[tuple[int, int]]:
    return {edge for bit, edge in enumerate(all_edges) if (mask >> bit) & 1}


def main() -> None:
    counters = {
        "graph systems": 0,
        "availability systems": 0,
        "complete assignments": 0,
        "Hall cores": 0,
        "monotone mask pairs": 0,
        "capacity consumption steps": 0,
        "eligibility toggles": 0,
        "availability toggles": 0,
        "multi-pair assignment rotations": 0,
        "matching-rank changes": 0,
    }

    cache: dict[tuple[int, int, int, int], tuple[tuple[int, ...], int]] = {}

    for demand_count in range(1, 4):
        for owner_count in range(1, 4):
            all_edges = [
                (demand, owner)
                for demand in range(demand_count)
                for owner in range(owner_count)
            ]

            for graph_mask in range(1 << len(all_edges)):
                edges = edge_set(all_edges, graph_mask)
                counters["graph systems"] += 1

                for spent_mask in range(1 << owner_count):
                    available = {
                        owner
                        for owner in range(owner_count)
                        if not ((spent_mask >> owner) & 1)
                    }
                    matching, rank = canonical_matching(
                        demand_count, owner_count, edges, available
                    )
                    cache[(demand_count, owner_count, graph_mask, spent_mask)] = (
                        matching,
                        rank,
                    )
                    counters["availability systems"] += 1

                    core = canonical_hall_core(
                        demand_count, owner_count, edges, available
                    )
                    if rank == demand_count:
                        assert core is None
                        counters["complete assignments"] += 1
                    else:
                        assert core is not None
                        neighbourhood = {
                            owner
                            for demand in core
                            for owner in available
                            if (demand, owner) in edges
                        }
                        assert len(neighbourhood) < len(core)
                        counters["Hall cores"] += 1

                    matched_owners = {
                        owner for owner in matching if owner < owner_count
                    }
                    for candidate in subsets(owner_count):
                        consumed = set(candidate) & matched_owners
                        if not consumed:
                            continue
                        new_spent = spent_mask
                        for owner in consumed:
                            new_spent |= 1 << owner
                        assert new_spent != spent_mask
                        assert (spent_mask & ~new_spent) == 0
                        counters["capacity consumption steps"] += 1

                # Matching rank is nonincreasing under mask growth.
                for spent_mask in range(1 << owner_count):
                    for larger_mask in range(1 << owner_count):
                        if spent_mask & ~larger_mask:
                            continue
                        _, old_rank = cache[
                            (demand_count, owner_count, graph_mask, spent_mask)
                        ]
                        _, new_rank = cache[
                            (demand_count, owner_count, graph_mask, larger_mask)
                        ]
                        assert new_rank <= old_rank
                        counters["monotone mask pairs"] += 1

                # Toggle one eligibility edge, counted once as an unordered pair.
                for spent_mask in range(1 << owner_count):
                    available = {
                        owner
                        for owner in range(owner_count)
                        if not ((spent_mask >> owner) & 1)
                    }
                    matching, rank = cache[
                        (demand_count, owner_count, graph_mask, spent_mask)
                    ]
                    for bit, _edge in enumerate(all_edges):
                        toggled_mask = graph_mask ^ (1 << bit)
                        if toggled_mask < graph_mask:
                            continue
                        toggled_edges = edge_set(all_edges, toggled_mask)
                        changed_matching, changed_rank = canonical_matching(
                            demand_count,
                            owner_count,
                            toggled_edges,
                            available,
                        )
                        assert abs(rank - changed_rank) <= 1
                        counters["eligibility toggles"] += 1
                        changed_pairs = sum(
                            left != right
                            for left, right in zip(matching, changed_matching)
                        )
                        if changed_pairs > 1:
                            counters["multi-pair assignment rotations"] += 1
                        if rank != changed_rank:
                            counters["matching-rank changes"] += 1

                    # Spend one currently available owner unit.
                    for owner in available:
                        smaller_available = available - {owner}
                        changed_matching, changed_rank = canonical_matching(
                            demand_count,
                            owner_count,
                            edges,
                            smaller_available,
                        )
                        assert rank - 1 <= changed_rank <= rank
                        counters["availability toggles"] += 1
                        changed_pairs = sum(
                            left != right
                            for left, right in zip(matching, changed_matching)
                        )
                        if changed_pairs > 1:
                            counters["multi-pair assignment rotations"] += 1
                        if rank != changed_rank:
                            counters["matching-rank changes"] += 1

    expected = {
        "graph systems": 682,
        "availability systems": 5_036,
        "complete assignments": 429,
        "Hall cores": 4_607,
        "monotone mask pairs": 16_566,
        "capacity consumption steps": 19_341,
        "eligibility toggles": 21_010,
        "availability toggles": 7_358,
        "multi-pair assignment rotations": 4_312,
        "matching-rank changes": 8_822,
    }
    assert counters == expected, (counters, expected)

    print("AC3nc--AC3nh exact finite audit passed")
    for label, count in counters.items():
        print(f"  {label}: {count:,}")


if __name__ == "__main__":
    main()
