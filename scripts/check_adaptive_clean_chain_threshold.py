#!/usr/bin/env python3
"""Check the adaptive clean-chain threshold and residual bound."""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable


Pair = tuple[int, int]


def parse_pairs(values: Iterable[Iterable[int]]) -> set[Pair]:
    result: set[Pair] = set()
    for raw in values:
        value = tuple(int(x) for x in raw)
        if len(value) != 2:
            raise ValueError("all forbidden entries must be pairs")
        result.add((value[0], value[1]))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    data = json.loads(args.instance.read_text(encoding="utf-8"))
    n = int(data["n"])
    centre = int(data["centre"])
    epsilon = float(data["epsilon"])
    if n < 6:
        raise ValueError("n must be at least 6")
    if not 0 <= centre < n:
        raise ValueError("invalid centre")
    if not 0 <= epsilon <= 1:
        raise ValueError("epsilon must lie in [0,1]")

    left = parse_pairs(data.get("forbidden_left", []))
    middle = parse_pairs(data.get("forbidden_middle", []))
    right = parse_pairs(data.get("forbidden_right", []))
    vertices = [v for v in range(n) if v != centre]

    middle_count = sum(
        1 for p in vertices for s in vertices
        if p != s and (p, s) in middle
    )
    alpha = max(
        epsilon ** 0.125,
        math.sqrt(2.0 * (middle_count + n)) / n,
        4.0 / n,
    )
    q = min(n - 2, math.ceil(alpha * n))

    safe_left = {
        p: {r for r in vertices if r != p and (r, p) not in left}
        for p in vertices
    }
    safe_right = {
        s: {t for t in vertices if t != s and (s, t) not in right}
        for s in vertices
    }
    p_set = {p for p in vertices if len(safe_left[p]) >= q}
    s_set = {s for s in vertices if len(safe_right[s]) >= q}

    clean = []
    for r, p, s, t in itertools.permutations(vertices, 4):
        if (r, p) in left or (p, s) in middle or (s, t) in right:
            continue
        clean.append((r, p, s, t))

    total_chains = falling(n - 1, 4)
    density = len(clean) / total_chains
    density_bound = math.sqrt(epsilon) / 32.0
    residual_bound = epsilon / density if density > 0 else math.inf

    pred_star = len(p_set) < q
    succ_star = len(s_set) < q

    if not pred_star and not succ_star:
        if q * q < 2 * (middle_count + n):
            raise AssertionError("adaptive threshold does not dominate middle")
        if len(clean) < q ** 4 / 16:
            raise AssertionError("clean-chain q^4/16 bound failed")
        if density + 1e-12 < density_bound:
            raise AssertionError("density lower bound failed")
        if residual_bound > 32.0 * math.sqrt(epsilon) + 1e-12:
            raise AssertionError("inverse-density residual bound failed")
        outcome = "adaptive_clean_bank"
    elif pred_star:
        outcome = "predecessor_role_star"
    else:
        outcome = "successor_role_star"

    result = {
        "n": n,
        "centre": centre,
        "epsilon": epsilon,
        "middle_forbidden_count": middle_count,
        "alpha": alpha,
        "q": q,
        "P_q_size": len(p_set),
        "S_q_size": len(s_set),
        "clean_chain_count": len(clean),
        "total_chain_count": total_chains,
        "clean_density": density,
        "density_lower_bound": density_bound,
        "conditioned_residual_upper_bound": residual_bound,
        "theorem_residual_upper_bound": 32.0 * math.sqrt(epsilon),
        "outcome": outcome,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


def falling(n: int, k: int) -> int:
    value = 1
    for offset in range(k):
        value *= n - offset
    return value


if __name__ == "__main__":
    main()
