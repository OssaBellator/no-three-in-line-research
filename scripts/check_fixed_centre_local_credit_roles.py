#!/usr/bin/env python3
"""Check seven-role local-credit concentration around one fixed centre."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROLES = (
    "unary_in",
    "unary_out",
    "rank3_left",
    "rank3_middle",
    "rank3_right",
    "rank4_in_cross",
    "rank4_out_cross",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def require_number(value: Any, label: str, minimum: float = 0.0) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value < minimum:
        raise ValueError(f"{label}: expected number >= {minimum}")
    return float(value)


def object_for(role: str, chain: tuple[int, int, int, int, int]) -> tuple[int, ...]:
    r, p, c, s, t = chain
    if role == "unary_in":
        return (p, c)
    if role == "unary_out":
        return (c, s)
    if role == "rank3_left":
        return (r, p, c)
    if role == "rank3_middle":
        return (p, c, s)
    if role == "rank3_right":
        return (c, s, t)
    if role == "rank4_in_cross":
        return (p, c, s, t)
    if role == "rank4_out_cross":
        return (c, s, r, p)
    raise AssertionError(role)


def cap_for(role: str, n: int) -> int:
    if role in {"unary_in", "unary_out"}:
        return (n - 2) * (n - 3) * (n - 4)
    if role in {"rank3_left", "rank3_middle", "rank3_right"}:
        return (n - 3) * (n - 4)
    return n - 4


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
        threshold = require_number(payload.get("lambda"), "lambda", minimum=1e-12)
        defaults = payload.get("role_weights")
        if not isinstance(defaults, dict):
            raise ValueError("role_weights: expected object")
        role_weights = {
            role: require_number(defaults.get(role, 0), f"role_weights.{role}")
            for role in ROLES
        }
        raw_invalid = payload.get("source_invalid_chains", [])
        if not isinstance(raw_invalid, list):
            raise ValueError("source_invalid_chains: expected list")
        invalid: set[tuple[int, int, int, int]] = set()
        for pos, item in enumerate(raw_invalid):
            if not isinstance(item, list) or len(item) != 4:
                raise ValueError(
                    f"source_invalid_chains[{pos}]: expected [r,p,s,t]"
                )
            values = tuple(
                require_int(x, f"source_invalid_chains[{pos}][{i}]")
                for i, x in enumerate(item)
            )
            if any(x >= n or x == centre for x in values) or len(set(values)) != 4:
                raise ValueError(
                    f"source_invalid_chains[{pos}]: expected four distinct noncentre indices"
                )
            invalid.add(values)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    noncentre = [x for x in range(n) if x != centre]
    heavy_chains: list[tuple[int, int, int, int, int]] = []
    role_assignments: dict[str, list[tuple[int, int, int, int, int]]] = defaultdict(list)

    for r, p, s, t in itertools.permutations(noncentre, 4):
        if (r, p, s, t) in invalid:
            continue
        chain = (r, p, centre, s, t)
        total = sum(role_weights.values())
        if total < threshold:
            continue
        heavy_chains.append(chain)
        qualifying = [
            role for role in ROLES
            if role_weights[role] >= threshold / 7.0
        ]
        if not qualifying:
            raise SystemExit("check failed: seven-role pigeonhole violated")
        chosen = max(qualifying, key=lambda role: (role_weights[role], -ROLES.index(role)))
        role_assignments[chosen].append(chain)

    if not heavy_chains:
        result = {
            "outcome": "cheap_local_chain_family",
            "n": n,
            "centre": centre,
            "lambda": threshold,
            "source_clean_chain_count": len(list(itertools.permutations(noncentre, 4))) - len(invalid),
            "expensive_chain_count": 0,
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return

    dominant_role = max(
        ROLES,
        key=lambda role: (len(role_assignments[role]), -ROLES.index(role)),
    )
    dominant_chains = role_assignments[dominant_role]
    if len(dominant_chains) * 7 < len(heavy_chains):
        raise SystemExit("check failed: dominant-role pigeonhole violated")

    object_counts = Counter(object_for(dominant_role, chain) for chain in dominant_chains)
    cap = cap_for(dominant_role, n)
    if max(object_counts.values(), default=0) > cap:
        raise SystemExit("check failed: extension multiplicity cap violated")
    distinct_objects = sorted(object_counts)
    lower_bound = len(heavy_chains) / (7.0 * cap)
    if len(distinct_objects) + 1e-12 < lower_bound:
        raise SystemExit("check failed: distinct-object lower bound violated")

    if dominant_role in {"unary_in", "unary_out"}:
        outcome = "heavy_unary_arc_family"
    elif dominant_role == "rank3_middle":
        outcome = "heavy_rank3_middle_grid"
    elif dominant_role in {"rank3_left", "rank3_right"}:
        outcome = "heavy_rank3_outer_path_family"
    else:
        outcome = "heavy_rank4_cross_partner_family"

    result = {
        "outcome": outcome,
        "n": n,
        "centre": centre,
        "lambda": threshold,
        "role_weights": role_weights,
        "source_invalid_chain_count": len(invalid),
        "expensive_chain_count": len(heavy_chains),
        "dominant_role": dominant_role,
        "dominant_role_chain_count": len(dominant_chains),
        "required_dominant_role_count": len(heavy_chains) / 7.0,
        "extension_multiplicity_cap": cap,
        "maximum_observed_extension_multiplicity": max(object_counts.values()),
        "distinct_heavy_object_count": len(distinct_objects),
        "distinct_object_lower_bound": lower_bound,
        "heavy_object_weight": role_weights[dominant_role],
        "distinct_heavy_objects": [list(obj) for obj in distinct_objects],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
