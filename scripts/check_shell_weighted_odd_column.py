#!/usr/bin/env python3
from fractions import Fraction

BASELINE=Fraction(15)
FRONTIER=((2,14),(4,13),(6,12))

def weighted_cost(uses,total_controls,action_cost):
    return total_controls-uses+uses*action_cost

switch=Fraction(3,2)
for uses,total in FRONTIER:
    assert weighted_cost(uses,total,switch)==BASELINE
for cost in (Fraction(0),Fraction(1),Fraction(7,5)):
    values=[(weighted_cost(uses,total,cost),uses) for uses,total in FRONTIER]
    assert min(values)[1]==6 and min(values)[0]<BASELINE
for cost in (Fraction(8,5),Fraction(2),Fraction(3)):
    assert all(weighted_cost(uses,total,cost)>BASELINE for uses,total in FRONTIER)
assert weighted_cost(6,12,Fraction(1))==12
assert weighted_cost(4,13,Fraction(1))==13
assert weighted_cost(2,14,Fraction(1))==14

print({
    "recorded_baseline_active_cost":str(BASELINE),
    "symmetric_column_frontier":FRONTIER,
    "weighted_cost_formula":"total_controls - uses + action_cost*uses",
    "sharp_action_cost_threshold":str(switch),
    "optimal_below_threshold":"six uses of (1,1,1)",
    "all_frontier_points_tie_at_threshold":True,
    "baseline_optimal_above_threshold":True,
    "unit_cost_active_saving":3,
    "remaining_gap":"a geometric clean macro must realize (1,1,1) with active-equivalent cost strictly below 3/2 and controlled collateral interactions",
    "evidence_level":"exact_weighted_shell_cost_frontier",
    "status":"passed",
})
