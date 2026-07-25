#!/usr/bin/env python3
"""Check PP3qs--PP3qy cross-block rectangle supervariables exactly."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from pathlib import Path
from typing import Any

Cell = tuple[str, str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def parse_pair(raw: Any, label: str) -> tuple[str, str]:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or not all(isinstance(value, str) and value for value in raw)
    ):
        raise ValueError(f"{label}: expected two nonempty strings")
    return raw[0], raw[1]


def parse_cell_set(raw: Any, label: str) -> set[Cell]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a list")
    return {parse_pair(value, f"{label}[{index}]") for index, value in enumerate(raw)}


def directional_matchings(left: tuple[str, str], right: tuple[str, str]) -> list[tuple[Cell, Cell]]:
    return [
        ((left[0], image[0]), (left[1], image[1]))
        for image in permutations(right)
    ]


def hall_witness(
    left: tuple[str, str], right: tuple[str, str], allowed: set[Cell]
) -> dict[str, Any] | None:
    for vertex in left:
        neighborhood = [target for target in right if (vertex, target) in allowed]
        if not neighborhood:
            return {
                "left_set": [vertex],
                "neighborhood": [],
                "deficiency": 1,
            }
    neighborhood = sorted(
        {target for vertex in left for target in right if (vertex, target) in allowed}
    )
    if len(neighborhood) < 2:
        return {
            "left_set": list(left),
            "neighborhood": neighborhood,
            "deficiency": 2 - len(neighborhood),
        }
    return None


def analyze_case(raw: dict[str, Any], index: int) -> dict[str, Any]:
    name = raw.get("name", f"case_{index}")
    if not isinstance(name, str) or not name:
        raise ValueError(f"cases[{index}].name must be a nonempty string")

    left_s = parse_pair(raw.get("left_s"), f"cases[{index}].left_s")
    right_s = parse_pair(raw.get("right_s"), f"cases[{index}].right_s")
    left_t = parse_pair(raw.get("left_t"), f"cases[{index}].left_t")
    right_t = parse_pair(raw.get("right_t"), f"cases[{index}].right_t")
    all_resources = [*left_s, *right_s, *left_t, *right_t]
    if len(set(all_resources)) != 8:
        raise ValueError(f"cases[{index}]: all eight resource labels must be distinct")

    owner_s = raw.get("owner_left_s")
    owner_t = raw.get("owner_left_t")
    if owner_s not in left_s or owner_t not in left_t:
        raise ValueError(f"cases[{index}]: owner columns must belong to their left pairs")

    recapture = parse_cell_set(
        raw.get("direct_recapture_cells", []),
        f"cases[{index}].direct_recapture_cells",
    )
    unary = parse_cell_set(
        raw.get("unary_forbidden_cells", []),
        f"cases[{index}].unary_forbidden_cells",
    )
    cross_universe = {
        *( (left, right) for left in left_s for right in right_t ),
        *( (left, right) for left in left_t for right in right_s ),
    }
    if not recapture <= cross_universe or not unary <= cross_universe:
        raise ValueError(f"cases[{index}]: forbidden cells must lie in a cross block")

    if sum(cell[0] == owner_s for cell in recapture) > 1:
        raise ValueError(f"cases[{index}]: owner s has more than one recapture cell")
    if sum(cell[0] == owner_t for cell in recapture) > 1:
        raise ValueError(f"cases[{index}]: owner t has more than one recapture cell")

    forward = directional_matchings(left_s, right_t)
    backward = directional_matchings(left_t, right_s)
    states: list[dict[str, Any]] = []
    for forward_index, forward_matching in enumerate(forward):
        for backward_index, backward_matching in enumerate(backward):
            cells = set(forward_matching + backward_matching)
            states.append(
                {
                    "forward_matching": forward_index,
                    "backward_matching": backward_index,
                    "cells": [list(cell) for cell in sorted(cells)],
                    "credit_preserving": cells.isdisjoint(recapture),
                    "source_safe": cells.isdisjoint(recapture | unary),
                }
            )

    allowed = cross_universe - recapture - unary
    allowed_forward = {(left, right) for left in left_s for right in right_t if (left, right) in allowed}
    allowed_backward = {(left, right) for left in left_t for right in right_s if (left, right) in allowed}
    forward_hall = hall_witness(left_s, right_t, allowed_forward)
    backward_hall = hall_witness(left_t, right_s, allowed_backward)

    safe_states = [state for state in states if state["source_safe"]]
    credit_states = [state for state in states if state["credit_preserving"]]
    return {
        "name": name,
        "cross_block_state_count": len(states),
        "credit_preserving_state_count": len(credit_states),
        "source_safe_state_count": len(safe_states),
        "pp3qt_credit_state_exists": bool(credit_states),
        "pp3qu_safe_state_exists": bool(safe_states),
        "forward_hall_witness": forward_hall,
        "backward_hall_witness": backward_hall,
        "states": states,
    }


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        raw_cases = payload.get("cases")
        if not isinstance(raw_cases, list):
            raise ValueError("cases must be a list")
        results = []
        for index, raw in enumerate(raw_cases):
            if not isinstance(raw, dict):
                raise ValueError(f"cases[{index}] must be an object")
            results.append(analyze_case(raw, index))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    print(json.dumps({"cases": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
