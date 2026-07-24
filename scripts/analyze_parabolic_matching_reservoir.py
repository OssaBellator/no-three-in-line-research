#!/usr/bin/env python3
"""Search finite certificates for monotone parabolic matching reservoirs.

For width t and translations A,B, the old column and row sets are
  {A + L*j*j, A + L*j*j + d : 0 <= j < t}
and the analogous B-set. A reservoir is a perfect matching of certificate
points between those sets. Deleting it and inserting the monotone parabolic
upper-left/lower-right patch preserves saturation and has no internal triples.
The program counts the two remaining external certificate classes exactly.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any, Iterable

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = tuple(points)
    return all(determinant(a, b, c) != 0 for a, b, c in combinations(pts, 3))


def saturated(points: Iterable[Point], n: int) -> bool:
    pts = tuple(points)
    return (
        len(pts) == 2 * n
        and len(set(pts)) == len(pts)
        and all(sum(x == col for x, _ in pts) == 2 for col in range(1, n + 1))
        and all(sum(y == row for _, y in pts) == 2 for row in range(1, n + 1))
    )


def load_cases(path: Path, selected_n: int | None) -> list[tuple[int, tuple[Point, ...]]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    raw_cases = payload if isinstance(payload, list) else [payload]
    parsed: list[tuple[int, tuple[Point, ...]]] = []
    for ordinal, raw in enumerate(raw_cases, 1):
        if not isinstance(raw, dict):
            raise ValueError(f"case {ordinal}: expected an object")
        n = raw.get("n")
        raw_points = raw.get("points")
        if isinstance(n, bool) or not isinstance(n, int) or n < 2:
            raise ValueError(f"case {ordinal}: invalid n")
        if not isinstance(raw_points, list):
            raise ValueError(f"case {ordinal}: points must be a list")
        points: list[Point] = []
        for index, raw_point in enumerate(raw_points):
            if not isinstance(raw_point, list) or len(raw_point) != 2:
                raise ValueError(f"case {ordinal}: malformed point {index}")
            x, y = raw_point
            if (
                isinstance(x, bool)
                or isinstance(y, bool)
                or not isinstance(x, int)
                or not isinstance(y, int)
            ):
                raise ValueError(f"case {ordinal}: nonintegral point {index}")
            points.append((x, y))
        if not saturated(points, n) or not no_three(points):
            raise ValueError(f"case {ordinal}: not a saturated no-three certificate")
        if selected_n is None or n == selected_n:
            parsed.append((n, tuple(sorted(points))))
    if selected_n is not None and len(parsed) != 1:
        raise ValueError("--n must select exactly one certificate")
    return parsed


def coordinate_set(offset: int, t: int, scale: int, gap: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            offset + scale * index * index + epsilon * gap
            for index in range(t)
            for epsilon in (0, 1)
        )
    )


def enumerate_matchings(
    core: tuple[Point, ...],
    columns: tuple[int, ...],
    rows: tuple[int, ...],
) -> list[tuple[Point, ...]]:
    row_set = set(rows)
    by_column = {
        column: tuple(
            point for point in core if point[0] == column and point[1] in row_set
        )
        for column in columns
    }
    if any(not options for options in by_column.values()):
        return []

    out: list[tuple[Point, ...]] = []

    def visit(index: int, used_rows: set[int], chosen: list[Point]) -> None:
        if index == len(columns):
            if len(used_rows) == len(rows):
                out.append(tuple(chosen))
            return
        column = columns[index]
        for point in by_column[column]:
            if point[1] in used_rows:
                continue
            visit(index + 1, used_rows | {point[1]}, chosen + [point])

    visit(0, set(), [])
    return out


def patch_points(
    n: int,
    t: int,
    column_offset: int,
    row_offset: int,
    scale: int,
    gap: int,
) -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    new_values = tuple(range(n + 1, n + t + 1))
    movement = tuple(
        (
            column_offset + scale * index * index + epsilon * gap,
            new_values[index],
        )
        for index in range(t)
        for epsilon in (0, 1)
    )
    refill = tuple(
        (
            new_values[index],
            row_offset + scale * index * index + epsilon * gap,
        )
        for index in range(t)
        for epsilon in (0, 1)
    )
    return movement, refill


def certificate_counts(
    retained: tuple[Point, ...], inserted: tuple[Point, ...]
) -> tuple[int, int, int]:
    retained_set = set(retained)
    inserted_set = set(inserted)
    blocked = 0
    anchored = 0
    internal = 0
    for triple in combinations(retained + inserted, 3):
        if determinant(*triple) != 0:
            continue
        retained_count = sum(point in retained_set for point in triple)
        if retained_count == 2:
            blocked += 1
        elif retained_count == 1:
            anchored += 1
        elif all(point in inserted_set for point in triple):
            internal += 1
    return blocked, anchored, internal


def analyze_case(
    n: int,
    core: tuple[Point, ...],
    widths: tuple[int, ...],
    scale: int,
    gap: int,
) -> dict[str, Any]:
    width_results: list[dict[str, Any]] = []
    for t in widths:
        span = scale * (t - 1) * (t - 1) + gap
        max_offset = n - span
        if max_offset < 1:
            width_results.append(
                {
                    "t": t,
                    "coordinate_span": span,
                    "feasible_translation_count": 0,
                    "matching_reservoir_count": 0,
                    "status": "coordinate-span-exceeds-core",
                }
            )
            continue

        candidates: list[dict[str, Any]] = []
        histogram: Counter[int] = Counter()
        for column_offset in range(1, max_offset + 1):
            columns = coordinate_set(column_offset, t, scale, gap)
            for row_offset in range(1, max_offset + 1):
                rows = coordinate_set(row_offset, t, scale, gap)
                for deleted in enumerate_matchings(core, columns, rows):
                    deleted_set = set(deleted)
                    retained = tuple(point for point in core if point not in deleted_set)
                    movement, refill = patch_points(
                        n, t, column_offset, row_offset, scale, gap
                    )
                    inserted = tuple(sorted(movement + refill))
                    target_n = n + t
                    if not no_three(inserted):
                        raise AssertionError("parabolic patch has an internal triple")
                    final = tuple(sorted(retained + inserted))
                    if not saturated(final, target_n):
                        raise AssertionError(
                            "parabolic patch does not preserve saturation"
                        )
                    blocked, anchored, internal = certificate_counts(retained, inserted)
                    total = blocked + anchored + internal
                    histogram[total] += 1
                    candidates.append(
                        {
                            "column_offset": column_offset,
                            "row_offset": row_offset,
                            "old_columns": list(columns),
                            "old_rows": list(rows),
                            "deleted": [list(point) for point in deleted],
                            "blocked_cell_triples": blocked,
                            "retained_anchor_triples": anchored,
                            "internal_patch_triples": internal,
                            "total_triples": total,
                            "valid_patch": total == 0,
                            "inserted": [list(point) for point in inserted],
                        }
                    )

        candidates.sort(
            key=lambda item: (
                item["total_triples"],
                item["blocked_cell_triples"],
                item["retained_anchor_triples"],
                item["column_offset"],
                item["row_offset"],
                item["deleted"],
            )
        )
        width_results.append(
            {
                "t": t,
                "coordinate_span": span,
                "feasible_translation_count": max_offset * max_offset,
                "matching_reservoir_count": len(candidates),
                "minimum_total_triples": (
                    candidates[0]["total_triples"] if candidates else None
                ),
                "clean_patch_count": sum(item["valid_patch"] for item in candidates),
                "triple_histogram": {
                    str(key): histogram[key] for key in sorted(histogram)
                },
                "best_candidates": candidates[:10],
                "status": "searched",
            }
        )

    return {
        "source_n": n,
        "scale": scale,
        "gap": gap,
        "widths": width_results,
    }


def parse_widths(
    text: str | None,
    cases: list[tuple[int, tuple[Point, ...]]],
    scale: int,
    gap: int,
) -> tuple[int, ...]:
    if text:
        try:
            widths = tuple(
                sorted({int(part) for part in text.split(",") if part.strip()})
            )
        except ValueError as exc:
            raise ValueError("--widths must be comma-separated integers") from exc
        if any(width < 2 for width in widths):
            raise ValueError("widths must be at least two")
        return widths
    maximum_n = max(n for n, _ in cases)
    widths = []
    t = 2
    while scale * (t - 1) * (t - 1) + gap <= maximum_n - 1:
        widths.append(t)
        t += 1
    return tuple(widths)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--n", type=int)
    parser.add_argument(
        "--widths", help="comma-separated widths; default is every feasible width"
    )
    parser.add_argument("--scale", type=int, default=2)
    parser.add_argument("--gap", type=int, default=1)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    try:
        if args.scale < 2:
            raise ValueError("--scale must be at least two")
        if not 1 <= args.gap < args.scale:
            raise ValueError("--gap must satisfy 1 <= gap < scale")
        cases = load_cases(args.certificate, args.n)
        widths = parse_widths(args.widths, cases, args.scale, args.gap)
        result = {
            "construction": "monotone-double-parabola",
            "cases": [
                analyze_case(n, core, widths, args.scale, args.gap)
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
