#!/usr/bin/env python3
"""Check the free-partner bank versus controller-partner core dichotomy."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def analyse_case(case: dict[str, Any]) -> dict[str, Any]:
    partners = case["partners"]
    points = [tuple(map(int, partner["point"])) for partner in partners]
    entries = [str(partner["entry"]) for partner in partners]
    if len(set(points)) != len(points):
        raise ValueError("partners must be distinct")
    if len(set(entries)) != len(entries):
        raise ValueError("designated entries must be distinct")
    if any(int(partner["layer"]) not in (0, 1) for partner in partners):
        raise ValueError("layers must be 0 or 1")

    degree = len(partners)
    controller_count = sum(bool(partner["controller"]) for partner in partners)
    free_by_layer = Counter(
        int(partner["layer"])
        for partner in partners
        if not bool(partner["controller"])
    )
    best_layer, bank_size = max(
        ((layer, free_by_layer[layer]) for layer in (0, 1)),
        key=lambda item: item[1],
    )

    if bank_size * 4 >= degree:
        outcome = "controller_preserving_free_partner_bank"
    elif controller_count * 2 >= degree:
        outcome = "controller_controller_star_core"
    else:
        raise AssertionError("partner dichotomy failed")

    return {
        "name": str(case.get("name", "case")),
        "star_degree": degree,
        "controller_partner_count": controller_count,
        "free_partner_count": degree - controller_count,
        "best_free_layer": best_layer,
        "free_partner_bank_size": bank_size,
        "credit_lower_bound": bank_size,
        "outcome": outcome,
    }


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    return {"cases": [analyse_case(case) for case in data["cases"]]}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(analyse(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
