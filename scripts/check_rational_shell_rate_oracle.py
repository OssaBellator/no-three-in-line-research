#!/usr/bin/env python3
from fractions import Fraction

nodes = list(range(4))
edges = [
    (0, 1, Fraction(2, 3)),
    (1, 0, Fraction(3, 4)),
    (1, 2, Fraction(4, 5)),
    (2, 1, Fraction(2, 3)),
    (2, 3, Fraction(3, 5)),
    (3, 2, Fraction(4, 5)),
    (0, 2, Fraction(1, 2)),
    (2, 0, Fraction(5, 6)),
    (0, 3, Fraction(1, 2)),
    (3, 0, Fraction(7, 10)),
]

def oracle(q: Fraction):
    a = [Fraction(1) for _ in nodes]
    pred = [None for _ in nodes]
    changed = None
    for _round in range(len(nodes)):
        changed = None
        old = a[:]
        for u, v, p in edges:
            candidate = p * old[v] / q
            if candidate > a[u]:
                a[u] = candidate
                pred[u] = v
                changed = u
        if changed is None:
            for u, v, p in edges:
                assert p * a[v] <= q * a[u]
            return True, a
    # A change in the |V|-th round implies an expansive cycle.  Follow
    # predecessor pointers into the cycle, then read it in edge orientation.
    x = changed
    for _ in nodes:
        x = pred[x]
    cycle = [x]
    y = pred[x]
    while y != x:
        cycle.append(y)
        y = pred[y]
    product_weight = Fraction(1)
    for u in cycle:
        v = pred[u]
        weight = next(p for uu, vv, p in edges if uu == u and vv == v)
        product_weight *= weight
    assert product_weight > q ** len(cycle)
    return False, (cycle, product_weight)

q_minus = Fraction(763, 1000)
q_plus = Fraction(191, 250)
ok_minus, witness = oracle(q_minus)
ok_plus, potential = oracle(q_plus)
assert not ok_minus and ok_plus
assert len(set(potential)) > 1

gamma = Fraction(1000, 999)
assert gamma * q_plus < 1
for u, v, p in edges:
    assert gamma * p * potential[v] <= gamma * q_plus * potential[u]

cycle, cycle_product = witness
print({
    "lower_rate": str(q_minus),
    "lower_cycle": cycle,
    "lower_cycle_product": str(cycle_product),
    "upper_rate": str(q_plus),
    "upper_potential": [str(x) for x in potential],
    "robust_factor": str(gamma),
    "robust_rate": str(gamma * q_plus),
})
