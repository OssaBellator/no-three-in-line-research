#!/usr/bin/env python3
from fractions import Fraction
import json

V = ("A", "B", "C")
edges = {
    ("A", "B"): Fraction(1, 2),
    ("B", "A"): Fraction(1, 1),
    ("B", "C"): Fraction(2, 3),
    ("C", "B"): Fraction(3, 4),
    ("A", "C"): Fraction(1, 3),
    ("C", "A"): Fraction(1, 1),
}
q = Fraction(4, 5)
Phi = {"A": Fraction(5), "B": Fraction(7), "C": Fraction(7)}

cycles = set()

def canon(cyc):
    body = cyc[:-1]
    rots = [tuple(body[i:] + body[:i]) for i in range(len(body))]
    return min(rots)

for start in V:
    def dfs(path):
        u = path[-1]
        for (a, b), p in edges.items():
            if a != u:
                continue
            if b == start and len(path) >= 2:
                cycles.add(canon(path + [start]))
            elif b not in path and len(path) < len(V):
                dfs(path + [b])
    dfs([start])

cycle_data = []
for body in sorted(cycles):
    prod = Fraction(1)
    for i in range(len(body)):
        prod *= edges[(body[i], body[(i+1) % len(body)])]
    rhs = q ** len(body)
    assert prod < rhs
    cycle_data.append({"cycle": body, "product": str(prod), "q_power": str(rhs)})

margins = {}
for (u, v), p in edges.items():
    lhs = p * Phi[v]
    rhs = q * Phi[u]
    assert lhs < rhs
    margins[f"{u}->{v}"] = str(rhs - lhs)

print(json.dumps({
    "all_checks_passed": True,
    "vertices": len(V),
    "edges": len(edges),
    "simple_cycles": cycle_data,
    "q": str(q),
    "potential": {k: str(v) for k, v in Phi.items()},
    "edge_margins": margins,
}, indent=2))
