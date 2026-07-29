#!/usr/bin/env python3
from math import ceil

S = range(3)
T = range(4)


def edge_coloring(edges, delta):
    # Exact backtracking is tiny for the 3x4 audit family.
    deg_s = {s: 0 for s in S}
    deg_t = {t: 0 for t in T}
    for s, t in edges:
        deg_s[s] += 1
        deg_t[t] += 1
    ordered = sorted(edges, key=lambda e: (deg_s[e[0]] + deg_t[e[1]], deg_s[e[0]], deg_t[e[1]]), reverse=True)
    used_s = {s: set() for s in S}
    used_t = {t: set() for t in T}
    color = {}

    def rec(i):
        if i == len(ordered):
            return True
        s, t = ordered[i]
        available = [c for c in range(delta) if c not in used_s[s] and c not in used_t[t]]
        for c in available:
            color[(s, t)] = c
            used_s[s].add(c)
            used_t[t].add(c)
            if rec(i + 1):
                return True
            used_s[s].remove(c)
            used_t[t].remove(c)
            del color[(s, t)]
        return False

    assert rec(0)
    return color


valid_graphs = 0
colored_edges = 0
largest_bank = 0
for mask in range(1 << 12):
    edges = [(s, t) for s in S for t in T if mask & (1 << (4 * s + t))]
    deg_s = [sum(1 for e in edges if e[0] == s) for s in S]
    if min(deg_s, default=0) < 2:
        continue
    deg_t = [sum(1 for e in edges if e[1] == t) for t in T]
    delta = max(max(deg_s), max(deg_t))
    coloring = edge_coloring(edges, delta)
    banks = [[] for _ in range(delta)]
    for edge, c in coloring.items():
        banks[c].append(edge)
    # Each color is a private-marker matching.
    for bank in banks:
        assert len({s for s, _ in bank}) == len(bank)
        assert len({t for _, t in bank}) == len(bank)
    assert sorted(edge for bank in banks for edge in bank) == sorted(edges)
    assert max(map(len, banks)) >= ceil(len(edges) / delta)
    valid_graphs += 1
    colored_edges += len(edges)
    largest_bank = max(largest_bank, max(map(len, banks)))

assert valid_graphs > 0
print({
    "valid_rectangles": valid_graphs,
    "colored_residual_edges": colored_edges,
    "max_private_bank": largest_bank,
    "core_size": 1,
})
