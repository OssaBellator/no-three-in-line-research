#!/usr/bin/env python3
from __future__ import annotations
import copy
import hashlib
import json
from itertools import permutations


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def allowed_responses(record):
    side = record["side"]
    allowed = {tuple(edge) for edge in record["host_edges"]}
    return [
        tuple((row, permutation[row]) for row in range(side))
        for permutation in permutations(range(side))
        if all((row, permutation[row]) in allowed for row in range(side))
    ]


def identifier(record):
    payload = {
        key: record[key]
        for key in ("side", "host_edges", "deletions", "target", "background", "labels")
    }
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def validate(record):
    side = record["side"]
    require(side >= 2, "side")
    edges = [tuple(edge) for edge in record["host_edges"]]
    require(all(0 <= row < side and 0 <= column < side for row, column in edges), "edge coordinates")
    require(tuple(record["target"]) in edges, "target in host")
    require(len({tuple(point) for point in record["background"]}) == len(record["background"]), "background unique")
    responses = allowed_responses(record)
    require(responses, "nonempty response family")
    require(record["response_count"] == len(responses), "response linkage")
    require(
        all(name in record["labels"] for name in ("owner", "fate", "collision", "line", "interface", "crt")),
        "provenance",
    )
    return responses


base = {
    "side": 3,
    "host_edges": [[0, 0], [0, 1], [1, 1], [1, 2], [2, 0], [2, 2]],
    "deletions": [],
    "target": [0, 0],
    "background": [[0, 2], [2, 1]],
    "labels": {
        "owner": "A",
        "fate": "self",
        "collision": "clean",
        "line": "L",
        "interface": "I",
        "crt": "C",
    },
    "response_count": 2,
}
responses = validate(base)
assert len(responses) == 2
other = copy.deepcopy(base)
other["background"] = [[0, 2], [1, 0]]
other["response_count"] = 2
assert identifier(base) != identifier(other)
mutations = [
    lambda item: item.update(side=2),
    lambda item: item.update(target=[2, 1]),
    lambda item: item["background"].append([0, 2]),
    lambda item: item.update(response_count=1),
    lambda item: item["labels"].pop("fate"),
]
rejected = 0
for mutate in mutations:
    bad = copy.deepcopy(base)
    mutate(bad)
    try:
        validate(bad)
    except (AssertionError, KeyError):
        rejected += 1
assert rejected == len(mutations)
print(f"verified raw-fibre lineage responses={len(responses)} corruptions={rejected}")
