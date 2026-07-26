#!/usr/bin/env python3
"""Finite diagnostic for PP3arx--PP3asb."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_target_cycle_complete_cancellation.py EXAMPLE.json")

    with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    cycle_length = int(data["cycle_length"])
    first_credit = int(data["first_removal_credit"])
    first_insertion = int(data["first_insertion_cost"])
    second_insertion = int(data["second_insertion_cost"])
    destroyed_first_insertion = int(data["destroyed_first_insertion"])

    if first_credit < cycle_length:
        raise AssertionError("fully credited cycle must pay at least its length")
    if destroyed_first_insertion < first_insertion:
        raise AssertionError("second trade did not destroy the complete first insertion table")
    if second_insertion != 0:
        raise AssertionError("stored second trade is not the zero-cost support-free branch")

    first_change = first_insertion - first_credit
    second_change = second_insertion - destroyed_first_insertion
    composite_change = first_change + second_change
    reduced_bound = second_insertion - first_credit

    if composite_change > reduced_bound:
        raise AssertionError("complete cancellation inequality failed")
    if composite_change >= 0:
        raise AssertionError("composite trade is not strict")

    print(f"cycle length {cycle_length}")
    print(f"first removal credit {first_credit}")
    print(f"first insertion cost {first_insertion}")
    print(f"first-step change {first_change}")
    print(f"second insertion cost {second_insertion}")
    print(f"destroyed first insertion {destroyed_first_insertion}")
    print(f"second-step change {second_change}")
    print(f"composite change {composite_change}")
    print(f"reduced composite bound {reduced_bound}")
    print("outcome target_cycle_complete_insertion_cancellation")


if __name__ == "__main__":
    main()
