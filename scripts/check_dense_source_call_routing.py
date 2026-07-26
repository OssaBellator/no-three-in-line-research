#!/usr/bin/env python3
"""Check routing of paired-secant source-row calls without raw host leaves."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

RAW_OUTCOMES = {
    "independent_cycle",
    "dense_current_support",
    "dense_source_support",
}
CALL_TYPES = {"paired_switch_bank", "fixed_centre_fillers"}
SOURCE_MODES = {
    "paired_switch_bank": "vanishing_after_amplification",
    "fixed_centre_fillers": "canonical_credited_source",
}


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label}: expected number")
    result = float(value)
    if not math.isfinite(result) or result < minimum:
        raise ValueError(f"{label}: expected finite number >= {minimum}")
    return result


def route(call_type: str, outcome: str) -> str:
    if outcome == "independent_cycle":
        return "source_valid_joint_state"
    if outcome == "dense_current_support":
        return "named_current_conversion"
    if call_type == "paired_switch_bank":
        return "source_mass_vanishes_or_current_support"
    return "direct_paid_canonical_source_structure"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        W = require_int(payload.get("macro_width"), "macro_width", 1)
        kappa = require_number(payload.get("kappa"), "kappa")
        calls = payload.get("calls")
        if not isinstance(calls, list) or not calls:
            raise ValueError("calls: expected nonempty list")

        checked: list[dict[str, Any]] = []
        seen_types: set[str] = set()
        seen_outcomes: set[str] = set()
        for i, raw in enumerate(calls):
            if not isinstance(raw, dict):
                raise ValueError(f"calls[{i}]: expected object")
            call_type = raw.get("call_type")
            if call_type not in CALL_TYPES:
                raise ValueError(f"calls[{i}].call_type: unsupported call")
            seen_types.add(call_type)

            r = require_int(raw.get("marked_size"), f"calls[{i}].marked_size", 1)
            if r > W:
                raise ValueError(f"calls[{i}].marked_size exceeds macro_width")
            helpers = require_int(raw.get("helper_count"), f"calls[{i}].helper_count", 1)
            if helpers < r * r:
                raise ValueError(f"calls[{i}].helper_count is below marked_size^2")
            exclusions = require_int(
                raw.get("max_role_exclusions"), f"calls[{i}].max_role_exclusions"
            )
            if exclusions > kappa * r + 1e-12:
                raise ValueError(f"calls[{i}].max_role_exclusions exceeds kappa*r")
            support_rank = require_int(raw.get("support_rank"), f"calls[{i}].support_rank")
            if support_rank > 3:
                raise ValueError(f"calls[{i}].support_rank exceeds three")

            source_mode = raw.get("source_mass_mode")
            if source_mode != SOURCE_MODES[call_type]:
                raise ValueError(f"calls[{i}].source_mass_mode is inconsistent with call type")

            outcome = raw.get("raw_outcome")
            if outcome not in RAW_OUTCOMES:
                raise ValueError(
                    f"calls[{i}].raw_outcome: raw Hall/alternating/host outcome is forbidden"
                )
            seen_outcomes.add(outcome)
            checked.append(
                {
                    "call_type": call_type,
                    "marked_size": r,
                    "helper_count": helpers,
                    "support_rank": support_rank,
                    "source_mass_mode": source_mode,
                    "raw_outcome": outcome,
                    "routed_to": route(call_type, outcome),
                    "raw_host_leaf": False,
                }
            )

        require_all_types = payload.get("require_all_call_types", False)
        if not isinstance(require_all_types, bool):
            raise ValueError("require_all_call_types: expected boolean")
        if require_all_types and seen_types != CALL_TYPES:
            raise ValueError(f"missing call types: {sorted(CALL_TYPES-seen_types)}")
        require_all_outcomes = payload.get("require_all_raw_outcomes", False)
        if not isinstance(require_all_outcomes, bool):
            raise ValueError("require_all_raw_outcomes: expected boolean")
        if require_all_outcomes and seen_outcomes != RAW_OUTCOMES:
            raise ValueError(f"missing raw outcomes: {sorted(RAW_OUTCOMES-seen_outcomes)}")

    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    print(
        json.dumps(
            {
                "outcome": "dense_source_host_leaf_eliminated",
                "macro_width": W,
                "kappa": kappa,
                "call_count": len(checked),
                "calls": checked,
                "seen_call_types": sorted(seen_types),
                "seen_raw_outcomes": sorted(seen_outcomes),
                "raw_conditional_hall_allowed": False,
                "raw_alternating_host_allowed": False,
                "raw_role_host_allowed": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
