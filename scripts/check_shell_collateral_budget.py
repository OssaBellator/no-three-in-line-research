#!/usr/bin/env python3
from fractions import Fraction

BASELINE=Fraction(15)
D_USES=6
RECORDED_CONTROLS=6

def total_cost(per_use_overhead,fixed_collateral):
    return RECORDED_CONTROLS + D_USES*(1+per_use_overhead) + fixed_collateral

assert total_cost(Fraction(0),0)==12
assert total_cost(Fraction(0),2)==14 < BASELINE
assert total_cost(Fraction(0),3)==BASELINE
assert total_cost(Fraction(1,3),0)==14 < BASELINE
assert total_cost(Fraction(1,2),0)==BASELINE
assert total_cost(Fraction(2,3),0)>BASELINE

# Exact strict-improvement region: 6*delta + C < 3.
for delta in (Fraction(0),Fraction(1,6),Fraction(1,3),Fraction(1,2),Fraction(2,3)):
    for collateral in range(5):
        assert (total_cost(delta,collateral)<BASELINE) == (6*delta+collateral<3)

print({
    "recorded_baseline_active_cost":str(BASELINE),
    "symmetric_macro_uses_per_period":D_USES,
    "recorded_controls_with_six_macro_uses":RECORDED_CONTROLS,
    "cost_formula":"12 + 6*per_use_overhead + fixed_collateral",
    "strict_improvement_region":"6*per_use_overhead + fixed_collateral < 3",
    "unit_macro_integer_collateral_budget":2,
    "three_unit_collateral_controls":"ties the baseline",
    "per_use_overhead_threshold_with_no_fixed_collateral":"1/2",
    "repair_spacing_consequence":"at most two unit repair controls across six macro uses; one repair per two uses only ties",
    "remaining_gap":"no geometric (1,1,1) macro is known with exposed-state legality and total overhead inside this budget",
    "evidence_level":"exact_shell_collateral_budget",
    "status":"passed",
})
