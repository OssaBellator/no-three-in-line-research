#!/usr/bin/env python3
"""Check the fixed-centre rank-three binary-Xi path localization."""

from __future__ import annotations

import argparse
import json
from itertools import permutations
from math import factorial, isqrt
from pathlib import Path
from typing import Any

Pair = tuple[int, int]
Chain = tuple[int, int, int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--enumeration-limit", type=int, default=8)
    return parser.parse_args()


def require_int(value: Any, label: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected an integer >= {minimum}")
    return value


def parse_pairs(raw: Any, label: str, n: int, centre: int) -> set[Pair]:
    if raw is None:
        return set()
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a list")
    result: set[Pair] = set()
    for position, item in enumerate(raw):
        item_label = f"{label}[{position}]"
        if (
            not isinstance(item, list)
            or len(item) != 2
            or any(isinstance(x, bool) or not isinstance(x, int) for x in item)
        ):
            raise ValueError(f"{item_label}: expected [first,second] integers")
        first, second = item
        if (
            not 0 <= first < n
            or not 0 <= second < n
            or first == centre
            or second == centre
            or first == second
        ):
            raise ValueError(
                f"{item_label}: expected distinct noncentre indices in [0,n)"
            )
        pair = (first, second)
        if pair in result:
            raise ValueError(f"{label}: duplicate pair {pair}")
        result.add(pair)
    return result


def parse_overrides(
    raw: Any,
    label: str,
    n: int,
    centre: int,
) -> dict[Pair, int]:
    if raw is None:
        return {}
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected a list")
    result: dict[Pair, int] = {}
    for position, item in enumerate(raw):
        item_label = f"{label}[{position}]"
        if not isinstance(item, list) or len(item) != 3:
            raise ValueError(f"{item_label}: expected [first,second,cost]")
        first = require_int(item[0], f"{item_label}[0]")
        second = require_int(item[1], f"{item_label}[1]")
        cost = require_int(item[2], f"{item_label}[2]")
        if (
            first >= n
            or second >= n
            or first == centre
            or second == centre
            or first == second
        ):
            raise ValueError(
                f"{item_label}: expected distinct noncentre indices in [0,n)"
            )
        pair = (first, second)
        if pair in result:
            raise ValueError(f"{label}: duplicate override for {pair}")
        result[pair] = cost
    return result


def make_costs(
    n: int,
    centre: int,
    default: int,
    overrides: dict[Pair, int],
) -> dict[Pair, int]:
    costs = {
        (first, second): default
        for first in range(n)
        for second in range(n)
        if first != centre and second != centre and first != second
    }
    costs.update(overrides)
    return costs


def count_cycles_with_chain(n: int, centre: int, chain: Chain) -> int:
    predecessor_outer, predecessor_inner, successor_inner, successor_outer = chain
    prescribed = {
        predecessor_outer: predecessor_inner,
        predecessor_inner: centre,
        centre: successor_inner,
        successor_inner: successor_outer,
    }
    count = 0
    remaining = [index for index in range(n) if index != 0]
    for tail in permutations(remaining):
        order = (0,) + tail
        image = {
            order[position]: order[(position + 1) % n]
            for position in range(n)
        }
        if all(image[source] == target for source, target in prescribed.items()):
            count += 1
    return count


def ceil_sqrt(value: int) -> int:
    root = isqrt(value)
    return root if root * root == value else root + 1


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")

        n = require_int(payload.get("n"), "n", minimum=5)
        centre = require_int(payload.get("centre"), "centre")
        if centre >= n:
            raise ValueError("centre must lie in [0,n)")
        budget = require_int(payload.get("budget"), "budget", minimum=1)

        left_default = require_int(
            payload.get("left_default_cost"), "left_default_cost"
        )
        middle_default = require_int(
            payload.get("middle_default_cost"), "middle_default_cost"
        )
        right_default = require_int(
            payload.get("right_default_cost"), "right_default_cost"
        )

        left_cost = make_costs(
            n,
            centre,
            left_default,
            parse_overrides(
                payload.get("left_cost_overrides"),
                "left_cost_overrides",
                n,
                centre,
            ),
        )
        middle_cost = make_costs(
            n,
            centre,
            middle_default,
            parse_overrides(
                payload.get("middle_cost_overrides"),
                "middle_cost_overrides",
                n,
                centre,
            ),
        )
        right_cost = make_costs(
            n,
            centre,
            right_default,
            parse_overrides(
                payload.get("right_cost_overrides"),
                "right_cost_overrides",
                n,
                centre,
            ),
        )

        forbidden_left = parse_pairs(
            payload.get("forbidden_left_paths"),
            "forbidden_left_paths",
            n,
            centre,
        )
        forbidden_middle = parse_pairs(
            payload.get("forbidden_middle_paths"),
            "forbidden_middle_paths",
            n,
            centre,
        )
        forbidden_right = parse_pairs(
            payload.get("forbidden_right_paths"),
            "forbidden_right_paths",
            n,
            centre,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    indices = [index for index in range(n) if index != centre]
    cheap_chains: list[tuple[int, Chain]] = []
    source_clean_chain_count = 0
    for predecessor_inner in indices:
        for successor_inner in indices:
            if predecessor_inner == successor_inner:
                continue
            if (predecessor_inner, successor_inner) in forbidden_middle:
                continue
            for predecessor_outer in indices:
                if predecessor_outer in {predecessor_inner, successor_inner}:
                    continue
                if (predecessor_outer, predecessor_inner) in forbidden_left:
                    continue
                for successor_outer in indices:
                    if successor_outer in {
                        predecessor_outer,
                        predecessor_inner,
                        successor_inner,
                    }:
                        continue
                    if (successor_inner, successor_outer) in forbidden_right:
                        continue
                    source_clean_chain_count += 1
                    cost = (
                        left_cost[(predecessor_outer, predecessor_inner)]
                        + middle_cost[(predecessor_inner, successor_inner)]
                        + right_cost[(successor_inner, successor_outer)]
                    )
                    if cost < budget:
                        cheap_chains.append(
                            (
                                cost,
                                (
                                    predecessor_outer,
                                    predecessor_inner,
                                    successor_inner,
                                    successor_outer,
                                ),
                            )
                        )

    low_left: dict[int, set[int]] = {}
    low_right: dict[int, set[int]] = {}
    for inner in indices:
        low_left[inner] = {
            outer
            for outer in indices
            if outer != inner
            and (outer, inner) not in forbidden_left
            and 3 * left_cost[(outer, inner)] < budget
        }
        low_right[inner] = {
            outer
            for outer in indices
            if outer != inner
            and (inner, outer) not in forbidden_right
            and 3 * right_cost[(inner, outer)] < budget
        }

    high_choice_left = {inner for inner in indices if len(low_left[inner]) >= 3}
    high_choice_right = {inner for inner in indices if len(low_right[inner]) >= 3}

    result: dict[str, Any] = {
        "n": n,
        "centre": centre,
        "budget": budget,
        "source_clean_chain_count": source_clean_chain_count,
        "cheap_chain_count": len(cheap_chains),
        "P3_size": len(high_choice_left),
        "S3_size": len(high_choice_right),
    }

    if cheap_chains:
        cost, chain = min(cheap_chains)
        result.update(
            {
                "outcome": "cheap_chain",
                "selected_chain": [chain[0], chain[1], centre, chain[2], chain[3]],
                "selected_cost": cost,
            }
        )
        if n <= args.enumeration_limit:
            enumerated = count_cycles_with_chain(n, centre, chain)
            formula = factorial(n - 5)
            if enumerated != formula:
                raise SystemExit(
                    f"check failed: cycle count {enumerated} != (n-5)!={formula}"
                )
            result["hamilton_cycles_containing_chain"] = enumerated
            result["cycle_count_formula"] = formula
    else:
        safe_distinct_middle: list[Pair] = []
        light_safe_middle: list[Pair] = []
        for predecessor_inner in high_choice_left:
            for successor_inner in high_choice_right:
                if predecessor_inner == successor_inner:
                    continue
                pair = (predecessor_inner, successor_inner)
                if pair in forbidden_middle:
                    continue
                safe_distinct_middle.append(pair)
                if 3 * middle_cost[pair] < budget:
                    light_safe_middle.append(pair)

        if light_safe_middle:
            raise SystemExit(
                "check failed: no cheap chain, but a high-choice source-valid "
                f"middle pair is light: {min(light_safe_middle)}"
            )

        product = len(high_choice_left) * len(high_choice_right)
        deleted_bound = len(forbidden_middle) + n
        heavy_middle_weight = sum(middle_cost[pair] for pair in safe_distinct_middle)
        theoretical_weight_numerator = budget * max(product - deleted_bound, 0)
        if 3 * heavy_middle_weight < theoretical_weight_numerator:
            raise SystemExit("check failed: heavy-middle weight bound is violated")

        small_core_bound = ceil_sqrt(2 * deleted_bound)
        if product > 2 * deleted_bound:
            outcome = "heavy_middle_rectangle"
            if 6 * heavy_middle_weight < budget * product:
                raise SystemExit(
                    "check failed: heavy rectangle has less than budget*product/6"
                )
        else:
            outcome = "small_outer_core"
            if min(len(high_choice_left), len(high_choice_right)) > small_core_bound:
                raise SystemExit("check failed: small outer-core bound is violated")

        safe_left_count = sum(
            1
            for outer in indices
            for inner in indices
            if outer != inner and (outer, inner) not in forbidden_left
        )
        safe_right_count = sum(
            1
            for inner in indices
            for outer in indices
            if outer != inner and (inner, outer) not in forbidden_right
        )
        heavy_left_count = sum(
            1
            for outer in indices
            for inner in indices
            if outer != inner
            and inner not in high_choice_left
            and (outer, inner) not in forbidden_left
            and 3 * left_cost[(outer, inner)] >= budget
        )
        heavy_right_count = sum(
            1
            for inner in indices
            for outer in indices
            if outer != inner
            and inner not in high_choice_right
            and (inner, outer) not in forbidden_right
            and 3 * right_cost[(inner, outer)] >= budget
        )

        result.update(
            {
                "outcome": outcome,
                "P3_times_S3": product,
                "middle_deleted_bound": deleted_bound,
                "safe_distinct_middle_count": len(safe_distinct_middle),
                "heavy_middle_weight": heavy_middle_weight,
                "ceil_sqrt_twice_deleted_bound": small_core_bound,
                "safe_left_path_count": safe_left_count,
                "safe_right_path_count": safe_right_count,
                "heavy_left_paths_outside_P3": heavy_left_count,
                "heavy_right_paths_outside_S3": heavy_right_count,
            }
        )

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
