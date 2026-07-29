#!/usr/bin/env python3
"""Verify PP3bwp--PP3bwr on a finite direct-clean action graph."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw = json.loads(args.input.read_text(encoding="utf-8"))
    neighborhoods_raw = raw.get("neighborhoods")
    if not isinstance(neighborhoods_raw, dict) or not neighborhoods_raw:
        raise SystemExit("check failed: neighborhoods must be a nonempty object")
    neighborhoods: dict[str, set[str]] = {}
    for source, targets in neighborhoods_raw.items():
        if not isinstance(source, str) or not isinstance(targets, list) or not targets:
            raise SystemExit("check failed: invalid source neighborhood")
        if any(not isinstance(target, str) for target in targets):
            raise SystemExit("check failed: target names must be strings")
        neighborhoods[source] = set(targets)

    sources = sorted(neighborhoods)
    degree = {source: len(neighborhoods[source]) for source in sources}
    codegree = {
        (x, y): len(neighborhoods[x] & neighborhoods[y])
        for x, y in combinations(sources, 2)
    }
    codegree_load = {
        x: sum(value for pair, value in codegree.items() if x in pair) for x in sources
    }
    d = min(degree.values())
    load_cap = max(codegree_load.values())
    sparse_bound = Fraction(d + load_cap, d * d)

    exact_lambda = Fraction(0)
    second_moment_bound = Fraction(0)
    subset_rows = []
    for size in range(1, len(sources) + 1):
        for subset in combinations(sources, size):
            union = set().union(*(neighborhoods[x] for x in subset))
            exact_ratio = Fraction(size, len(union))
            exact_lambda = max(exact_lambda, exact_ratio)
            total_degree = sum(degree[x] for x in subset)
            pair_sum = sum(codegree[pair] for pair in combinations(subset, 2))
            moment_ratio = Fraction(size * (total_degree + 2 * pair_sum), total_degree**2)
            second_moment_bound = max(second_moment_bound, moment_ratio)
            assert exact_ratio <= moment_ratio
            subset_rows.append(
                {
                    "sources": subset,
                    "exact_ratio": str(exact_ratio),
                    "second_moment_bound": str(moment_ratio),
                }
            )

    assert exact_lambda <= second_moment_bound <= sparse_bound < 1
    print(
        json.dumps(
            {
                "minimum_degree": d,
                "maximum_total_codegree_load": load_cap,
                "exact_fractional_reverse_load": str(exact_lambda),
                "maximum_second_moment_bound": str(second_moment_bound),
                "sparse_codegree_bound": str(sparse_bound),
                "subsets": subset_rows,
                "all_checks_passed": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
