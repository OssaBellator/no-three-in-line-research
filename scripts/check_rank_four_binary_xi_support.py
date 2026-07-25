#!/usr/bin/env python3
"""Check rank-four binary-Xi support avoidance and partner localization."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

Edge = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    return parser.parse_args()


def require_int(value: Any, label: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{label}: expected integer >= {minimum}")
    return value


def parse_fraction(raw: Any, label: str) -> Fraction:
    if isinstance(raw, int) and not isinstance(raw, bool):
        return Fraction(raw, 1)
    if not isinstance(raw, str):
        raise ValueError(f"{label}: expected integer or fraction string")
    try:
        value = Fraction(raw)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label}: invalid fraction") from exc
    if value < 0:
        raise ValueError(f"{label}: expected nonnegative fraction")
    return value


def parse_edges(raw: Any, label: str, n: int, excluded: set[int]) -> list[Edge]:
    if not isinstance(raw, list):
        raise ValueError(f"{label}: expected list")
    result: list[Edge] = []
    seen: set[Edge] = set()
    for pos, item in enumerate(raw):
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError(f"{label}[{pos}]: expected [tail,head]")
        tail = require_int(item[0], f"{label}[{pos}][0]")
        head = require_int(item[1], f"{label}[{pos}][1]")
        if tail >= n or head >= n or tail in excluded or head in excluded:
            raise ValueError(f"{label}[{pos}]: endpoint excluded or outside [0,n)")
        if tail == head:
            raise ValueError(f"{label}[{pos}]: loops are not remote partner arcs")
        edge = (tail, head)
        if edge in seen:
            raise ValueError(f"{label}: duplicate edge {edge}")
        seen.add(edge)
        result.append(edge)
    return result


def maximal_matching(edges: list[Edge]) -> list[Edge]:
    used_left: set[int] = set()
    used_right: set[int] = set()
    matching: list[Edge] = []
    for tail, head in sorted(edges):
        if tail in used_left or head in used_right:
            continue
        matching.append((tail, head))
        used_left.add(tail)
        used_right.add(head)
    return matching


def main() -> None:
    args = parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        n = require_int(payload.get("n"), "n", minimum=4)
        centre = require_int(payload.get("centre"), "centre")
        incident = require_int(payload.get("incident"), "incident")
        if centre >= n or incident >= n or centre == incident:
            raise ValueError("centre and incident must be distinct members of [0,n)")
        block_size = require_int(payload.get("block_size"), "block_size", minimum=4)
        if block_size > n:
            raise ValueError("block_size must not exceed n")
        residual_slack = parse_fraction(payload.get("residual_slack"), "residual_slack")
        if residual_slack > 1:
            raise ValueError("residual_slack must not exceed 1")
        level = require_int(payload.get("star_threshold"), "star_threshold", minimum=1)
        edges = parse_edges(
            payload.get("partner_support"),
            "partner_support",
            n,
            {centre, incident},
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"check failed: {exc}") from exc

    h = len(edges)
    kappa = Fraction(block_size - 3, (n - 2) * (n - 3))
    support_expectation = kappa * h

    left_degree: dict[int, int] = {}
    right_degree: dict[int, int] = {}
    for tail, head in edges:
        left_degree[tail] = left_degree.get(tail, 0) + 1
        right_degree[head] = right_degree.get(head, 0) + 1
    max_left = max(left_degree.values(), default=0)
    max_right = max(right_degree.values(), default=0)
    maximum_reported_degree = max(max_left, max_right)

    result: dict[str, Any] = {
        "n": n,
        "centre": centre,
        "incident": incident,
        "block_size": block_size,
        "kappa": str(kappa),
        "support_size": h,
        "support_expectation": str(support_expectation),
        "residual_slack": str(residual_slack),
        "star_threshold": level,
        "max_left_degree": max_left,
        "max_right_degree": max_right,
    }

    if support_expectation < residual_slack:
        result["outcome"] = "support_avoidance_regime"
        result["criterion_margin"] = str(residual_slack - support_expectation)
    else:
        matching = maximal_matching(edges)
        required = Fraction(h, 2 * level)
        if maximum_reported_degree >= level:
            result.update({
                "outcome": "partner_resource_star",
                "maximum_partner_degree": maximum_reported_degree,
            })
        else:
            if len(matching) < required:
                raise SystemExit(
                    "check failed: maximal matching violates h/(2L) lower bound"
                )
            result.update({
                "outcome": "remote_partner_matching",
                "matching_size": len(matching),
                "matching_lower_bound": str(required),
                "matching": [[tail, head] for tail, head in matching],
            })

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
