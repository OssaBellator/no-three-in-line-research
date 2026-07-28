#!/usr/bin/env python3
"""Finite audit for GC2im--GC2iq two-stage remedy/height transport."""

from __future__ import annotations

import collections
import random


def maxflow_bipartite(demands: list[int], capacities: list[int], adjacency: list[list[int]]) -> tuple[int, list[int]]:
    n_left, n_right = len(demands), len(capacities)
    source, sink = n_left + n_right, n_left + n_right + 1
    size = sink + 1
    residual = [[0] * size for _ in range(size)]
    for i, demand in enumerate(demands):
        residual[source][i] = demand
    infinity = sum(demands) + sum(capacities) + 1
    for i, neighbours in enumerate(adjacency):
        for j in neighbours:
            residual[i][n_left + j] = infinity
    for j, capacity in enumerate(capacities):
        residual[n_left + j][sink] = capacity

    value = 0
    while True:
        parent = [-1] * size
        parent[source] = source
        queue = collections.deque([source])
        while queue and parent[sink] < 0:
            u = queue.popleft()
            for v, cap in enumerate(residual[u]):
                if cap > 0 and parent[v] < 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if parent[sink] < 0:
            break
        augment = 10**9
        v = sink
        while v != source:
            u = parent[v]
            augment = min(augment, residual[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= augment
            residual[v][u] += augment
            v = u
        value += augment

    used = [residual[sink][n_left + j] for j in range(n_right)]
    return value, used


def main() -> None:
    rng = random.Random(1204)
    totals = collections.Counter()

    for _ in range(6500):
        n_causes = rng.randint(1, 5)
        n_remedies = rng.randint(1, 5)
        n_height_sources = rng.randint(1, 5)

        cause_demand = [rng.randint(0, 4) for _ in range(n_causes)]
        if sum(cause_demand) == 0:
            cause_demand[rng.randrange(n_causes)] = 1
        remedy_capacity = [rng.randint(0, 6) for _ in range(n_remedies)]

        cause_adjacency: list[list[int]] = []
        for _cause in range(n_causes):
            neighbours = {j for j in range(n_remedies) if rng.random() < 0.6}
            if not neighbours and rng.random() < 0.75:
                neighbours.add(rng.randrange(n_remedies))
            cause_adjacency.append(sorted(neighbours))

        first_flow, used_remedy = maxflow_bipartite(
            cause_demand, remedy_capacity, cause_adjacency
        )
        totals["systems"] += 1
        totals["cause_units"] += sum(cause_demand)
        totals["cause_remedy_arcs"] += sum(map(len, cause_adjacency))
        totals["remedy_units_used"] += sum(used_remedy)

        if first_flow < sum(cause_demand):
            totals["cause_cut_systems"] += 1
            totals["cause_deficiency_units"] += sum(cause_demand) - first_flow
            continue

        totals["cause_paid_systems"] += 1
        height_cost = [rng.randint(0, 4) for _ in range(n_remedies)]
        height_demand = [
            height_cost[j] * used_remedy[j] for j in range(n_remedies)
        ]
        height_capacity = [rng.randint(0, 10) for _ in range(n_height_sources)]

        height_adjacency: list[list[int]] = []
        for j in range(n_remedies):
            neighbours = {k for k in range(n_height_sources) if rng.random() < 0.62}
            if height_demand[j] and not neighbours and rng.random() < 0.8:
                neighbours.add(rng.randrange(n_height_sources))
            height_adjacency.append(sorted(neighbours))

        second_flow, _ = maxflow_bipartite(
            height_demand, height_capacity, height_adjacency
        )
        maximum_deficit = 0
        for mask in range(1 << n_remedies):
            subset_demand = sum(
                height_demand[j] for j in range(n_remedies) if (mask >> j) & 1
            )
            neighbourhood: set[int] = set()
            for j in range(n_remedies):
                if (mask >> j) & 1:
                    neighbourhood.update(height_adjacency[j])
            deficit = max(
                0,
                subset_demand - sum(height_capacity[k] for k in neighbourhood),
            )
            maximum_deficit = max(maximum_deficit, deficit)
            totals["height_hall_checks"] += 1

        assert sum(height_demand) - second_flow == maximum_deficit
        totals["height_demand_units"] += sum(height_demand)
        totals["height_source_arcs"] += sum(map(len, height_adjacency))

        if maximum_deficit:
            totals["height_cut_systems"] += 1
            totals["height_deficiency_units"] += maximum_deficit
        else:
            totals["jointly_paid_systems"] += 1

    print("GC remedy/height-source transport audit")
    for key in (
        "systems", "cause_units", "cause_remedy_arcs", "remedy_units_used",
        "cause_paid_systems", "cause_cut_systems", "cause_deficiency_units",
        "height_demand_units", "height_source_arcs", "jointly_paid_systems",
        "height_cut_systems", "height_deficiency_units", "height_hall_checks",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
