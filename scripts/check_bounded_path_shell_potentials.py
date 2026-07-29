#!/usr/bin/env python3
"""Exact checks for docs/427 bounded-path shell potentials."""

from fractions import Fraction
import json


def frac(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}"


vertices = ("A", "B", "C", "D")
edges = {
    ("A", "A"): Fraction(2, 5),
    ("A", "B"): Fraction(1, 2),
    ("B", "A"): Fraction(2, 3),
    ("B", "B"): Fraction(1, 2),
    ("B", "C"): Fraction(6, 5),
    ("C", "D"): Fraction(3, 5),
    ("D", "C"): Fraction(2, 5),
    ("D", "D"): Fraction(1, 3),
}


def simple_cycles():
    found = set()
    out = {u: [] for u in vertices}
    for (u, v), w in edges.items():
        out[u].append(v)

    def canonical(cycle):
        rotations = []
        n = len(cycle)
        for i in range(n):
            rotations.append(tuple(cycle[i:] + cycle[:i]))
        return min(rotations)

    def dfs(start, u, path, used):
        for v in out[u]:
            if v == start:
                found.add(canonical(path.copy()))
            elif v not in used and len(path) < len(vertices):
                used.add(v)
                path.append(v)
                dfs(start, v, path, used)
                path.pop()
                used.remove(v)

    for s in vertices:
        dfs(s, s, [s], {s})
    return sorted(found)


cycles = simple_cycles()
assert cycles


def cycle_product(cycle):
    ans = Fraction(1)
    for i, u in enumerate(cycle):
        v = cycle[(i + 1) % len(cycle)]
        ans *= edges[(u, v)]
    return ans


q_fail = Fraction(1, 2)
bad = [c for c in cycles if cycle_product(c) > q_fail ** len(c)]
assert bad
short_witness = min(bad, key=len)
assert len(short_witness) <= len(vertices)

q = Fraction(3, 4)
for c in cycles:
    assert cycle_product(c) <= q ** len(c)

out = {u: [] for u in vertices}
for (u, v), w in edges.items():
    out[u].append(v)


def max_path_gain(start):
    best = Fraction(1)

    def dfs(u, used, gain):
        nonlocal best
        best = max(best, gain)
        for v in out[u]:
            if v not in used:
                dfs(v, used | {v}, gain * edges[(u, v)] / q)

    dfs(start, {start}, Fraction(1))
    return best


potential = {u: max_path_gain(u) for u in vertices}
for (u, v), p in edges.items():
    assert p * potential[v] <= q * potential[u]

reach = {u: {u} for u in vertices}
for (u, v) in edges:
    reach[u].add(v)
changed = True
while changed:
    changed = False
    for u in vertices:
        expanded = set().union(*(reach[v] for v in list(reach[u])))
        if not expanded <= reach[u]:
            reach[u] |= expanded
            changed = True
sccs = []
unused = set(vertices)
while unused:
    u = next(iter(unused))
    comp = {v for v in vertices if v in reach[u] and u in reach[v]}
    sccs.append(sorted(comp))
    unused -= comp
assert sorted(map(tuple, sccs)) == sorted([("A", "B"), ("C", "D")])

print(json.dumps({
    "all_checks_passed": True,
    "simple_cycles": [
        {"cycle": list(c), "product": frac(cycle_product(c)), "length": len(c)}
        for c in cycles
    ],
    "failing_rate": frac(q_fail),
    "short_witness": list(short_witness),
    "successful_rate": frac(q),
    "bounded_path_potential": {u: frac(a) for u, a in potential.items()},
    "strongly_connected_components": sccs,
}, indent=2))
