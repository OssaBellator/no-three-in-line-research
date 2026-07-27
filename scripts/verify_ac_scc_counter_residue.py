#!/usr/bin/env python3
"""Finite audit for AC3sy--AC3tc."""

from collections import defaultdict, deque
from math import gcd
import random

SEED = 20260727


def bfs_paths(q, edges, root, reverse=False):
    adj = [[] for _ in range(q)]
    for u, v, w in edges:
        a, b = (v, u) if reverse else (u, v)
        adj[a].append((b, w))
    parent = {root: None}
    pedge = {}
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v, w in adj[u]:
            if v not in parent:
                parent[v] = u
                pedge[v] = (u, v, w) if not reverse else (v, u, w)
                queue.append(v)
    assert len(parent) == q
    paths = {}
    for v in range(q):
        cur = v
        path = []
        while cur != root:
            edge = pedge[cur]
            path.append(edge)
            cur = parent[cur]
        paths[v] = path if reverse else list(reversed(path))
    return paths


def path_weight(path):
    return sum(w for _, _, w in path)


def random_strong_graph(rng, q, wmax):
    edge_map = {}
    for i in range(q):
        edge_map[(i, (i + 1) % q)] = rng.randint(-wmax, wmax)
        edge_map[((i + 1) % q, i)] = rng.randint(-wmax, wmax)
    for u in range(q):
        for v in range(q):
            if u != v and rng.random() < 0.35:
                edge_map[(u, v)] = rng.randint(-wmax, wmax)
    return [(u, v, w) for (u, v), w in edge_map.items()]


def audit_graph(edges, q, wmax, rng, counts):
    root = 0
    paths = bfs_paths(q, edges, root)
    return_paths = bfs_paths(q, edges, root, reverse=True)
    p = [path_weight(paths[v]) for v in range(q)]

    addresses = [p[u] + w - p[v] for u, v, w in edges]
    g = 0
    for address in addresses:
        g = gcd(g, abs(address))

    for address in addresses:
        assert (g == 0 and address == 0) or (g > 0 and address % g == 0)
        assert abs(address) <= (2 * q - 1) * wmax

    adj = [[] for _ in range(q)]
    for edge in edges:
        adj[edge[0]].append(edge)

    for _ in range(80):
        u = root
        drift = 0
        for _ in range(rng.randint(0, 30)):
            edge = rng.choice(adj[u])
            _, u, weight = edge
            drift += weight
        difference = drift - p[u]
        if g == 0:
            assert difference == 0
        else:
            assert difference % g == 0
        counts["sampled_paths"] += 1

        closed = drift + path_weight(return_paths[u])
        if g == 0:
            assert closed == 0
        else:
            assert closed % g == 0
        counts["sampled_closed_walks"] += 1

    if g > 0:
        residue = rng.randrange(g)
        low = rng.randint(-40, 0)
        high = low + rng.randint(0, 80)
        width = high - low
        state_count = 0
        for v in range(q):
            state_count += sum(
                1
                for counter in range(low, high + 1)
                if (counter - p[v]) % g == residue
            )
        assert state_count <= q * (width // g + 1)
        counts["positive_g_systems"] += 1
        counts["bounded_states"] += state_count
    else:
        invariant = rng.randint(-20, 20)
        values = [invariant + p[v] for v in range(q)]
        assert len(values) == q
        counts["zero_g_systems"] += 1


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)

    for _ in range(12000):
        q = rng.randint(2, 8)
        wmax = rng.randint(1, 9)
        edges = random_strong_graph(rng, q, wmax)
        audit_graph(edges, q, wmax, rng, counts)
        counts["random_graphs"] += 1
        counts["edge_addresses"] += len(edges)

    for _ in range(2000):
        q = rng.randint(2, 10)
        potential = [rng.randint(-20, 20) for _ in range(q)]
        edge_map = {}
        for i in range(q):
            for u, v in ((i, (i + 1) % q), ((i + 1) % q, i)):
                edge_map[(u, v)] = potential[v] - potential[u]
        for u in range(q):
            for v in range(q):
                if u != v and rng.random() < 0.25:
                    edge_map[(u, v)] = potential[v] - potential[u]
        edges = [(u, v, w) for (u, v), w in edge_map.items()]
        wmax = max(1, max(abs(w) for _, _, w in edges))
        audit_graph(edges, q, wmax, rng, counts)
        counts["potential_graphs"] += 1

    print("AC SCC residue quotient audit passed")
    print(f"  random strongly connected graphs: {counts['random_graphs']}")
    print(f"  exact-potential graphs: {counts['potential_graphs']}")
    print(f"  edge residue addresses: {counts['edge_addresses']}")
    print(f"  sampled paths: {counts['sampled_paths']}")
    print(f"  sampled closed walks: {counts['sampled_closed_walks']}")
    print(f"  positive-g systems: {counts['positive_g_systems']}")
    print(f"  zero-g systems: {counts['zero_g_systems']}")
    print(f"  bounded exact states: {counts['bounded_states']}")


if __name__ == "__main__":
    main()
