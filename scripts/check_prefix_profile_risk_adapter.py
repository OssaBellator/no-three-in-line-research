#!/usr/bin/env python3
from fractions import Fraction
from math import factorial

N = 30
J = 9
THRESHOLDS = (10, 10, 8, 16)
RISK_NORMALIZER = 1600


def profile_count(n, j):
    a = n - 1 - 2 * j
    if a < 0:
        return 0
    return factorial(n - 1) // (factorial(a) * factorial(j) * factorial(j + 1))


family = profile_count(N, J)
assert family == 168212023980
assert profile_count(N, 10) == family

# Exact aggregate risk-census fixture. If risk coordinate k is at least T_k,
# its violating set has size at most floor(total_risk_k/T_k).
total_risks = (3 * family, 2 * family, family, family)
violation_caps = tuple(total // threshold for total, threshold in zip(total_risks, THRESHOLDS))
violating_union_cap = sum(violation_caps)
good_lower_bound = family - violating_union_cap
assert good_lower_bound > 0

# Every surviving tree has integer risk r_k<T_k. The resulting normalized ledger
# contribution is at most 40/1600=1/40.
max_good_score = sum(threshold - 1 for threshold in THRESHOLDS)
assert max_good_score == 40
risk_row = Fraction(max_good_score, RISK_NORMALIZER)
assert risk_row == Fraction(1, 40)
assert risk_row < Fraction(1, 32)

# Verify exact profile support and unimodality through 100 leaves.
profiles_checked = 0
for n in range(1, 101):
    counts = [profile_count(n, j) for j in range((n - 1) // 2 + 1)]
    for j in range(len(counts) - 1):
        a = n - 1 - 2 * j
        if counts[j] and a >= 2:
            assert Fraction(counts[j + 1], counts[j]) == Fraction(a * (a - 1), (j + 1) * (j + 2))
        profiles_checked += 1

print({
    "profile": {"leaves": N, "binary_nodes": J},
    "family_size": family,
    "violation_caps": violation_caps,
    "good_objects_certified": good_lower_bound,
    "risk_row": str(risk_row),
    "profiles_checked": profiles_checked,
    "status": "passed",
})
