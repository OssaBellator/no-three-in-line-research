#!/usr/bin/env python3
"""Check elimination of raw explicit-host failures in the complete second host."""

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


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


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{label}: expected list")
    return value


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        width = require_int(payload.get("macro_width"), "macro_width", minimum=1)
        kappa = require_number(payload.get("kappa"), "kappa")
        blocks = require_list(payload.get("blocks"), "blocks")
        if not blocks:
            raise ValueError("blocks: expected at least one block")

        total_marked = 0
        total_square = 0
        seen_outcomes: set[str] = set()
        checked_blocks: list[dict[str, Any]] = []

        for pos, raw in enumerate(blocks):
            if not isinstance(raw, dict):
                raise ValueError(f"blocks[{pos}]: expected object")

            r = require_int(raw.get("marked_size"), f"blocks[{pos}].marked_size", 1)
            if r > width:
                raise ValueError(f"blocks[{pos}].marked_size exceeds macro_width")

            helper_count = require_int(
                raw.get("helper_count"), f"blocks[{pos}].helper_count", 1
            )
            if helper_count < r * r:
                raise ValueError(
                    f"blocks[{pos}].helper_count: expected at least marked_size^2"
                )

            max_exclusions = require_int(
                raw.get("max_role_exclusions"),
                f"blocks[{pos}].max_role_exclusions",
            )
            if max_exclusions > kappa * r + 1e-12:
                raise ValueError(
                    f"blocks[{pos}].max_role_exclusions exceeds kappa*marked_size"
                )

            support_rank = require_int(
                raw.get("support_rank"), f"blocks[{pos}].support_rank"
            )
            if support_rank > 3:
                raise ValueError(f"blocks[{pos}].support_rank exceeds three")

            outcome = raw.get("outcome")
            if not isinstance(outcome, str):
                raise ValueError(f"blocks[{pos}].outcome: expected string")
            if outcome not in RAW_OUTCOMES:
                raise ValueError(
                    f"blocks[{pos}].outcome: raw explicit-host outcome is not allowed"
                )
            seen_outcomes.add(outcome)

            buffer_size = math.ceil((kappa + 1.0) * r)
            minimum_allowed_per_role = buffer_size - max_exclusions
            if minimum_allowed_per_role < r:
                raise ValueError(
                    f"blocks[{pos}]: buffered Hall lower bound is below marked_size"
                )
            if helper_count < buffer_size:
                raise ValueError(
                    f"blocks[{pos}].helper_count is smaller than buffered set size"
                )

            total_marked += r
            total_square += r * r
            checked_blocks.append(
                {
                    "marked_size": r,
                    "helper_count": helper_count,
                    "buffer_size": buffer_size,
                    "minimum_allowed_per_role": minimum_allowed_per_role,
                    "support_rank": support_rank,
                    "outcome": outcome,
                }
            )

        if total_square > total_marked * total_marked:
            raise ValueError("sum of block squares exceeds square of total marked size")

        require_all = payload.get("require_all_raw_outcomes", False)
        if not isinstance(require_all, bool):
            raise ValueError("require_all_raw_outcomes: expected boolean")
        if require_all and seen_outcomes != RAW_OUTCOMES:
            missing = sorted(RAW_OUTCOMES - seen_outcomes)
            raise ValueError(f"missing raw outcomes: {missing}")

    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    result = {
        "outcome": "raw_second_host_leaf_eliminated",
        "macro_width": width,
        "kappa": kappa,
        "block_count": len(checked_blocks),
        "blocks": checked_blocks,
        "seen_raw_outcomes": sorted(seen_outcomes),
        "raw_explicit_host_failure_allowed": False,
        "total_marked_size": total_marked,
        "sum_block_squares": total_square,
        "square_total_marked_size": total_marked * total_marked,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
