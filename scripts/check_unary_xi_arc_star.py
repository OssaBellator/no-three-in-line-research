#!/usr/bin/env python3
"""Check the fixed-centre unary-Xi cheap-pair/heavy-star dichotomy."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from math import factorial, isqrt
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=9)
    return parser.parse_args()


def require_int(value: Any, label: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected an integer >= {minimum}")
    return value


def parse_costs(raw: Any, label: str, n: int, centre: int) -> dict[int, int]:
    if not isinstance(raw, dict):
        raise ValueError(f"{label}: expected an object")
    expected = {str(index) for index in range(n) if index != centre}
    if set(raw) != expected:
        missing = sorted(expected - set(raw))
        extra = sorted(set(raw) - expected)
        raise ValueError(
            f"{label}: keys must be all noncentre indices; "
            f"missing={missing}, extra={extra}"
        )
    return {
        int(key): require_int(value, f"{label}[{key!r}]")
        for key, value in raw.items()
    }


def parse_index_set(raw: Any, label: str, n: int, centre: int) -> set[int]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a list")
    result: set[int] = set()
    for position, value in enumerate(raw):
        index = require_int(value, f"{label}[{position}]")
        if index >= n or index == centre:
            raise ValueError(
                f"{label}[{position}]: index must be noncentre and in [0,n)"
            )
        if index in result:
            raise ValueError(f"{label}: duplicate index {index}")
        result.add(index)
    return result


def parse_pairs(
    raw: Any, label: str, n: int, centre: int
) -> set[tuple[int, int]]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a list")
    result: set[tuple[int, int]] = set()
    for position, value in enumerate(raw):
        item_label = f"{label}[{position}]"
        if (
            not isinstance(value, list)
            or len(value) != 2
            or any(isinstance(x, bool) or not isinstance(x, int) for x in value)
        ):
            raise ValueError(
                f"{item_label}: expected [predecessor,successor] integers"
            )
        predecessor, successor = value
        if (
            not 0 <= predecessor < n
            or not 0 <= successor < n
            or predecessor == centre
            or successor == centre
        ):
            raise ValueError(
                f"{item_label}: indices must be noncentre and in [0,n)"
            )
        pair = (predecessor, successor)
        if pair in result:
            raise ValueError(f"{label}: duplicate pair {pair}")
        result.add(pair)
    return result


def count_cycles_with_segment(
    n: int, predecessor: int, centre: int, successor: int
) -> int:
    """Enumerate directed Hamilton cycles using cyclic orders starting at zero."""
    count = 0
    remaining = [index for index in range(n) if index != 0]
    for tail in permutations(remaining):
        order = (0,) + tail
        image = {
            order[position]: order[(position + 1) % n]
            for position in range(n)
        }
        if image[predecessor] == centre and image[centre] == successor:
            count += 1
    return count


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = require_int(payload.get("n"), "n", minimum=3)
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")
        budget = require_int(payload.get("budget"), "budget", minimum=1)
        incoming = parse_costs(
            payload.get("incoming_cost"), "incoming_cost", n, centre
        )
        outgoing = parse_costs(
            payload.get("outgoing_cost"), "outgoing_cost", n, centre
        )
        safe_in = parse_index_set(
            payload.get("safe_predecessors"), "safe_predecessors", n, centre
        )
        safe_out = parse_index_set(
            payload.get("safe_successors"), "safe_successors", n, centre
        )
        middle = parse_pairs(
            payload.get("forbidden_middle_pairs", []),
            "forbidden_middle_pairs",
            n,
            centre,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    compatible_pairs = sorted(
        (predecessor, successor)
        for predecessor in safe_in
        for successor in safe_out
        if predecessor != successor and (predecessor, successor) not in middle
    )
    cheap_pairs = [
        (predecessor, successor)
        for predecessor, successor in compatible_pairs
        if incoming[predecessor] + outgoing[successor] < budget
    ]

    low_in = {index for index in safe_in if 2 * incoming[index] < budget}
    low_out = {index for index in safe_out if 2 * outgoing[index] < budget}
    distinct_low_pairs = {
        (predecessor, successor)
        for predecessor in low_in
        for successor in low_out
        if predecessor != successor
    }
    forbidden_low_pairs = distinct_low_pairs & middle

    result: dict[str, Any] = {
        "n": n,
        "centre": centre,
        "budget": budget,
        "compatible_pair_count": len(compatible_pairs),
        "cheap_pair_count": len(cheap_pairs),
        "low_incoming_count": len(low_in),
        "low_outgoing_count": len(low_out),
        "forbidden_middle_pair_count": len(middle),
    }

    if cheap_pairs:
        predecessor, successor = min(
            cheap_pairs,
            key=lambda pair: (
                incoming[pair[0]] + outgoing[pair[1]],
                pair,
            ),
        )
        result.update(
            {
                "outcome": "cheap_pair",
                "selected_predecessor": predecessor,
                "selected_successor": successor,
                "selected_local_cost": (
                    incoming[predecessor] + outgoing[successor]
                ),
            }
        )
        if n <= args.enumeration_limit:
            enumerated = count_cycles_with_segment(
                n, predecessor, centre, successor
            )
            formula = factorial(n - 3)
            if enumerated != formula:
                raise SystemExit(
                    f"check failed: cycle count {enumerated} != (n-3)!={formula}"
                )
            result["hamilton_cycles_containing_segment"] = enumerated
            result["cycle_count_formula"] = formula
    else:
        if forbidden_low_pairs != distinct_low_pairs:
            missing = sorted(distinct_low_pairs - forbidden_low_pairs)
            raise SystemExit(
                "check failed: no cheap pair, but a distinct low-low pair is not "
                f"middle-forbidden: {missing[0]}"
            )
        product_bound_lhs = len(low_in) * len(low_out) - min(
            len(low_in), len(low_out)
        )
        if product_bound_lhs > len(middle):
            raise SystemExit(
                "check failed: low-set product bound exceeds middle relation size"
            )
        square_root_bound = isqrt(len(middle) + n)
        if square_root_bound * square_root_bound < len(middle) + n:
            square_root_bound += 1
        heavy_side = "incoming" if len(low_in) <= len(low_out) else "outgoing"
        exceptional = low_in if heavy_side == "incoming" else low_out
        safe_side = safe_in if heavy_side == "incoming" else safe_out
        result.update(
            {
                "outcome": "heavy_star",
                "heavy_side": heavy_side,
                "heavy_arc_threshold_twice": budget,
                "safe_arc_count_on_heavy_side": len(safe_side),
                "exceptional_low_arc_count": len(exceptional),
                "ceil_sqrt_middle_plus_n": square_root_bound,
                "product_bound_lhs": product_bound_lhs,
                "all_distinct_low_low_pairs_middle_forbidden": True,
            }
        )

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
