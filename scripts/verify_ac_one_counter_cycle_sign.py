#!/usr/bin/env python3
"""Finite audit for AC3st--AC3sx."""

import random
from collections import defaultdict, deque

SEED = 20260727
INF = 10**12


def shortest_labels(q, edges):
    d = [0] * q
    for _ in range(q - 1):
        changed = False
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                changed = True
        if not changed:
            break
    negative_cycle = any(d[v] > d[u] + w for u, v, w in edges)
    return d, negative_cycle


def no_negative_cycle(q, edges):
    dist = [[INF] * q for _ in range(q)]
    for i in range(q):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
    for k in range(q):
        for i in range(q):
            if dist[i][k] >= INF:
                continue
            for j in range(q):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return all(dist[i][i] >= 0 for i in range(q))


def zero_graph_acyclic(q, reduced_edges):
    adj = [[] for _ in range(q)]
    indeg = [0] * q
    for u, v, w in reduced_edges:
        if w == 0:
            adj[u].append(v)
            indeg[v] += 1
    queue = deque(i for i in range(q) if indeg[i] == 0)
    seen = 0
    while queue:
        u = queue.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                queue.append(v)
    return seen == q


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)
    for q in range(2, 9):
        for _ in range(6000):
            W = rng.randint(1, 7)
            edges = []
            for u in range(q):
                for v in range(q):
                    if rng.random() < 0.24:
                        edges.append((u, v, rng.randint(-W, W)))
            if not edges:
                continue

            nonnegative = no_negative_cycle(q, edges)
            d, negative_cycle = shortest_labels(q, edges)
            assert nonnegative == (not negative_cycle)
            if nonnegative:
                assert min(d) >= -(q - 1) * W
                assert max(d) <= 0
                reduced = [(u, v, w + d[u] - d[v]) for u, v, w in edges]
                assert all(w >= 0 for _, _, w in reduced)
                counts["nonnegative_systems"] += 1
                if zero_graph_acyclic(q, reduced):
                    counts["zero_edge_acyclic_systems"] += 1

            negated = [(u, v, -w) for u, v, w in edges]
            nonpositive = no_negative_cycle(q, negated)
            d_minus, positive_cycle = shortest_labels(q, negated)
            assert nonpositive == (not positive_cycle)
            if nonpositive:
                assert min(d_minus) >= -(q - 1) * W
                assert max(d_minus) <= 0
                assert all(w + d_minus[v] - d_minus[u] <= 0 for u, v, w in edges)
                counts["nonpositive_systems"] += 1

            counts["graphs"] += 1

    print("AC one-counter cycle-sign audit passed")
    print(f"  weighted control graphs: {counts['graphs']}")
    print(f"  nonnegative-cycle systems: {counts['nonnegative_systems']}")
    print(f"  nonpositive-cycle systems: {counts['nonpositive_systems']}")
    print(f"  zero-reduced-edge acyclic systems: {counts['zero_edge_acyclic_systems']}")


if __name__ == "__main__":
    main()
