#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)

ROWS = [
    {"name": "boundary", "period": 3, "denominator": 120, "loss": Fraction(7, 120), "perturbation": Fraction(1, 960)},
    {"name": "hall", "period": 8, "denominator": 160, "loss": Fraction(9, 160), "perturbation": Fraction(1, 960)},
    {"name": "threshold", "period": 12, "denominator": 24, "loss": Fraction(1, 24), "perturbation": Fraction(1, 1920)},
    {"name": "prefix", "period": 2, "denominator": 32, "loss": Fraction(1, 32), "perturbation": Fraction(1, 1920)},
    {"name": "shell", "period": 3, "denominator": 40, "loss": Fraction(1, 40), "perturbation": Fraction(1, 1920)},
    {"name": "interaction", "period": 2, "denominator": 48, "loss": Fraction(1, 48), "perturbation": Fraction(1, 1920)},
]

combined_period = 1
combined_denominator = 1
for row in ROWS:
    combined_period = lcm(combined_period, row["period"])
    combined_denominator = lcm(combined_denominator, row["denominator"])

base_loss = sum((row["loss"] for row in ROWS), Fraction(0))
perturbation = sum((row["perturbation"] for row in ROWS), Fraction(0))
margin = Fraction(1, 4)
base_slack = margin - base_loss
robust_slack = margin - base_loss - perturbation

assert combined_period == 24
assert combined_denominator == 480
assert base_loss == Fraction(7, 30)
assert base_slack == Fraction(1, 60)
assert perturbation == Fraction(1, 240)
assert robust_slack == Fraction(1, 80)

scaled = {row["name"]: row["loss"] * combined_denominator for row in ROWS}
assert all(value.denominator == 1 for value in scaled.values())
assert sum(int(value) for value in scaled.values()) == 112
assert margin * combined_denominator == 120
assert base_slack * combined_denominator == 8

residue_table = []
for residue in range(combined_period):
    residue_table.append((residue, tuple(residue % row["period"] for row in ROWS)))
assert len(set(states for _, states in residue_table)) == combined_period

print({
    "frontiers": len(ROWS),
    "combined_period": combined_period,
    "combined_denominator": combined_denominator,
    "scaled_base_loss": 112,
    "scaled_margin": 120,
    "base_slack": str(base_slack),
    "perturbation_budget": str(perturbation),
    "robust_slack": str(robust_slack),
    "residue_states": len(residue_table),
    "status": "passed",
})
