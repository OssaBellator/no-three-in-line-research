#!/usr/bin/env python3
"""Check marked high-support source probabilities and recursive link localization."""

from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(message)


def falling(n: int, r: int) -> int:
    out = 1
    for j in range(r):
        out *= n - j
    return out


def greedy_matching(edges: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    used: set[int] = set()
    chosen: list[tuple[int, ...]] = []
    for edge in edges:
        if all(v not in used for v in edge):
            chosen.append(edge)
            used.update(edge)
    return chosen


def decompose(edges: list[tuple[int, ...]], k: int) -> tuple[list[int], list[tuple[int, ...]]]:
    """Return a fixed core and pairwise-disjoint residual petals."""
    if not edges:
        return [], []
    if k == 1:
        return [], edges

    E = len(edges)
    threshold = math.ceil(E ** ((k - 1) / k))
    degrees = Counter(v for edge in edges for v in edge)
    vertex, max_degree = max(degrees.items(), key=lambda item: item[1])

    if max_degree >= threshold:
        link = [tuple(v for v in edge if v != vertex) for edge in edges if vertex in edge]
        core, petals = decompose(link, k - 1)
        return [vertex, *core], petals

    return [], greedy_matching(edges)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_marked_high_support_source.py INSTANCE.json")

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    N = int(data["N"])
    b = int(data["b"])
    tau = float(data["tau"])
    n = int(data["link_vertices"])

    if N < 7 or not 6 <= b <= N or not 0 < tau < 1:
        fail("invalid N, b, or tau")
    if n > N - 1 or n < 5:
        fail("invalid link vertex count")

    p_P = (b - 3) / falling(N - 1, 3)
    p_4 = 1 / falling(N - 1, 3)
    p_5 = (b - 4) / falling(N - 1, 4)
    p_6 = (b - 4) * (b - 5) / falling(N - 1, 5)

    links = {
        "anchored_pair": list(itertools.combinations(range(n), 3)),
        "rank4_triple": list(itertools.combinations(range(n), 3)),
        "rank5_triple": list(itertools.combinations(range(n), 4)),
        "rank6_triple": list(itertools.combinations(range(n), 5)),
    }
    probabilities = {
        "anchored_pair": p_P,
        "rank4_triple": p_4,
        "rank5_triple": p_5,
        "rank6_triple": p_6,
    }
    thresholds = {
        "anchored_pair": tau * falling(N - 1, 3) / (4 * (b - 3)),
        "rank4_triple": tau * falling(N - 1, 3) / 4,
        "rank5_triple": tau * falling(N - 1, 4) / (4 * (b - 4)),
        "rank6_triple": tau * falling(N - 1, 5) / (4 * (b - 4) * (b - 5)),
    }

    total_expectation = sum(probabilities[name] * len(edges) for name, edges in links.items())
    if total_expectation <= tau:
        fail("stored instance should fail the combined support-avoidance threshold")

    print(f"N {N}")
    print(f"b {b}")
    print(f"tau {tau}")
    print(f"p_P {p_P:.12f}")
    print(f"p_4 {p_4:.12f}")
    print(f"p_5 {p_5:.12f}")
    print(f"p_6 {p_6:.12f}")
    print(f"combined support expectation {total_expectation:.12f}")

    for name, edges in links.items():
        k = len(edges[0])
        E = len(edges)
        core, petals = decompose(edges, k)
        lower_bound = E ** (1 / k) / math.factorial(k)
        if len(petals) + 1e-9 < lower_bound:
            fail(f"recursive sunflower bound failed for {name}")
        if any(set(a) & set(b) for i, a in enumerate(petals) for b in petals[i + 1 :]):
            fail(f"petals are not pairwise disjoint for {name}")
        if E + 1e-9 < thresholds[name]:
            fail(f"stored {name} link is below its density threshold")

        print(f"{name} signatures {E}")
        print(f"{name} density threshold {thresholds[name]:.3f}")
        print(f"{name} fixed core size {len(core)}")
        print(f"{name} petal count {len(petals)}")
        print(f"{name} theorem lower bound {lower_bound:.3f}")

    print("outcome marked_high_support_source_sunflowers")


if __name__ == "__main__":
    main()
