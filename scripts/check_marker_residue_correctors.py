#!/usr/bin/env python3
from fractions import Fraction

# State 0 has a correction loop D of scalar cost 2 and a critical
# three-edge cycle A,B,C of scalar cost 1 per edge.
# Every closed walk is D^r (ABC)^q up to cyclic ordering.

def optimum(n: int):
    q, r = divmod(n, 3)
    word = "D" * r + "ABC" * q
    counts = tuple(word.count(ch) for ch in "ABCD")
    cost = 3 * q + 2 * r
    return word, counts, cost

for n in range(1, 121):
    word, counts, cost = optimum(n)
    q, r = divmod(n, 3)
    assert len(word) == n
    assert counts == (q, q, q, r)
    assert cost == n + r
    # Any closed walk has k copies of ABC and l D-loops with 3k+l=n.
    candidates = []
    for k in range(n // 3 + 1):
        l = n - 3 * k
        candidates.append((3 * k + 2 * l, k, l))
    assert min(candidates)[0] == cost
    rate = tuple(Fraction(x, n) for x in counts)
    target = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3), Fraction(0))
    assert max(abs(rate[i] - target[i]) for i in range(4)) <= Fraction(2, n)

print({
    "lengths_checked": 120,
    "critical_period": 3,
    "residue_costs": (0, 2, 4),
    "exact_cost_formula": "N + (N mod 3)",
    "rate_error_bound": "2/N",
})
