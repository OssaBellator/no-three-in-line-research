#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def candidate_cost(deltas, collateral, setup):
    assert len(deltas) == len(collateral)
    periods = len(deltas)
    return Fraction(12*periods) + sum(6*d + c for d,c in zip(deltas, collateral)) + setup


def baseline(periods):
    return Fraction(15*periods)


def saving(deltas, collateral, setup):
    return baseline(len(deltas)) - candidate_cost(deltas, collateral, setup)

examples = [
    ((Fraction(0),Fraction(0)), (0,3), Fraction(0)),
    ((Fraction(1,4),Fraction(0),Fraction(1,4)), (1,3,0), Fraction(2)),
    ((Fraction(0),)*4, (4,0,4,0), Fraction(1)),
]
for deltas, collateral, setup in examples:
    exact = sum(Fraction(3)-6*d-c for d,c in zip(deltas,collateral)) - setup
    assert saving(deltas, collateral, setup) == exact

deltas = (Fraction(0), Fraction(0))
collateral = (0, 3)
assert saving(deltas, collateral, Fraction(0)) == 3
assert Fraction(sum(6*d+c for d,c in zip(deltas,collateral)), len(deltas)) == Fraction(3,2)

cycle_records = {}
for length in range(1,7):
    help_count = 0
    for cycle in product(range(6), repeat=length):
        mean = Fraction(sum(cycle), length)
        helps = mean < 3
        margin = Fraction(3*length-sum(cycle))
        assert helps == (margin > 0)
        help_count += int(helps)
    cycle_records[length] = help_count


def repetitions_needed(margin, setup):
    assert margin > 0
    return setup // margin + 1

assert repetitions_needed(Fraction(3), Fraction(7)) == 3
assert 3*Fraction(3) > 7 and 2*Fraction(3) <= 7

print({
    "irregular_schedule_saving": "sum_i(3-6*delta_i-c_i)-S",
    "repeatable_cycle_condition": "mean_i(6*delta_i+c_i)<3",
    "individually_losing_periods_allowed": True,
    "example_unit_cost_collateral_cycle": [0,3],
    "example_cycle_mean_burden": "3/2",
    "example_cycle_saving": 3,
    "minimum_repetitions_rule": "floor(S/cycle_margin)+1",
    "enumerated_helpful_integer_cycles_by_length": cycle_records,
    "remaining_gap": "no geometric (1,1,1) macro schedule has measured period burdens whose repeatable mean is below three",
    "evidence_level": "exact_irregular_shell_schedule",
    "status": "passed",
})
