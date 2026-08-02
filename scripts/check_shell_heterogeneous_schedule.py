#!/usr/bin/env python3
from fractions import Fraction
from math import floor

THREE = Fraction(3)

def burden(delta, collateral):
    return 6 * Fraction(delta) + Fraction(collateral)

def prefix_savings(burdens):
    total = Fraction(0)
    result = []
    for value in burdens:
        total += THREE - Fraction(value)
        result.append(total)
    return tuple(result)

def first_improving_prefix(burdens, setup):
    setup = Fraction(setup)
    for index, saving in enumerate(prefix_savings(burdens), 1):
        if saving > setup:
            return index
    return None

def periodic_minimum_prefix(period, setup):
    period = tuple(Fraction(value) for value in period)
    setup = Fraction(setup)
    savings = prefix_savings(period)
    gain = savings[-1]
    if gain <= 0:
        candidates = [index for index, value in enumerate(savings, 1) if value > setup]
        return min(candidates, default=None)
    best = None
    size = len(period)
    for residue, partial in enumerate(savings, 1):
        cycles = max(0, floor((setup - partial) / gain) + 1)
        candidate = cycles * size + residue
        if cycles * gain + partial > setup:
            best = candidate if best is None else min(best, candidate)
    return best

assert burden(0, 2) == 2
assert periodic_minimum_prefix((burden(0, 2),), 7) == 8
assert periodic_minimum_prefix((burden(Fraction(1, 2), 0),), 0) is None
assert prefix_savings((2, 3)) == (1, 1)
assert periodic_minimum_prefix((2, 3), 10) == 21
assert periodic_minimum_prefix((2, 4), Fraction(1, 2)) == 1
assert periodic_minimum_prefix((2, 4), 1) is None
assert periodic_minimum_prefix((1, 6), 1) == 1
assert periodic_minimum_prefix((1, 6), 2) is None
assert first_improving_prefix((3, 4, 1), 0) == 3
assert first_improving_prefix((3, 3, 3), 0) is None

print({
    "period_i_burden": "b_i=6*delta_i+c_i",
    "prefix_saving": "B_k=sum_{i<=k}(3-b_i)",
    "setup_S_improves": "exists k with B_k>S",
    "all_fixed_setups_amortizable": "sup_k B_k=infinity",
    "periodic_period_gain": "G=sum_{i=1}^m(3-b_i)",
    "periodic_classification": {"G>0":"every fixed setup", "G=0":"only S below the largest within-period prefix", "G<0":"only S below the largest first-period prefix"},
    "positive_period_example_minimum_prefix": 21,
    "remaining_gap": "no geometric (1,1,1) macro supplies a certified burden sequence whose cumulative saving is unbounded",
    "evidence_level": "exact_heterogeneous_shell_schedule_envelope",
    "status": "passed",
})
