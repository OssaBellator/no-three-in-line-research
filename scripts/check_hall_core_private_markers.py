#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations
from math import comb, ceil
import random

rng = random.Random(20260729)
checked = 0
nontrivial = 0

for _ in range(10_000):
    s = rng.randint(4, 8)
    t = rng.randint(5, 9)
    d0 = rng.randint(2, min(4, t - 1))
    graph = []
    for _x in range(s):
        degree = rng.randint(d0, min(t, d0 + 2))
        graph.append(set(rng.sample(range(t), degree)))
    d = min(map(len, graph))
    D = max(map(len, graph))
    target_deg = [sum(y in graph[x] for x in range(s)) for y in range(t)]
    Delta = max(target_deg)

    for q in range(1, d):
        support = defaultdict(list)
        for x, neigh in enumerate(graph):
            for C in combinations(sorted(neigh), q):
                support[C].append(x)
        C, F = max(support.items(), key=lambda kv: len(kv[1]))
        f_bound = ceil(s * comb(d, q) / comb(t, q))
        assert len(F) >= f_bound

        residual_edges = [(x, y) for x in F for y in graph[x] if y not in C]
        assert len(residual_edges) >= len(F) * (d - q)

        remaining = list(residual_edges)
        matching = []
        while remaining:
            edge = remaining[0]
            matching.append(edge)
            x0, y0 = edge
            remaining = [(x, y) for x, y in remaining if x != x0 and y != y0]
        bound = ceil(len(F) * (d - q) / (D + Delta - 1))
        assert len(matching) >= bound
        assert len({x for x, _ in matching}) == len(matching)
        assert len({y for _, y in matching}) == len(matching)
        checked += 1
        nontrivial += int(bound >= 2)

print({"rectangles": 10_000, "core_orders_checked": checked, "bounds_at_least_two": nontrivial})
