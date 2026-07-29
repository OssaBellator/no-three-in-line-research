#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

loads = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]
p = Fraction(3, 4)
m = len(loads)

best = None
best_lengths = None
feasible = []
for lengths in product(range(1, m), repeat=m):
    kraft = sum(Fraction(1, 2**ell) for ell in lengths)
    if kraft > 1:
        continue
    risk = max(loads[i] * p ** (-lengths[i]) for i in range(m))
    feasible.append((risk, lengths))
    if best is None or risk < best:
        best = risk
        best_lengths = lengths

assert best == Fraction(2, 3)
assert best_lengths is not None

candidates = sorted({loads[i] * p ** (-ell) for i in range(m) for ell in range(1, m)})
def kraft_test(R: Fraction) -> bool:
    lengths = []
    for lam in loads:
        allowed = [ell for ell in range(1, m) if lam * p ** (-ell) <= R]
        if not allowed:
            return False
        lengths.append(max(allowed))
    return sum(Fraction(1, 2**ell) for ell in lengths) <= 1

candidate_optimum = next(R for R in candidates if kraft_test(R))
assert candidate_optimum == best
assert max(best_lengths) <= m - 1
print({
    "classes": m,
    "feasible_length_vectors": len(feasible),
    "optimum": str(best),
    "one_optimal_length_vector": best_lengths,
    "candidate_count": len(candidates),
})
