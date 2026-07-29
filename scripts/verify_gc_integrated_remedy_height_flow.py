#!/usr/bin/env python3
"""Finite audit for GC2iw--GC2ja."""

import random
from collections import deque

SEED = 1404
SYSTEMS = 6000


class Dinic:
    def __init__(self, size):
        self.graph = [[] for _ in range(size)]

    def add(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def maxflow(self, source, sink):
        total = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, capacity, _reverse in self.graph[u]:
                    if capacity and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] < 0:
                return total
            position = [0] * len(self.graph)

            def send(u, amount):
                if u == sink:
                    return amount
                while position[u] < len(self.graph[u]):
                    edge = self.graph[u][position[u]]
                    v, capacity, reverse = edge
                    if capacity and level[v] == level[u] + 1:
                        pushed = send(v, min(amount, capacity))
                        if pushed:
                            edge[1] -= pushed
                            self.graph[v][reverse][1] += pushed
                            return pushed
                    position[u] += 1
                return 0

            while True:
                pushed = send(source, 10 ** 9)
                if not pushed:
                    break
                total += pushed


def integrated_flow(demands, remedy_capacity, height_capacity, cause_remedy, remedy_height):
    cause_count = len(demands)
    remedy_count = len(remedy_capacity)
    height_count = len(height_capacity)
    source = 0
    cause0 = 1
    remedy_in0 = cause0 + cause_count
    remedy_out0 = remedy_in0 + remedy_count
    height0 = remedy_out0 + remedy_count
    sink = height0 + height_count
    network = Dinic(sink + 1)
    infinity = sum(demands) + sum(remedy_capacity) + sum(height_capacity) + 1

    for i, demand in enumerate(demands):
        network.add(source, cause0 + i, demand)
    for i, neighbours in enumerate(cause_remedy):
        for remedy in neighbours:
            network.add(cause0 + i, remedy_in0 + remedy, infinity)
    for remedy, capacity in enumerate(remedy_capacity):
        network.add(remedy_in0 + remedy, remedy_out0 + remedy, capacity)
    for remedy, neighbours in enumerate(remedy_height):
        for height in neighbours:
            network.add(remedy_out0 + remedy, height0 + height, infinity)
    for height, capacity in enumerate(height_capacity):
        network.add(height0 + height, sink, capacity)

    return network.maxflow(source, sink)


def cause_remedy_flow(demands, capacities, adjacency):
    height_capacity = [sum(demands)]
    remedy_height = [[0] for _ in capacities]
    return integrated_flow(demands, capacities, height_capacity, adjacency, remedy_height)


rng = random.Random(SEED)
stats = {
    "systems": 0, "cause_units": 0, "cause_remedy_arcs": 0,
    "remedy_height_arcs": 0, "jointly_paid": 0, "mixed_cuts": 0,
    "deficient_units": 0, "stage_selection_witnesses": 0,
}

for _ in range(SYSTEMS):
    cause_count = rng.randint(1, 4)
    remedy_count = rng.randint(1, 4)
    height_count = rng.randint(1, 4)
    demands = [rng.randint(0, 3) for _ in range(cause_count)]
    remedy_capacity = [rng.randint(0, 5) for _ in range(remedy_count)]
    height_capacity = [rng.randint(0, 5) for _ in range(height_count)]

    cause_remedy = []
    for _i in range(cause_count):
        neighbours = [r for r in range(remedy_count) if rng.random() < 0.55]
        if not neighbours:
            neighbours = [rng.randrange(remedy_count)]
        cause_remedy.append(sorted(set(neighbours)))

    remedy_height = []
    for _r in range(remedy_count):
        neighbours = [h for h in range(height_count) if rng.random() < 0.55]
        if not neighbours:
            neighbours = [rng.randrange(height_count)]
        remedy_height.append(sorted(set(neighbours)))

    flow = integrated_flow(
        demands, remedy_capacity, height_capacity, cause_remedy, remedy_height
    )
    total = sum(demands)
    assert flow <= total

    preliminary = cause_remedy_flow(demands, remedy_capacity, cause_remedy)
    if preliminary == total and sum(height_capacity) >= total and flow < total:
        stats["stage_selection_witnesses"] += 1

    if flow == total:
        stats["jointly_paid"] += 1
    else:
        stats["mixed_cuts"] += 1
        stats["deficient_units"] += total - flow

    stats["systems"] += 1
    stats["cause_units"] += total
    stats["cause_remedy_arcs"] += sum(map(len, cause_remedy))
    stats["remedy_height_arcs"] += sum(map(len, remedy_height))

for key, value in stats.items():
    print(f"{key}: {value}")
