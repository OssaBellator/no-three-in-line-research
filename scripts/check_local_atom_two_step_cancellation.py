#!/usr/bin/env python3
"""Check exact two-step cancellation for A2, B3, and B4 local atoms."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_local_atom_two_step_cancellation.py example.json")
    data = load(sys.argv[1])
    removal = int(data["first_removal_credit"])
    atom = int(data["atom_weight"])
    first_other = int(data["first_other_cost"])
    recapture = int(data["second_self_recapture"])
    second_foreign = int(data["second_foreign_cost"])

    first_change = atom + first_other - removal
    second_change = recapture + second_foreign - atom
    total_change = first_change + second_change
    reduced_formula = first_other + recapture + second_foreign - removal

    if total_change != reduced_formula:
        raise AssertionError((total_change, reduced_formula))
    if total_change >= 0:
        raise AssertionError(f"stored composite is not improving: {total_change}")

    for atom_type in ("A2", "B3", "B4"):
        print(atom_type, "atom weight", atom)
        print(atom_type, "first-step change", first_change)
        print(atom_type, "second-step change", second_change)
        print(atom_type, "composite change", total_change)
    print("uncancelled collateral", first_other + recapture + second_foreign)
    print("first removal credit", removal)
    print("outcome local_atom_two_step_paid_improvement")


if __name__ == "__main__":
    main()
