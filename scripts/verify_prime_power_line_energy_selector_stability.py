#!/usr/bin/env python3
from __future__ import annotations
from math import floor


def minimizers(scores):
    minimum = min(scores.values())
    return {response for response, value in scores.items() if value == minimum}


base = {"a": 4, "b": 7, "c": 9}
assert minimizers(base) == {"a"}
gap = min(value - base["a"] for response, value in base.items() if response != "a")
perturbation = {"a": 2, "b": 4, "c": 6}
new_scores = {response: base[response] + perturbation[response] for response in base}
assert minimizers(new_scores) == {"a"}
assert all(
    perturbation[response] - perturbation["a"] < base[response] - base["a"]
    for response in base
    if response != "a"
)
switch_perturbation = {"a": 4, "b": 0, "c": 5}
switched = {response: base[response] + switch_perturbation[response] for response in base}
assert "b" in minimizers(switched)
assert switch_perturbation["b"] - switch_perturbation["a"] <= -(base["b"] - base["a"])
tie = {"a": 5, "b": 5, "c": 8}
assert minimizers(tie) == {"a", "b"}
tie_perturbation = {"a": 2, "b": 2, "c": 0}
assert minimizers({response: tie[response] + tie_perturbation[response] for response in tie}) == {"a", "b"}
variation_budget, switch_cost = 17, 4
assert floor(variation_budget / switch_cost) == 4
print(f"verified selector stability unique_gap={gap} episode_bound={floor(variation_budget / switch_cost)}")
