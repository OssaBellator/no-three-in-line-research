#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def minimum_unconstrained_burden(periods, burdens):
    return periods * min(burdens)


def minimum_quota_burden(periods, burdens, lower_quotas):
    mandatory = sum(lower_quotas)
    if mandatory > periods:
        return None
    return sum(Fraction(count) * burden for count, burden in zip(lower_quotas, burdens)) \
        + (periods - mandatory) * min(burdens)


def brute_minimum(periods, burdens, lower_quotas):
    best = None

    def enumerate_counts(index, remaining, counts):
        nonlocal best
        if index == len(burdens) - 1:
            candidate = counts + [remaining]
            if any(count < quota for count, quota in zip(candidate, lower_quotas)):
                return
            value = sum(Fraction(count) * burden for count, burden in zip(candidate, burdens))
            best = value if best is None else min(best, value)
            return
        for count in range(remaining + 1):
            enumerate_counts(index + 1, remaining - count, counts + [count])

    enumerate_counts(0, periods, [])
    return best


def minimum_robust_periods(maximum_burden, setup):
    margin = Fraction(3) - maximum_burden
    if margin <= 0:
        return None
    return int(Fraction(setup, 1) // margin) + 1


burdens = (Fraction(1), Fraction(5, 2), Fraction(4))
for periods in range(1, 9):
    assert minimum_unconstrained_burden(periods, burdens) == periods
    for lower_quotas in product(range(3), repeat=len(burdens)):
        if sum(lower_quotas) <= periods:
            assert minimum_quota_burden(periods, burdens, lower_quotas) == brute_minimum(periods, burdens, lower_quotas)
        else:
            assert minimum_quota_burden(periods, burdens, lower_quotas) is None

assert minimum_quota_burden(8, burdens, (1, 2, 1)) == Fraction(14)
assert Fraction(3 * 8) - minimum_quota_burden(8, burdens, (1, 2, 1)) == 10
assert minimum_robust_periods(Fraction(5, 2), 10) == 21
assert minimum_robust_periods(Fraction(3), 0) is None
assert minimum_robust_periods(Fraction(4), 0) is None

for maximum in (Fraction(0), Fraction(1), Fraction(5, 2)):
    threshold = minimum_robust_periods(maximum, 17)
    assert threshold * (3 - maximum) > 17
    assert (threshold - 1) * (3 - maximum) <= 17

print({
    "macro_type_burden": "b_j=6*delta_j+c_j",
    "unconstrained_minimum_burden_for_K_periods": "K*min_j(b_j)",
    "unconstrained_strict_improvement": "K*(3-min_j(b_j))>S",
    "lower_quota_minimum_burden": "sum_j ell_j*b_j+(K-sum_j ell_j)*min_j(b_j)",
    "lower_quota_strict_improvement": "3K-sum_j ell_j*b_j-(K-sum_j ell_j)*min_j(b_j)>S",
    "robust_all_schedule_condition_at_length_K": "K*(3-max_j(b_j))>S",
    "some_uniformly_improving_length_exists": "max_j(b_j)<3",
    "minimum_robust_length": "floor(S/(3-max_j(b_j)))+1",
    "mixing_without_constraints_improves_best_type": False,
    "remaining_gap": "the geometric macro repertoire must supply exact burdens and compatibility or frequency constraints",
    "evidence_level": "exact_shell_repertoire_envelope",
    "status": "passed",
})
