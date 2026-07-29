#!/usr/bin/env python3

import random
from collections import deque


def max_flow(demands, supplies, edges):
    residual_count = len(demands)
    source_count = len(supplies)
    source = residual_count + source_count
    sink = source + 1
    size = sink + 1
    capacity = [[0] * size for _ in range(size)]
    for i, demand in enumerate(demands):
        capacity[source][i] = demand
    infinity = sum(demands) + sum(supplies) + 1
    for residual, payment_source in edges:
        capacity[residual][residual_count + payment_source] = infinity
    for j, supply in enumerate(supplies):
        capacity[residual_count + j][sink] = supply

    flow = 0
    while True:
        parent = [-1] * size
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] < 0:
            u = queue.popleft()
            for v, cap in enumerate(capacity[u]):
                if cap > 0 and parent[v] < 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if parent[sink] < 0:
            return flow
        augment = 10**9
        v = sink
        while v != source:
            augment = min(augment, capacity[parent[v]][v])
            v = parent[v]
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= augment
            capacity[v][u] += augment
            v = u
        flow += augment


def hall_deficit(demands, supplies, edges):
    neighbours = [set() for _ in demands]
    for residual, payment_source in edges:
        neighbours[residual].add(payment_source)
    best = 0
    for mask in range(1 << len(demands)):
        demand = sum(demands[i] for i in range(len(demands)) if (mask >> i) & 1)
        reachable = set()
        for i in range(len(demands)):
            if (mask >> i) & 1:
                reachable.update(neighbours[i])
        supply = sum(supplies[j] for j in reachable)
        best = max(best, demand - supply)
    return best


def main():
    rng = random.Random(20260728)
    epochs = feasible = deficient = total_demand = 0
    for _ in range(8500):
        residual_count = rng.randint(1, 6)
        source_count = rng.randint(1, 6)
        demands = [rng.randint(0, 7) for _ in range(residual_count)]
        supplies = [rng.randint(0, 8) for _ in range(source_count)]
        edges = {
            (i, j)
            for i in range(residual_count)
            for j in range(source_count)
            if rng.random() < 0.50
        }
        flow = max_flow(demands, supplies, edges)
        deficit = hall_deficit(demands, supplies, edges)
        assert sum(demands) - flow == deficit
        feasible += deficit == 0
        deficient += deficit > 0
        total_demand += sum(demands)
        epochs += 1

    print(f"audited {epochs:,} zero-drift residual transport systems")
    print(f"found {feasible:,} fully payable systems")
    print(f"returned {deficient:,} exact deficient residual cuts")
    print(f"checked {total_demand:,} physical residual demand units")


if __name__ == "__main__":
    main()
