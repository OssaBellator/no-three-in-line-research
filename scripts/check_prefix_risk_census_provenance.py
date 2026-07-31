#!/usr/bin/env python3
import json
from fractions import Fraction
from math import factorial
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "certificates" / "prime-patching-provenance-audit-555-560.json"
record = json.loads(DATA.read_text())["frontiers"]["prefix"]
profile = record["profile"]

assert record["evidence_level"] == "fixture_derived"
assert record["independent_geometric_source"] is None
assert record["risk_enumerator"] is None

n = profile["leaves"]
j = profile["binary_nodes"]
a = n - 1 - 2 * j
family = factorial(n - 1) // (factorial(a) * factorial(j) * factorial(j + 1))
assert family == profile["family_size"] == 168212023980

thresholds = tuple(record["thresholds"])
multipliers = tuple(record["aggregate_risk_multipliers"])
totals = tuple(multiplier * family for multiplier in multipliers)
violation_caps = tuple(total // threshold for total, threshold in zip(totals, thresholds))
good_lower_bound = family - sum(violation_caps)
assert good_lower_bound == 52566257495
assert good_lower_bound > 0

risk_row = Fraction(sum(threshold - 1 for threshold in thresholds), 1600)
assert risk_row == Fraction(1, 40)

# Aggregate totals certify existence, but do not identify a deterministic witness.
# Two toy censuses have the same total risk and different good-object sets.
toy_uniform = (1, 1, 1, 1)
toy_concentrated = (4, 0, 0, 0)
assert sum(toy_uniform) == sum(toy_concentrated) == 4
good_uniform = tuple(i for i, value in enumerate(toy_uniform) if value < 2)
good_concentrated = tuple(i for i, value in enumerate(toy_concentrated) if value < 2)
assert good_uniform != good_concentrated
assert len(good_uniform) == 4 and len(good_concentrated) == 3

assert len(record["required_for_promotion"]) == 5
print({
    "profile_family": family,
    "aggregate_risk_totals": totals,
    "certified_good_lower_bound": good_lower_bound,
    "risk_row": str(risk_row),
    "aggregate_totals_identify_witness": False,
    "risk_enumerator_present": False,
    "status": "passed",
})
