#!/usr/bin/env python3
"""Finite audit for BDA5as--BDA5au."""

from __future__ import annotations


def omega_pf(n: int) -> int:
    out = 0
    p = 2
    while p * p <= n:
        while n % p == 0:
            out += 1
            n //= p
        p += 1
    if n > 1:
        out += 1
    return out


def graph_edges(vertices, q):
    V = set(vertices)
    return {tuple(sorted((h, h + q))) for h in V if h + q in V}


def components(vertices, edges):
    adj = {v: set() for v in vertices}
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    seen = set()
    comps = []
    for v in vertices:
        if v in seen:
            continue
        stack = [v]
        comp = set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            seen.add(x)
            stack.extend(adj[x] - comp)
        comps.append(comp)
    return comps, adj


def verify_forests():
    systems = 0
    edges_checked = 0
    for H in range(1, 14):
        universe = list(range(1, H + 1))
        for mask in range(1, 1 << H):
            vertices = [universe[i] for i in range(H) if (mask >> i) & 1]
            for q in range(1, 6):
                E = graph_edges(vertices, q)
                comps, adj = components(vertices, E)
                assert all(len(adj[v]) <= 2 for v in vertices)
                for comp in comps:
                    edge_count = sum(len(adj[v]) for v in comp) // 2
                    assert edge_count == len(comp) - 1 or len(comp) == 1
                systems += 1
                edges_checked += len(E)
    return systems, edges_checked


def enumerate_walks(vertices, edges, length):
    adj = {v: [] for v in vertices}
    for x, y in edges:
        adj[x].append((y, tuple(sorted((x, y)))))
        adj[y].append((x, tuple(sorted((x, y)))))
    for start in vertices:
        stack = [(start, [], [start])]
        while stack:
            current, used, path = stack.pop()
            if len(used) == length:
                yield path, used
                continue
            for nxt, edge in adj[current]:
                stack.append((nxt, used + [edge], path + [nxt]))


def verify_walk_tickets():
    walks = 0
    closed = 0
    repeated = 0
    for H in range(3, 10):
        vertices = list(range(1, H + 1))
        for q in range(1, 4):
            E = graph_edges(vertices, q)
            for length in range(1, 8):
                for path, used in enumerate_walks(vertices, E, length):
                    walks += 1
                    if path[0] == path[-1]:
                        closed += 1
                        assert len(set(used)) < len(used)
                        repeated += 1
    return walks, closed, repeated


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def verify_descent_and_potential():
    divisor_edges = 0
    potential_steps = 0
    bounds = 0
    for q0 in range(2, 101):
        D = divisors(q0)
        for q in D:
            for qp in D:
                if q != qp and q % qp == 0:
                    assert omega_pf(qp) <= omega_pf(q) - 1
                    divisor_edges += 1
        for R in range(0, 30):
            ceiling = (R + 1) * omega_pf(q0) + R
            for q in D:
                for c in range(R + 1):
                    Xi = (R + 1) * (omega_pf(q0) - omega_pf(q)) + c
                    assert 0 <= Xi <= ceiling
                    bounds += 1
                    if c < R:
                        assert Xi + 1 > Xi
                        potential_steps += 1
                    for qp in D:
                        if q != qp and q % qp == 0:
                            Xip = (R + 1) * (omega_pf(q0) - omega_pf(qp)) + c
                            assert Xip >= Xi + R + 1
                            potential_steps += 1
    return divisor_edges, potential_steps, bounds


def main():
    forests = verify_forests()
    walks = verify_walk_tickets()
    desc = verify_descent_and_potential()
    print("BDA scalar cycle termination audit passed")
    print(f"finite scale graphs: {forests[0]}")
    print(f"adjacent edges checked: {forests[1]}")
    print(f"walks checked: {walks[0]}")
    print(f"closed walks: {walks[1]}")
    print(f"repeated-edge witnesses: {walks[2]}")
    print(f"strict divisor edges: {desc[0]}")
    print(f"potential transitions: {desc[1]}")
    print(f"potential bounds: {desc[2]}")


if __name__ == "__main__":
    main()
