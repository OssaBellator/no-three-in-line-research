#!/usr/bin/env python3
"""Search all small reservoir-row choices for clean full row-lift banks.

For each certificate and each requested width t in {2,3}, enumerate all t-row
reservoirs and the complete row-lift bank from Theorem PP3i. Results are exact.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Any

from analyze_row_lift_bank import analyze, load_case


def load_cases(path: Path) -> list[tuple[int, tuple[tuple[int, int], ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    side_lengths = []
    for raw in raw_cases:
        if not isinstance(raw, dict) or not isinstance(raw.get("n"), int):
            raise ValueError("every case must contain an integer n")
        side_lengths.append(raw["n"])
    if len(side_lengths) != len(set(side_lengths)):
        raise ValueError("side lengths must be unique")
    return [load_case(path, n) for n in sorted(side_lengths)]


def summarize(m: int, core: tuple[tuple[int, int], ...], t: int) -> dict[str, Any]:
    results = [
        analyze(m, core, rows, 100_000)
        for rows in combinations(range(1, m + 1), t)
    ]
    results.sort(
        key=lambda item: (
            item["minimum_certificate_count"],
            Fraction(item["exact_expected_certificate_count_fraction"]),
            item["internal_support_triples"],
            item["blocked_support_cells"],
            item["anchored_support_pairs"],
            item["old_rows"],
        )
    )
    best = results[0]
    clean = [result for result in results if result["clean_state_count"] > 0]
    return {
        "source_n": m,
        "t": t,
        "reservoir_subset_count": len(results),
        "clean_reservoir_subset_count": len(clean),
        "total_clean_state_count": sum(result["clean_state_count"] for result in clean),
        "best_rows": best["old_rows"],
        "best_minimum_certificate_count": best["minimum_certificate_count"],
        "best_exact_average_fraction": best["exact_expected_certificate_count_fraction"],
        "best_blocked_support_cells": best["blocked_support_cells"],
        "best_anchored_support_pairs": best["anchored_support_pairs"],
        "best_internal_support_triples": best["internal_support_triples"],
        "best_clean_state_count": best["clean_state_count"],
    }


def parse_widths(text: str) -> tuple[int, ...]:
    try:
        widths = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("widths must be comma-separated integers") from exc
    if not widths or any(width not in (2, 3) for width in widths):
        raise ValueError("exact corpus search supports widths 2 and 3")
    return widths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--widths", default="2,3")
    parser.add_argument("--n-min", type=int, default=2)
    parser.add_argument("--n-max", type=int)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        widths = parse_widths(args.widths)
        cases = load_cases(args.certificate)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    summaries = []
    for m, core in cases:
        if m < args.n_min or (args.n_max is not None and m > args.n_max):
            continue
        for t in widths:
            if t <= m:
                summaries.append(summarize(m, core, t))

    payload = {
        "widths": list(widths),
        "summary_count": len(summaries),
        "any_clean_reservoir": any(
            item["clean_reservoir_subset_count"] for item in summaries
        ),
        "summaries": summaries,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
