#!/usr/bin/env python3
from __future__ import annotations
import copy

CATEGORIES = ("return", "selector", "collision", "line", "interface", "geometric")
ALLOWED = ((0, 0), (0, 1), (1, 0), (1, 1))
WEIGHTS = {"r": 2, "s": 3, "c": 1, "l": 2, "i": 1, "g": 4}
TERMS = {
    edge: [
        {"category": category, "child": child, "coefficient": 1}
        for category, child in zip(CATEGORIES, WEIGHTS)
    ]
    for edge in ALLOWED
}
INNER = {"rank2": set(ALLOWED), "rank3": set(ALLOWED)}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def validate(manifest):
    require(set(manifest["terms"]) == set(ALLOWED), "complete allowed table")
    for edge, terms in manifest["terms"].items():
        require({term["category"] for term in terms} == set(CATEGORIES), f"{edge}: compulsory categories")
        for term in terms:
            require(
                term["child"] in manifest["weights"] and manifest["weights"][term["child"]] > 0,
                "positive child weight",
            )
    require(
        set(manifest["inner"]) == {"rank2", "rank3"}
        and all(set(manifest["inner"][key]) == set(ALLOWED) for key in manifest["inner"]),
        "inner coverage",
    )
    score = {
        edge: sum(term["coefficient"] * manifest["weights"][term["child"]] for term in terms)
        for edge, terms in manifest["terms"].items()
    }
    for (row, column), value in score.items():
        require(manifest["u"][row] + manifest["v"][column] >= value, "outer feasibility")
    objective = sum(manifest["u"].values()) + sum(manifest["v"].values())
    require(manifest["budget"] - objective > 0, "strict slack")
    return score, objective


base = {
    "terms": TERMS,
    "weights": WEIGHTS,
    "inner": INNER,
    "u": {0: 13, 1: 13},
    "v": {0: 0, 1: 0},
    "budget": 27,
}
score, objective = validate(base)
mutations = [
    lambda item: item["terms"].pop((0, 0)),
    lambda item: item["terms"][(0, 0)].pop(),
    lambda item: item["weights"].pop("g"),
    lambda item: item["weights"].update(g=0),
    lambda item: item["inner"]["rank2"].remove((0, 0)),
    lambda item: item["inner"].pop("rank3"),
    lambda item: item["u"].update({0: 0}),
    lambda item: item.update(budget=objective),
]
rejected = 0
for mutate in mutations:
    bad = copy.deepcopy(base)
    mutate(bad)
    try:
        validate(bad)
    except (AssertionError, KeyError):
        rejected += 1
require(rejected == len(mutations), "corruption accepted")
print(f"verified compulsory weighted assignment edges={len(ALLOWED)} corruptions={rejected}")
