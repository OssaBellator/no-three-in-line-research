#!/usr/bin/env python3
"""Finite audit for SAS5jl--SAS5jp zero-boundary completion transport."""

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
    rng = random.Random(1207)
    totals = collections.Counter()

    for _ in range(7500):
        n_tasks = rng.randint(1, 6)
        n_moves = rng.randint(1, 6)
        task_demand = [rng.randint(0, 4) for _ in range(n_tasks)]
        if sum(task_demand) == 0:
            task_demand[rng.randrange(n_tasks)] = 1
        move_capacity = [rng.randint(0, 6) for _ in range(n_moves)]

        adjacency: list[list[int]] = []
        for _task in range(n_tasks):
            neighbours = {j for j in range(n_moves) if rng.random() < 0.58}
            if not neighbours and rng.random() < 0.75:
                neighbours.add(rng.randrange(n_moves))
            adjacency.append(sorted(neighbours))

        flow, used = maxflow_bipartite(task_demand, move_capacity, adjacency)
        maximum_deficit = 0
        for mask in range(1 << n_tasks):
            subset_demand = sum(
                task_demand[i] for i in range(n_tasks) if (mask >> i) & 1
            )
            neighbourhood: set[int] = set()
            for i in range(n_tasks):
                if (mask >> i) & 1:
                    neighbourhood.update(adjacency[i])
            deficit = max(
                0,
                subset_demand - sum(move_capacity[j] for j in neighbourhood),
            )
            maximum_deficit = max(maximum_deficit, deficit)
            totals["hall_subset_checks"] += 1

        assert sum(task_demand) - flow == maximum_deficit

        dimension = rng.randint(1, 5)
        boundary = [0] * dimension
        neutral_move_vectors = [[0] * dimension for _ in range(n_moves)]
        final_boundary = [
            boundary[k]
            + sum(used[j] * neutral_move_vectors[j][k] for j in range(n_moves))
            for k in range(dimension)
        ]
        assert final_boundary == boundary

        if maximum_deficit == 0:
            totals["completed_systems"] += 1
        else:
            totals["deficient_systems"] += 1
            totals["deficiency_units"] += maximum_deficit

        totals["systems"] += 1
        totals["task_units"] += sum(task_demand)
        totals["move_units_used"] += flow
        totals["compatibility_arcs"] += sum(map(len, adjacency))
        totals["task_classes"] += n_tasks
        totals["move_classes"] += n_moves

    print("SAS zero-boundary completion transport audit")
    for key in (
        "systems", "task_classes", "move_classes", "compatibility_arcs",
        "task_units", "move_units_used", "completed_systems",
        "deficient_systems", "deficiency_units", "hall_subset_checks",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
