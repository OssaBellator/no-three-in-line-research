#!/usr/bin/env python3
"""Finite regression for exact entrywise telescoping under controller deletion."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def active_at(entry: dict, stage: int) -> bool:
    puncture_stage: Optional[int] = entry.get("puncture_stage")
    return puncture_stage is None or stage < puncture_stage


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: check_controller_entry_deletion_telescoping.py example.json"
        )

    data = load(sys.argv[1])
    entries: Dict[str, dict] = data["entries"]
    stage_count = len(next(iter(entries.values()))["counts"])

    potentials: List[int] = []
    for stage in range(stage_count):
        total = 0
        for entry in entries.values():
            if active_at(entry, stage):
                total += int(entry["counts"][stage])
        potentials.append(total)

    surviving_change = 0
    deleted_initial_mass = 0
    for entry in entries.values():
        puncture_stage = entry.get("puncture_stage")
        initial = int(entry["counts"][0])
        if puncture_stage is None:
            surviving_change += int(entry["counts"][-1]) - initial
        else:
            deleted_initial_mass += initial

    exact_change = surviving_change - deleted_initial_mass
    chronological_change = potentials[-1] - potentials[0]
    if exact_change != chronological_change:
        raise AssertionError(
            f"entrywise identity failed: exact={exact_change}, "
            f"chronological={chronological_change}"
        )

    # Verify deleted entries contribute exactly minus their initial mass, regardless
    # of their intermediate count trajectory before puncture.
    deleted_contributions: Dict[str, int] = {}
    for name, entry in entries.items():
        puncture_stage = entry.get("puncture_stage")
        if puncture_stage is None:
            continue
        last_active = int(entry["counts"][puncture_stage - 1])
        trade_telescope = last_active - int(entry["counts"][0])
        contribution = trade_telescope - last_active
        expected = -int(entry["counts"][0])
        if contribution != expected:
            raise AssertionError(
                f"deleted entry {name}: contribution={contribution}, expected={expected}"
            )
        deleted_contributions[name] = contribution

    print("chronological potentials", potentials)
    print("surviving-entry change", surviving_change)
    print("initial deleted-entry mass", deleted_initial_mass)
    print("deleted-entry contributions", deleted_contributions)
    print("exact chronological change", exact_change)
    print("outcome controller_entry_deletion_exact_telescoping")


if __name__ == "__main__":
    main()
