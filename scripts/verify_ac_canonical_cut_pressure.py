#!/usr/bin/env python3
"""Finite audit for alternating-core canonical cut pressure."""

from collections import deque
from random import Random

SEED = 2101
SYSTEMS = 3000
TYPED = False


def maxflow(n, edges, source, sink, enabled):
    cap = [[0] * n for _ in range(n)]
    for u, v, c, key in edges:
        cap[u][v] += enabled.get(key, c)
    residual = [row[:] for row in cap]
    value = 0
    while True:
        parent = [-1] * n
        parent[source] = source
        queue = deque([source])
        while queue and parent[sink] < 0:
            u = queue.popleft()
            for v in range(n):
                if parent[v] < 0 and residual[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if parent[sink] < 0:
            break
        aug = 10**9
        v = sink
        while v != source:
            u = parent[v]
            aug = min(aug, residual[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= aug
            residual[v][u] += aug
            v = u
        value += aug
    reachable = [False] * n
    reachable[source] = True
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not reachable[v] and residual[u][v] > 0:
                reachable[v] = True
                queue.append(v)
    flow = {(u, v, key): cap[u][v] - residual[u][v]
            for u, v, _, key in edges}
    return value, flow, reachable


def make_system(rng):
    terminal_count = rng.randint(2, 4)
    p_count = rng.randint(2, 4)
    q_count = rng.randint(2, 4)
    source = 0
    p0 = 1
    q0 = p0 + p_count
    terminal0 = q0 + q_count
    sink = terminal0 + terminal_count
    edges = []
    for i in range(p_count):
        edges.append((source, p0 + i, rng.randint(1, 3), ("sp", i)))
    for i in range(p_count):
        used = False
        for j in range(q_count):
            if rng.random() < 0.65:
                edges.append((p0 + i, q0 + j, rng.randint(1, 3), ("pq", i, j)))
                used = True
        if not used:
            j = rng.randrange(q_count)
            edges.append((p0 + i, q0 + j, rng.randint(1, 3), ("pq", i, j)))
    for j in range(q_count):
        used = False
        for k in range(terminal_count):
            if rng.random() < 0.65:
                edges.append((q0 + j, terminal0 + k, rng.randint(1, 3), ("qt", j, k)))
                used = True
        if not used:
            k = rng.randrange(terminal_count)
            edges.append((q0 + j, terminal0 + k, rng.randint(1, 3), ("qt", j, k)))
    demands = [rng.randint(1, 3) for _ in range(terminal_count)]
    for k, demand in enumerate(demands):
        edges.append((terminal0 + k, sink, demand, ("term", k)))
    types = [rng.randrange(2) for _ in range(terminal_count)] if TYPED else [0] * terminal_count
    return sink + 1, edges, source, sink, demands, types


def enabled(demands, mask):
    return {("term", k): demand if mask >> k & 1 else 0
            for k, demand in enumerate(demands)}


def main():
    rng = Random(SEED)
    stats = dict(systems=SYSTEMS, subset_checks=0, deficient=0, singletons=0,
                 nontrivial=0, cut_arcs=0, positive_arcs=0, deficit_units=0,
                 nontrivial_deficit=0, positive_pressure=0,
                 backward_crossings=0, typed_mixed=0)
    for _ in range(SYSTEMS):
        n, edges, source, sink, demands, types = make_system(rng)
        terminal_count = len(demands)
        values = {}
        for mask in range(1, 1 << terminal_count):
            value, _, _ = maxflow(n, edges, source, sink, enabled(demands, mask))
            demand = sum(demands[k] for k in range(terminal_count) if mask >> k & 1)
            values[mask] = (value, demand - value)
            stats["subset_checks"] += 1
        deficient = [mask for mask, (_, gap) in values.items() if gap > 0]
        if not deficient:
            continue
        size = min(mask.bit_count() for mask in deficient)
        core = min(mask for mask in deficient if mask.bit_count() == size)
        assert all(values[sub][1] == 0 for sub in range(1, 1 << terminal_count)
                   if sub != core and sub & core == sub)
        delta = values[core][1]
        stats["deficient"] += 1
        stats["deficit_units"] += delta
        members = [k for k in range(terminal_count) if core >> k & 1]
        if len(members) == 1:
            stats["singletons"] += 1
            continue
        left_type = [k for k in members if types[k] == 0]
        right_type = [k for k in members if types[k] == 1]
        if TYPED and left_type and right_type:
            part_a = sum(1 << k for k in left_type)
            stats["typed_mixed"] += 1
        else:
            part_a = sum(1 << k for k in members[:len(members) // 2])
        part_b = core ^ part_a
        assert values[part_a][1] == values[part_b][1] == 0
        stats["nontrivial"] += 1
        stats["nontrivial_deficit"] += delta
        _, _, reachable = maxflow(n, edges, source, sink, enabled(demands, core))
        value_a, flow_a, _ = maxflow(n, edges, source, sink, enabled(demands, part_a))
        value_b, flow_b, _ = maxflow(n, edges, source, sink, enabled(demands, part_b))
        assert value_a + value_b == sum(demands[k] for k in members)
        signed = positive = positive_count = cut_count = backward = 0
        maximum = 0
        caps = enabled(demands, core)
        for u, v, capacity, key in edges:
            capacity = caps.get(key, capacity)
            load = flow_a[(u, v, key)] + flow_b[(u, v, key)]
            if reachable[u] and not reachable[v]:
                pressure = load - capacity
                signed += pressure
                cut_count += 1
                if pressure > 0:
                    positive += pressure
                    positive_count += 1
                    maximum = max(maximum, pressure)
            elif not reachable[u] and reachable[v]:
                signed -= load
                backward += load
        assert signed == delta
        assert positive >= delta and positive_count > 0
        assert maximum * cut_count >= delta
        stats["cut_arcs"] += cut_count
        stats["positive_arcs"] += positive_count
        stats["positive_pressure"] += positive
        stats["backward_crossings"] += backward
    print("AC canonical cut-pressure audit passed")
    for key, value in stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
