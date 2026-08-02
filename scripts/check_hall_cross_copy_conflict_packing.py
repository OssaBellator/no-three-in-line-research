#!/usr/bin/env python3
from math import ceil

TARGET = 28
GOOD_PER_MOTIF = 3

def guaranteed_independent_set(motifs: int, extra_corruptions: int, cross_degree: int) -> int:
    good = max(0, GOOD_PER_MOTIF * motifs - extra_corruptions)
    return ceil(good / (cross_degree + 1))

def exact_motif_threshold(extra_corruptions: int, cross_degree: int) -> int:
    required_good = (TARGET - 1) * (cross_degree + 1) + 1
    return ceil((required_good + extra_corruptions) / GOOD_PER_MOTIF)

assert [exact_motif_threshold(0, degree) for degree in range(7)] == [10, 19, 28, 37, 46, 55, 64]
assert exact_motif_threshold(2, 0) == 10
assert exact_motif_threshold(3, 0) == 11

for degree in range(7):
    threshold = exact_motif_threshold(0, degree)
    assert guaranteed_independent_set(threshold, 0, degree) >= TARGET
    assert guaranteed_independent_set(threshold - 1, 0, degree) < TARGET

for degree in range(5):
    d = degree + 1
    for vertices in range(0, 27 * d + 1):
        assert ceil(vertices / d) <= 27

print({
    "good_centres_per_motif": GOOD_PER_MOTIF,
    "hall_target": TARGET,
    "guaranteed_independent_set": "ceil((3t-e)/(Delta+1))",
    "exact_good_vertex_threshold": "27*(Delta+1)+1",
    "exact_motif_threshold": "ceil((27*(Delta+1)+1+e)/3)",
    "zero_corruption_thresholds_Delta_0_through_6": tuple(exact_motif_threshold(0, degree) for degree in range(7)),
    "sharpness_model": "partition into at most 27 cliques of size at most Delta+1",
    "remaining_gap": "the geometric host must bound the cross-copy collision degree and still prove degree at most two for the source and host-defect restrictions",
    "evidence_level": "exact_cross_copy_conflict_degree_interface",
    "status": "passed",
})
