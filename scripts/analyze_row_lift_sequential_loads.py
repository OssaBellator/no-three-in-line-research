#!/usr/bin/env python3
"""Compute sequential permutation-local-lemma loads for a row-lift reservoir.

The row-lift construction has four independent permutation layers. For a chosen
layer order, this program enumerates every legal prefix, forms the distinct
canonical events activated in the next permutation, and computes the maximum
Lu--Szekely vertex load. Exact enumeration is intended for t<=3.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, permutations, product
from pathlib import Path
from typing import Any

from analyze_row_lift_bank import balanced_coloring, determinant, load_case

Point = tuple[int, int]
Edge = tuple[int, int, int]
Certificate = frozenset[Edge]

LAYER_NAMES = ("red-move", "blue-move", "refill-a", "refill-b")


def falling(n: int, r: int) -> int:
    out = 1
    for value in range(n, n - r, -1):
        out *= value
    return out


def compatible(edges: tuple[Edge, ...]) -> bool:
    by_layer: dict[int, list[tuple[int, int]]] = {}
    for layer, domain, codomain in edges:
        by_layer.setdefault(layer, []).append((domain, codomain))
    for assignments in by_layer.values():
        domains = [domain for domain, _ in assignments]
        codomains = [codomain for _, codomain in assignments]
        if len(domains) != len(set(domains)) or len(codomains) != len(set(codomains)):
            return False
    return True


def build_model(
    m: int,
    core: tuple[Point, ...],
    old_rows: tuple[int, ...],
) -> tuple[tuple[Point, ...], dict[Edge, Point], set[Certificate], dict[str, int]]:
    t = len(old_rows)
    target_n = m + t
    new_values = tuple(range(m + 1, target_n + 1))
    old_row_set = set(old_rows)
    deleted = tuple(point for point in core if point[1] in old_row_set)
    retained = tuple(point for point in core if point[1] not in old_row_set)
    red, blue = balanced_coloring(deleted, t)

    edge_cell: dict[Edge, Point] = {}
    for layer, points in ((0, red), (1, blue)):
        for domain, point in enumerate(points):
            for codomain, new_row in enumerate(new_values):
                edge_cell[(layer, domain, codomain)] = (point[0], new_row)
    for layer in (2, 3):
        for domain, old_row in enumerate(old_rows):
            for codomain, new_column in enumerate(new_values):
                edge_cell[(layer, domain, codomain)] = (new_column, old_row)

    cell_edges: dict[Point, list[Edge]] = {}
    for edge, cell in edge_cell.items():
        cell_edges.setdefault(cell, []).append(edge)
    support = tuple(sorted(cell_edges))
    certificates: set[Certificate] = set()
    counts = {
        "movement_duplicate": 0,
        "refill_duplicate": 0,
        "blocked_cell": 0,
        "anchored_pair": 0,
        "internal_triple": 0,
    }

    for red_index, red_point in enumerate(red):
        for blue_index, blue_point in enumerate(blue):
            if red_point[0] != blue_point[0]:
                continue
            for codomain in range(t):
                certificate = frozenset(
                    ((0, red_index, codomain), (1, blue_index, codomain))
                )
                if certificate not in certificates:
                    counts["movement_duplicate"] += 1
                certificates.add(certificate)
    for domain in range(t):
        for codomain in range(t):
            certificate = frozenset(((2, domain, codomain), (3, domain, codomain)))
            if certificate not in certificates:
                counts["refill_duplicate"] += 1
            certificates.add(certificate)

    retained_pairs = tuple(combinations(retained, 2))
    blocked = {
        cell
        for cell in support
        if any(determinant(first, second, cell) == 0 for first, second in retained_pairs)
    }
    for cell in blocked:
        for edge in cell_edges[cell]:
            certificate = frozenset((edge,))
            if certificate not in certificates:
                counts["blocked_cell"] += 1
            certificates.add(certificate)

    for first_cell, second_cell in combinations(support, 2):
        if not any(
            determinant(first_cell, second_cell, anchor) == 0 for anchor in retained
        ):
            continue
        for first_edge in cell_edges[first_cell]:
            for second_edge in cell_edges[second_cell]:
                edges = (first_edge, second_edge)
                if compatible(edges):
                    certificate = frozenset(edges)
                    if certificate not in certificates:
                        counts["anchored_pair"] += 1
                    certificates.add(certificate)

    for cells in combinations(support, 3):
        if len({point[0] for point in cells}) < 3 or len({point[1] for point in cells}) < 3:
            continue
        if determinant(*cells) != 0:
            continue
        for edges in product(*(cell_edges[cell] for cell in cells)):
            if compatible(edges):
                certificate = frozenset(edges)
                if certificate not in certificates:
                    counts["internal_triple"] += 1
                certificates.add(certificate)

    return retained, edge_cell, certificates, counts


def permutation_edges(layer: int, permutation: tuple[int, ...]) -> frozenset[Edge]:
    return frozenset(
        (layer, domain, codomain) for domain, codomain in enumerate(permutation)
    )


def activated_events(
    certificates: set[Certificate],
    order_position: dict[int, int],
    stage: int,
    current_layer: int,
    prefix_edges: frozenset[Edge],
) -> set[frozenset[Edge]]:
    events: set[frozenset[Edge]] = set()
    for certificate in certificates:
        latest = max(order_position[edge[0]] for edge in certificate)
        if latest != stage:
            continue
        earlier = frozenset(
            edge for edge in certificate if order_position[edge[0]] < stage
        )
        if not earlier.issubset(prefix_edges):
            continue
        event = frozenset(edge for edge in certificate if edge[0] == current_layer)
        if event:
            events.add(event)
    return events


def event_load(events: set[frozenset[Edge]], t: int) -> Fraction:
    loads: dict[tuple[str, int], Fraction] = {}
    for event in events:
        probability = Fraction(1, falling(t, len(event)))
        for _, domain, codomain in event:
            loads[("domain", domain)] = (
                loads.get(("domain", domain), Fraction()) + probability
            )
            loads[("codomain", codomain)] = (
                loads.get(("codomain", codomain), Fraction()) + probability
            )
    return max(loads.values(), default=Fraction())


def analyze_order(
    t: int,
    certificates: set[Certificate],
    order: tuple[int, ...],
) -> dict[str, Any]:
    all_permutations = tuple(permutations(range(t)))
    edges_by_layer = {
        layer: tuple(
            permutation_edges(layer, permutation) for permutation in all_permutations
        )
        for layer in range(4)
    }
    order_position = {layer: position for position, layer in enumerate(order)}
    maximum_load = Fraction()
    maximum_events = 0
    prefix_counts = [1]
    prefixes: list[frozenset[Edge]] = [frozenset()]

    for stage, layer in enumerate(order):
        next_prefixes: list[frozenset[Edge]] = []
        for prefix in prefixes:
            events = activated_events(
                certificates, order_position, stage, layer, prefix
            )
            maximum_events = max(maximum_events, len(events))
            maximum_load = max(maximum_load, event_load(events, t))
            for permutation in edges_by_layer[layer]:
                if any(event.issubset(permutation) for event in events):
                    continue
                next_prefixes.append(prefix.union(permutation))
        prefixes = next_prefixes
        prefix_counts.append(len(prefixes))
        if not prefixes:
            break

    return {
        "order": [LAYER_NAMES[layer] for layer in order],
        "maximum_stage_vertex_load_fraction": (
            f"{maximum_load.numerator}/{maximum_load.denominator}"
        ),
        "uniform_prefix_LLL_criterion_passes": maximum_load <= Fraction(1, 24),
        "maximum_activated_event_count": maximum_events,
        "legal_prefix_counts": prefix_counts,
        "clean_full_state_count": len(prefixes) if len(prefix_counts) == 5 else 0,
    }


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    try:
        rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("rows must be comma-separated integers") from exc
    if not 2 <= len(rows) <= 3:
        raise ValueError("exact sequential enumeration requires two or three rows")
    if any(row < 1 or row > m for row in rows):
        raise ValueError(f"rows must lie in [1,{m}]")
    return rows


def parse_order(text: str) -> tuple[int, ...]:
    aliases = {name: index for index, name in enumerate(LAYER_NAMES)}
    aliases.update({str(index): index for index in range(4)})
    parts = [part.strip() for part in text.split(",")]
    try:
        order = tuple(aliases[part] for part in parts)
    except KeyError as exc:
        raise ValueError(f"unknown layer {exc.args[0]!r}") from exc
    if sorted(order) != [0, 1, 2, 3]:
        raise ValueError("order must list each of the four layers exactly once")
    return order


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--rows", required=True)
    parser.add_argument(
        "--order",
        default="red-move,blue-move,refill-a,refill-b",
        help="comma-separated layer names or indices",
    )
    parser.add_argument("--all-orders", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        m, core = load_case(args.certificate, args.n)
        rows = parse_rows(args.rows, m)
        retained, edge_cell, certificates, certificate_counts = build_model(
            m, core, rows
        )
        orders = (
            tuple(permutations(range(4)))
            if args.all_orders
            else (parse_order(args.order),)
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    analyses = [analyze_order(len(rows), certificates, order) for order in orders]
    analyses.sort(
        key=lambda item: (
            Fraction(item["maximum_stage_vertex_load_fraction"]),
            -item["clean_full_state_count"],
            item["order"],
        )
    )
    payload = {
        "source_n": m,
        "target_n": m + len(rows),
        "t": len(rows),
        "old_rows": list(rows),
        "retained_point_count": len(retained),
        "layer_edge_count": len(edge_cell),
        "canonical_certificate_count": len(certificates),
        "certificate_counts_by_origin": certificate_counts,
        "best_order": analyses[0],
        "orders": analyses,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
