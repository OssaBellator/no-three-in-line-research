#!/usr/bin/env python3
"""Finite audit for RI5cq--RI5cu compatibility perturbation stability."""

from __future__ import annotations

import random


SEED = 90212
SYSTEMS = 7_500


def maximum_deficit(
    demands: list[int],
    capacities: list[int],
    adjacency: list[set[int]],
) -> int:
    owner_count = len(demands)
    best = 0
    for mask in range(1, 1 << owner_count):
        demand = sum(
            demands[owner]
            for owner in range(owner_count)
            if (mask >> owner) & 1
        )
        neighborhood: set[int] = set()
        for owner in range(owner_count):
            if (mask >> owner) & 1:
                neighborhood.update(adjacency[owner])
        deficit = demand - sum(capacities[source] for source in neighborhood)
        best = max(best, deficit)
    return max(0, best)


def main() -> None:
    rng = random.Random(SEED)
    deleted_arcs = 0
    added_arcs = 0
    worsened_systems = 0
    nonworsened_systems = 0
    reference_deficit_units = 0
    actual_deficit_units = 0
    perturbation_bound_units = 0

    for _ in range(SYSTEMS):
        owner_count = rng.randint(2, 6)
        source_count = rng.randint(2, 6)
        demands = [rng.randint(1, 4) for _ in range(owner_count)]
        capacities = [rng.randint(1, 5) for _ in range(source_count)]

        reference: list[set[int]] = []
        for _owner in range(owner_count):
            neighborhood = {
                source
                for source in range(source_count)
                if rng.random() < 0.55
            }
            if not neighborhood:
                neighborhood = {rng.randrange(source_count)}
            reference.append(neighborhood)

        actual = [set(neighborhood) for neighborhood in reference]
        for owner in range(owner_count):
            for source in list(actual[owner]):
                if rng.random() < 0.15:
                    actual[owner].remove(source)
                    deleted_arcs += 1
            for source in range(source_count):
                if source not in actual[owner] and rng.random() < 0.08:
                    actual[owner].add(source)
                    added_arcs += 1

        reference_deficit = maximum_deficit(demands, capacities, reference)
        actual_deficit = maximum_deficit(demands, capacities, actual)
        bound = 0

        for mask in range(1, 1 << owner_count):
            owners = [
                owner
                for owner in range(owner_count)
                if (mask >> owner) & 1
            ]
            demand = sum(demands[owner] for owner in owners)
            reference_neighborhood: set[int] = set()
            actual_neighborhood: set[int] = set()
            for owner in owners:
                reference_neighborhood.update(reference[owner])
                actual_neighborhood.update(actual[owner])

            reference_subset_deficit = max(
                0,
                demand
                - sum(
                    capacities[source]
                    for source in reference_neighborhood
                ),
            )
            lost_capacity = sum(
                capacities[source]
                for source in reference_neighborhood - actual_neighborhood
            )
            actual_subset_deficit = max(
                0,
                demand
                - sum(capacities[source] for source in actual_neighborhood),
            )
            assert (
                actual_subset_deficit
                <= reference_subset_deficit + lost_capacity
            )
            bound = max(
                bound,
                reference_subset_deficit + lost_capacity,
            )

        assert actual_deficit <= bound
        reference_deficit_units += reference_deficit
        actual_deficit_units += actual_deficit
        perturbation_bound_units += bound
        if actual_deficit > reference_deficit:
            worsened_systems += 1
        else:
            nonworsened_systems += 1

    print(f"systems={SYSTEMS}")
    print(f"deleted_compatibility_arcs={deleted_arcs}")
    print(f"added_compatibility_arcs={added_arcs}")
    print(f"worsened_systems={worsened_systems}")
    print(f"nonworsened_systems={nonworsened_systems}")
    print(f"reference_deficit_units={reference_deficit_units}")
    print(f"actual_deficit_units={actual_deficit_units}")
    print(f"perturbation_bound_units={perturbation_bound_units}")


if __name__ == "__main__":
    main()
