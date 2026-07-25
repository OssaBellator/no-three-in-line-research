#!/usr/bin/env python3
"""Check the source-clean five-chain supply dichotomy."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable


Pair = tuple[int, int]


def parse_pairs(values: Iterable[Iterable[int]]) -> set[Pair]:
    result: set[Pair] = set()
    for value in values:
        pair = tuple(int(x) for x in value)
        if len(pair) != 2:
            raise ValueError(f"expected a pair, got {value!r}")
        result.add((pair[0], pair[1]))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    data = json.loads(args.instance.read_text(encoding="utf-8"))
    n = int(data["n"])
    centre = int(data["centre"])
    q = int(data["q"])
    if n < 5:
        raise ValueError("n must be at least 5")
    if not 0 <= centre < n:
        raise ValueError("centre must be an endpoint index")
    if q < 3:
        raise ValueError("q must be at least 3")

    left = parse_pairs(data.get("forbidden_left", []))
    middle = parse_pairs(data.get("forbidden_middle", []))
    right = parse_pairs(data.get("forbidden_right", []))

    vertices = [v for v in range(n) if v != centre]

    safe_left: dict[int, set[int]] = {}
    safe_right: dict[int, set[int]] = {}
    for p in vertices:
        safe_left[p] = {
            r for r in vertices if r != p and (r, p) not in left
        }
    for s in vertices:
        safe_right[s] = {
            t for t in vertices if t != s and (s, t) not in right
        }

    p_set = {p for p in vertices if len(safe_left[p]) >= q}
    s_set = {s for s in vertices if len(safe_right[s]) >= q}

    clean_chains: list[tuple[int, int, int, int]] = []
    for r, p, s, t in itertools.permutations(vertices, 4):
        if (r, p) in left:
            continue
        if (p, s) in middle:
            continue
        if (s, t) in right:
            continue
        clean_chains.append((r, p, s, t))

    middle_count = sum(
        1 for p in vertices for s in vertices
        if p != s and (p, s) in middle
    )
    clean_middle_lower = max(0, len(p_set) * len(s_set) - middle_count - n)
    lower_bound = clean_middle_lower * (q - 1) * (q - 2)
    if len(clean_chains) < lower_bound:
        raise AssertionError(
            f"clean-chain count {len(clean_chains)} is below {lower_bound}"
        )

    pred_star = len(p_set) < q
    succ_star = len(s_set) < q
    middle_saturation = middle_count + n >= q * q

    pred_min = min(
        (sum(1 for r in vertices if r != p and (r, p) in left)
         for p in vertices if p not in p_set),
        default=None,
    )
    succ_min = min(
        (sum(1 for t in vertices if t != s and (s, t) in right)
         for s in vertices if s not in s_set),
        default=None,
    )

    if pred_star and pred_min is not None and pred_min < n - q - 1:
        raise AssertionError("predecessor-star degree bound failed")
    if succ_star and succ_min is not None and succ_min < n - q - 1:
        raise AssertionError("successor-star degree bound failed")

    if lower_bound > 0:
        outcome = "clean_five_chain_bank"
    elif pred_star:
        outcome = "predecessor_role_star"
    elif succ_star:
        outcome = "successor_role_star"
    elif middle_saturation:
        outcome = "middle_saturation"
    else:
        raise AssertionError("no theorem branch detected")

    result = {
        "n": n,
        "centre": centre,
        "q": q,
        "P_q_size": len(p_set),
        "S_q_size": len(s_set),
        "middle_forbidden_count": middle_count,
        "clean_chain_count": len(clean_chains),
        "proved_lower_bound": lower_bound,
        "predecessor_exception_count": len(p_set),
        "successor_exception_count": len(s_set),
        "predecessor_star_min_degree": pred_min,
        "successor_star_min_degree": succ_min,
        "outcome": outcome,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
