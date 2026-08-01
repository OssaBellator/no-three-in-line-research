#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

UNARY_NODES = 11
SPACING = 20
N = 30
BINARY_NODES = 9

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def compositions(total):
    if total == 0:
        yield ()
        return
    for first in range(1, total + 1):
        for tail in compositions(total - first):
            yield (first,) + tail

def embed(lengths):
    points = []
    labels = []
    anchors = []
    used_columns = set()
    used_rows = set()
    for run_index, length in enumerate(lengths):
        parameter = SPACING * run_index
        first_anchor = (parameter, parameter * parameter)
        second_anchor = (parameter + 1, (parameter + 1) * (parameter + 1))
        for point in (first_anchor, second_anchor):
            assert point[0] not in used_columns and point[1] not in used_rows
            points.append(point)
            labels.append(run_index)
            anchors.append(point)
            used_columns.add(point[0])
            used_rows.add(point[1])
        direction = (1, 2 * parameter + 1)
        multiplier = 2
        inserted = 0
        while inserted < length:
            point = (first_anchor[0] + multiplier * direction[0], first_anchor[1] + multiplier * direction[1])
            multiplier += 1
            if point[0] in used_columns or point[1] in used_rows:
                continue
            if any(
                collinear(points[a], points[b], point) and not (labels[a] == labels[b] == run_index)
                for a, b in combinations(range(len(points)), 2)
            ):
                continue
            points.append(point)
            labels.append(run_index)
            used_columns.add(point[0])
            used_rows.add(point[1])
            inserted += 1
    assert all(not collinear(*triple) for triple in combinations(anchors, 3))
    for indices in combinations(range(len(points)), 3):
        if collinear(*(points[index] for index in indices)):
            assert len({labels[index] for index in indices}) == 1
    return points, anchors

composition_count = 0
maximum_coordinate = 0
for lengths in compositions(UNARY_NODES):
    points, anchors = embed(lengths)
    composition_count += 1
    maximum_coordinate = max(maximum_coordinate, max(max(abs(x), abs(y)) for x, y in points))
    assert len(points) == UNARY_NODES + 2 * len(lengths)
    assert len({x for x, _ in points}) == len(points) == len({y for _, y in points})
assert composition_count == 1024
assert maximum_coordinate == 40802

# Exact tree-profile count and aggregate number of maximal unary runs.
dp = [[{0: [0, 0], 1: [0, 0]} for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][0][0] = [1, 0]
for size in range(2, N + 1):
    for binary in range((size - 1) // 2 + 1):
        for root_unary, (count, run_total) in dp[size - 1][binary].items():
            if count:
                dp[size][binary][1][0] += count
                dp[size][binary][1][1] += run_total + (0 if root_unary else count)
        if binary:
            for left_size in range(1, size - 1):
                right_size = size - 1 - left_size
                for left_binary in range(binary):
                    right_binary = binary - 1 - left_binary
                    for _, (left_count, left_runs) in dp[left_size][left_binary].items():
                        for _, (right_count, right_runs) in dp[right_size][right_binary].items():
                            dp[size][binary][0][0] += left_count * right_count
                            dp[size][binary][0][1] += left_runs * right_count + right_runs * left_count
family = sum(dp[N][BINARY_NODES][root][0] for root in (0, 1))
aggregate_runs = sum(dp[N][BINARY_NODES][root][1] for root in (0, 1))
assert family == 168212023980
assert aggregate_runs == 1212286655580
assert Fraction(aggregate_runs, family) == Fraction(209, 29)

print({
    "unary_run_compositions_checked": composition_count,
    "retained_source_model": "distinct points on the integer parabola y=x^2, paired into secant anchors",
    "retained_source_no_three": True,
    "row_and_column_resources_distinct": True,
    "cross_run_collinear_triples": 0,
    "maximum_coordinate": maximum_coordinate,
    "profile_family_size": family,
    "aggregate_maximal_unary_runs": aggregate_runs,
    "mean_source_anchor_deletions_needed": str(Fraction(aggregate_runs, family)),
    "removal_credit_rule": "one deleted anchor per maximal unary run removes every anchor-pair blocker on that run line",
    "remaining_gap": "the parabola anchor source is explicit and no-three but is not the saturated retained source used by prime patching",
    "evidence_level": "explicit_parabola_retained_source_anchor_model",
    "status": "passed",
})
