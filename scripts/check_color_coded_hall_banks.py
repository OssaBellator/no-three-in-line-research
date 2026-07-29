#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

TARGETS = 4
NONEMPTY = [tuple(y for y in range(TARGETS) if (mask >> y) & 1) for mask in range(1, 1 << TARGETS)]

def edge_color(neighborhoods):
    edges = [(x, y) for x, ns in enumerate(neighborhoods) for y in ns]
    dx = [len(ns) for ns in neighborhoods]
    dy = [sum(y in ns for ns in neighborhoods) for y in range(TARGETS)]
    delta = max(dx + dy)
    used_x = [set() for _ in neighborhoods]
    used_y = [set() for _ in range(TARGETS)]
    color = {}
    def recurse():
        if len(color) == len(edges):
            return True
        best = best_avail = None
        for edge in edges:
            if edge in color:
                continue
            x, y = edge
            avail = [c for c in range(delta) if c not in used_x[x] and c not in used_y[y]]
            if not avail:
                return False
            if best is None or len(avail) < len(best_avail):
                best, best_avail = edge, avail
                if len(avail) == 1:
                    break
        x, y = best
        for c in best_avail:
            color[best] = c
            used_x[x].add(c)
            used_y[y].add(c)
            if recurse():
                return True
            del color[best]
            used_x[x].remove(c)
            used_y[y].remove(c)
        return False
    assert recurse()
    return delta, color

graphs = edges_checked = 0
for neighborhoods in product(NONEMPTY, repeat=3):
    delta, colors = edge_color(neighborhoods)
    d_min = min(len(ns) for ns in neighborhoods)
    tagged = {}
    for (x, y), c in colors.items():
        key = (y, c)
        tagged[key] = tagged.get(key, Fraction(0)) + Fraction(1, len(neighborhoods[x]))
    assert max(tagged.values()) <= Fraction(1, d_min)
    g = max(sum(1 for c in range(delta) if c % 2 == bit) for bit in (0, 1))
    coded = {}
    for (x, y), c in colors.items():
        key = (y, c % 2)
        coded[key] = coded.get(key, Fraction(0)) + Fraction(1, len(neighborhoods[x]))
    assert max(coded.values()) <= Fraction(g, d_min)
    graphs += 1
    edges_checked += len(colors)

print({
    "graphs_checked": graphs,
    "colored_edges_checked": edges_checked,
    "maximum_degree": 4,
    "tagged_bound": "1/d_min",
    "coded_bound": "g/d_min",
})
