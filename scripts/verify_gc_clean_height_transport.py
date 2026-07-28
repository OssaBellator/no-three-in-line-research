#!/usr/bin/env python3
"""Finite audit for GC2hx--GC2ib clean-height threshold transport."""

from __future__ import annotations

from functools import lru_cache
import random


SEED = 90213
SYSTEMS = 5_000
INFINITY = 10**9


def minimum_cost_assignment(
    cause_units: list[int],
    source_copies: list[int],
    compatibility: list[set[int]],
    costs: list[int],
) -> int:
    @lru_cache(maxsize=None)
    def solve(index: int, used_mask: int) -> int:
        if index == len(cause_units):
            return 0
        cause = cause_units[index]
        best = INFINITY
        for copy_index, source in enumerate(source_copies):
            if (used_mask >> copy_index) & 1:
                continue
            if source not in compatibility[cause]:
                continue
            best = min(
                best,
                costs[source]
                + solve(index + 1, used_mask | (1 << copy_index)),
            )
        return best

    return solve(0, 0)


def maximum_threshold_matching(
    cause_units: list[int],
    source_copies: list[int],
    compatibility: list[set[int]],
    costs: list[int],
    threshold: int,
) -> int:
    @lru_cache(maxsize=None)
    def solve(index: int, used_mask: int) -> int:
        if index == len(cause_units):
            return 0

        best = solve(index + 1, used_mask)
        cause = cause_units[index]
        for copy_index, source in enumerate(source_copies):
            if (used_mask >> copy_index) & 1:
                continue
            if costs[source] >= threshold:
                continue
            if source not in compatibility[cause]:
                continue
            best = max(
                best,
                1 + solve(index + 1, used_mask | (1 << copy_index)),
            )
        return best

    return solve(0, 0)


def main() -> None:
    rng = random.Random(SEED)
    feasible_systems = 0
    infeasible_systems = 0
    cause_demand_units = 0
    remedy_capacity_units = 0
    height_thresholds = 0
    minimum_height_loss_units = 0
    threshold_deficiency_units = 0

    for _ in range(SYSTEMS):
        cause_count = rng.randint(2, 5)
        source_count = rng.randint(2, 5)
        demands = [rng.randint(1, 2) for _ in range(cause_count)]
        capacities = [rng.randint(1, 2) for _ in range(source_count)]
        while sum(capacities) > 9:
            source = rng.randrange(source_count)
            if capacities[source] > 1:
                capacities[source] -= 1

        costs = [rng.randint(0, 4) for _ in range(source_count)]
        compatibility: list[set[int]] = []
        for _cause in range(cause_count):
            neighborhood = {
                source
                for source in range(source_count)
                if rng.random() < 0.58
            }
            if not neighborhood:
                neighborhood = {rng.randrange(source_count)}
            compatibility.append(neighborhood)

        cause_units = [
            cause
            for cause, demand in enumerate(demands)
            for _copy in range(demand)
        ]
        source_copies = [
            source
            for source, capacity in enumerate(capacities)
            for _copy in range(capacity)
        ]
        cause_demand_units += len(cause_units)
        remedy_capacity_units += len(source_copies)

        minimum_cost = minimum_cost_assignment(
            cause_units,
            source_copies,
            compatibility,
            costs,
        )
        if minimum_cost >= INFINITY:
            infeasible_systems += 1
            continue

        feasible_systems += 1
        minimum_height_loss_units += minimum_cost
        layer_cake = 0
        for threshold in range(1, max(costs) + 1):
            matching_size = maximum_threshold_matching(
                cause_units,
                source_copies,
                compatibility,
                costs,
                threshold,
            )
            deficiency = len(cause_units) - matching_size
            layer_cake += deficiency
            threshold_deficiency_units += deficiency
            height_thresholds += 1

        assert layer_cake == minimum_cost

    print(f"systems={SYSTEMS}")
    print(f"feasible_systems={feasible_systems}")
    print(f"infeasible_systems={infeasible_systems}")
    print(f"cause_demand_units={cause_demand_units}")
    print(f"remedy_capacity_units={remedy_capacity_units}")
    print(f"height_thresholds={height_thresholds}")
    print(f"minimum_height_loss_units={minimum_height_loss_units}")
    print(f"threshold_deficiency_units={threshold_deficiency_units}")


if __name__ == "__main__":
    main()
