#!/usr/bin/env python3
"""Finite diagnostic for PP3ase--PP3asj."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_joint_local_constraint_fusion.py EXAMPLE.json")

    with Path(sys.argv[1]).open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    w = int(data["W"])
    n = int(data["N"])
    chosen = set(data["chosen_helpers"])
    if len(chosen) != w or n != w * w:
        raise AssertionError("stored example requires a W-set in N=W^2")

    family_supports: dict[str, list[set[int]]] = {
        name: [set(edge) for edge in supports]
        for name, supports in data["local_constraint_families"].items()
    }
    max_rank = max(len(edge) for supports in family_supports.values() for edge in supports)
    selected = {
        name: sum(1 for edge in supports if edge <= chosen)
        for name, supports in family_supports.items()
    }
    if max_rank > 3:
        raise AssertionError("joint local support rank exceeds three")
    if any(selected.values()):
        raise AssertionError("chosen helper block violates a fused local constraint")

    # Dense fused-failure model: W-1 cliques, with clique edges cyclically assigned
    # to three local constraint types.  Any independent set has size at most W-1.
    parts = w - 1
    sizes = [n // parts + (1 if i < n % parts else 0) for i in range(parts)]
    types = ["source", "transition_anchor", "endpoint_arc"]
    edges_by_type = {name: 0 for name in types}
    for idx, size in enumerate(sizes):
        edges_by_type[types[idx % len(types)]] += math.comb(size, 2)

    total_edges = sum(edges_by_type.values())
    threshold = n * (n - 1) / (2 * w * (w - 1))
    concentrated_type = max(edges_by_type, key=edges_by_type.get)
    concentrated_edges = edges_by_type[concentrated_type]

    if total_edges < threshold:
        raise AssertionError("fused rank-two density threshold failed")
    if concentrated_edges < total_edges / len(types):
        raise AssertionError("finite type refinement failed")

    print(f"W {w}")
    print(f"N {n}")
    print(f"joint maximum support rank {max_rank}")
    print(f"chosen helper count {len(chosen)}")
    print(f"selected local constraints {sum(selected.values())}")
    print(f"dense fused clique parts {parts}")
    print(f"dense fused rank-two edges {total_edges}")
    print(f"rank-two density threshold {threshold:.1f}")
    print(f"concentrated constraint type {concentrated_type}")
    print(f"concentrated type edges {concentrated_edges}")
    print("outcome joint_local_constraints_independent_or_concentrated")


if __name__ == "__main__":
    main()
