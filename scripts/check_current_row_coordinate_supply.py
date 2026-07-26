#!/usr/bin/env python3
"""Check finite coordinate supply for dense current-support marked blocks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        m = require_int(payload.get("side_length"), "side_length", 1)
        macro_count = require_int(payload.get("macro_count"), "macro_count")
        pool_size = require_int(payload.get("pool_size"), "pool_size")
        macro_width = require_int(payload.get("macro_width"), "macro_width", 1)
        small_reserved = require_int(
            payload.get("additional_internal_reserved"),
            "additional_internal_reserved",
        )
        helper_constant = require_int(
            payload.get("helper_constant"), "helper_constant", 1
        )
        raw_blocks = payload.get("marked_blocks")
        if not isinstance(raw_blocks, list) or not raw_blocks:
            raise ValueError("marked_blocks: expected nonempty list")

        slab_reserved = macro_count * pool_size
        if slab_reserved >= m:
            raise ValueError("slab reservation must be smaller than side length")
        available_before_marked = m - slab_reserved - small_reserved
        if available_before_marked <= 0:
            raise ValueError("internal reservations leave no available coordinates")

        blocks: list[dict[str, int]] = []
        total_marked = 0
        sum_squares = 0
        for pos, value in enumerate(raw_blocks):
            h = require_int(value, f"marked_blocks[{pos}]", 1)
            if h > macro_width:
                raise ValueError(f"marked_blocks[{pos}] exceeds macro_width")
            available = available_before_marked - h
            required = helper_constant * h * h
            if available <= required:
                raise ValueError(
                    f"marked_blocks[{pos}]: available coordinates do not exceed "
                    "the quadratic helper requirement"
                )
            total_marked += h
            sum_squares += h * h
            blocks.append(
                {
                    "marked_size": h,
                    "available_after_marked": available,
                    "quadratic_helper_requirement": required,
                    "surplus": available - required,
                }
            )

        if sum_squares > total_marked * total_marked:
            raise ValueError("sum of block squares exceeds square of total marked size")
        aggregate_required = helper_constant * sum_squares
        if available_before_marked <= aggregate_required:
            raise ValueError(
                "available coordinates do not exceed aggregate blockwise helper volume"
            )

    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    result = {
        "outcome": "internal_coordinate_cover_eliminated",
        "side_length": m,
        "macro_count": macro_count,
        "pool_size": pool_size,
        "slab_reserved": slab_reserved,
        "additional_internal_reserved": small_reserved,
        "available_before_marked": available_before_marked,
        "macro_width": macro_width,
        "helper_constant": helper_constant,
        "blocks": blocks,
        "total_marked_size": total_marked,
        "sum_block_squares": sum_squares,
        "aggregate_quadratic_helper_requirement": aggregate_required,
        "aggregate_surplus": available_before_marked - aggregate_required,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
