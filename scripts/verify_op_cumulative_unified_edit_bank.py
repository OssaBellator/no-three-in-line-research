#!/usr/bin/env python3
"""Finite audit for OP4cv--OP4cz."""

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
    used = [residual[sink][n + j] for j in range(m)]
    return total, used


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


SEED = 1405
SYSTEMS = 5500
rng = random.Random(SEED)
stats = {
    "systems": 0, "epochs": 0, "demand_classes": 0, "source_classes": 0,
    "edit_compatibility_arcs": 0, "demand_units": 0, "paid_units": 0,
    "deposit_units": 0, "deficient_epochs": 0, "unpaid_units": 0,
    "hall_subset_checks": 0,
}

for _ in range(SYSTEMS):
    deletion_count = rng.randint(1, 3)
    unit_count = rng.randint(1, 3)
    source_count = rng.randint(2, 5)
    demand_count = deletion_count + unit_count
    balances = [rng.randint(0, 7) for _ in range(source_count)]
    adjacency = []
    for _i in range(demand_count):
        neighbours = [j for j in range(source_count) if rng.random() < 0.55]
        if not neighbours:
            neighbours = [rng.randrange(source_count)]
        adjacency.append(sorted(set(neighbours)))

    for _epoch in range(rng.randint(1, 4)):
        for j in range(source_count):
            deposit = rng.randint(0, 3)
            balances[j] += deposit
            stats["deposit_units"] += deposit
        demands = [rng.randint(0, 4) for _ in range(demand_count)]
        flow, used = maximum_flow(demands, balances, adjacency)
        total = sum(demands)
        stats["epochs"] += 1
        stats["demand_units"] += total
        stats["edit_compatibility_arcs"] += sum(map(len, adjacency))
        if flow == total:
            stats["paid_units"] += flow
            balances = [balances[j] - used[j] for j in range(source_count)]
            assert all(value >= 0 for value in balances)
        else:
            deficit, checks = canonical_deficit(demands, balances, adjacency)
            assert deficit == total - flow and deficit > 0
            stats["deficient_epochs"] += 1
            stats["unpaid_units"] += deficit
            stats["hall_subset_checks"] += checks
            break

    stats["systems"] += 1
    stats["demand_classes"] += demand_count
    stats["source_classes"] += source_count

for key, value in stats.items():
    print(f"{key}: {value}")
