#!/usr/bin/env python3
"""Finite audit for OP4bw--OP4ca dynamic residual-signature edit banks."""

from __future__ import annotations

import random


SEED = 90214
SYSTEMS = 7_000


def maximum_deficit(
    demands: list[int],
    capacities: list[int],
    adjacency: list[set[int]],
) -> int:
    residual_count = len(demands)
    best = 0
    for mask in range(1, 1 << residual_count):
        demand = sum(
            demands[residual]
            for residual in range(residual_count)
            if (mask >> residual) & 1
        )
        neighborhood: set[int] = set()
        for residual in range(residual_count):
            if (mask >> residual) & 1:
                neighborhood.update(adjacency[residual])
        deficit = demand - sum(
            capacities[source] for source in neighborhood
        )
        best = max(best, deficit)
    return max(0, best)


def main() -> None:
    rng = random.Random(SEED)
    edit_steps = 0
    deleted_source_arcs = 0
    added_source_arcs = 0
    neighborhood_change_steps = 0
    unit_field_edits = 0
    observed_deficit_increase_units = 0
    deleted_capacity_bound_units = 0

    for _ in range(SYSTEMS):
        residual_count = rng.randint(2, 6)
        source_count = rng.randint(2, 6)
        demands = [rng.randint(1, 3) for _ in range(residual_count)]
        capacities = [rng.randint(1, 4) for _ in range(source_count)]
        unit_classes = [
            rng.randint(0, 3) for _ in range(residual_count)
        ]

        adjacency: list[set[int]] = []
        for _residual in range(residual_count):
            neighborhood = {
                source
                for source in range(source_count)
                if rng.random() < 0.55
            }
            if not neighborhood:
                neighborhood = {rng.randrange(source_count)}
            adjacency.append(neighborhood)

        deficit = maximum_deficit(demands, capacities, adjacency)
        initial_deficit = deficit
        cumulative_deleted_capacity = 0

        for _step in range(rng.randint(2, 8)):
            edit_steps += 1
            updated = [set(neighborhood) for neighborhood in adjacency]
            deleted_capacity = 0

            for residual in range(residual_count):
                for source in list(updated[residual]):
                    if rng.random() < 0.12:
                        updated[residual].remove(source)
                        deleted_source_arcs += 1
                        deleted_capacity += capacities[source]
                for source in range(source_count):
                    if (
                        source not in updated[residual]
                        and rng.random() < 0.08
                    ):
                        updated[residual].add(source)
                        added_source_arcs += 1
                if rng.random() < 0.05:
                    unit_classes[residual] = (
                        unit_classes[residual] + rng.randint(1, 3)
                    ) % 4
                    unit_field_edits += 1

            updated_deficit = maximum_deficit(
                demands,
                capacities,
                updated,
            )
            assert updated_deficit <= deficit + deleted_capacity
            observed_deficit_increase_units += max(
                0,
                updated_deficit - deficit,
            )
            deleted_capacity_bound_units += deleted_capacity
            cumulative_deleted_capacity += deleted_capacity
            assert (
                updated_deficit
                <= initial_deficit + cumulative_deleted_capacity
            )

            if any(
                updated[residual] != adjacency[residual]
                for residual in range(residual_count)
            ):
                neighborhood_change_steps += 1

            adjacency = updated
            deficit = updated_deficit

    print(f"systems={SYSTEMS}")
    print(f"edit_steps={edit_steps}")
    print(f"deleted_source_arcs={deleted_source_arcs}")
    print(f"added_source_arcs={added_source_arcs}")
    print(f"neighborhood_change_steps={neighborhood_change_steps}")
    print(f"unit_field_edits={unit_field_edits}")
    print(
        "observed_deficit_increase_units="
        f"{observed_deficit_increase_units}"
    )
    print(
        "deleted_capacity_bound_units="
        f"{deleted_capacity_bound_units}"
    )


if __name__ == "__main__":
    main()
