#!/usr/bin/env python3
"""Finite audit for AC5cd--AC5ch layer-defect certificate transport."""

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
    rng = random.Random(1201)
    totals = collections.Counter()

    for _ in range(7000):
        n_layers = rng.randint(1, 5)
        n_certificates = rng.randint(1, 5)
        demands = [rng.randint(0, 5) for _ in range(n_layers)]
        if sum(demands) == 0:
            demands[rng.randrange(n_layers)] = rng.randint(1, 5)
        capacities = [rng.randint(0, 6) for _ in range(n_certificates)]

        adjacency: list[list[int]] = []
        for _layer in range(n_layers):
            neighbours = {j for j in range(n_certificates) if rng.random() < 0.55}
            if not neighbours and rng.random() < 0.7:
                neighbours.add(rng.randrange(n_certificates))
            adjacency.append(sorted(neighbours))

        flow, used = maxflow_bipartite(demands, capacities, adjacency)
        maximum_deficit = 0
        for mask in range(1 << n_layers):
            subset_demand = sum(demands[i] for i in range(n_layers) if (mask >> i) & 1)
            neighbourhood: set[int] = set()
            for i in range(n_layers):
                if (mask >> i) & 1:
                    neighbourhood.update(adjacency[i])
            deficit = max(0, subset_demand - sum(capacities[j] for j in neighbourhood))
            maximum_deficit = max(maximum_deficit, deficit)

        assert sum(demands) - flow == maximum_deficit
        assert all(amount <= capacity for amount, capacity in zip(used, capacities))

        classes = [rng.randrange(max(1, min(4, n_certificates))) for _ in range(n_certificates)]
        class_used: collections.Counter[int] = collections.Counter()
        class_capacity: collections.Counter[int] = collections.Counter()
        for j in range(n_certificates):
            class_used[classes[j]] += used[j]
            class_capacity[classes[j]] += capacities[j]
        assert all(class_used[key] <= class_capacity[key] for key in class_used)

        totals["systems"] += 1
        totals["layers"] += n_layers
        totals["certificates"] += n_certificates
        totals["arcs"] += sum(map(len, adjacency))
        totals["demand_units"] += sum(demands)
        totals["paid_units"] += flow
        totals["deficiency_units"] += maximum_deficit
        if maximum_deficit == 0:
            totals["fully_paid"] += 1
        else:
            totals["deficient"] += 1
            totals["hall_subset_checks"] += (1 << n_layers) - 1

    print("AC layer-defect certificate transport audit")
    for key in (
        "systems", "layers", "certificates", "arcs", "demand_units",
        "paid_units", "deficiency_units", "fully_paid", "deficient",
        "hall_subset_checks",
    ):
        print(f"{key}: {totals[key]}")


if __name__ == "__main__":
    main()
