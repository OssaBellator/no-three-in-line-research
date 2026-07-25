#!/usr/bin/env python3
"""Finite diagnostic for candidate fans in complete two-resource grids."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    data = json.loads(args.instance.read_text())

    a_size = int(data["a_size"])
    b_size = int(data["b_size"])
    credit = float(data.get("removal_credit", 1.0))
    compatible = {
        (int(a), int(b)) for a, b in data.get(
            "compatible_states",
            [[a, b] for a in range(a_size) for b in range(b_size)],
        )
    }
    raw = data["candidates"]

    state_candidates: dict[tuple[int, int], set[str]] = {}
    candidate_states: dict[str, list[tuple[int, int]]] = defaultdict(list)
    for key, values in raw.items():
        a_text, b_text = key.split(",")
        state = (int(a_text), int(b_text))
        if state not in compatible:
            raise ValueError(f"candidate list for incompatible state {state}")
        colours = {str(value) for value in values}
        if not colours:
            raise ValueError(f"state {state} has no blocker candidate")
        state_candidates[state] = colours
        for colour in colours:
            candidate_states[colour].append(state)

    missing = compatible - set(state_candidates)
    if missing:
        raise ValueError(f"missing candidate lists for {sorted(missing)}")

    for colour, states in candidate_states.items():
        rows = [a for a, _ in states]
        cols = [b for _, b in states]
        if len(rows) != len(set(rows)) or len(cols) != len(set(cols)):
            raise AssertionError(f"candidate {colour} is not a matching")

    row_partners: dict[int, set[int]] = defaultdict(set)
    row_candidates: dict[int, set[str]] = defaultdict(set)
    column_partners: dict[int, set[int]] = defaultdict(set)
    column_candidates: dict[int, set[str]] = defaultdict(set)
    total_weight = 0
    for (a, b), colours in state_candidates.items():
        row_partners[a].add(b)
        column_partners[b].add(a)
        before = len(row_candidates[a])
        row_candidates[a].update(colours)
        if len(row_candidates[a]) != before + len(colours):
            raise AssertionError("candidate repeated within one row")
        before = len(column_candidates[b])
        column_candidates[b].update(colours)
        if len(column_candidates[b]) != before + len(colours):
            raise AssertionError("candidate repeated within one column")
        total_weight += len(colours)

    best_row = max(row_candidates, key=lambda a: len(row_candidates[a]))
    best_column = max(column_candidates, key=lambda b: len(column_candidates[b]))
    row_bound = total_weight / max(1, a_size)
    column_bound = total_weight / max(1, b_size)
    if len(row_candidates[best_row]) + 1e-12 < row_bound:
        raise AssertionError("weighted row-average bound failed")
    if len(column_candidates[best_column]) + 1e-12 < column_bound:
        raise AssertionError("weighted column-average bound failed")

    result = {
        "a_size": a_size,
        "b_size": b_size,
        "state_count": len(compatible),
        "distinct_candidates": len(candidate_states),
        "total_candidate_incidence": total_weight,
        "removal_credit": credit,
        "best_row": best_row,
        "best_row_partner_count": len(row_partners[best_row]),
        "best_row_candidate_count": len(row_candidates[best_row]),
        "row_average_lower_bound": row_bound,
        "best_column": best_column,
        "best_column_partner_count": len(column_partners[best_column]),
        "best_column_candidate_count": len(column_candidates[best_column]),
        "column_average_lower_bound": column_bound,
        "outcome": "fixed_cell_credit_fan",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
