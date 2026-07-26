#!/usr/bin/env python3
"""Check ambient unary positive-support avoidance and witness extraction."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(message)


def greedy_matching(edges: list[tuple[int, int]]) -> int:
    used: set[int] = set()
    size = 0
    for a, b in edges:
        if a not in used and b not in used:
            used.add(a)
            used.add(b)
            size += 1
    return size


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_ambient_unary_positive_support.py INSTANCE.json")

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    Q = int(data["Q"])
    q = int(data["q"])
    tau = float(data["tau"])
    S1 = int(data["positive_signatures"])
    n = int(data["witness_cycle_vertices"])

    if Q < 3 or not 2 <= q <= Q or not 0 < tau < 1:
        fail("invalid Q, q, or tau")
    if S1 < 0 or n < 3:
        fail("invalid support or witness size")

    p1 = 1 / (Q - 1)
    support_expectation = p1 * S1
    density_threshold = tau * (Q - 1)

    witness_edges = [(i, (i + 1) % n) for i in range(n)]
    degrees = [0] * n
    for a, b in witness_edges:
        degrees[a] += 1
        degrees[b] += 1
    max_degree = max(degrees)
    matching_size = greedy_matching(witness_edges)
    D = math.ceil(math.sqrt(S1)) if S1 else 1
    matching_lower_bound = S1 / (2 * D)
    one_layer_bank = matching_size // 2

    if support_expectation <= tau:
        fail("stored example should fail the unary support-avoidance threshold")
    if S1 < density_threshold:
        fail("avoidance failure did not force the unary density lower bound")
    if max_degree < D and matching_size + 1e-9 < matching_lower_bound:
        fail("witness star/matching decomposition failed")
    if q**3 >= Q:
        fail("stored example should satisfy q^3<Q")
    if one_layer_bank <= q:
        fail("stored one-layer bank should exceed the selected state size")

    outcome = (
        "source_star"
        if max_degree >= D
        else "one_layer_credited_witness_bank"
    )

    print(f"Q {Q}")
    print(f"q {q}")
    print(f"tau {tau}")
    print(f"p1 {p1:.12f}")
    print(f"positive signatures {S1}")
    print(f"support expectation {support_expectation:.12f}")
    print(f"density threshold {density_threshold:.3f}")
    print(f"witness maximum degree {max_degree}")
    print(f"sqrt threshold {D}")
    print(f"greedy witness matching {matching_size}")
    print(f"matching lower bound {matching_lower_bound:.3f}")
    print(f"one-layer endpoint bank {one_layer_bank}")
    print(f"q^3/Q {q**3 / Q:.6f}")
    print(f"outcome {outcome}")


if __name__ == "__main__":
    main()
