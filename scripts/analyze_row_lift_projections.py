#!/usr/bin/env python3
"""Check the PP3u projection-dispersion condition for a row-lift reservoir.

For selected old reservoir rows, compute the hit old columns C and the cross
support U=(C x N) union (N x Y). The program enumerates primitive nonaxis
functionals ax+by up to a requested coefficient height and reports directions
whose support image has fewer than 2t levels.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
from typing import Any

from analyze_row_lift_bank import load_case


def parse_rows(text: str, m: int) -> tuple[int, ...]:
    try:
        rows = tuple(sorted({int(part) for part in text.split(",") if part.strip()}))
    except ValueError as exc:
        raise ValueError("rows must be comma-separated integers") from exc
    if not rows:
        raise ValueError("choose at least one reservoir row")
    if any(row < 1 or row > m for row in rows):
        raise ValueError(f"rows must lie in [1,{m}]")
    return rows


def is_interval(values: tuple[int, ...]) -> bool:
    return bool(values) and values == tuple(range(values[0], values[0] + len(values)))


def analyze(
    m: int,
    core: tuple[tuple[int, int], ...],
    rows: tuple[int, ...],
    height: int,
) -> dict[str, Any]:
    t = len(rows)
    row_set = set(rows)
    deleted = tuple(point for point in core if point[1] in row_set)
    columns = tuple(sorted({point[0] for point in deleted}))
    new_values = tuple(range(m + 1, m + t + 1))

    directions = []
    minimum_levels: int | None = None
    minimum_direction_count = 0
    tested = 0

    for a in range(1, height + 1):
        for b in range(-height, height + 1):
            if b == 0 or gcd(a, abs(b)) != 1:
                continue
            tested += 1
            levels = {
                a * x + b * y
                for x in columns
                for y in new_values
            }
            levels.update(
                a * x + b * y
                for x in new_values
                for y in rows
            )
            level_count = len(levels)
            if minimum_levels is None or level_count < minimum_levels:
                minimum_levels = level_count
                minimum_direction_count = 1
            elif level_count == minimum_levels:
                minimum_direction_count += 1
            if level_count < 2 * t:
                directions.append(
                    {
                        "a": a,
                        "b": b,
                        "level_count": level_count,
                        "required_count": 2 * t,
                    }
                )

    aligned_interval = (
        len(columns) == t
        and is_interval(columns)
        and is_interval(rows)
        and columns == rows
    )

    return {
        "source_n": m,
        "target_n": m + t,
        "t": t,
        "old_rows": list(rows),
        "deleted_point_count": len(deleted),
        "hit_old_columns": list(columns),
        "hit_old_column_count": len(columns),
        "coefficient_height": height,
        "primitive_direction_count": tested,
        "minimum_projection_level_count": minimum_levels,
        "minimum_direction_count": minimum_direction_count,
        "required_projection_level_count": 2 * t,
        "failing_direction_count": len(directions),
        "failing_directions": directions,
        "aligned_interval_PP3s_obstruction": aligned_interval,
        "tested_PP3u_screen_passes": not directions,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument("--rows", required=True, help="comma-separated old row indices")
    parser.add_argument(
        "--height",
        type=int,
        help="maximum absolute coefficient; default is the target side length",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        m, core = load_case(args.certificate, args.n)
        rows = parse_rows(args.rows, m)
        height = args.height if args.height is not None else m + len(rows)
        if height < 1:
            raise ValueError("height must be positive")
        result = analyze(m, core, rows, height)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
