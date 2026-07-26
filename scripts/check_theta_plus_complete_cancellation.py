#!/usr/bin/env python3
"""Check first-deletion cancellation across all three Theta-plus tables."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    order = list(data["block_order"])
    blocks = {name: set(values) for name, values in data["blocks"].items()}
    records = data["first_insertion_records"]
    first_credit = int(data["first_removal_credit"])

    stage_totals = {name: 0 for name in order}
    type_totals: dict[str, int] = defaultdict(int)
    assignments: dict[str, str] = {}

    for record in records:
        name = str(record["name"])
        table = str(record["table"])
        support = set(record["support"])
        weight = int(record["weight"])
        assert support, f"empty support for {name}"
        type_totals[table] += weight
        assigned = None
        for block in order:
            if support & blocks[block]:
                assigned = block
                break
        assert assigned is not None, f"record {name} misses the inserted set"
        assignments[name] = assigned
        stage_totals[assigned] += weight

    first_insertion = sum(type_totals.values())
    later_removal = sum(stage_totals.values())
    first_change = first_insertion - first_credit
    later_change = -later_removal
    composite_change = first_change + later_change

    assert later_removal == first_insertion
    assert composite_change == -first_credit

    print("inserted points", sum(len(values) for values in blocks.values()))
    print("block order", order)
    print("first insertion by table", dict(sorted(type_totals.items())))
    print("complete first insertion", first_insertion)
    print("first removal credit", first_credit)
    print("first-step change", first_change)
    print("later removal by block", stage_totals)
    print("complete later removal", later_removal)
    print("later zero-insertion change", later_change)
    print("composite change", composite_change)
    print("assigned records", len(assignments))
    print("outcome theta_plus_complete_insertion_cancellation")


if __name__ == "__main__":
    main()
