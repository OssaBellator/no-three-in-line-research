#!/usr/bin/env python3
"""Verify controller-aware domain monotonicity under source deletion."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Any

Point = tuple[int, int]


def collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def controller_safe(
    source: list[Point], edge: Point, movement_label: int, refill_label: int
) -> tuple[bool, dict[str, bool]]:
    x, y = edge
    movement = (x, movement_label)
    refill = (refill_label, y)

    movement_safe = True
    refill_safe = True
    for p, q in itertools.combinations(source, 2):
        if edge not in (p, q) and collinear(p, q, movement):
            movement_safe = False
        if edge not in (p, q) and collinear(p, q, refill):
            refill_safe = False

    anchor_bad = False
    for u, v in source:
        if (u, v) == edge:
            continue
        lhs = (movement_label - v) * (refill_label - u)
        rhs = (x - u) * (y - v)
        if lhs == rhs and lhs > 0:
            anchor_bad = True
            break

    return movement_safe and refill_safe and not anchor_bad, {
        "movement_safe": movement_safe,
        "refill_safe": refill_safe,
        "anchor_bad": anchor_bad,
    }


def analyse(data: dict[str, Any]) -> dict[str, Any]:
    source = [tuple(map(int, point)) for point in data["source_points"]]
    retained = [tuple(map(int, point)) for point in data["retained_points"]]
    controllers = [tuple(map(int, point)) for point in data["controller_edges"]]
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))
    gamma_count = int(data["gamma_count"])

    source_set = set(source)
    retained_set = set(retained)
    if not retained_set <= source_set:
        raise ValueError("retained source must be a subset of the original source")
    if not set(controllers) <= retained_set:
        raise ValueError("every controller edge must remain in the retained source")

    full_domains: dict[Point, set[tuple[int, int]]] = {}
    retained_domains: dict[Point, set[tuple[int, int]]] = {}
    gained: dict[str, list[list[int]]] = {}

    for edge in controllers:
        full: set[tuple[int, int]] = set()
        reduced: set[tuple[int, int]] = set()
        for movement_label in movement_labels:
            for refill_label in refill_labels:
                ok_full, _ = controller_safe(
                    source, edge, movement_label, refill_label
                )
                ok_reduced, _ = controller_safe(
                    retained, edge, movement_label, refill_label
                )
                if ok_full:
                    full.add((movement_label, refill_label))
                if ok_reduced:
                    reduced.add((movement_label, refill_label))
        if not full <= reduced:
            raise AssertionError("controller-safe domain shrank after source deletion")
        full_domains[edge] = full
        retained_domains[edge] = reduced
        gained[str(edge)] = [list(pair) for pair in sorted(reduced - full)]

    original_good = {
        edge: domain for edge, domain in full_domains.items() if len(domain) >= gamma_count
    }
    retained_good = {
        edge: domain
        for edge, domain in retained_domains.items()
        if len(domain) >= gamma_count
    }
    if not set(original_good) <= set(retained_good):
        raise AssertionError("a gamma-good controller became bad after deletion")

    outcome = (
        "retained_original_domains_expand"
        if any(retained_domains[edge] != full_domains[edge] for edge in controllers)
        else "retained_original_domains_unchanged"
    )
    return {
        "source_size": len(source),
        "retained_size": len(retained),
        "deleted_size": len(source) - len(retained),
        "controller_count": len(controllers),
        "label_pair_count": len(movement_labels) * len(refill_labels),
        "gamma_count": gamma_count,
        "original_domain_sizes": {
            str(edge): len(full_domains[edge]) for edge in controllers
        },
        "retained_domain_sizes": {
            str(edge): len(retained_domains[edge]) for edge in controllers
        },
        "gained_pairs": gained,
        "original_gamma_good": len(original_good),
        "retained_gamma_good": len(retained_good),
        "monotonicity_verified": True,
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
