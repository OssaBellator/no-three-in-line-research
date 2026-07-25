#!/usr/bin/env python3
"""Verify uniform five-chain fibres and inverse-density averaging."""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("instance", type=Path)
    args = parser.parse_args()

    data = json.loads(args.instance.read_text(encoding="utf-8"))
    n = int(data["n"])
    b = int(data["b"])
    centre = int(data["centre"])
    cost_arc = tuple(int(x) for x in data["cost_arc"])
    clean_rule = str(data.get("clean_rule", "r_lt_t"))

    if not 5 <= b <= n:
        raise ValueError("require 5 <= b <= n")
    if not 0 <= centre < n:
        raise ValueError("invalid centre")
    if len(cost_arc) != 2:
        raise ValueError("cost_arc must have two endpoints")

    others = [v for v in range(n) if v != centre]
    records: list[tuple[tuple[int, int, int, int], int]] = []

    for subset in itertools.combinations(others, b - 1):
        for order_after_c in itertools.permutations(subset):
            order = (centre,) + order_after_c
            arcs = {
                (order[i], order[(i + 1) % b])
                for i in range(b)
            }
            h = (
                order_after_c[-2],
                order_after_c[-1],
                order_after_c[0],
                order_after_c[1],
            )
            records.append((h, int(cost_arc in arcs)))

    fibre_counts = Counter(h for h, _ in records)
    expected_fibre = (
        math_comb(n - 5, b - 5) * math_factorial(b - 5)
    )
    if not fibre_counts:
        raise AssertionError("no local chains found")
    if min(fibre_counts.values()) != expected_fibre:
        raise AssertionError("minimum fibre size is incorrect")
    if max(fibre_counts.values()) != expected_fibre:
        raise AssertionError("maximum fibre size is incorrect")

    all_chains = sorted(fibre_counts)
    if clean_rule == "r_lt_t":
        clean = {h for h in all_chains if h[0] < h[3]}
    elif clean_rule == "p_lt_s":
        clean = {h for h in all_chains if h[1] < h[2]}
    elif clean_rule == "all":
        clean = set(all_chains)
    else:
        raise ValueError(f"unknown clean_rule {clean_rule!r}")

    if not clean:
        raise AssertionError("clean family is empty")

    total_states = len(records)
    clean_records = [(h, x) for h, x in records if h in clean]
    density = len(clean) / len(all_chains)
    full_expectation = sum(x for _, x in records) / total_states
    clean_expectation = (
        sum(x for _, x in clean_records) / len(clean_records)
    )
    bound = full_expectation / density

    if clean_expectation > bound + 1e-12:
        raise AssertionError("inverse-density inequality failed")

    result = {
        "n": n,
        "b": b,
        "centre": centre,
        "total_states": total_states,
        "local_chain_count": len(all_chains),
        "expected_fibre_size": expected_fibre,
        "minimum_fibre_size": min(fibre_counts.values()),
        "maximum_fibre_size": max(fibre_counts.values()),
        "clean_chain_count": len(clean),
        "clean_density": density,
        "full_objective_expectation": full_expectation,
        "clean_objective_expectation": clean_expectation,
        "inverse_density_bound": bound,
        "outcome": "inverse_density_verified",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


def math_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result


def math_factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


if __name__ == "__main__":
    main()
