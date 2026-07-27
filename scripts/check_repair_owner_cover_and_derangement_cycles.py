#!/usr/bin/env python3
"""Verify weighted bad-line owner covers and repair derangement cycle counts."""
from __future__ import annotations

import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path


def derangements(n: int) -> int:
    values = [1, 0]
    for k in range(2, n + 1):
        values.append((k - 1) * (values[-1] + values[-2]))
    return values[n]


def partitions_without_ones(n: int, minimum: int = 2):
    if n == 0:
        yield []
        return
    for part in range(minimum, n + 1):
        for rest in partitions_without_ones(n - part, part):
            yield [part] + rest


def cycle_type_count(parts: list[int]) -> int:
    multiplicities = Counter(parts)
    denominator = 1
    for length, count in multiplicities.items():
        denominator *= length**count * math.factorial(count)
    return math.factorial(sum(parts)) // denominator


def orbit_cells(n: int, source: int, target: int, orientation: int):
    reverse_source = n - 1 - source
    reverse_target = n - 1 - target
    if orientation == 0:
        return {
            (source, target),
            (reverse_source, reverse_target),
            (target, reverse_source),
            (reverse_target, source),
        }
    return {
        (source, reverse_target),
        (reverse_source, target),
        (target, source),
        (reverse_target, reverse_source),
    }


def verify_case(path: str):
    data = json.loads(Path(path).read_text())
    p = data["p"]
    n = p - 1
    m = n // 2
    pair_permutation = [value - 1 for value in data["pair_permutation"]]
    orientations = data["pair_orientations"]
    assert sorted(pair_permutation) == list(range(m))

    cell_owner: dict[tuple[int, int], int] = {}
    for source, (target, orientation) in enumerate(
        zip(pair_permutation, orientations)
    ):
        if source == target:
            orientation = 0
        for cell in orbit_cells(n, source, target, orientation):
            assert cell not in cell_owner
            cell_owner[cell] = source + 1

    owner_multisets = []
    for triple in data["bad_triples"]:
        points = [(x - 1, y - 1) for x, y in triple]
        (x1, y1), (x2, y2), (x3, y3) = points
        assert (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)
        owner_multisets.append(Counter(cell_owner[point] for point in points))

    assert all(multiset == owner_multisets[0] for multiset in owner_multisets)
    owners = sorted(owner_multisets[0])
    assert owners == sorted(data["bad_orbit_owners"])

    # Each audited line has occupancy three, so a repair must remove owner weight
    # at least one from every line.
    constraints = [(multiset, 1) for multiset in owner_multisets]
    minimum_cover = m + 1
    minimum_covers = []
    for size in range(m + 1):
        for combination in itertools.combinations(range(1, m + 1), size):
            support = set(combination)
            if all(
                sum(multiset[owner] for owner in support) >= demand
                for multiset, demand in constraints
            ):
                minimum_cover = size
                minimum_covers.append(combination)
        if minimum_covers:
            break

    assert minimum_cover == 1
    assert minimum_covers == [(owner,) for owner in owners]

    support_counts = {}
    for size in range(1, m + 1):
        count = 0
        for combination in itertools.combinations(range(1, m + 1), size):
            support = set(combination)
            if all(
                sum(multiset[owner] for owner in support) >= demand
                for multiset, demand in constraints
            ):
                count += 1
        expected = math.comb(m, size) - math.comb(m - len(owners), size)
        assert count == expected
        support_counts[str(size)] = count

    return {
        "p": p,
        "m": m,
        "owner_multiset": dict(owner_multisets[0]),
        "minimum_owner_cover": minimum_cover,
        "minimum_owner_covers": [list(cover) for cover in minimum_covers],
        "support_subset_counts": support_counts,
    }


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        raise SystemExit("usage: P37_NEAR_JSON P41_NEAR_JSON")

    cases = [verify_case(argv[1]), verify_case(argv[2])]
    derangement_counts = {str(k): derangements(k) for k in range(14)}
    assert derangement_counts["13"] == 2_290_792_932

    cycle_types = {}
    for size in range(2, 14):
        rows = []
        total = 0
        for parts in partitions_without_ones(size):
            count = cycle_type_count(parts)
            total += count
            rows.append({"cycle_type": parts, "count": count})
        assert total == derangements(size)
        cycle_types[str(size)] = rows

    output = {
        "cases": cases,
        "derangements_through_13": derangement_counts,
        "support_13_target_derangements": derangement_counts["13"],
        "support_13_all_target_bijections": math.factorial(13),
        "factorial_to_derangement_ratio": (
            math.factorial(13) / derangement_counts["13"]
        ),
        "cycle_types": cycle_types,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main(sys.argv)
