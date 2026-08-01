#!/usr/bin/env python3
from collections import defaultdict
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


def embed_run_lengths(lengths):
    points = []
    run_labels = []
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
        if len(new_points) >= 2:
            assert all(not collinear(old, new_points[0], new_points[-1]) for old in points)
        points.extend(new_points)
        run_labels.extend([run_index] * length)

    triples = []
    for indices in combinations(range(len(points)), 3):
        if collinear(*(points[index] for index in indices)):
            triples.append(indices)
    expected = sum(length * (length - 1) * (length - 2) // 6 for length in lengths)
    assert len(triples) == expected
    assert all(run_labels[a] == run_labels[b] == run_labels[c] for a, b, c in triples)
    assert len({x for x, _ in points}) == len(points) == len({y for _, y in points})
    return points, len(triples)


composition_histogram = defaultdict(int)
maximum_coordinate = 0
composition_count = 0
for lengths in compositions(UNARY):
    points, triples = embed_run_lengths(lengths)
    composition_count += 1
    composition_histogram[triples] += 1
    maximum_coordinate = max(maximum_coordinate, max(max(abs(x), abs(y)) for x, y in points))
assert composition_count == 1024
assert maximum_coordinate == 113


def profile_count(size, binary):
    unary = size - 1 - 2 * binary
    if unary < 0:
        return 0
    return factorial(size - 1) // (factorial(unary) * factorial(binary) * factorial(binary + 1))


def choose_three(value):
    return value * (value - 1) * (value - 2) // 6


dp = [[defaultdict(lambda: [0, 0]) for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0][0] = [1, 0]
for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for top_run, (count, total) in tuple(dp[size - 1][binary].items()):
            next_run = top_run + 1 if top_run else 1
            record = dp[size][binary][next_run]
            record[0] += count
            record[1] += total
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for left_run, (left_count, left_total) in dp[left_size][left_binary].items():
                        for right_run, (right_count, right_total) in dp[right_size][right_binary].items():
                            record = dp[size][binary][0]
                            record[0] += left_count * right_count
                            record[1] += (left_total + choose_three(left_run) * left_count) * right_count
                            record[1] += (right_total + choose_three(right_run) * right_count) * left_count

family = sum(record[0] for record in dp[N][J].values())
aggregate = sum(record[1] + choose_three(top_run) * record[0] for top_run, record in dp[N][J].items())
assert family == profile_count(N, J) == 168212023980
assert aggregate == 396499770810
assert Fraction(aggregate, family) == Fraction(33, 14)

print({
    "unary_run_compositions_checked": composition_count,
    "maximum_coordinate_in_canonical_greedy_audit": maximum_coordinate,
    "row_and_column_resources_distinct": True,
    "cross_run_collinear_triples": 0,
    "family_size": family,
    "aggregate_exact_collinear_triples": aggregate,
    "mean_exact_collinear_triples": str(Fraction(aggregate, family)),
    "remaining_gap": "the integer run lines are a canonical encoding geometry and are not yet identified with source-derived prime-patching support chords",
    "evidence_level": "row_column_distinct_ancestry_geometry",
    "status": "passed",
})
