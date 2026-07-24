#!/usr/bin/env python3
"""Compute static PP3p and PP3r loads for a row-lift reservoir.

Unlike analyze_row_lift_sequential_loads.py, this tool does not enumerate legal
prefixes or permutations. For each of the 24 layer orders it collects every
possible residual event at its terminal layer, computes the static vertex load
of PP3p, and computes the collision-conditioned event mass of PP3r.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from typing import Any

from analyze_row_lift_bank import load_case
from analyze_row_lift_sequential_loads import (
    LAYER_NAMES,
    Certificate,
    Edge,
    build_model,
    event_load,
    falling,
)

PARTNER = {0: 1, 1: 0, 2: 3, 3: 2}


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    try:
        rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("rows must be comma-separated integers") from exc
    if len(rows) < 2:
        raise ValueError("choose at least two reservoir rows")
    if len(rows) > 6:
        raise ValueError("static certificate generation is limited to six rows")
    if any(row < 1 or row > m for row in rows):
        raise ValueError(f"rows must lie in [1,{m}]")
    return rows


def is_duplicate_certificate(
    certificate: Certificate,
    edge_cell: dict[Edge, tuple[int, int]],
) -> bool:
    """Return whether a certificate is one of the two projection collisions."""
    return len(certificate) == 2 and len({edge_cell[edge] for edge in certificate}) == 1


def rank_histogram(events: set[frozenset[Edge]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for event in events:
        key = str(len(event))
        counts[key] = counts.get(key, 0) + 1
    return {key: counts[key] for key in sorted(counts)}


def analyze_order(
    t: int,
    certificates: set[Certificate],
    edge_cell: dict[Edge, tuple[int, int]],
    order: tuple[int, ...],
) -> dict[str, Any]:
    position = {layer: stage for stage, layer in enumerate(order)}
    all_stage_events: list[set[frozenset[Edge]]] = [set() for _ in range(4)]
    geometric_stage_events: list[set[frozenset[Edge]]] = [set() for _ in range(4)]

    for certificate in certificates:
        stage = max(position[edge[0]] for edge in certificate)
        layer = order[stage]
        residual = frozenset(edge for edge in certificate if edge[0] == layer)
        if not residual:
            raise AssertionError("terminal certificate has no terminal-layer edge")
        all_stage_events[stage].add(residual)
        if not is_duplicate_certificate(certificate, edge_cell):
            geometric_stage_events[stage].add(residual)

    stage_rows = []
    maximum_vertex_load = Fraction()
    maximum_conditioned_mass = Fraction()

    for stage, layer in enumerate(order):
        all_events = all_stage_events[stage]
        geometric_events = geometric_stage_events[stage]
        vertex_load = event_load(all_events, t)
        conditioned = position[PARTNER[layer]] < stage
        coefficient = 3 if conditioned else 1
        conditioned_mass = sum(
            (Fraction(coefficient, falling(t, len(event))) for event in geometric_events),
            Fraction(),
        )
        maximum_vertex_load = max(maximum_vertex_load, vertex_load)
        maximum_conditioned_mass = max(maximum_conditioned_mass, conditioned_mass)
        stage_rows.append(
            {
                "stage": stage + 1,
                "layer": LAYER_NAMES[layer],
                "conditioned_second_in_pair": conditioned,
                "all_residual_event_count": len(all_events),
                "all_rank_histogram": rank_histogram(all_events),
                "geometric_residual_event_count": len(geometric_events),
                "geometric_rank_histogram": rank_histogram(geometric_events),
                "PP3p_vertex_load_fraction": (
                    f"{vertex_load.numerator}/{vertex_load.denominator}"
                ),
                "PP3r_conditioned_mass_fraction": (
                    f"{conditioned_mass.numerator}/{conditioned_mass.denominator}"
                ),
            }
        )

    return {
        "order": [LAYER_NAMES[layer] for layer in order],
        "maximum_PP3p_vertex_load_fraction": (
            f"{maximum_vertex_load.numerator}/{maximum_vertex_load.denominator}"
        ),
        "PP3p_criterion_passes": maximum_vertex_load <= Fraction(1, 24),
        "maximum_PP3r_conditioned_mass_fraction": (
            f"{maximum_conditioned_mass.numerator}/{maximum_conditioned_mass.denominator}"
        ),
        "PP3r_criterion_passes": maximum_conditioned_mass < 1,
        "stages": stage_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--rows", required=True, help="comma-separated old row indices")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        m, core = load_case(args.certificate, args.n)
        rows = parse_rows(args.rows, m)
        retained, edge_cell, certificates, certificate_counts = build_model(m, core, rows)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    analyses = [
        analyze_order(len(rows), certificates, edge_cell, order)
        for order in permutations(range(4))
    ]
    analyses.sort(
        key=lambda item: (
            Fraction(item["maximum_PP3r_conditioned_mass_fraction"]),
            Fraction(item["maximum_PP3p_vertex_load_fraction"]),
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
        "best_order_by_PP3r_then_PP3p": analyses[0],
        "orders": analyses,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
