#!/usr/bin/env python3
from fractions import Fraction

BASELINE_PER_PERIOD = Fraction(15)
MACRO_BASE_PER_PERIOD = Fraction(12)
USES_PER_PERIOD = 6

def total_cost(periods: int, per_use_overhead: Fraction, fixed_collateral: int) -> Fraction:
    return periods * (MACRO_BASE_PER_PERIOD + USES_PER_PERIOD * per_use_overhead) + fixed_collateral

def improves(periods: int, per_use_overhead: Fraction, fixed_collateral: int) -> bool:
    return total_cost(periods, per_use_overhead, fixed_collateral) < periods * BASELINE_PER_PERIOD

def minimum_periods(per_use_overhead: Fraction, fixed_collateral: int):
    if per_use_overhead >= Fraction(1,2):
        return None
    periods=1
    while not improves(periods, per_use_overhead, fixed_collateral):
        periods += 1
    return periods

for collateral in range(13):
    assert minimum_periods(Fraction(0), collateral) == collateral//3 + 1
assert minimum_periods(Fraction(1,6), 1) == 1
assert minimum_periods(Fraction(1,6), 2) == 2
assert minimum_periods(Fraction(1,6), 5) == 3
assert minimum_periods(Fraction(1,2), 0) is None
assert minimum_periods(Fraction(3,5), 0) is None

for delta in (Fraction(0),Fraction(1,10),Fraction(1,6),Fraction(2,5)):
    for collateral in range(8):
        periods=minimum_periods(delta,collateral)
        assert periods is not None
        assert periods*(3-6*delta) > collateral
        if periods>1:
            assert (periods-1)*(3-6*delta) <= collateral

print({
    "batched_cost_formula":"t*(12+6*delta)+C",
    "strict_improvement_condition":"t*(3-6*delta)>C",
    "amortization_possible_exactly_when":"delta<1/2",
    "minimum_periods_at_zero_overhead":"floor(C/3)+1",
    "examples":{"delta=1/6,C=1":1,"delta=1/6,C=2":2,"delta=1/6,C=5":3},
    "remaining_gap":"a geometric (1,1,1) macro must identify its actual per-use overhead and fixed collateral before this amortization law can be applied",
    "evidence_level":"exact_shell_batch_amortization_frontier",
    "status":"passed",
})
