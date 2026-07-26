#!/usr/bin/env python3
"""Finite checks for final-universe puncture-credit telescoping."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def greedy_matching(records: List[dict], keys: Tuple[str, ...]) -> int:
    used: Dict[str, Set[str]] = {key: set() for key in keys}
    size = 0
    for record in records:
        if any(record[key] in used[key] for key in keys):
            continue
        for key in keys:
            used[key].add(record[key])
        size += 1
    return size


def max_degree(records: List[dict], key: str) -> int:
    counts: Dict[str, int] = {}
    for record in records:
        counts[record[key]] = counts.get(record[key], 0) + 1
    return max(counts.values(), default=0)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_final_universe_credit_telescoping.py example.json")
    data = load(sys.argv[1])

    paid = data["paid_case"]
    paid_surviving = int(paid["credit"]) - int(paid["lost_credit"])
    paid_gap = paid_surviving - int(paid["final_insertion"])
    if paid_gap <= 0:
        raise AssertionError("stored paid case does not strictly improve")

    boundary = data["boundary_case"]
    credit = int(boundary["history_centres"]) * int(boundary["width"])
    insertion = int(boundary["final_insertion"])
    lost = int(boundary["lost_credit"])
    surviving = credit - lost
    if insertion != surviving:
        raise AssertionError((insertion, surviving))

    repeated_records = boundary["repeated_records"]
    diffuse_records = boundary["diffuse_records"]
    repeated_degree = max_degree(repeated_records, "candidate")
    diffuse_candidate_degree = max_degree(diffuse_records, "candidate")
    diffuse_controller_degree = max_degree(diffuse_records, "later_controller")
    full_matching = greedy_matching(
        diffuse_records,
        ("earlier_centre", "partner", "later_controller", "label", "candidate"),
    )

    print("paid credit", paid["credit"])
    print("paid lost credit", paid["lost_credit"])
    print("paid surviving credit", paid_surviving)
    print("paid final insertion", paid["final_insertion"])
    print("paid strict gap", paid_gap)
    print("boundary total credit", credit)
    print("boundary lost credit", lost)
    print("boundary surviving credit", surviving)
    print("boundary final insertion", insertion)
    print("repeated lost candidate degree", repeated_degree)
    print("diffuse maximum candidate degree", diffuse_candidate_degree)
    print("diffuse maximum future-controller degree", diffuse_controller_degree)
    print("full forward dependency matching", full_matching)
    print("outcome final_universe_payment_or_future_controller_dependency")


if __name__ == "__main__":
    main()
