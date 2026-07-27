#!/usr/bin/env python3
"""Reconstruct residual target matrices and Hall witnesses for p=41."""
from __future__ import annotations

import json
import math
import sys
from collections import defaultdict
from pathlib import Path


def maximal_cell_lines(n: int):
    cell_lines = [[] for _ in range(n * n)]
    line_count = 0
    for dx in range(1, n):
        for dy in range(-(n - 1), n):
            if dy == 0 or math.gcd(dx, abs(dy)) != 1:
                continue
            for x in range(n):
                for y in range(n):
                    if 0 <= x - dx < n and 0 <= y - dy < n:
                        continue
                    cells = []
                    current_x, current_y = x, y
                    while 0 <= current_x < n and 0 <= current_y < n:
                        cells.append(current_x * n + current_y)
                        current_x += dx
                        current_y += dy
                    if len(cells) >= 3:
                        for cell in cells:
                            cell_lines[cell].append(line_count)
                        line_count += 1
    return cell_lines, line_count


def canonical_orbit_id(m: int, source: int, target: int, orientation: int):
    if source == target:
        return source * m + source
    if source < target:
        return m * m + 2 * (source * m + target) + orientation
    return m * m + 2 * (target * m + source) + 1 - orientation


def orbit_cells(n: int, source: int, target: int, orientation: int):
    reverse_source = n - 1 - source
    reverse_target = n - 1 - target
    if orientation == 0:
        return [
            (source, target),
            (reverse_source, reverse_target),
            (target, reverse_source),
            (reverse_target, source),
        ]
    return [
        (source, reverse_target),
        (reverse_source, target),
        (target, source),
        (reverse_target, reverse_source),
    ]


def permanent(row_masks: list[int], size: int) -> int:
    values = [0] * (1 << size)
    values[0] = 1
    for mask in range(1 << size):
        row = mask.bit_count()
        if row == size:
            continue
        available = row_masks[row] & ~mask
        while available:
            bit = available & -available
            values[mask | bit] += values[mask]
            available -= bit
    return values[-1]


def smallest_hall_witness(row_masks: list[int], size: int):
    best = None
    for source_mask in range(1, 1 << size):
        neighbour_mask = 0
        for row in range(size):
            if source_mask >> row & 1:
                neighbour_mask |= row_masks[row]
        source_size = source_mask.bit_count()
        neighbour_size = neighbour_mask.bit_count()
        if neighbour_size < source_size:
            key = (
                source_size,
                -(source_size - neighbour_size),
                source_mask,
                neighbour_mask,
            )
            if best is None or key < best:
                best = key
    assert best is not None
    return best[2], best[3], -best[1]


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit("usage: P41_NEAR_JSON PERMANENT_AUDIT_JSON")

    near = json.loads(Path(argv[1]).read_text())
    audit = json.loads(Path(argv[2]).read_text())
    assert near["p"] == 41
    n = 40
    m = 20
    support_size = 13
    rho = [value - 1 for value in near["pair_permutation"]]
    base_orientation = near["pair_orientations"]

    cell_lines, line_count = maximal_cell_lines(n)
    assert line_count == 108190

    options = []
    by_source_target = [[[] for _ in range(m)] for _ in range(m)]
    for source in range(m):
        for target in range(m):
            for orientation in range(1 if source == target else 2):
                counts = defaultdict(int)
                for x, y in orbit_cells(n, source, target, orientation):
                    for line in cell_lines[x * n + y]:
                        counts[line] += 1
                option_id = len(options)
                options.append(
                    (
                        source,
                        target,
                        orientation,
                        canonical_orbit_id(m, source, target, orientation),
                        dict(counts),
                    )
                )
                by_source_target[source][target].append(option_id)

    base_option = []
    base_occupancy = [0] * line_count
    for source in range(m):
        orientation = 0 if rho[source] == source else base_orientation[source]
        option_id = next(
            option_id
            for option_id in by_source_target[source][rho[source]]
            if options[option_id][2] == orientation
        )
        base_option.append(option_id)
        for line, count in options[option_id][4].items():
            base_occupancy[line] += count

    witnesses = []
    for raw_support in audit["zero_permanent_supports"]:
        support = [value - 1 for value in raw_support]
        in_support = set(support)
        residual_occupancy = base_occupancy.copy()
        retained_orbits = {
            options[base_option[source]][3]
            for source in range(m)
            if source not in in_support
        }
        for source in support:
            for line, count in options[base_option[source]][4].items():
                residual_occupancy[line] -= count

        row_masks = []
        for source in support:
            row_mask = 0
            for column, old_target_owner in enumerate(support):
                if source == old_target_owner:
                    continue
                target = rho[old_target_owner]
                edge_legal = False
                for option_id in by_source_target[source][target]:
                    _, _, _, orbit_id, counts = options[option_id]
                    direct_legal = orbit_id not in retained_orbits and all(
                        residual_occupancy[line] + count <= 2
                        for line, count in counts.items()
                    )
                    signature_legal = orbit_id not in retained_orbits and all(
                        base_occupancy[line] - residual_occupancy[line]
                        >= base_occupancy[line] + count - 2
                        for line, count in counts.items()
                    )
                    assert direct_legal == signature_legal
                    edge_legal |= direct_legal
                if edge_legal:
                    row_mask |= 1 << column
            row_masks.append(row_mask)

        assert permanent(row_masks, support_size) == 0
        source_mask, target_mask, deficit = smallest_hall_witness(
            row_masks, support_size
        )
        hall_sources = [
            support[index] + 1
            for index in range(support_size)
            if source_mask >> index & 1
        ]
        hall_targets = [
            support[index] + 1
            for index in range(support_size)
            if target_mask >> index & 1
        ]
        zero_rows = [
            support[index] + 1
            for index, row_mask in enumerate(row_masks)
            if row_mask == 0
        ]
        column_union = 0
        for row_mask in row_masks:
            column_union |= row_mask
        zero_columns = [
            support[index] + 1
            for index in range(support_size)
            if not (column_union >> index & 1)
        ]
        witnesses.append(
            {
                "support": raw_support,
                "hall_sources": hall_sources,
                "hall_target_owners": hall_targets,
                "deficit": deficit,
                "zero_source_rows": zero_rows,
                "zero_target_columns": zero_columns,
            }
        )

    assert sum(bool(row["zero_source_rows"]) for row in witnesses) == 7
    assert sum(bool(row["zero_target_columns"]) for row in witnesses) == 1
    output = {
        "p": 41,
        "signature_equivalence_verified": True,
        "zero_row_supports": 7,
        "zero_column_supports": 1,
        "higher_order_hall_cores": 0,
        "witnesses": witnesses,
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main(sys.argv)
