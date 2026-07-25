#!/usr/bin/env python3
"""Check exact ambient support survival under uniform endpoint thinning."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict
from pathlib import Path


def falling(n: int, k: int) -> int:
    out = 1
    for t in range(k):
        out *= n - t
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()
    data = json.loads(args.instance.read_text(encoding="utf-8"))

    Q = int(data["bank_size"])
    q = int(data["subbank_size"])
    unary = [frozenset(map(int, e)) for e in data.get("unary_supports", [])]
    binary_by_rank: dict[int, list[frozenset[int]]] = defaultdict(list)
    for raw in data.get("binary_supports", []):
        support = frozenset(map(int, raw))
        h = len(support)
        if h not in (2, 3, 4):
            raise ValueError("binary supports must have rank 2, 3, or 4")
        binary_by_rank[h].append(support)

    for support in unary:
        if len(support) != 2:
            raise ValueError("unary support must use two endpoint indices")
    all_supports = unary + [
        s for h in (2, 3, 4) for s in binary_by_rank[h]
    ]
    if any(not all(0 <= x < Q for x in s) for s in all_supports):
        raise ValueError("support index out of range")

    subsets = list(itertools.combinations(range(Q), q))
    subsets_containing = {
        i: [set(I) for I in subsets if i in I] for i in range(Q)
    }

    def ambient_degree(family, i):
        return sum(i in s for s in family)

    checks = {}
    families = {1: unary, **binary_by_rank}
    for rank, family in families.items():
        h = 2 if rank == 1 else rank
        factor = falling(q - 1, h - 1) / falling(Q - 1, h - 1)
        max_error = 0.0
        for i in range(Q):
            ambient = ambient_degree(family, i)
            values = [
                sum(s.issubset(I) and i in s for s in family)
                for I in subsets_containing[i]
            ]
            observed = sum(values) / len(values)
            expected = ambient * factor
            max_error = max(max_error, abs(observed - expected))
        if max_error > 1e-12:
            raise AssertionError(f"conditional survival mismatch at rank {rank}")
        checks[str(rank)] = {
            "support_count": len(family),
            "survival_factor": factor,
            "max_conditional_error": max_error,
        }

    best = None
    for tup in subsets:
        I = set(tup)
        unary_deg = [
            sum(s.issubset(I) and i in s for s in unary) for i in I
        ]
        binary_deg = []
        for i in I:
            degree = 0
            for h in (2, 3, 4):
                degree += sum(
                    s.issubset(I) and i in s for s in binary_by_rank[h]
                )
            binary_deg.append(degree)
        score = (
            max(unary_deg, default=0) / q
            + max(binary_deg, default=0) / (q * (q - 1))
        )
        candidate = {
            "subset": list(tup),
            "max_unary_degree": max(unary_deg, default=0),
            "max_binary_degree": max(binary_deg, default=0),
            "normalized_support_mass": score,
        }
        if best is None or score < best["normalized_support_mass"]:
            best = candidate

    result = {
        "bank_size": Q,
        "subbank_size": q,
        "conditional_survival_checks": checks,
        "best_subbank": best,
        "outcome": (
            "diffuse_support_subbank"
            if best and best["normalized_support_mass"] < 1 / 24
            else "finite_support_core"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
