#!/usr/bin/env python3
"""Finite audit for SAS5jv--SAS5jz."""

import random
from collections import deque


def maximum_flow(demands, capacities, adjacency):
    n, m = len(demands), len(capacities)
    source, sink = n + m, n + m + 1
    size = sink + 1
    residual = [[0] * size for _ in range(size)]
    infinity = sum(demands) + sum(capacities) + 1
    for i, demand in enumerate(demands):
        residual[source][i] = demand
    for i, neighbours in enumerate(adjacency):
        for j in neighbours:
            residual[i][n + j] = infinity
    for j, capacity in enumerate(capacities):
        residual[n + j][sink] = capacity
    total = 0
    while True:
        parent = [-1] * size
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] < 0:
            u = queue.popleft()
            for v, capacity in enumerate(residual[u]):
                if capacity > 0 and parent[v] < 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if parent[sink] < 0:
            break
        amount = 10 ** 9
        v = sink
        while v != source:
            amount = min(amount, residual[parent[v]][v])
            v = parent[v]
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= amount
            residual[v][u] += amount
            v = u
        total += amount
    return total


def canonical_deficit(demands, capacities, adjacency):
    best_deficit = -1
    best_subset = None
    checks = 0
    for mask in range(1, 1 << len(demands)):
        checks += 1
        subset = [i for i in range(len(demands)) if mask >> i & 1]
        neighbours = set()
        for i in subset:
            neighbours.update(adjacency[i])
        deficit = sum(demands[i] for i in subset) - sum(capacities[j] for j in neighbours)
        if deficit > best_deficit or (
            deficit == best_deficit
            and (len(subset), tuple(subset)) < (len(best_subset or []), tuple(best_subset or []))
        ):
            best_deficit = deficit
            best_subset = subset
    return best_deficit, checks


SEED = 1407
SYSTEMS = 6000
rng = random.Random(SEED)
stats = {
    "systems": 0, "pair_cost_units": 0, "completion_task_units": 0,
    "compatibility_arcs": 0, "jointly_paid": 0, "mixed_cuts": 0,
    "deficient_units": 0, "hall_subset_checks": 0,
    "shared_capacity_double_spend_witnesses": 0,
}

for _ in range(SYSTEMS):
    pair_count = rng.randint(1, 3)
    task_count = rng.randint(1, 3)
    move_count = rng.randint(2, 5)
    pair_demands = [rng.randint(0, 4) for _ in range(pair_count)]
    task_demands = [rng.randint(0, 4) for _ in range(task_count)]
    capacities = [rng.randint(0, 7) for _ in range(move_count)]

    pair_adjacency = []
    for _i in range(pair_count):
        neighbours = [j for j in range(move_count) if rng.random() < 0.55]
        if not neighbours:
            neighbours = [rng.randrange(move_count)]
        pair_adjacency.append(sorted(set(neighbours)))

    task_adjacency = []
    for _i in range(task_count):
        neighbours = [j for j in range(move_count) if rng.random() < 0.55]
        if not neighbours:
            neighbours = [rng.randrange(move_count)]
        task_adjacency.append(sorted(set(neighbours)))

    pair_flow = maximum_flow(pair_demands, capacities, pair_adjacency)
    task_flow = maximum_flow(task_demands, capacities, task_adjacency)
    demands = pair_demands + task_demands
    adjacency = pair_adjacency + task_adjacency
    joint_flow = maximum_flow(demands, capacities, adjacency)
    total = sum(demands)

    if pair_flow == sum(pair_demands) and task_flow == sum(task_demands) and joint_flow < total:
        stats["shared_capacity_double_spend_witnesses"] += 1

    if joint_flow == total:
        stats["jointly_paid"] += 1
    else:
        deficit, checks = canonical_deficit(demands, capacities, adjacency)
        assert deficit == total - joint_flow
        stats["mixed_cuts"] += 1
        stats["deficient_units"] += deficit
        stats["hall_subset_checks"] += checks

    stats["systems"] += 1
    stats["pair_cost_units"] += sum(pair_demands)
    stats["completion_task_units"] += sum(task_demands)
    stats["compatibility_arcs"] += sum(map(len, adjacency))

for key, value in stats.items():
    print(f"{key}: {value}")
