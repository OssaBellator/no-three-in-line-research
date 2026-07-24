#!/usr/bin/env python3
"""Sweep monotone parabolic reservoir parameters over a certificate corpus."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from analyze_parabolic_matching_reservoir import analyze_case, load_cases


def parse_widths(text: str) -> tuple[int, ...]:
    try:
        widths = tuple(
            sorted({int(part) for part in text.split(",") if part.strip()})
        )
    except ValueError as exc:
        raise ValueError("--widths must be comma-separated integers") from exc
    if not widths or any(width < 2 for width in widths):
        raise ValueError("widths must be integers at least two")
    return widths


def sweep_case(
    n: int,
    core: tuple[tuple[int, int], ...],
    widths: tuple[int, ...],
    max_scale: int,
) -> dict[str, Any]:
    rows = []
    aggregate_candidates = 0
    aggregate_clean = 0
    minimum = None
    best = []
    parameter_instances = 0

    for width in widths:
        for scale in range(2, max_scale + 1):
            for gap in range(1, scale):
                result = analyze_case(n, core, (width,), scale, gap)["widths"][0]
                count = result["matching_reservoir_count"]
                if count == 0:
                    continue
                parameter_instances += 1
                aggregate_candidates += count
                aggregate_clean += result["clean_patch_count"]
                candidate_minimum = result["minimum_total_triples"]
                if minimum is None or candidate_minimum < minimum:
                    minimum = candidate_minimum
                for candidate in result["best_candidates"]:
                    best.append(
                        {
                            "t": width,
                            "scale": scale,
                            "gap": gap,
                            **candidate,
                        }
                    )
                rows.append(
                    {
                        "t": width,
                        "scale": scale,
                        "gap": gap,
                        "matching_reservoir_count": count,
                        "clean_patch_count": result["clean_patch_count"],
                        "minimum_total_triples": candidate_minimum,
                    }
                )

    best.sort(
        key=lambda item: (
            item["total_triples"],
            item["blocked_cell_triples"],
            item["retained_anchor_triples"],
            item["t"],
            item["scale"],
            item["gap"],
            item["column_offset"],
            item["row_offset"],
            item["deleted"],
        )
    )
    rows.sort(
        key=lambda item: (
            item["minimum_total_triples"],
            item["t"],
            item["scale"],
            item["gap"],
        )
    )
    return {
        "source_n": n,
        "parameter_instances_with_matchings": parameter_instances,
        "matching_reservoir_count": aggregate_candidates,
        "clean_patch_count": aggregate_clean,
        "minimum_total_triples": minimum,
        "parameter_results": rows,
        "best_candidates": best[:10],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--widths", default="2,3")
    parser.add_argument("--max-scale", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        if args.max_scale < 2:
            raise ValueError("--max-scale must be at least two")
        cases = load_cases(args.certificate, args.n)
        widths = parse_widths(args.widths)
        result = {
            "widths": list(widths),
            "maximum_scale": args.max_scale,
            "gap_range": "1 <= gap < scale",
            "cases": [
                sweep_case(n, core, widths, args.max_scale)
                for n, core in cases
            ],
        }
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
