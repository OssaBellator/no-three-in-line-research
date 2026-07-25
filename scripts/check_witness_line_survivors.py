#!/usr/bin/env python3
"""Exact checker for witness-line survivor covers.

The input JSON has the form

{
  "q": 6,
  "lines": [
    [[1, 0], [2, 1]],
    ...
  ]
}

Each listed trace must be a matching in the q by q endpoint-resource graph.
The script enumerates one survivor cell per trace, constructs the simple union
of all remaining trace cells, and minimizes its maximum endpoint-resource
degree.  It also records the multiplicity load from PP3lr.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Iterable

Cell = tuple[int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument(
        "--max-states",
        type=int,
        default=2_000_000,
        help="refuse exact enumeration above this many survivor assignments",
    )
    return parser.parse_args()


def load_instance(path: Path) -> tuple[int, list[list[Cell]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    q = data.get("q")
    raw_lines = data.get("lines")
    if not isinstance(q, int) or q <= 0:
        raise ValueError("q must be a positive integer")
    if not isinstance(raw_lines, list) or not raw_lines:
        raise ValueError("lines must be a nonempty list")

    lines: list[list[Cell]] = []
    for line_index, raw_trace in enumerate(raw_lines):
        if not isinstance(raw_trace, list) or not raw_trace:
            raise ValueError(f"line {line_index} has an empty trace")
        trace: list[Cell] = []
        for raw_cell in raw_trace:
            if (
                not isinstance(raw_cell, list)
                or len(raw_cell) != 2
                or not all(isinstance(value, int) for value in raw_cell)
            ):
                raise ValueError(f"invalid cell on line {line_index}: {raw_cell!r}")
            cell = (raw_cell[0], raw_cell[1])
            if not (0 <= cell[0] < q and 0 <= cell[1] < q):
                raise ValueError(f"cell outside q by q host: {cell}")
            trace.append(cell)

        if len(set(trace)) != len(trace):
            raise ValueError(f"line {line_index} repeats a cell")
        if len({x for x, _ in trace}) != len(trace):
            raise ValueError(f"line {line_index} repeats a left resource")
        if len({y for _, y in trace}) != len(trace):
            raise ValueError(f"line {line_index} repeats a right resource")
        lines.append(trace)

    return q, lines


def pairwise_intersection_cap(lines: list[list[Cell]]) -> int:
    cap = 0
    sets = [set(trace) for trace in lines]
    for first, second in itertools.combinations(sets, 2):
        cap = max(cap, len(first & second))
    return cap


def resource_degrees(q: int, cells: Iterable[Cell]) -> list[int]:
    degrees = [0] * (2 * q)
    for x, y in cells:
        degrees[x] += 1
        degrees[q + y] += 1
    return degrees


def main() -> None:
    args = parse_args()
    q, lines = load_instance(args.input)

    state_count = math.prod(len(trace) for trace in lines)
    if state_count > args.max_states:
        raise RuntimeError(
            f"exact search has {state_count} states; increase --max-states explicitly"
        )

    best_key: tuple[int, int, tuple[int, ...]] | None = None
    best_cover: set[Cell] | None = None
    best_survivors: list[Cell] | None = None
    best_multiplicity: list[int] | None = None

    choices = [range(len(trace)) for trace in lines]
    for choice in itertools.product(*choices):
        cover: set[Cell] = set()
        multiplicity = [0] * (2 * q)
        survivors: list[Cell] = []

        for trace_index, trace in enumerate(lines):
            survivor = trace[choice[trace_index]]
            survivors.append(survivor)
            for cell in trace:
                if cell == survivor:
                    continue
                cover.add(cell)
                multiplicity[cell[0]] += 1
                multiplicity[q + cell[1]] += 1

        simple_degrees = resource_degrees(q, cover)
        key = (max(simple_degrees), max(multiplicity), choice)
        if best_key is None or key < best_key:
            best_key = key
            best_cover = cover
            best_survivors = survivors
            best_multiplicity = multiplicity

    assert best_key is not None
    assert best_cover is not None
    assert best_survivors is not None
    assert best_multiplicity is not None

    r = len(lines)
    total_deleted_multiplicity = sum(len(trace) - 1 for trace in lines)
    denominator = total_deleted_multiplicity + r * (r - 1)
    union_lower_bound = math.ceil(
        total_deleted_multiplicity**2 / denominator
    ) if denominator else 0
    congestion_lower_bound = math.ceil(union_lower_bound / q)
    multiplicity_average_lower_bound = math.ceil(total_deleted_multiplicity / q)

    result = {
        "q": q,
        "line_count": r,
        "trace_lengths": [len(trace) for trace in lines],
        "state_count": state_count,
        "pairwise_trace_intersection_cap": pairwise_intersection_cap(lines),
        "total_deleted_multiplicity": total_deleted_multiplicity,
        "pp3ls_union_lower_bound": union_lower_bound,
        "pp3ls_congestion_lower_bound": congestion_lower_bound,
        "pp3lr_multiplicity_lower_bound": multiplicity_average_lower_bound,
        "minimum_simple_congestion": best_key[0],
        "minimum_multiplicity_congestion_at_optimum": best_key[1],
        "survivors": [list(cell) for cell in best_survivors],
        "cover_size": len(best_cover),
        "cover": [list(cell) for cell in sorted(best_cover)],
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
