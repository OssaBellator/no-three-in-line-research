#!/usr/bin/env python3
"""Finite regression for controller-disjoint bounded marked layer embedding."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Set


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_bounded_marked_layer_embedding.py example.json")

    data = load(sys.argv[1])
    m = int(data["layer_size"])
    controllers: Set[int] = set(data["active_controllers"])
    marked: List[int] = list(data["marked_indices"])
    forbidden: Set[int] = set(data["forbidden_helpers"])
    helpers: List[int] = list(data["chosen_helpers"])
    cycle: List[int] = list(data["cycle"])

    punctured = controllers.intersection(marked)
    active_after = controllers - punctured
    reservoir = set(range(m)) - active_after - set(marked) - forbidden

    if len(marked) > 4:
        raise AssertionError("marked set exceeds the bounded theorem")
    if not set(helpers).issubset(reservoir):
        raise AssertionError("chosen helpers are not in the controller-disjoint reservoir")
    if len(helpers) < len(marked):
        raise AssertionError("not enough helpers to separate the marked indices")
    if set(cycle) != set(marked) | set(helpers):
        raise AssertionError("cycle support is not exactly marked plus chosen helpers")
    if len(cycle) != len(set(cycle)):
        raise AssertionError("cycle repeats an endpoint index")

    marked_set = set(marked)
    marked_marked_arcs = 0
    successor: Dict[int, int] = {}
    for i, tail in enumerate(cycle):
        head = cycle[(i + 1) % len(cycle)]
        successor[tail] = head
        if tail in marked_set and head in marked_set:
            marked_marked_arcs += 1
    if marked_marked_arcs:
        raise AssertionError("cycle is not marked-separated")
    if active_after.intersection(cycle):
        raise AssertionError("an active controller is moved by the cycle")

    # The selected permutation uses each chosen head once and fixes every index
    # outside the cycle, hence it remains a permutation of the layer.
    image = set(successor.values()) | (set(range(m)) - set(cycle))
    if image != set(range(m)):
        raise AssertionError("endpoint state does not preserve the permutation layer")

    print("layer size", m)
    print("initial active controllers", len(controllers))
    print("bounded controller punctures", len(punctured))
    print("active controllers after puncture", len(active_after))
    print("controller-disjoint reservoir", len(reservoir))
    print("marked indices", marked)
    print("chosen helpers", helpers)
    print("marked-marked arcs", marked_marked_arcs)
    print("permutation image size", len(image))
    print("outcome bounded_marked_controller_disjoint_layer_embedding")


if __name__ == "__main__":
    main()
