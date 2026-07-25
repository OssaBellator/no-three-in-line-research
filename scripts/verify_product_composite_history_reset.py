#!/usr/bin/env python3
"""Finite verifier for PX330--PX333."""

from itertools import product


def has_cycle(n, arcs):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in arcs:
        adj[u].append(v)
        indeg[v] += 1
    stack = [v for v in range(n) if indeg[v] == 0]
    seen = 0
    while stack:
        u = stack.pop()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    return seen != n


def topological_order(n, arcs):
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in arcs:
        adj[u].append(v)
        indeg[v] += 1
    stack = [v for v in range(n) if indeg[v] == 0]
    order = []
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                stack.append(v)
    assert len(order) == n
    return order


def check_pattern(n, states):
    arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
    base = {a for a, x in zip(arcs, states) if x == 0}
    hist = {a for a, x in zip(arcs, states) if x == 1}

    row = [sum((u, v) in base for v in range(n) if v != u) for u in range(n)]
    col = [sum((u, v) in base for u in range(n) if u != v) for v in range(n)]
    delta0 = max(row + col, default=0)

    if not has_cycle(n, hist):
        assert n <= delta0 + 1
        order = topological_order(n, hist)
        pos = {v: i for i, v in enumerate(order)}
        for u in range(n):
            for v in range(n):
                if u != v and pos[u] > pos[v]:
                    assert (u, v) in base


def exhaustive():
    for n in range(1, 5):
        arcs = n * (n - 1)
        for states in product((0, 1), repeat=arcs):
            check_pattern(n, states)

    n = 5
    arcs = [(u, v) for u in range(n) for v in range(n) if u != v]
    forward = [(u, v) for u in range(n) for v in range(u + 1, n)]
    for bits in product((0, 1), repeat=len(forward)):
        hist = {a for a, bit in zip(forward, bits) if bit}
        states = tuple(1 if a in hist else 0 for a in arcs)
        check_pattern(n, states)


def sharp_transitive_split():
    for delta0 in range(0, 5):
        n = delta0 + 1
        base = {(u, v) for u in range(n) for v in range(n) if u > v}
        hist = {(u, v) for u in range(n) for v in range(n) if u < v}
        assert not has_cycle(n, hist)
        row = [sum((u, v) in base for v in range(n) if v != u) for u in range(n)]
        col = [sum((u, v) in base for u in range(n) if u != v) for v in range(n)]
        assert max(row + col, default=0) == delta0
        assert n == delta0 + 1


if __name__ == "__main__":
    exhaustive()
    sharp_transitive_split()
    print("PX330--PX333 verified")
