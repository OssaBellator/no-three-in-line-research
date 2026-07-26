#!/usr/bin/env python3
"""Finite diagnostic for PP3arr--PP3aru."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_critical_square_root_helper_host.py EXAMPLE.json")

    data = load(sys.argv[1])
    w = int(data["W"])
    n = int(data["N"])
    if n != w * w:
        raise AssertionError("stored example requires N=W^2")

    # Rank-two obstruction: partition into W-1 cliques.  An independent set takes
    # at most one vertex per clique, so its size is at most W-1.
    parts = w - 1
    sizes = [n // parts + (1 if i < n % parts else 0) for i in range(parts)]
    e2 = sum(math.comb(size, 2) for size in sizes)
    rank2_threshold = (n * (n - 1)) / (2 * w * (w - 1))
    max_degree = max(size - 1 for size in sizes)
    matching_size = sum(size // 2 for size in sizes)

    if e2 < rank2_threshold:
        raise AssertionError("rank-two density threshold failed")
    if max_degree < w and matching_size < w:
        raise AssertionError("star-or-matching extraction failed")

    # Rank-three obstruction: the complete 3-graph has independence number two.
    e3 = math.comb(n, 3)
    rank3_threshold = (n * (n - 1) * (n - 2)) / (2 * w * (w - 1) * (w - 2))
    fixed_pair_petals = n - 2
    if e3 < rank3_threshold:
        raise AssertionError("rank-three density threshold failed")
    if fixed_pair_petals < w:
        raise AssertionError("fixed-core petal extraction failed")

    # Independent branch: all stored supports lie in the tail, while the first W
    # helpers form the selected independent block.
    support_tail_start = int(data["support_tail_start"])
    chosen = set(range(w))
    stored_supports = [set(edge) for edge in data["independent_branch_supports"]]
    selected_supports = sum(1 for edge in stored_supports if edge <= chosen)
    if support_tail_start < w or selected_supports != 0:
        raise AssertionError("independent helper block is not support-free")

    print(f"W {w}")
    print(f"N {n}")
    print(f"independent chosen helpers {w}")
    print(f"independent selected supports {selected_supports}")
    print(f"rank-two clique parts {parts}")
    print(f"rank-two support edges {e2}")
    print(f"rank-two density threshold {rank2_threshold:.1f}")
    print(f"rank-two maximum degree {max_degree}")
    print(f"rank-two matching size {matching_size}")
    print(f"rank-three support edges {e3}")
    print(f"rank-three density threshold {rank3_threshold:.1f}")
    print(f"rank-three fixed-pair petals {fixed_pair_petals}")
    print("outcome critical_square_root_independent_or_target_support")


if __name__ == "__main__":
    main()
