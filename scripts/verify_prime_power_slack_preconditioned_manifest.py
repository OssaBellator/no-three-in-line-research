#!/usr/bin/env python3
from __future__ import annotations
import copy


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def validate(manifest):
    denominator, rank_three = manifest["Z"], manifest["A3"]
    require(isinstance(denominator, int) and denominator > 0 and 0 <= rank_three <= denominator, "host denominator/slack")
    slack = denominator - rank_three
    allocation = manifest["allocation"]
    require(set(allocation) == set(manifest["components"]), "allocation coverage")
    require(all(isinstance(value, int) and value >= 0 for value in allocation.values()), "nonnegative allocation")
    require(sum(allocation.values()) <= max(slack - 1, 0), "allocated residual budget")
    require(all(manifest["components"][key] <= allocation[key] for key in allocation), "component fit")
    require(set(manifest["inner"]) == set(manifest["required_inner"]), "inner coverage")
    require(manifest["outer_bound"] == sum(manifest["components"].values()), "outer complete score")
    require(rank_three + manifest["outer_bound"] <= denominator - 1, "strict integer row")
    return slack


base = {
    "Z": 20,
    "A3": 11,
    "components": {"rank1": 2, "rank2": 3, "return_selector": 2},
    "allocation": {"rank1": 2, "rank2": 3, "return_selector": 2},
    "required_inner": {"rank2", "rank3"},
    "inner": {"rank2", "rank3"},
    "outer_bound": 7,
}
require(validate(base) == 9, "slack")
mutations = [
    lambda item: item.update(A3=21),
    lambda item: item["allocation"].update(rank1=-1),
    lambda item: item["allocation"].pop("rank2"),
    lambda item: item["allocation"].update(rank1=4, rank2=4, return_selector=2),
    lambda item: item["components"].update(rank2=4),
    lambda item: item["inner"].remove("rank3"),
    lambda item: item.update(outer_bound=6),
    lambda item: item.update(Z=18),
]
rejected = 0
for mutate in mutations:
    bad = copy.deepcopy(base)
    mutate(bad)
    try:
        validate(bad)
    except (AssertionError, KeyError):
        rejected += 1
require(rejected == len(mutations), "precondition corruption accepted")
print(f"verified slack-preconditioned manifest slack={validate(base)} corruptions={rejected}")
