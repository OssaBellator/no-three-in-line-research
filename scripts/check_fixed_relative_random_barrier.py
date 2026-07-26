#!/usr/bin/env python3
"""Count exact random-permutation cylinders for fixed relative seed states.

For each JSON case {"n": ..., "pi": [...]}, pi is one-based. The checker
enumerates maximal nonaxis grid lines, their collinear triples, all eight layer
patterns, and the canonical permutation assignments induced by each pattern.
It reports the exact expected number of selected collinear triples for uniform
sigma and a row-image conflict lower bound for the natural canonical-event
permutation dependency graph.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from itertools import combinations, product
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def maximal_nonaxis_lines(n: int) -> list[tuple[Point, ...]]:
    lines: list[tuple[Point, ...]] = []
    for dx in range(1, n):
        for dy in range(-(n - 1), n):
            if dy == 0 or math.gcd(dx, abs(dy)) != 1:
                continue
            for x in range(n):
                for y in range(n):
                    if 0 <= x - dx < n and 0 <= y - dy < n:
                        continue
                    line: list[Point] = []
                    xx, yy = x, y
                    while 0 <= xx < n and 0 <= yy < n:
                        line.append((xx, yy))
                        xx += dx
                        yy += dy
                    if len(line) >= 3:
                        lines.append(tuple(line))
    return lines


def parse_case(raw: Any, ordinal: int) -> tuple[str, int, list[int]]:
    if not isinstance(raw, dict):
        raise ValueError(f"case {ordinal}: expected an object")
    n = raw.get("n")
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError(f"case {ordinal}: n must be an integer at least 3")
    label = str(raw.get("label", f"n={n}"))
    pi_raw = raw.get("pi")
    if not isinstance(pi_raw, list) or len(pi_raw) != n:
        raise ValueError(f"{label}: pi must have length n")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in pi_raw):
        raise ValueError(f"{label}: pi entries must be integers")
    if sorted(pi_raw) != list(range(1, n + 1)):
        raise ValueError(f"{label}: pi is not a one-based permutation")
    pi = [v - 1 for v in pi_raw]
    if any(pi[i] == i for i in range(n)):
        raise ValueError(f"{label}: pi is not a derangement")
    return label, n, pi


def analyse(label: str, n: int, pi: list[int]) -> dict[str, Any]:
    lines = maximal_nonaxis_lines(n)
    triple_count = 0
    admissible_patterns = 0
    row_load: Counter[int] = Counter()
    assignment_load: Counter[tuple[int, int]] = Counter()
    canonical_events: list[tuple[tuple[int, int], ...]] = []

    for line in lines:
        for triple in combinations(line, 3):
            xs = [p[0] for p in triple]
            rs = [p[1] for p in triple]
            if len(set(xs)) != 3 or len(set(rs)) != 3:
                raise ValueError(f"{label}: nonaxis triple lacks distinct rows/columns")
            triple_count += 1
            local_patterns = 0
            for bits in product((0, 1), repeat=3):
                domains = [pi[x] if bit else x for x, bit in zip(xs, bits)]
                if len(set(domains)) != 3:
                    continue
                assignments = tuple(sorted(zip(domains, rs)))
                canonical_events.append(assignments)
                local_patterns += 1
                for z, r in assignments:
                    row_load[r] += 1
                    assignment_load[(z, r)] += 1
            if not 1 <= local_patterns <= 8:
                raise ValueError(f"{label}: invalid layer-pattern count {local_patterns}")
            admissible_patterns += local_patterns

    denominator = n * (n - 1) * (n - 2)
    expected = admissible_patterns / denominator
    lower = triple_count / denominator
    upper = 8 * triple_count / denominator
    if not (lower <= expected <= upper):
        raise ValueError(f"{label}: expectation outside exact cylinder bounds")

    conflict_lower = 0
    witness: tuple[int, int] | None = None
    for event in canonical_events:
        for z, r in event:
            value = row_load[r] - assignment_load[(z, r)]
            if value > conflict_lower:
                conflict_lower = value
                witness = (z, r)
    symmetric_lll_lower = math.e * conflict_lower / denominator

    return {
        "label": label,
        "n": n,
        "maximal_nonaxis_lines": len(lines),
        "collinear_nonaxis_triples": triple_count,
        "admissible_labelled_patterns": admissible_patterns,
        "permutation_denominator": denominator,
        "expected_bad_triples": expected,
        "expectation_lower": lower,
        "expectation_upper": upper,
        "row_conflict_degree_lower_bound": conflict_lower,
        "conflict_witness_assignment": None if witness is None else [witness[0] + 1, witness[1] + 1],
        "symmetric_lll_left_side_lower_bound": symmetric_lll_lower,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        cases = payload if isinstance(payload, list) else [payload]
        results = [analyse(*parse_case(raw, i + 1)) for i, raw in enumerate(cases)]
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"verification failed: {exc}") from exc
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
