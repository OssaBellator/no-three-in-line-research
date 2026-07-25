#!/usr/bin/env python3
"""Exhaustively check PP3qd--PP3qg on finite homogeneous signatures."""

from __future__ import annotations

import argparse
import json
from itertools import combinations, product
from pathlib import Path
from typing import Any

Pair = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def parse_pair(raw: Any, label: str) -> Pair:
    if (
        not isinstance(raw, list)
        or len(raw) != 2
        or any(isinstance(value, bool) or value not in (0, 1) for value in raw)
    ):
        raise ValueError(f"{label}: expected [0|1,0|1]")
    return int(raw[0]), int(raw[1])


def valid_sequence(bits: tuple[int, ...], forbidden: set[Pair]) -> bool:
    return all(
        (bits[left], bits[right]) not in forbidden
        for left, right in combinations(range(len(bits)), 2)
    )


def classification(forbidden: set[Pair]) -> str:
    diagonal_zero = (0, 0) in forbidden
    diagonal_one = (1, 1) in forbidden
    if diagonal_zero and diagonal_one:
        return "local_contradiction_for_h_at_least_3"
    if diagonal_one:
        return "credit_poor_all_zero"
    return "credit_rich_all_cross"


def analyze_case(name: str, h: int, forbidden: set[Pair]) -> dict[str, Any]:
    if h <= 0 or h > 24:
        raise ValueError(f"{name}: h must lie in [1,24]")
    valid = [
        bits
        for bits in product((0, 1), repeat=h)
        if valid_sequence(bits, forbidden)
    ]
    max_cross = max((sum(bits) for bits in valid), default=None)
    result = {
        "name": name,
        "h": h,
        "forbidden_pairs": [list(pair) for pair in sorted(forbidden)],
        "classification": classification(forbidden),
        "valid_sequence_count": len(valid),
        "maximum_cross_states": max_cross,
        "all_zero_valid": valid_sequence((0,) * h, forbidden),
        "all_one_valid": valid_sequence((1,) * h, forbidden),
        "first_valid_sequences": [list(bits) for bits in valid[:8]],
    }

    if (1, 1) not in forbidden:
        result["pp3qe_cross_capacity_verified"] = max_cross == h
    elif (0, 0) in forbidden and h >= 3:
        result["pp3qe_local_contradiction_verified"] = not valid
    else:
        result["pp3qe_credit_poor_verified"] = (
            max_cross is not None
            and max_cross <= 1
            and result["all_zero_valid"]
        )
    return result


def verify_all_signatures(max_h: int) -> dict[str, Any]:
    if max_h < 3 or max_h > 16:
        raise ValueError("verify_all_signatures_up_to must lie in [3,16]")
    universe = [(0, 0), (0, 1), (1, 0), (1, 1)]
    checked = 0
    failures: list[dict[str, Any]] = []
    for mask in range(16):
        forbidden = {
            universe[index] for index in range(4) if mask & (1 << index)
        }
        for h in range(3, max_h + 1):
            result = analyze_case(f"signature_{mask}_h_{h}", h, forbidden)
            checked += 1
            verified = any(
                result.get(key) is True
                for key in (
                    "pp3qe_cross_capacity_verified",
                    "pp3qe_local_contradiction_verified",
                    "pp3qe_credit_poor_verified",
                )
            )
            if not verified:
                failures.append(result)
    return {
        "signatures": 16,
        "maximum_h": max_h,
        "cases_checked": checked,
        "failure_count": len(failures),
        "failures": failures,
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

        results: list[dict[str, Any]] = []
        for index, raw_case in enumerate(raw_cases):
            if not isinstance(raw_case, dict):
                raise ValueError(f"cases[{index}] must be an object")
            name = raw_case.get("name", f"case_{index}")
            h = raw_case.get("h")
            if not isinstance(name, str) or not name:
                raise ValueError(f"cases[{index}].name must be a nonempty string")
            if not isinstance(h, int) or isinstance(h, bool):
                raise ValueError(f"cases[{index}].h must be an integer")
            raw_pairs = raw_case.get("forbidden_pairs")
            if not isinstance(raw_pairs, list):
                raise ValueError(f"cases[{index}].forbidden_pairs must be a list")
            forbidden = {
                parse_pair(pair, f"cases[{index}].forbidden_pairs[{pair_index}]")
                for pair_index, pair in enumerate(raw_pairs)
            }
            results.append(analyze_case(name, h, forbidden))

        verify_limit = payload.get("verify_all_signatures_up_to", 8)
        if not isinstance(verify_limit, int) or isinstance(verify_limit, bool):
            raise ValueError("verify_all_signatures_up_to must be an integer")
        verification = verify_all_signatures(verify_limit)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    print(
        json.dumps(
            {
                "cases": results,
                "all_signature_verification": verification,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
