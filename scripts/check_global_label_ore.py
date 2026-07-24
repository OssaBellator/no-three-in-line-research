#!/usr/bin/env python3
"""Check PP3gj--PP3gm for a finite family of macro compatibility graphs.

Input JSON schema::

    {
      "graphs": [
        [[0, 2], [1], ...],
        ...
      ],
      "ownership": [0, 0, 1, 1, ...]  # optional
    }

``graphs[i][a]`` is the list of refill-label indices adjacent to movement label
``a`` in macro graph ``J_i``.  Every graph must be square of the same order
``T``.  When ``ownership`` is present it must be balanced, so each of the ``M``
macro labels occurs exactly ``T/M`` times.

The checker reports:

- the average refill degrees ``q_B`` used in PP3gl;
- the minimum complementary nonedge margin
  ``deg(J_i,A)+q_B-T``;
- the PP3gl concentration test for a user-supplied ``--h``;
- for a supplied ownership, the exact global Ore condition and maximum matching.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"invalid fraction: {text}") from exc
    if value < 0:
        raise argparse.ArgumentTypeError("value must be nonnegative")
    return value


def fraction_json(value: Fraction) -> dict[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": str(value),
        "decimal": float(value),
    }


def maximum_bipartite_matching(adjacency: list[set[int]], right_size: int) -> int:
    """Return a maximum-cardinality matching size by augmenting paths."""

    match_right = [-1] * right_size

    def augment(left: int, seen: set[int]) -> bool:
        for right in sorted(adjacency[left]):
            if right in seen:
                continue
            seen.add(right)
            owner = match_right[right]
            if owner == -1 or augment(owner, seen):
                match_right[right] = left
                return True
        return False

    matched = 0
    for left in range(len(adjacency)):
        if augment(left, set()):
            matched += 1
    return matched


def load_payload(path: Path) -> tuple[list[list[set[int]]], list[int] | None]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON must be an object")

    raw_graphs = payload.get("graphs")
    if not isinstance(raw_graphs, list) or not raw_graphs:
        raise ValueError("graphs must be a nonempty list")

    graphs: list[list[set[int]]] = []
    order: int | None = None
    for macro_index, raw_graph in enumerate(raw_graphs):
        if not isinstance(raw_graph, list) or not raw_graph:
            raise ValueError(f"graph {macro_index} must be a nonempty row list")
        if order is None:
            order = len(raw_graph)
        if len(raw_graph) != order:
            raise ValueError("all graphs must have the same number of rows")

        graph: list[set[int]] = []
        for left, raw_neighbors in enumerate(raw_graph):
            if not isinstance(raw_neighbors, list):
                raise ValueError(
                    f"graph {macro_index}, row {left}: neighbors must be a list"
                )
            neighbors: set[int] = set()
            for value in raw_neighbors:
                if isinstance(value, bool) or not isinstance(value, int):
                    raise ValueError("neighbor indices must be integers")
                if value < 0 or value >= order:
                    raise ValueError("neighbor index out of range")
                neighbors.add(value)
            graph.append(neighbors)
        graphs.append(graph)

    raw_ownership = payload.get("ownership")
    ownership: list[int] | None = None
    if raw_ownership is not None:
        if not isinstance(raw_ownership, list) or len(raw_ownership) != order:
            raise ValueError("ownership must have exactly T entries")
        ownership = []
        for value in raw_ownership:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("ownership entries must be integers")
            if value < 0 or value >= len(graphs):
                raise ValueError("ownership macro index out of range")
            ownership.append(value)

    return graphs, ownership


def analyze(
    graphs: list[list[set[int]]],
    ownership: list[int] | None,
    h: Fraction,
) -> dict[str, Any]:
    macro_count = len(graphs)
    order = len(graphs[0])
    if order % macro_count != 0:
        raise ValueError("T must be divisible by the macro count M")
    width = order // macro_count

    row_degrees = [[len(row) for row in graph] for graph in graphs]
    average_right_degrees: list[Fraction] = []
    for right in range(order):
        total = sum(
            sum(right in graphs[macro][left] for left in range(order))
            for macro in range(macro_count)
        )
        average_right_degrees.append(Fraction(total, macro_count))

    margins: list[tuple[Fraction, int, int, int]] = []
    for macro, graph in enumerate(graphs):
        for left, neighbors in enumerate(graph):
            for right in range(order):
                if right not in neighbors:
                    margin = (
                        Fraction(row_degrees[macro][left])
                        + average_right_degrees[right]
                        - order
                    )
                    margins.append((margin, macro, left, right))

    minimum_margin = min((entry[0] for entry in margins), default=Fraction(order))
    worst_nonedge = None
    if margins:
        margin, macro, left, right = min(margins)
        worst_nonedge = {
            "macro": macro,
            "movement_label": left,
            "refill_label": right,
            "row_degree": row_degrees[macro][left],
            "average_refill_degree": fraction_json(average_right_degrees[right]),
            "margin_above_T": fraction_json(margin),
        }

    concentration_union_bound = order * math.exp(-float(h * h) / (32 * order))
    random_condition = minimum_margin >= h and concentration_union_bound < 1

    result: dict[str, Any] = {
        "macro_count_M": macro_count,
        "label_count_T": order,
        "width_per_macro_W": width,
        "average_refill_degrees_q": [
            fraction_json(value) for value in average_right_degrees
        ],
        "minimum_complementary_nonedge_margin": fraction_json(minimum_margin),
        "worst_complementary_nonedge": worst_nonedge,
        "h": fraction_json(h),
        "PP3gl_concentration_union_bound": concentration_union_bound,
        "PP3gl_complementary_degree_condition": minimum_margin >= h,
        "PP3gl_concentration_condition": concentration_union_bound < 1,
        "PP3gl_certifies_balanced_allocation": random_condition,
    }

    if ownership is not None:
        counts = Counter(ownership)
        balanced = all(counts[macro] == width for macro in range(macro_count))
        global_graph = [
            set(graphs[ownership[left]][left]) for left in range(order)
        ]
        right_degrees = [
            sum(right in global_graph[left] for left in range(order))
            for right in range(order)
        ]
        ore_margins: list[tuple[int, int, int]] = []
        for left, neighbors in enumerate(global_graph):
            for right in range(order):
                if right not in neighbors:
                    ore_margins.append(
                        (len(neighbors) + right_degrees[right] - order, left, right)
                    )
        minimum_ore_margin = min(
            (entry[0] for entry in ore_margins), default=order
        )
        matching_size = maximum_bipartite_matching(global_graph, order)
        result["ownership"] = {
            "values": ownership,
            "macro_counts": {
                str(macro): counts[macro] for macro in range(macro_count)
            },
            "balanced": balanced,
            "global_left_degrees": [len(row) for row in global_graph],
            "global_right_degrees": right_degrees,
            "minimum_Ore_margin_above_T": minimum_ore_margin,
            "PP3gk_Ore_condition": minimum_ore_margin >= 0,
            "maximum_matching_size": matching_size,
            "has_perfect_matching": matching_size == order,
            "minimum_degree_T_over_2_condition": min(
                [len(row) for row in global_graph] + right_degrees
            )
            >= Fraction(order, 2),
        }

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--h", type=parse_fraction, default=Fraction(0))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        graphs, ownership = load_payload(args.input)
        result = analyze(graphs, ownership, args.h)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
