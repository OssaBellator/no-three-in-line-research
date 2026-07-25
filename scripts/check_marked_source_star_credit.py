#!/usr/bin/env python3
"""Finite diagnostic for marked source-star credit amortisation."""
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def derangements(items: tuple[int, ...]) -> Iterable[dict[int, int]]:
    for perm in itertools.permutations(items):
        if all(i != j for i, j in zip(items, perm)):
            yield dict(zip(items, perm))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())

    Q = int(data["ambient_size"])
    q = int(data["subbank_size"])
    centre = int(data["centre"])
    traces = [
        [(int(k), int(l)) for k, l in trace]
        for trace in data["credit_line_traces"]
    ]
    foreign_cost = Fraction(str(data.get("foreign_cost_per_state", 0)))

    if not 3 <= q <= Q:
        raise ValueError("require 3 <= subbank_size <= ambient_size")
    if not 0 <= centre < Q:
        raise ValueError("centre outside ambient index set")

    universe = tuple(range(Q))
    others = tuple(i for i in universe if i != centre)

    for trace in traces:
        seen_left: set[int] = set()
        seen_right: set[int] = set()
        for k, l in trace:
            if k == l or k == centre or l == centre:
                raise ValueError("trace entries must be off-diagonal and avoid centre")
            if k in seen_left or l in seen_right:
                raise ValueError("each credit-line trace must be a partial matching")
            seen_left.add(k)
            seen_right.add(l)

    total_states = 0
    total_self = 0
    best_delta: Fraction | None = None
    best_state = None
    credit = len(traces)

    for tail in itertools.combinations(others, q - 1):
        bank = (centre,) + tail
        bank_set = set(bank)
        for sigma in derangements(bank):
            total_states += 1
            self_cost = 0
            for trace in traces:
                self_cost += sum(
                    1
                    for k, l in trace
                    if k in bank_set and l in bank_set and sigma[k] == l
                )
            total_self += self_cost
            delta = Fraction(self_cost, 1) + foreign_cost - credit
            if best_delta is None or delta < best_delta:
                best_delta = delta
                best_state = {
                    "bank": list(bank),
                    "permutation": sigma,
                    "self_cost": self_cost,
                }

    if total_states == 0 or best_delta is None:
        raise RuntimeError("no marked derangement state was generated")

    exact_average = Fraction(total_self, total_states)
    theorem_bound = Fraction(credit * (q - 2), Q - 2)
    if exact_average > theorem_bound:
        raise AssertionError("exact average exceeds PP3agj bound")

    outcome = "paid_completion" if best_delta < 0 else "foreign_or_host_obstruction"
    print(
        json.dumps(
            {
                "ambient_size": Q,
                "subbank_size": q,
                "credit_lines": credit,
                "states": total_states,
                "average_self_recapture": str(exact_average),
                "theorem_bound": str(theorem_bound),
                "best_potential_change": str(best_delta),
                "best_state": best_state,
                "outcome": outcome,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
