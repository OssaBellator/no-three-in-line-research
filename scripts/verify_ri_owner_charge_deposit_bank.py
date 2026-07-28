#!/usr/bin/env python3
"""Finite audit for RI5df--RI5dj cumulative owner-charge deposits."""

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
    rng = random.Random(1203)
    totals = collections.Counter()

    for _ in range(5000):
        n_owners = rng.randint(1, 5)
        n_sources = rng.randint(1, 5)
        balances = [rng.randint(0, 8) for _ in range(n_sources)]
        initial = balances[:]
        deposits = [0] * n_sources
        debits = [0] * n_sources
        completed = True

        for _epoch in range(rng.randint(1, 5)):
            totals["epochs"] += 1
            epoch_deposits = [
                rng.randint(0, 3) if rng.random() < 0.55 else 0
                for _ in range(n_sources)
            ]
            for j, amount in enumerate(epoch_deposits):
                balances[j] += amount
                deposits[j] += amount

            demands = [rng.randint(0, 5) for _ in range(n_owners)]
            if sum(demands) == 0:
                demands[rng.randrange(n_owners)] = 1

            adjacency: list[list[int]] = []
            for _owner in range(n_owners):
                neighbours = {j for j in range(n_sources) if rng.random() < 0.58}
                if not neighbours and rng.random() < 0.7:
                    neighbours.add(rng.randrange(n_sources))
                adjacency.append(sorted(neighbours))

            flow, used = maxflow_bipartite(demands, balances, adjacency)
            maximum_deficit = 0
            for mask in range(1 << n_owners):
                subset_demand = sum(demands[i] for i in range(n_owners) if (mask >> i) & 1)
                neighbourhood: set[int] = set()
                for i in range(n_owners):
                    if (mask >> i) & 1:
                        neighbourhood.update(adjacency[i])
                deficit = max(0, subset_demand - sum(balances[j] for j in neighbourhood))
                maximum_deficit = max(maximum_deficit, deficit)
                totals["hall_subset_checks"] += 1

            assert sum(demands) - flow == maximum_deficit
            totals["demand_units"] += sum(demands)
            totals["paid_units"] += flow
            totals["deposit_units"] += sum(epoch_deposits)
            totals["compatibility_arcs"] += sum(map(len, adjacency))

            if maximum_deficit:
                totals["deficient_epochs"] += 1
                totals["deficiency_units"] += maximum_deficit
                completed = False
                break

            totals["fully_paid_epochs"] += 1
            for j, amount in enumerate(used):
                balances[j] -= amount
                debits[j] += amount
                assert balances[j] >= 0
                assert debits[j] <= initial[j] + deposits[j]

        totals["systems"] += 1
        if completed:
            totals["completed_systems"] += 1

    print("RI cumulative owner-charge deposit audit")
    for key in (
        "systems", "epochs", "compatibility_arcs", "demand_units",
        "paid_units", "deposit_units", "fully_paid_epochs",
        "deficient_epochs", "deficiency_units", "completed_systems",
        "hall_subset_checks",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
