#!/usr/bin/env python3
"""Check fixed candidate cells and zero-mass anchor activation after a pool repair."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

Point = tuple[int, int]


def is_collinear(a: Point, b: Point, c: Point) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def is_no_three(points: Iterable[Point]) -> bool:
    pts = list(points)
    return all(not is_collinear(a, b, c) for a, b, c in itertools.combinations(pts, 3))


def layer_points(perm: Sequence[int]) -> set[Point]:
    return {(x, y) for x, y in enumerate(perm)}


def blocker_count(source: set[Point], candidate: Point) -> int:
    return sum(
        1
        for p, q in itertools.combinations(source, 2)
        if is_collinear(p, q, candidate)
    )


def candidate_cells(
    pool_columns: Sequence[int],
    pool_rows: Sequence[int],
    movement_labels: Sequence[int],
    refill_labels: Sequence[int],
) -> list[Point]:
    movement = [(x, a) for x in pool_columns for a in movement_labels]
    refill = [(b, y) for b in refill_labels for y in pool_rows]
    return movement + refill


def excess_cell_potential(source: set[Point], candidates: Sequence[Point]) -> int:
    values = [blocker_count(source, z) - 1 for z in candidates]
    if any(value < 0 for value in values):
        raise AssertionError("axis-subtracted candidate potential became negative")
    return sum(values)


def edge_anchor_mass(
    source: set[Point],
    edge: Point,
    movement_labels: Sequence[int],
    refill_labels: Sequence[int],
    anchor_filter: set[Point] | None = None,
) -> int:
    x, y = edge
    total = 0
    for a in movement_labels:
        for b in refill_labels:
            for u, v in source:
                point = (u, v)
                if point == edge:
                    continue
                if anchor_filter is not None and point not in anchor_filter:
                    continue
                if (
                    (a - v) * (b - u) == (x - u) * (y - v)
                    and (x - u) * (y - v) > 0
                ):
                    total += 1
    return total


def active_anchor_mass(
    source: set[Point],
    controller_perm: Sequence[int],
    pool_columns: Sequence[int],
    movement_labels: Sequence[int],
    refill_labels: Sequence[int],
) -> int:
    return sum(
        edge_anchor_mass(
            source,
            (x, controller_perm[x]),
            movement_labels,
            refill_labels,
        )
        for x in pool_columns
    )


def pair_weight(p: Point, q: Point, candidates: Sequence[Point]) -> int:
    return sum(1 for z in candidates if is_collinear(p, q, z))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    m = int(data["m"])
    initial_controller = list(map(int, data["initial_controller_layer"]))
    final_controller = list(map(int, data["final_controller_layer"]))
    complementary = list(map(int, data["complementary_layer"]))
    moved_columns = list(map(int, data["moved_columns"]))
    pool_columns = list(map(int, data["pool_columns"]))
    movement_labels = list(map(int, data["movement_labels"]))
    refill_labels = list(map(int, data["refill_labels"]))

    if not all(len(p) == m for p in (initial_controller, final_controller, complementary)):
        raise AssertionError("all permutations must have length m")
    if any(len(set(p)) != m for p in (initial_controller, final_controller, complementary)):
        raise AssertionError("layer data must be permutations")

    pool_rows = sorted(initial_controller[x] for x in pool_columns)
    if sorted(final_controller[x] for x in pool_columns) != pool_rows:
        raise AssertionError("the repair did not preserve the pool row set")
    if any(initial_controller[x] != final_controller[x] for x in range(m) if x not in moved_columns):
        raise AssertionError("the repair changed a controller outside the selected block")

    initial_source = layer_points(initial_controller) | layer_points(complementary)
    final_source = layer_points(final_controller) | layer_points(complementary)
    if len(initial_source) != 2 * m or len(final_source) != 2 * m:
        raise AssertionError("the source layers are not edge-disjoint")
    if not is_no_three(initial_source) or not is_no_three(final_source):
        raise AssertionError("stored source is not no-three before and after the repair")

    candidates = candidate_cells(
        pool_columns, pool_rows, movement_labels, refill_labels
    )
    xi_initial = excess_cell_potential(initial_source, candidates)
    xi_final = excess_cell_potential(final_source, candidates)

    anchor_initial = active_anchor_mass(
        initial_source,
        initial_controller,
        pool_columns,
        movement_labels,
        refill_labels,
    )
    anchor_final = active_anchor_mass(
        final_source,
        final_controller,
        pool_columns,
        movement_labels,
        refill_labels,
    )

    initial_edges = {(x, initial_controller[x]) for x in pool_columns}
    final_edges = {(x, final_controller[x]) for x in pool_columns}
    new_edges = final_edges - initial_edges
    kept_edges = final_edges & initial_edges

    removed = {(x, initial_controller[x]) for x in moved_columns}
    inserted = {(x, final_controller[x]) for x in moved_columns}
    fixed = initial_source - removed
    if fixed | inserted != final_source:
        raise AssertionError("repair decomposition is inconsistent")

    new_edge_anchor_mass = sum(
        edge_anchor_mass(
            final_source, edge, movement_labels, refill_labels
        )
        for edge in new_edges
    )
    inserted_anchor_mass_on_kept = sum(
        edge_anchor_mass(
            final_source,
            edge,
            movement_labels,
            refill_labels,
            anchor_filter=inserted,
        )
        for edge in kept_edges
    )
    if new_edge_anchor_mass != 0:
        raise AssertionError("new controller entries were activated with positive anchor mass")
    if inserted_anchor_mass_on_kept != 0:
        raise AssertionError("inserted source points created anchor mass on unchanged entries")
    if anchor_final > anchor_initial:
        raise AssertionError("active anchor potential increased despite zero-mass activation")

    cell_removal = sum(
        pair_weight(d, p, candidates) for d in removed for p in fixed
    ) + sum(pair_weight(d, e, candidates) for d, e in itertools.combinations(removed, 2))
    cell_insertion = sum(
        pair_weight(a, p, candidates) for a in inserted for p in fixed
    ) + sum(pair_weight(a, b, candidates) for a, b in itertools.combinations(inserted, 2))
    if xi_final - xi_initial != cell_insertion - cell_removal:
        raise AssertionError("fixed candidate-cell identity failed")

    theta_initial = xi_initial + anchor_initial
    theta_final = xi_final + anchor_final
    if theta_final >= theta_initial:
        raise AssertionError("restart potential did not strictly decrease")

    print("m", m)
    print("pool columns", pool_columns)
    print("pool rows", pool_rows)
    print("pool size", len(pool_columns))
    print("candidate cell universe", len(candidates))
    print("initial no-three", True)
    print("final no-three", True)
    print("new controller edges", sorted(new_edges))
    print("new-edge anchor activation mass", new_edge_anchor_mass)
    print("inserted-anchor mass on kept edges", inserted_anchor_mass_on_kept)
    print("active anchor potential", [anchor_initial, anchor_final])
    print("excess cell potential", [xi_initial, xi_final])
    print("current restart potential", [theta_initial, theta_final])
    print("cell removal and insertion", [cell_removal, cell_insertion])
    print("direct potential change", theta_final - theta_initial)
    print("outcome", "fixed_cells_zero_mass_anchor_activation")


if __name__ == "__main__":
    main()
