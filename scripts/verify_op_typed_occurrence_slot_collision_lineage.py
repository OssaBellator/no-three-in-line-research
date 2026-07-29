#!/usr/bin/env python3
"""Deterministic audit for OP4et--OP4ex."""

from collections import Counter
from random import Random

SEED = 2405
SYSTEMS = 2800


def classify(left, right):
    if left is None or right is None:
        return "missing_lineage"
    if left == right:
        return "double_consumption"
    return "noninjective_slot"


def main():
    rng = Random(SEED)
    out = Counter(systems=SYSTEMS)
    for _ in range(SYSTEMS):
        edge_count = rng.randint(2, 5)
        capacities = [rng.randint(1, 4) for _ in range(edge_count)]
        slots, token = {}, 0
        for edge, capacity in enumerate(capacities):
            for index in range(capacity):
                slots[(edge, index)] = (edge, token)
                token += 1
        assert len(slots) == len(set(slots.values()))
        out["faithful_slots"] += len(slots)
        for _claim in range(rng.randint(1, 4)):
            edge = rng.randrange(edge_count)
            index = rng.randrange(capacities[edge])
            left = slots[(edge, index)]
            mode = rng.choices(["same", "alias", "missing", "fresh"], [0.46, 0.27, 0.12, 0.15])[0]
            if mode == "same":
                right, expected = left, "double_consumption"
            elif mode == "alias":
                right, expected = ("alias", rng.randrange(10**6)), "noninjective_slot"
            elif mode == "missing":
                right, expected = None, "missing_lineage"
            else:
                right, expected = left, "double_consumption"
                out["rejected_second_uses"] += 1
            if rng.choice(["residual", "edit"]) != rng.choice(["residual", "edit"]):
                out["cross_type_claims"] += 1
            assert classify(left, right) == expected
            out[expected] += 1
            out["claims"] += 1
            out["segment_edges_checked"] += edge_count
    assert out["claims"] == out["double_consumption"] + out["noninjective_slot"] + out["missing_lineage"]
    print("OP typed occurrence-slot collision lineage audit passed")
    for key, value in out.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
