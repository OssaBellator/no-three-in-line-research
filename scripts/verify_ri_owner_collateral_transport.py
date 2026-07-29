#!/usr/bin/env python3

import random
from collections import deque


def max_flow(demands, supplies, edges):
    owner_count = len(demands)
    source_count = len(supplies)
    source = owner_count + source_count
    sink = source + 1
    size = sink + 1
    capacity = [[0] * size for _ in range(size)]
    for i, demand in enumerate(demands):
        capacity[source][i] = demand
    infinity = sum(demands) + sum(supplies) + 1
    for owner, collateral in edges:
        capacity[owner][owner_count + collateral] = infinity
    for j, supply in enumerate(supplies):
        capacity[owner_count + j][sink] = supply

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
    for owner, collateral in edges:
        neighbours[owner].add(collateral)
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
    for _ in range(9000):
        owner_count = rng.randint(1, 6)
        source_count = rng.randint(1, 6)
        demands = [rng.randint(0, 8) for _ in range(owner_count)]
        supplies = [rng.randint(0, 9) for _ in range(source_count)]
        edges = {
            (i, j)
            for i in range(owner_count)
            for j in range(source_count)
            if rng.random() < 0.45
        }
        flow = max_flow(demands, supplies, edges)
        deficit = hall_deficit(demands, supplies, edges)
        assert sum(demands) - flow == deficit
        feasible += deficit == 0
        deficient += deficit > 0
        total_demand += sum(demands)
        epochs += 1

    print(f"audited {epochs:,} owner-collateral transport systems")
    print(f"found {feasible:,} fully payable systems")
    print(f"returned {deficient:,} exact deficient owner cuts")
    print(f"checked {total_demand:,} symmetric demand units")


if __name__ == "__main__":
    main()
