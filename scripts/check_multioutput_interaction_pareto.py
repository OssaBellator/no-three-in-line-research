#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

atoms = {
    "A": (2, (F(2, 5), F(0))),
    "B": (2, (F(0), F(2, 5))),
    "C": (3, (F(1, 4), F(1, 4))),
    "D": (1, (F(1, 10), F(1, 10))),
}
total = (F(4, 5), F(4, 5))
max_budget = sum(cost for cost, _ in atoms.values())

def omitted(subset):
    red0 = sum(atoms[a][1][0] for a in subset)
    red1 = sum(atoms[a][1][1] for a in subset)
    return (total[0] - red0, total[1] - red1)

def cost(subset):
    return sum(atoms[a][0] for a in subset)

def pareto(points):
    out = []
    for p, witness in points:
        if any(q[0] <= p[0] and q[1] <= p[1] and q != p for q, _ in points):
            continue
        if p not in [q for q, _ in out]:
            out.append((p, witness))
    return sorted(out)

frontiers = {}
names = tuple(atoms)
for budget in range(max_budget + 1):
    pts = []
    for r in range(len(names) + 1):
        for subset in combinations(names, r):
            if cost(subset) <= budget:
                pts.append((omitted(subset), subset))
    frontiers[budget] = pareto(pts)

budget3 = {p: s for p, s in frontiers[3]}
assert budget3 == {
    (F(3, 10), F(7, 10)): ("A", "D"),
    (F(7, 10), F(3, 10)): ("B", "D"),
    (F(11, 20), F(11, 20)): ("C",),
}
unsupported = (F(11, 20), F(11, 20))
for k in range(101):
    w = F(k, 100)
    score = lambda p: w * p[0] + (1 - w) * p[1]
    assert score(unsupported) >= min(score(p) for p in budget3 if p != unsupported)

tol = (F(3, 5), F(3, 5))
first = next(b for b in frontiers if any(p[0] <= tol[0] and p[1] <= tol[1] for p, _ in frontiers[b]))
assert first == 3
assert not any(p[0] <= tol[0] and p[1] <= tol[1] for p, _ in frontiers[2])
assert [s for p, s in frontiers[3] if p[0] <= tol[0] and p[1] <= tol[1]] == [("C",)]

print({
    "atoms": len(atoms),
    "budget3_pareto_vectors": [[str(x), str(y)] for (x, y), _ in frontiers[3]],
    "unsupported_pareto_vector": [str(x) for x in unsupported],
    "minimum_tolerance_budget": first,
    "unique_budget3_plan": ["C"],
})
