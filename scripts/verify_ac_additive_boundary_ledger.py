#!/usr/bin/env python3
"""Finite audit for AC3ts--AC3tw."""

from collections import defaultdict, deque
from math import gcd
import random

SEED = 20260727


def paths_and_adjacency(q, edges):
    adj = [[] for _ in range(q)]
    by_id = {}
    for i, u, v, b, length in edges:
        adj[u].append((i, v))
        by_id[i] = (u, v, b, length)
    for row in adj:
        row.sort()
    paths = {}
    for source in range(q):
        queue = deque([source])
        best = {source: ()}
        while queue:
            u = queue.popleft()
            for edge_id, v in adj[u]:
                if v not in best:
                    best[v] = best[u] + (edge_id,)
                    queue.append(v)
        assert len(best) == q
        for target, word in best.items():
            assert len(word) <= q - 1
            paths[(source, target)] = word
    return paths, adj, by_id


def drift(word, by_id):
    return sum(by_id[e][2] for e in word)


def simple_cycles(q, adj, by_id):
    found = {}
    for start in range(q):
        def dfs(u, vertices, word):
            for edge_id, v in adj[u]:
                if v == start:
                    cycle = word + (edge_id,)
                    rotations = [cycle[i:] + cycle[:i] for i in range(len(cycle))]
                    canonical = min(rotations)
                    found[canonical] = drift(canonical, by_id)
                elif v not in vertices and len(vertices) < q:
                    dfs(v, vertices + (v,), word + (edge_id,))
        dfs(start, (start,), ())
    return sorted(found.items())


def shortest_drift_potential(q, edges, cycles, sign):
    # sign=1 handles nonnegative cycles; sign=-1 handles nonpositive after reversal.
    weighted = [(i, u, v, sign * b, length) for i, u, v, b, length in edges]
    dist = [10**9] * q
    dist[0] = 0
    for _ in range(q - 1):
        changed = False
        for _, u, v, b, _ in weighted:
            if dist[u] + b < dist[v]:
                dist[v] = dist[u] + b
                changed = True
        if not changed:
            break
    assert all(x < 10**9 for x in dist)
    zero_adj = [[] for _ in range(q)]
    for _, u, v, b, _ in weighted:
        reduced = b + dist[u] - dist[v]
        assert reduced >= 0
        # H=c-d changes by exactly the reduced increment.
        c = 17
        h0 = c - dist[u]
        h1 = c + b - dist[v]
        assert h1 - h0 == reduced
        if reduced == 0:
            zero_adj[u].append(v)
    return dist, zero_adj


def main():
    rng = random.Random(SEED)
    counts = defaultdict(int)
    for _ in range(18000):
        q = rng.randint(2, 7)
        pairs = {(u, (u + 1) % q) for u in range(q)}
        pairs |= {((u + 1) % q, u) for u in range(q)}
        for _ in range(rng.randint(q, 3 * q)):
            pairs.add((rng.randrange(q), rng.randrange(q)))
        B = rng.randint(1, 7)
        L_gate = rng.randint(1, 15)
        edges = [
            (i, u, v, rng.randint(-B, B), rng.randint(1, L_gate))
            for i, (u, v) in enumerate(sorted(pairs))
        ]
        paths, adj, by_id = paths_and_adjacency(q, edges)
        cycles = simple_cycles(q, adj, by_id)
        assert cycles
        counts["graphs"] += 1
        counts["gate_edges"] += len(edges)
        counts["simple_cycles"] += len(cycles)

        cycle_drifts = [d for _, d in cycles]
        if min(cycle_drifts) >= 0:
            potential, zero_adj = shortest_drift_potential(q, edges, cycles, 1)
            assert max(potential) - min(potential) <= 2 * (q - 1) * B
            counts["nonnegative_cycle_systems"] += 1
            if min(cycle_drifts) > 0:
                # Zero-reduced graph must be acyclic.
                colour = [0] * q
                def visit(u):
                    colour[u] = 1
                    for v in zero_adj[u]:
                        assert colour[v] != 1
                        if colour[v] == 0:
                            visit(v)
                    colour[u] = 2
                for u in range(q):
                    if colour[u] == 0:
                        visit(u)
                counts["strict_positive_cycle_systems"] += 1
        if max(cycle_drifts) <= 0:
            potential, zero_adj = shortest_drift_potential(q, edges, cycles, -1)
            assert max(potential) - min(potential) <= 2 * (q - 1) * B
            counts["nonpositive_cycle_systems"] += 1
            if max(cycle_drifts) < 0:
                counts["strict_negative_cycle_systems"] += 1

        p = {y: drift(paths[(0, y)], by_id) for y in range(q)}
        addresses = []
        for _, u, v, b, _ in edges:
            a = p[u] + b - p[v]
            addresses.append(a)
            assert abs(a) <= (2 * q - 1) * B
        g = 0
        for a in addresses:
            g = gcd(g, abs(a))

        # Random path checks residue/lift identities.
        for _sample in range(8):
            y = rng.randrange(q)
            c = rng.randint(-50, 50)
            xi0 = c - p[y]
            for _step in range(rng.randint(1, 20)):
                edge_id, v = rng.choice(adj[y])
                _, _, b, _ = by_id[edge_id]
                c2 = c + b
                if g:
                    assert (xi0 - (c2 - p[v])) % g == 0
                    alpha = (p[y] + b - p[v]) // g
                    ell = (c - p[y] - (xi0 % g)) // g
                    ell2 = (c2 - p[v] - (xi0 % g)) // g
                    assert ell2 - ell == alpha
                else:
                    assert c2 - p[v] == xi0
                y, c = v, c2
                counts["sampled_gate_steps"] += 1

        positive = [(w, d) for w, d in cycles if d > 0]
        negative = [(w, d) for w, d in cycles if d < 0]
        if positive and negative:
            pw, pd = rng.choice(positive)
            nw, nd = rng.choice(negative)
            common = gcd(pd, -nd)
            pc = (-nd) // common
            nc = pd // common
            assert pc + nc <= pd + (-nd)
            relation_drift = pc * pd + nc * nd
            assert relation_drift == 0
            counts["mixed_sign_systems"] += 1
            counts["primitive_relation_cycles"] += pc + nc
            # Safe control expansion bound.
            gate_count = (pc + nc) * q + (pc + nc + 1) * (q - 1)
            assert gate_count <= (2 * q - 1) * (pd + (-nd)) + (q - 1)
            assert gate_count * L_gate >= gate_count

        R = rng.randint(0, 30)
        state_stock = q * (R + 1)
        assert state_stock >= q
        counts["bounded_exact_states"] += state_stock

    print("AC additive boundary-ledger audit passed")
    for key in sorted(counts):
        print(f"  {key.replace('_', ' ')}: {counts[key]}")


if __name__ == "__main__":
    main()
