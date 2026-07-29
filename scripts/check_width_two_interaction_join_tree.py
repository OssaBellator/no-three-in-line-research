#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product

def dominates(u, v):
    return u[0] <= v[0] and u[1] <= v[1] and u != v

def pareto(plans):
    out = []
    for plan in plans:
        w, e, witness = plan
        if any(w2 <= w and (e2 == e or dominates(e2, e))
               for w2, e2, other in plans if (w2, e2, other) != plan):
            continue
        if not any(w == w2 and e == e2 for w2, e2, _ in out):
            out.append(plan)
    return sorted(out, key=lambda z: (z[0], z[1], z[2]))

def budget_frontier(plans, budget):
    candidates = [(w, e, witness) for w, e, witness in plans if w <= budget]
    vectors = []
    for w, e, witness in candidates:
        if any(dominates(e2, e) for _, e2, _ in candidates):
            continue
        if not any(e == e2 for _, e2, _ in vectors):
            vectors.append((w, e, witness))
    return sorted(vectors, key=lambda z: (z[1], z[0], z[2]))

left_messages = {}
for b, c in product((0, 1), repeat=2):
    plans = []
    for a in (0, 1):
        work = a + b
        error = (F(2) - F(a + b, 2), F(0))
        plans.append((work, error, (a, b, c)))
    left_messages[(b, c)] = pareto(plans)

assert set(left_messages) == set(product((0, 1), repeat=2))

joined = []
for b, c in product((0, 1), repeat=2):
    for lw, le, left_witness in left_messages[(b, c)]:
        for d in (0, 1):
            rw = c + d
            re = (F(0), F(2) - F(c + d, 2))
            witness = (left_witness[0], b, c, d)
            joined.append((lw + rw, (le[0] + re[0], le[1] + re[1]), witness))

direct = []
for a, b, c, d in product((0, 1), repeat=4):
    work = a + b + c + d
    error = (F(2) - F(a + b, 2), F(2) - F(c + d, 2))
    direct.append((work, error, (a, b, c, d)))

assert sorted(joined) == sorted(direct)
assert len(joined) == 16

frontier_sizes = {}
for budget in range(5):
    jt = budget_frontier(joined, budget)
    brute = budget_frontier(direct, budget)
    assert [(w, e) for w, e, _ in jt] == [(w, e) for w, e, _ in brute]
    frontier_sizes[budget] = len(jt)

tolerance = (F(1), F(1))
feasible_by_budget = {}
for budget in range(5):
    plans = [p for p in budget_frontier(joined, budget)
             if p[1][0] <= tolerance[0] and p[1][1] <= tolerance[1]]
    feasible_by_budget[budget] = plans

assert not feasible_by_budget[3]
assert feasible_by_budget[4] == [(4, (F(1), F(1)), (1, 1, 1, 1))]

print({
    "bag_count": 2,
    "bag_size": 3,
    "separator_size": 2,
    "separator_signatures": len(left_messages),
    "global_assignments": len(direct),
    "frontier_sizes_by_budget": frontier_sizes,
    "tolerance": [str(x) for x in tolerance],
    "minimum_work": 4,
    "unique_plan": feasible_by_budget[4][0][2],
})
