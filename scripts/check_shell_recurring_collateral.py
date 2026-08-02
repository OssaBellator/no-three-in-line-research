#!/usr/bin/env python3
from fractions import Fraction

def total_cost(periods, per_use_overhead, recurring_collateral, fixed_setup):
    return periods * (12 + 6 * per_use_overhead + recurring_collateral) + fixed_setup

def improves(periods, per_use_overhead, recurring_collateral, fixed_setup):
    return total_cost(periods, per_use_overhead, recurring_collateral, fixed_setup) < 15 * periods

def minimum_periods(per_use_overhead, recurring_collateral, fixed_setup):
    margin = Fraction(3) - 6 * per_use_overhead - recurring_collateral
    if margin <= 0:
        return None
    return int(Fraction(fixed_setup,1) // margin) + 1

assert minimum_periods(Fraction(0), Fraction(0), 10) == 4
assert minimum_periods(Fraction(0), Fraction(2), 10) == 11
assert minimum_periods(Fraction(0), Fraction(3), 0) is None
assert minimum_periods(Fraction(1,3), Fraction(0), 5) == 6
assert minimum_periods(Fraction(1,4), Fraction(1), 7) == 15

for periods in range(1,30):
    assert improves(periods, Fraction(0), Fraction(2), periods-1)
    assert not improves(periods, Fraction(0), Fraction(2), periods)
    assert not improves(periods, Fraction(0), Fraction(3), 0)

for delta, collateral in ((Fraction(0),Fraction(0)),(Fraction(0),Fraction(2)),(Fraction(1,4),Fraction(1)),(Fraction(2,5),Fraction(0))):
    assert 6*delta + collateral < 3
for delta, collateral in ((Fraction(0),Fraction(3)),(Fraction(1,2),Fraction(0)),(Fraction(1,3),Fraction(1))):
    assert 6*delta + collateral >= 3

print({
    "batched_cost_formula": "k(12+6*delta+c)+S",
    "strict_improvement_condition": "6*delta+c+S/k<3",
    "asymptotic_recurring_condition": "6*delta+c<3",
    "minimum_batch_length": "floor(S/(3-6*delta-c))+1",
    "unit_cost_maximum_integer_recurring_collateral_per_period": 2,
    "unit_cost_with_recurring_collateral_two_setup_budget": "S<=k-1",
    "recurring_collateral_three": "ties or loses for every batch length",
    "remaining_gap": "the geometric macro must bound recurring repair and collision costs, not merely one-time setup",
    "evidence_level": "exact_recurring_shell_collateral_barrier",
    "status": "passed",
})
