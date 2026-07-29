#!/usr/bin/env python3
from fractions import Fraction

V = range(4)
EDGES = {
    (0, 1): Fraction(3, 4),
    (1, 0): Fraction(4, 5),
    (1, 2): Fraction(2, 3),
    (2, 3): Fraction(5, 6),
    (3, 1): Fraction(3, 4),
    (0, 2): Fraction(7, 10),
    (2, 0): Fraction(4, 5),
}


def canonical_cycle(vertices):
    # vertices does not repeat the start.  Rotate to the lexicographically least tuple.
    rotations = [tuple(vertices[i:] + vertices[:i]) for i in range(len(vertices))]
    return min(rotations)


def simple_cycles():
    found = set()
    for start in V:
        stack = [(start, [start])]
        while stack:
            u, path = stack.pop()
            for (a, b), _ in EDGES.items():
                if a != u:
                    continue
                if b == start and len(path) >= 2:
                    found.add(canonical_cycle(path))
                elif b not in path and len(path) < len(V):
                    stack.append((b, path + [b]))
    return sorted(found)


def product_of_cycle(cycle):
    out = Fraction(1)
    for i, u in enumerate(cycle):
        v = cycle[(i + 1) % len(cycle)]
        out *= EDGES[(u, v)]
    return out


def rate_greater(c1, c2):
    p1, l1 = product_of_cycle(c1), len(c1)
    p2, l2 = product_of_cycle(c2), len(c2)
    return p1 ** l2 > p2 ** l1

cycles = simple_cycles()
assert cycles
critical = cycles[0]
for cycle in cycles[1:]:
    if rate_greater(cycle, critical):
        critical = cycle

critical_product = product_of_cycle(critical)
critical_length = len(critical)
assert critical == (0, 1)
assert critical_product == Fraction(3, 5)
assert critical_length == 2

# Exact algebraic certificate: every other cycle D obeys P_D^ell <= P_C^|D|.
for cycle in cycles:
    p = product_of_cycle(cycle)
    assert p ** critical_length <= critical_product ** len(cycle)

# A rational edgewise perturbation factor Gamma preserves the unique critical cycle
# when P_C^m > P_D^ell Gamma^(2 ell m) for every D != C.
Gamma = Fraction(1001, 1000)
for cycle in cycles:
    if cycle == critical:
        continue
    p = product_of_cycle(cycle)
    m = len(cycle)
    assert critical_product ** m > p ** critical_length * Gamma ** (2 * critical_length * m)

print({
    "simple_cycles": len(cycles),
    "critical_cycle": critical,
    "critical_product": str(critical_product),
    "critical_polynomial": "x^2-3/5",
    "robust_gamma": str(Gamma),
    "cycle_data": [(cycle, str(product_of_cycle(cycle))) for cycle in cycles],
})
