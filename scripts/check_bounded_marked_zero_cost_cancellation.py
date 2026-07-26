#!/usr/bin/env python3
"""Finite regression for separated bounded-marked zero-cost cancellation."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List, Set, Tuple


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def cycle_arcs(order: List[str]) -> List[Tuple[str, str]]:
    return [(order[i], order[(i + 1) % len(order)]) for i in range(len(order))]


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_bounded_marked_zero_cost_cancellation.py example.json")
    data = load(sys.argv[1])
    marked = list(data["marked"])
    helpers = list(data["helpers"])
    if len(helpers) < len(marked):
        raise AssertionError("not enough helpers to separate marked indices")

    order: List[str] = []
    for d, h in zip(marked, helpers[: len(marked)]):
        order.extend((d, h))
    order.extend(helpers[len(marked) :])
    arcs = cycle_arcs(order)
    marked_set: Set[str] = set(marked)
    helper_set: Set[str] = set(helpers)

    dd_arcs = [(a, b) for a, b in arcs if a in marked_set and b in marked_set]
    if dd_arcs:
        raise AssertionError(dd_arcs)
    if any(a == b for a, b in arcs):
        raise AssertionError("fixed point in single cycle")
    if any(a not in helper_set and b not in helper_set for a, b in arcs):
        raise AssertionError("selected arc without helper support")

    local_cost = sum(int(weight) for weight in data["local_atom_weights"])
    first_credit = int(data["first_removal_credit"])
    nonlocal_cost = int(data["first_nonlocal_cost"])
    second_cost = int(data["second_insertion_cost"])
    first_change = local_cost + nonlocal_cost - first_credit
    second_change = second_cost - local_cost
    composite = first_change + second_change
    reduced = nonlocal_cost + second_cost - first_credit
    if composite != reduced:
        raise AssertionError((composite, reduced))
    if composite >= 0:
        raise AssertionError(f"stored composite is not improving: {composite}")

    print("marked indices", len(marked))
    print("helper indices", len(helpers))
    print("separated cycle order", order)
    print("marked-marked arcs", len(dd_arcs))
    print("local atom count", len(data["local_atom_weights"]))
    print("complete local table weight", local_cost)
    print("first-step change", first_change)
    print("second-step insertion cost", second_cost)
    print("second-step change", second_change)
    print("composite change", composite)
    print("outcome bounded_marked_zero_cost_cancellation")


if __name__ == "__main__":
    main()
