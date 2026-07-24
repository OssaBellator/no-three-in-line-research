#!/usr/bin/env python3
"""Exhaustive small-instance search for prime-patching boundary extensions.

The input is one saturated no-three-in-line certificate on [m]^2. For each
number r up to --max-delete, the program deletes r old points and searches for
an exact degree completion on [m+t]^2. New points are admitted only when exact
integer determinant tests show that they create no collinear triple.

With --boundary-only, every inserted point must lie in a new row or new column.
Without it, old-old replacement cells are also allowed. A negative result is a
certificate only when the program prints status "exhausted"; hitting either
search limit prints "cutoff" and is explicitly inconclusive.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable, Iterator

Point = tuple[int, int]


def determinant(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def no_three(points: Iterable[Point]) -> bool:
    pts = list(points)
    return all(determinant(a, b, c) != 0 for a, b, c in combinations(pts, 3))


def saturated(points: Iterable[Point], n: int) -> bool:
    pts = list(points)
    return (
        len(pts) == 2 * n
        and len(set(pts)) == len(pts)
        and all(sum(x == col for x, _ in pts) == 2 for col in range(1, n + 1))
        and all(sum(y == row for _, y in pts) == 2 for row in range(1, n + 1))
    )


def load_core(path: Path) -> tuple[int, tuple[Point, ...]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("the search input must be one JSON object")
    m = payload.get("n")
    raw_points = payload.get("points")
    if isinstance(m, bool) or not isinstance(m, int) or m < 2:
        raise ValueError("n must be an integer at least 2")
    if not isinstance(raw_points, list):
        raise ValueError("points must be a JSON list")
    points: list[Point] = []
    for i, raw in enumerate(raw_points):
        if not isinstance(raw, list) or len(raw) != 2:
            raise ValueError(f"point {i} is not a two-entry list")
        x, y = raw
        if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError(f"point {i} is not integral")
        if not (1 <= x <= m and 1 <= y <= m):
            raise ValueError(f"point {i}={(x, y)} lies outside [1,{m}]^2")
        points.append((x, y))
    if not saturated(points, m):
        raise ValueError("input is not saturated with exactly two points per row and column")
    if not no_three(points):
        raise ValueError("input contains a collinear triple")
    return m, tuple(sorted(points))


def safe_add(point: Point, current: tuple[Point, ...]) -> bool:
    return all(determinant(a, b, point) != 0 for a, b in combinations(current, 2))


@dataclass
class Limits:
    max_nodes: int
    max_delete_subsets: int
    nodes: int = 0
    delete_subsets: int = 0
    cutoff: bool = False

    def visit_node(self) -> bool:
        self.nodes += 1
        if self.nodes > self.max_nodes:
            self.cutoff = True
            return False
        return True

    def visit_deletion(self) -> bool:
        self.delete_subsets += 1
        if self.delete_subsets > self.max_delete_subsets:
            self.cutoff = True
            return False
        return True


def candidate_cells(
    m: int,
    n: int,
    retained: frozenset[Point],
    deleted: frozenset[Point],
    boundary_only: bool,
) -> tuple[Point, ...]:
    out = []
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            point = (x, y)
            if point in retained or point in deleted:
                continue
            if boundary_only and x <= m and y <= m:
                continue
            out.append(point)
    return tuple(out)


def available_for_vertex(
    side: str,
    index: int,
    cells: tuple[Point, ...],
    rem_cols: tuple[int, ...],
    rem_rows: tuple[int, ...],
    chosen: frozenset[Point],
) -> list[Point]:
    out: list[Point] = []
    for x, y in cells:
        if (x, y) in chosen or rem_cols[x] <= 0 or rem_rows[y] <= 0:
            continue
        if (side == "c" and x == index) or (side == "r" and y == index):
            out.append((x, y))
    return out


def capacity_prune(
    cells: tuple[Point, ...],
    rem_cols: tuple[int, ...],
    rem_rows: tuple[int, ...],
    chosen: frozenset[Point],
) -> bool:
    n = len(rem_cols) - 1
    for x in range(1, n + 1):
        if rem_cols[x] > 0:
            capacity = sum(
                (x, y) not in chosen and rem_rows[y] > 0
                for xx, y in cells
                if xx == x
            )
            if capacity < rem_cols[x]:
                return False
    for y in range(1, n + 1):
        if rem_rows[y] > 0:
            capacity = sum(
                (x, y) not in chosen and rem_cols[x] > 0
                for x, yy in cells
                if yy == y
            )
            if capacity < rem_rows[y]:
                return False
    return True


def extend_batch(batch: tuple[Point, ...], current: tuple[Point, ...]) -> tuple[Point, ...] | None:
    out = current
    for point in batch:
        if not safe_add(point, out):
            return None
        out = out + (point,)
    return out


def search_completion(
    cells: tuple[Point, ...],
    retained: tuple[Point, ...],
    rem_cols: tuple[int, ...],
    rem_rows: tuple[int, ...],
    limits: Limits,
) -> tuple[Point, ...] | None:
    def recurse(
        current: tuple[Point, ...],
        selected: tuple[Point, ...],
        selected_set: frozenset[Point],
        cols: tuple[int, ...],
        rows: tuple[int, ...],
    ) -> tuple[Point, ...] | None:
        if not limits.visit_node():
            return None
        if sum(cols) == 0:
            return selected
        if not capacity_prune(cells, cols, rows, selected_set):
            return None

        choices: list[tuple[int, str, int, list[Point]]] = []
        n = len(cols) - 1
        for x in range(1, n + 1):
            if cols[x] > 0:
                available = available_for_vertex("c", x, cells, cols, rows, selected_set)
                choices.append((len(available), "c", x, available))
        for y in range(1, n + 1):
            if rows[y] > 0:
                available = available_for_vertex("r", y, cells, cols, rows, selected_set)
                choices.append((len(available), "r", y, available))
        _, side, index, available = min(choices, key=lambda item: (item[0], item[1], item[2]))
        need = cols[index] if side == "c" else rows[index]
        if len(available) < need:
            return None

        for raw_batch in combinations(available, need):
            batch = tuple(sorted(raw_batch))
            if side == "c" and any(
                sum(y == point[1] for point in batch) > rows[y]
                for y in {point[1] for point in batch}
            ):
                continue
            if side == "r" and any(
                sum(x == point[0] for point in batch) > cols[x]
                for x in {point[0] for point in batch}
            ):
                continue
            next_current = extend_batch(batch, current)
            if next_current is None:
                continue

            new_cols = list(cols)
            new_rows = list(rows)
            valid = True
            for x, y in batch:
                new_cols[x] -= 1
                new_rows[y] -= 1
                if new_cols[x] < 0 or new_rows[y] < 0:
                    valid = False
                    break
            if not valid:
                continue
            answer = recurse(
                next_current,
                selected + batch,
                selected_set.union(batch),
                tuple(new_cols),
                tuple(new_rows),
            )
            if answer is not None:
                return answer
            if limits.cutoff:
                return None
        return None

    return recurse(retained, (), frozenset(), rem_cols, rem_rows)


def deletion_sets(points: tuple[Point, ...], r: int) -> Iterator[frozenset[Point]]:
    for subset in combinations(points, r):
        yield frozenset(subset)


def search(
    m: int,
    core: tuple[Point, ...],
    t: int,
    max_delete: int,
    boundary_only: bool,
    limits: Limits,
) -> dict[str, object]:
    n = m + t
    for r in range(max_delete + 1):
        for deleted in deletion_sets(core, r):
            if not limits.visit_deletion():
                return {"status": "cutoff", "reason": "deletion-subset limit"}
            retained_set = frozenset(core).difference(deleted)
            retained = tuple(sorted(retained_set))
            rem_cols = [0] * (n + 1)
            rem_rows = [0] * (n + 1)
            for x, y in deleted:
                rem_cols[x] += 1
                rem_rows[y] += 1
            for index in range(m + 1, n + 1):
                rem_cols[index] = 2
                rem_rows[index] = 2
            cells = candidate_cells(m, n, retained_set, deleted, boundary_only)
            added = search_completion(cells, retained, tuple(rem_cols), tuple(rem_rows), limits)
            if added is not None:
                points = tuple(sorted(retained + added))
                assert saturated(points, n)
                assert no_three(points)
                return {
                    "status": "found",
                    "n": n,
                    "source_n": m,
                    "t": t,
                    "deleted": [list(point) for point in sorted(deleted)],
                    "added": [list(point) for point in sorted(added)],
                    "points": [list(point) for point in points],
                }
            if limits.cutoff:
                return {"status": "cutoff", "reason": "search-node limit"}
    return {"status": "exhausted", "n": n, "source_n": m, "t": t, "max_delete": max_delete}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--t", type=int, required=True, help="number of new rows and columns")
    parser.add_argument("--max-delete", type=int, default=2)
    parser.add_argument("--boundary-only", action="store_true")
    parser.add_argument("--max-nodes", type=int, default=200_000)
    parser.add_argument("--max-delete-subsets", type=int, default=50_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.t < 1 or args.max_delete < 0 or args.max_nodes < 1 or args.max_delete_subsets < 1:
        raise SystemExit("t and search limits must be positive; max-delete must be nonnegative")
    try:
        m, core = load_core(args.certificate)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"invalid input: {exc}") from exc

    limits = Limits(args.max_nodes, args.max_delete_subsets)
    result = search(m, core, args.t, args.max_delete, args.boundary_only, limits)
    result["boundary_only"] = args.boundary_only
    result["nodes"] = limits.nodes
    result["deletion_subsets"] = limits.delete_subsets
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.write_text(text + "\n", encoding="utf-8")
    if result["status"] == "cutoff":
        raise SystemExit(2)
    if result["status"] == "exhausted":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
