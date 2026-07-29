#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations_with_replacement

rhos = [Fraction(1, 12), Fraction(1, 10), Fraction(1, 8), Fraction(1, 6), Fraction(1, 5), Fraction(1, 4), Fraction(1, 3)]
p = Fraction(3, 4)
K = len(rhos)

best = None
best_lengths = None
count = 0
for nondecreasing in combinations_with_replacement(range(1, K), K):
    lengths = tuple(reversed(nondecreasing))  # rho ascending, lengths descending
    if sum(Fraction(1, 2**ell) for ell in lengths) > 1:
        continue
    count += 1
    risk = max(rhos[i] * p ** (-lengths[i]) for i in range(K))
    if best is None or risk < best:
        best = risk
        best_lengths = lengths

assert best == Fraction(2048, 3645)
assert best_lengths == (6, 6, 5, 4, 3, 2, 1)

candidates = sorted({rho * p ** (-ell) for rho in rhos for ell in range(1, K)})
def feasible(R: Fraction) -> bool:
    lengths = []
    for rho in rhos:
        allowed = [ell for ell in range(1, K) if rho * p ** (-ell) <= R]
        if not allowed:
            return False
        lengths.append(max(allowed))
    return sum(Fraction(1, 2**ell) for ell in lengths) <= 1

candidate_best = next(R for R in candidates if feasible(R))
assert candidate_best == best
print({
    "banks": K,
    "monotone_length_vectors": count,
    "optimum": str(best),
    "optimal_lengths": best_lengths,
    "candidate_risks": len(candidates),
})
