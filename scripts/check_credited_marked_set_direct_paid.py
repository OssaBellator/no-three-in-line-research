#!/usr/bin/env python3
"""Check direct paid conversion of a credited marked set across two layers."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} EXAMPLE.json")

    data = json.loads(Path(sys.argv[1]).read_text())
    sizes = [int(x) for x in data["layer_marked_sizes"]]
    within = [int(x) for x in data["within_layer_credit"]]
    cross = int(data["cross_layer_credit"])
    insertions = [int(x) for x in data["second_insertion_costs"]]
    R = int(data["R"])
    all_selected_are_controllers = bool(data["all_selected_are_controllers"])

    if len(sizes) != 2 or len(within) != 2 or len(insertions) != 2:
        raise AssertionError("stored model must have two source layers")
    if any(value < 0 for value in sizes + within + insertions) or cross < 0:
        raise AssertionError("all stored masses must be nonnegative")
    if any(value != 0 for value in insertions):
        raise AssertionError("direct complete-support cycles must have zero insertion cost")

    marked = sum(sizes)
    designated_credit = sum(within) + cross

    # Assign every cross-layer incidence to the first layer trade.  The second layer
    # removes only its remaining within-layer credit.
    removals = [within[0] + cross, within[1]]
    if sum(removals) != designated_credit:
        raise AssertionError("designated credit was not removed exactly once")

    composite_change = sum(insertions) - sum(removals)
    if composite_change != -designated_credit:
        raise AssertionError("direct paid identity failed")

    square_demand = sum(size * size for size in sizes)
    global_square = marked * marked
    if square_demand > global_square:
        raise AssertionError("layerwise helper demand exceeds the global square budget")

    selected_controllers = 2 * marked if all_selected_are_controllers else 0
    if selected_controllers >= R:
        raise AssertionError("selected-controller puncturing is not sub-domain-scale")

    print("layer marked sizes", sizes)
    print("total marked size", marked)
    print("within-layer designated credit", within)
    print("cross-layer designated credit", cross)
    print("total designated credit", designated_credit)
    print("layerwise removals", removals)
    print("layerwise insertion costs", insertions)
    print("composite change", composite_change)
    print("layerwise square demand", square_demand)
    print("global square budget", global_square)
    print("selected controller punctures", selected_controllers)
    print("puncture to R ratio", selected_controllers / R)
    print("outcome credited_marked_set_direct_paid_trade")


if __name__ == "__main__":
    main()
