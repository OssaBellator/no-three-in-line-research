#!/usr/bin/env python3
"""Check the maximal-independent helper-core localization on finite hypergraphs."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
from typing import Any, Iterable


def contains_edge(vertices: set[int], edges: Iterable[frozenset[int]]) -> bool:
    return any(edge.issubset(vertices) for edge in edges)


def greedy_maximal_independent(N: int, edges: list[frozenset[int]]) -> set[int]:
    independent: set[int] = set()
    for v in range(N):
        trial = set(independent)
        trial.add(v)
        if not contains_edge(trial, edges):
            independent.add(v)
    return independent


def completion_core(
    N: int, independent: set[int], edges: list[frozenset[int]], k0: int
) -> tuple[frozenset[int], int, int]:
    counts: Counter[frozenset[int]] = Counter()
    outside = [v for v in range(N) if v not in independent]
    for v in outside:
        records = [
            edge - {v}
            for edge in edges
            if v in edge and edge.issubset(independent | {v})
        ]
        if not records:
            raise AssertionError("independent set is not maximal")
        record = min(records, key=lambda x: (len(x), tuple(sorted(x))))
        if len(record) > k0 - 1:
            raise AssertionError("completion core exceeds support-rank bound")
        counts[record] += 1
    core, degree = counts.most_common(1)[0]
    possible_records = sum(comb(len(independent), r) for r in range(k0))
    return core, degree, possible_records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    data: dict[str, Any] = json.loads(args.input.read_text())

    N = int(data["N"])
    b = int(data["b"])
    k0 = int(data["k0"])

    dense_edges = [frozenset(edge) for edge in combinations(range(N), k0)]
    dense_I = greedy_maximal_independent(N, dense_edges)
    if len(dense_I) >= b - 1:
        raise AssertionError("complete hypergraph should enter the core branch")
    core, degree, records = completion_core(N, dense_I, dense_edges, k0)
    lower = (N - 1 - len(dense_I)) / records
    theorem_lower = (N - b) / sum(comb(b - 2, r) for r in range(k0))
    if degree + 1e-12 < lower or degree + 1e-12 < theorem_lower:
        raise AssertionError("fixed-core degree below theorem bound")

    sparse_edges = [
        frozenset(range(start, min(start + k0, N)))
        for start in range(0, N - k0 + 1, k0)
    ]
    sparse_I = greedy_maximal_independent(N, sparse_edges)
    if len(sparse_I) < b - 1:
        raise AssertionError("sparse support should admit the required helper set")
    sparse_host = sorted(sparse_I)[: b - 1]
    if contains_edge(set(sparse_host), sparse_edges):
        raise AssertionError("stored sparse helper host is not support-independent")

    print(f"N {N}")
    print(f"b {b}")
    print(f"maximum support rank {k0}")
    print(f"dense complete supports {len(dense_edges)}")
    print(f"dense maximal independent size {len(dense_I)}")
    print(f"dense fixed core {sorted(core)}")
    print(f"dense fixed core size {len(core)}")
    print(f"dense extension degree {degree}")
    print(f"completion record count {records}")
    print(f"exact pigeonhole lower bound {lower:.12f}")
    print(f"required-size theorem lower bound {theorem_lower:.12f}")
    print(f"sparse disjoint supports {len(sparse_edges)}")
    print(f"sparse maximal independent size {len(sparse_I)}")
    print(f"support-free helper host {sparse_host}")
    print("outcome support_free_host_or_fixed_core_pencil")


if __name__ == "__main__":
    main()
