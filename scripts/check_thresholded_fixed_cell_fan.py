#!/usr/bin/env python3
"""Finite diagnostic for thresholded fixed-cell binary fans."""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


def perfect_matchings(n: int, allowed: set[tuple[int, int]]):
    for perm in itertools.permutations(range(n)):
        edges = [(i, perm[i]) for i in range(n)]
        if all(edge in allowed for edge in edges):
            yield edges


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    n = int(data["residual_size"])
    credit = Fraction(str(data["removal_credit"]))
    tau = Fraction(str(data["slack_fraction"]))
    if n <= 0 or credit <= 0 or not Fraction(0) < tau <= 1:
        raise ValueError("invalid residual size, credit, or slack fraction")

    weights = {
        (int(i), int(j)): Fraction(str(weight))
        for i, j, weight in data["partner_weights"]
    }
    host = {(i, j) for i in range(n) for j in range(n)}
    for edge, weight in weights.items():
        if edge not in host:
            raise ValueError(f"weight edge outside host: {edge}")
        if weight < 0:
            raise ValueError("partner weights must be nonnegative")

    threshold = tau * credit / (2 * n)
    heavy = {edge for edge in host if weights.get(edge, Fraction(0)) > threshold}
    light_host = host - heavy
    matchings = list(perfect_matchings(n, light_host))

    row_degree = [sum((i, j) in heavy for j in range(n)) for i in range(n)]
    col_degree = [sum((i, j) in heavy for i in range(n)) for j in range(n)]
    max_heavy_degree = max(row_degree + col_degree, default=0)

    if matchings:
        costs = [sum(weights.get(edge, Fraction(0)) for edge in matching) for matching in matchings]
        best_cost = min(costs)
        if best_cost > tau * credit / 2:
            raise AssertionError("light matching cost exceeds PP3ago budget")
        outcome = "paid_light_completion"
        best_matching = matchings[costs.index(best_cost)]
    else:
        best_cost = None
        best_matching = None
        outcome = "heavy_hall_star"

    print(
        json.dumps(
            {
                "residual_size": n,
                "removal_credit": str(credit),
                "slack_fraction": str(tau),
                "heavy_threshold": str(threshold),
                "heavy_edges": len(heavy),
                "max_heavy_degree": max_heavy_degree,
                "light_matchings": len(matchings),
                "best_light_cost": None if best_cost is None else str(best_cost),
                "best_matching": best_matching,
                "outcome": outcome,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
