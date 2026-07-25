#!/usr/bin/env python3
"""Check exact defect growth under fresh-helper single-cycle endpoint moves."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate_permutation(pi: list[int]) -> None:
    if sorted(pi) != list(range(len(pi))):
        raise ValueError("not a permutation of 0..m-1")


def relative_cycles(pi0: list[int], pi: list[int]) -> list[list[int]]:
    inv0 = [0] * len(pi0)
    for row, col in enumerate(pi0):
        inv0[col] = row
    sigma = [inv0[pi[row]] for row in range(len(pi))]
    seen: set[int] = set()
    cycles: list[list[int]] = []
    for start in range(len(pi)):
        if start in seen:
            continue
        cycle: list[int] = []
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = sigma[current]
        if len(cycle) > 1:
            cycles.append(cycle)
    return cycles


def defect_set(pi0: list[int], pi: list[int]) -> set[int]:
    return {row for row, (a, b) in enumerate(zip(pi0, pi)) if a != b}


def apply_single_cycle_move(
    pi0: list[int], pi: list[int], centre: int, helpers: list[int], order: list[int]
) -> list[int]:
    selected = [centre] + helpers
    if len(set(selected)) != len(selected):
        raise ValueError("selected rows are not distinct")
    if set(order) != set(selected) or len(order) != len(selected):
        raise ValueError("cycle_order must be a cyclic ordering of the selected rows")
    defects = defect_set(pi0, pi)
    if defects:
        if centre not in defects:
            raise ValueError("non-seed centre must be a defect row")
    elif centre in defects:
        raise ValueError("seed centre cannot already be defective")
    if any(helper in defects for helper in helpers):
        raise ValueError("all helpers must be untouched original rows")

    updated = pi.copy()
    for tail, successor in zip(order, order[1:] + order[:1]):
        updated[tail] = pi[successor]
    validate_permutation(updated)

    if any(updated[row] == pi0[row] for row in selected):
        raise AssertionError("selected single-cycle move reinserted an original edge")
    return updated


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    pi0 = list(map(int, data["initial_permutation"]))
    validate_permutation(pi0)
    pi = pi0.copy()
    controller_rows = set(map(int, data.get("controller_rows", [])))
    moves = data["moves"]
    records: list[dict[str, Any]] = []

    previous_cycle_count = 0
    for step, move in enumerate(moves, start=1):
        centre = int(move["centre"])
        helpers = list(map(int, move["helpers"]))
        order = list(map(int, move["cycle_order"]))
        before_defects = defect_set(pi0, pi)
        before_cycles = relative_cycles(pi0, pi)
        if step > 1 and centre in controller_rows:
            raise ValueError("a post-seed defect centre cannot be a fixed controller row")
        pi = apply_single_cycle_move(pi0, pi, centre, helpers, order)
        after_defects = defect_set(pi0, pi)
        after_cycles = relative_cycles(pi0, pi)
        q = 1 + len(helpers)
        expected = len(before_defects) + q if step == 1 else len(before_defects) + q - 1
        if len(after_defects) != expected:
            raise AssertionError("defect increment is not exact")
        if step == 1:
            if len(after_cycles) != 1 or len(after_cycles[0]) != q:
                raise AssertionError("seed move did not create one q-cycle")
        else:
            if len(after_cycles) != len(before_cycles):
                raise AssertionError("fresh-helper move changed the defect-cycle count")
            if len(after_cycles) != previous_cycle_count:
                raise AssertionError("cycle-count invariant failed")
        previous_cycle_count = len(after_cycles)
        records.append(
            {
                "step": step,
                "q": q,
                "centre": centre,
                "defect_before": len(before_defects),
                "defect_after": len(after_defects),
                "cycle_count_after": len(after_cycles),
                "cycle_lengths_after": sorted((len(c) for c in after_cycles), reverse=True),
            }
        )

    final_defects = defect_set(pi0, pi)
    final_cycles = relative_cycles(pi0, pi)
    threshold = int(data.get("target_defect_threshold", 0))
    outcome = (
        "target_scale_single_cycle_core"
        if threshold and len(final_defects) >= threshold and len(final_cycles) == 1
        else "exact_single_cycle_growth"
    )
    return {
        "m": len(pi0),
        "steps": len(moves),
        "final_defect_size": len(final_defects),
        "final_cycle_count": len(final_cycles),
        "final_cycle_lengths": sorted((len(c) for c in final_cycles), reverse=True),
        "untouched_original_rows": len(pi0) - len(final_defects),
        "records": records,
        "outcome": outcome,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(analyse(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
