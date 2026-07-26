#!/usr/bin/env python3
"""Finite regression for a zero-cost punctured marked-star host."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import FrozenSet, List, Set


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_zero_cost_punctured_star.py example.json")

    data = load(sys.argv[1])
    centre = str(data["centre"])
    chosen: Set[str] = set(data["chosen_helpers"])
    cycle: List[str] = list(data["cycle"])
    supports: List[FrozenSet[str]] = [
        frozenset(support) for support in data["positive_supports"]
    ]
    star_entries = data["star_entries"]

    if set(cycle) != chosen | {centre}:
        raise AssertionError("cycle does not use exactly the centre and chosen helpers")
    if len(cycle) != len(set(cycle)):
        raise AssertionError("cycle repeats an endpoint index")
    if len(chosen) != int(data["required_helpers"]):
        raise AssertionError("chosen helper count does not match the required size")

    selected_supports = [support for support in supports if support.issubset(chosen)]
    if selected_supports:
        raise AssertionError(f"chosen helper block selects supports: {selected_supports}")

    for entry in star_entries:
        if entry["controller"] == centre:
            raise AssertionError("designated star entry is deleted by puncturing the centre")

    star_credit = len(star_entries)
    insertion_cost = 0
    potential_change = insertion_cost - star_credit
    if potential_change >= 0:
        raise AssertionError("zero-cost punctured-star trade is not strictly paid")

    print("punctured centre", centre)
    print("required ordinary helpers", data["required_helpers"])
    print("chosen independent helpers", sorted(chosen))
    print("positive helper supports", len(supports))
    print("selected positive supports", len(selected_supports))
    print("designated star credit", star_credit)
    print("insertion cost", insertion_cost)
    print("punctured-universe potential change", potential_change)
    print("outcome zero_cost_punctured_star_nested_progress")


if __name__ == "__main__":
    main()
