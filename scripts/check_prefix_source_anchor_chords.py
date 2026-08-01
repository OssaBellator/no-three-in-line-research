#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import factorial

N = 30
J = 9
UNARY = 11


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def compositions(total):
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        for tail in compositions(total - first):
            yield (first,) + tail


def base_embedding(lengths):
    points = []
    labels = []
    lines = []
    used_columns = set()
    used_rows = set()
    for run_index, length in enumerate(lengths):
        slope = run_index + 1
        intercept = 0
        while any(y == slope * x + intercept for x, y in points):
            intercept += 1
        new_points = []
        column = 0
        while len(new_points) < length:
            row = slope * column + intercept
            point = (column, row)
            if column in used_columns or row in used_rows:
                column += 1
                continue
            if any(collinear(a, b, point) for a, b in combinations(points, 2)):
                column += 1
                continue
            new_points.append(point)
            used_columns.add(column)
            used_rows.add(row)
            column += 1
        points.extend(new_points)
        labels.extend([run_index] * length)
        lines.append((slope, intercept))
    return points, labels, lines


def anchored_embedding(lengths):
    points, labels, lines = base_embedding(lengths)
    used_columns = {x for x, _ in points}
    used_rows = {y for _, y in points}
    anchors = []
    for run_index, (slope, intercept) in enumerate(lines):
        selected = []
        column = max(used_columns, default=0) + 1
        while len(selected) < 2:
            row = slope * column + intercept
            point = (column, row)
            if column in used_columns or row in used_rows:
                column += 1
                continue
            labelled = list(zip(points, labels)) + anchors + [(chosen, run_index) for chosen in selected]
            if any(
                collinear(first, second, point) and not (first_label == second_label == run_index)
                for (first, first_label), (second, second_label) in combinations(labelled, 2)
            ):
                column += 1
                continue
            selected.append(point)
            used_columns.add(column)
            used_rows.add(row)
            column += 1
        anchors.extend((point, run_index) for point in selected)

    labelled = list(zip(points, labels)) + anchors
    mixed_triples = 0
    for triple in combinations(labelled, 3):
        if collinear(triple[0][0], triple[1][0], triple[2][0]):
            if len({triple[0][1], triple[1][1], triple[2][1]}) > 1:
                mixed_triples += 1
    assert mixed_triples == 0
    assert len({point[0] for point, _ in labelled}) == len(labelled)
    assert len({point[1] for point, _ in labelled}) == len(labelled)
    source_pair_blockers = 0
    for run_index, length in enumerate(lengths):
        run_anchors = [point for point, label in anchors if label == run_index]
        run_points = [point for point, label in zip(points, labels) if label == run_index]
        assert len(run_anchors) == 2
        assert all(collinear(run_anchors[0], run_anchors[1], point) for point in run_points)
        source_pair_blockers += len(run_points)
    return labelled, source_pair_blockers


composition_count = 0
maximum_coordinate = 0
anchor_histogram = Counter()
for lengths in compositions(UNARY):
    labelled, blockers = anchored_embedding(lengths)
    composition_count += 1
    assert blockers == UNARY
    anchor_histogram[2 * len(lengths)] += 1
    maximum_coordinate = max(
        maximum_coordinate,
        max(max(abs(x), abs(y)) for (x, y), _ in labelled),
    )

assert composition_count == 1024
assert maximum_coordinate == 419
assert anchor_histogram == Counter({
    2: 1, 4: 10, 6: 45, 8: 120, 10: 210, 12: 252,
    14: 210, 16: 120, 18: 45, 20: 10, 22: 1,
})


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (
        factorial(unary) * factorial(binary) * factorial(binary + 1)
    )

family = profile_count(N, J)
assert family == 168212023980
aggregate_source_pair_blockers = family * UNARY
assert aggregate_source_pair_blockers == 1850332263780

print({
    "unary_run_compositions_checked": composition_count,
    "synthetic_source_anchors_per_run": 2,
    "maximum_coordinate": maximum_coordinate,
    "all_anchor_and_inserted_rows_distinct": True,
    "all_anchor_and_inserted_columns_distinct": True,
    "cross_run_collinear_triples": 0,
    "source_anchor_pair_blockers_per_encoding": UNARY,
    "profile_family_size": family,
    "aggregate_source_anchor_pair_blockers": aggregate_source_pair_blockers,
    "mean_source_anchor_pair_blockers": str(Fraction(aggregate_source_pair_blockers, family)),
    "remaining_gap": "the two anchors per run are synthetic source points; they are not identified with retained prime-patching source cells or removal credit",
    "evidence_level": "explicit_synthetic_source_chord_lift",
    "status": "passed",
})
