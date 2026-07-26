#!/usr/bin/env python3
"""Check ambient rank-three/rank-four positive-support link bounds."""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(message)


def greedy_graph_matching(edges: list[tuple[int, int]]) -> int:
    used: set[int] = set()
    size = 0
    for a, b in edges:
        if a not in used and b not in used:
            used.add(a)
            used.add(b)
            size += 1
    return size


def greedy_triple_matching(edges: list[tuple[int, int, int]]) -> int:
    used: set[int] = set()
    size = 0
    for edge in edges:
        if all(v not in used for v in edge):
            used.update(edge)
            size += 1
    return size


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: check_ambient_binary_link_decomposition.py INSTANCE.json")

    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    Q = int(data["Q"])
    q = int(data["q"])
    tau = float(data["tau"])
    n3 = int(data["rank3_vertices"])
    n4 = int(data["rank4_vertices"])

    if Q < 5 or not 4 <= q <= Q or not 0 < tau < 1:
        fail("invalid Q, q, or tau")
    if n3 > Q - 1 or n4 > Q - 1:
        fail("link vertex counts exceed the conditioned ambient bank")

    rank3_edges = list(itertools.combinations(range(n3), 2))
    rank4_edges = list(itertools.combinations(range(n4), 3))
    S3 = len(rank3_edges)
    S4 = len(rank4_edges)

    p3 = 1 / ((Q - 1) * (Q - 2))
    p4 = (q - 3) / ((Q - 1) * (Q - 2) * (Q - 3))
    support_expectation = p3 * S3 + p4 * S4

    rank3_threshold = tau * (Q - 1) * (Q - 2) / 2
    rank4_threshold = tau * (Q - 1) * (Q - 2) * (Q - 3) / (2 * (q - 3))

    deg3 = [0] * n3
    for a, b in rank3_edges:
        deg3[a] += 1
        deg3[b] += 1
    max_deg3 = max(deg3, default=0)
    rank3_matching = greedy_graph_matching(rank3_edges)

    deg4 = [0] * n4
    for edge in rank4_edges:
        for v in edge:
            deg4[v] += 1
    max_deg4 = max(deg4, default=0)
    hyper_D = math.ceil(S4 ** (2 / 3))
    triple_matching = greedy_triple_matching(rank4_edges)

    if not rank4_edges:
        fail("rank-four example must be nonempty")
    center = max(range(n4), key=deg4.__getitem__)
    graph_link = [tuple(v for v in edge if v != center) for edge in rank4_edges if center in edge]
    link_deg = [0] * n4
    for a, b in graph_link:
        link_deg[a] += 1
        link_deg[b] += 1
    max_link_deg = max(link_deg, default=0)
    nested_threshold = math.ceil(S4 ** (1 / 3))
    graph_link_matching = greedy_graph_matching(graph_link)

    if support_expectation <= tau:
        fail("stored example should fail the positive-support avoidance threshold")
    if S3 < rank3_threshold and S4 < rank4_threshold:
        fail("avoidance failure did not force either support lower bound")
    if max_deg3 < 1 and rank3_matching < 1:
        fail("rank-three star/matching decomposition failed")
    if max_deg4 < hyper_D and triple_matching < S4 / (3 * hyper_D) - 1e-9:
        fail("rank-four hypergraph decomposition failed")
    if max_deg4 >= hyper_D:
        if max_link_deg < nested_threshold and graph_link_matching < len(graph_link) / (2 * nested_threshold) - 1e-9:
            fail("nested rank-four graph-link decomposition failed")

    rank4_outcome = (
        "fixed_two_partner_pencil"
        if max_deg4 >= hyper_D and max_link_deg >= nested_threshold
        else "fixed_partner_pair_matching"
        if max_deg4 >= hyper_D
        else "vertex_disjoint_triple_bank"
    )

    print(f"Q {Q}")
    print(f"q {q}")
    print(f"tau {tau}")
    print(f"p3 {p3:.12f}")
    print(f"p4 {p4:.12f}")
    print(f"rank3 signatures {S3}")
    print(f"rank4 signatures {S4}")
    print(f"positive-support expectation {support_expectation:.12f}")
    print(f"rank3 lower threshold {rank3_threshold:.3f}")
    print(f"rank4 lower threshold {rank4_threshold:.3f}")
    print(f"rank3 maximum degree {max_deg3}")
    print(f"rank3 greedy matching {rank3_matching}")
    print(f"rank4 maximum vertex degree {max_deg4}")
    print(f"rank4 hypergraph threshold {hyper_D}")
    print(f"rank4 greedy triple matching {triple_matching}")
    print(f"nested graph-link edges {len(graph_link)}")
    print(f"nested graph maximum degree {max_link_deg}")
    print(f"nested threshold {nested_threshold}")
    print(f"nested graph matching {graph_link_matching}")
    print(f"rank4 outcome {rank4_outcome}")
    print("outcome ambient_binary_positive_support_localized")


if __name__ == "__main__":
    main()
