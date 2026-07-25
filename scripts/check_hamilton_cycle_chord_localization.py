#!/usr/bin/env python3
"""Check the sparse-hub / dense chord-star-or-matching localization."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


def successor_path(n: int, start: int, end: int) -> list[int]:
    path = [start]
    current = start
    while current != end:
        current = (current + 1) % n
        if current in path:
            raise ValueError("failed to reach endpoint on successor cycle")
        path.append(current)
    return path


def maximal_chord_matching(chords: list[tuple[int, int]]) -> list[tuple[int, int]]:
    used_tails: set[int] = set()
    used_heads: set[int] = set()
    matching: list[tuple[int, int]] = []
    for tail, head in chords:
        if tail not in used_tails and head not in used_heads:
            matching.append((tail, head))
            used_tails.add(tail)
            used_heads.add(head)
    return matching


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    n = int(data["cycle_length"])
    chords = [tuple(map(int, edge)) for edge in data["chords"]]
    dense_edge_threshold = int(data.get("dense_edge_threshold", n))
    if n < 4:
        raise ValueError("cycle_length must be at least four")
    if len(set(chords)) != len(chords):
        raise ValueError("duplicate chords")
    for tail, head in chords:
        if not (0 <= tail < n and 0 <= head < n):
            raise ValueError("chord endpoint outside cycle")
        if tail == head:
            raise ValueError("loops are reference edges, not chords")
        if head == (tail + 1) % n:
            raise ValueError("Hamilton successor arcs are not chords")

    tail_degree = Counter(tail for tail, _ in chords)
    head_degree = Counter(head for _, head in chords)
    max_tail = max(tail_degree.values(), default=0)
    max_head = max(head_degree.values(), default=0)
    max_degree = max(max_tail, max_head)
    rich_side = "tail" if max_tail >= max_head else "head"
    rich_vertex = (
        max(tail_degree, key=tail_degree.get)
        if rich_side == "tail" and tail_degree
        else max(head_degree, key=head_degree.get)
        if head_degree
        else None
    )

    matching = maximal_chord_matching(chords)
    e = len(chords)
    delta = max(1, math.ceil(math.sqrt(e)))
    endpoints = {vertex for edge in chords for vertex in edge}
    feedback_hub = set(endpoints)
    feedback_hub.add(0)
    canonical_lengths = {
        f"{tail}->{head}": len(successor_path(n, head, tail))
        for tail, head in chords
    }

    if e < dense_edge_threshold:
        outcome = "sparse_chord_feedback_hub"
    elif max_degree >= delta:
        outcome = "rich_chord_cycle_star"
    else:
        outcome = "distinct_signature_chord_cycle_bank"

    matching_lower_bound = e / (2 * delta) if delta else 0.0
    if e >= dense_edge_threshold and max_degree < delta and len(matching) < matching_lower_bound:
        raise AssertionError("greedy matching missed the maximal-matching lower bound")

    return {
        "cycle_length": n,
        "chord_count": e,
        "dense_edge_threshold": dense_edge_threshold,
        "sqrt_threshold": delta,
        "maximum_tail_degree": max_tail,
        "maximum_head_degree": max_head,
        "maximum_chord_degree": max_degree,
        "rich_side": rich_side,
        "rich_vertex": rich_vertex,
        "maximal_distinct_signature_matching_size": len(matching),
        "matching_lower_bound": matching_lower_bound,
        "matching_chords": matching,
        "sparse_feedback_hub_size_bound": 2 * e + 1,
        "constructed_feedback_hub_size": len(feedback_hub),
        "canonical_cycle_lengths": canonical_lengths,
        "outcome": outcome,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    with args.input.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    print(json.dumps(analyse(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
