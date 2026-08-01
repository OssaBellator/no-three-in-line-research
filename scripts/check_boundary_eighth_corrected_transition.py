#!/usr/bin/env python3
"""Audit all small eighth-step transversals and the unique corrected transition."""
from __future__ import annotations

from collections import Counter
from itertools import product
from runpy import run_path

previous = run_path("scripts/check_boundary_corrector_transition_state.py")
VARIANTS = previous["VARIANTS"]
NODES = previous["NODES"]
RADIUS = previous["RADIUS"]
bad_cross_triples = previous["bad_cross_triples"]
hitting_set_at_most = previous["hitting_set_at_most"]
all_hitting_sets = previous["all_hitting_sets"]
correction_from_core = previous["correction_from_core"]
first_collinear = previous["first_collinear"]
seventh_corrected = previous["seventh_corrected"]
next_x = previous["next_x"]
next_y = previous["next_y"]

histogram: Counter[object] = Counter()
small_records = []
for node, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
    kind, variant = node
    block = frozenset(
        (next_x + x, next_y + offset + y)
        for x, y in VARIANTS[kind][variant]
    )
    triples = bad_cross_triples(seventh_corrected, block)
    minimum = None
    for size in range(1, 7):
        if hitting_set_at_most(triples, size) is not None:
            minimum = size
            break
    histogram[minimum if minimum is not None else ">6"] += 1
    if minimum is not None and minimum <= 5:
        transversals = all_hitting_sets(triples, minimum)
        small_records.append((node, offset, minimum, triples, transversals, block))

assert histogram == {4: 1, 5: 6, 6: 21, ">6": 492}
assert len(small_records) == 7
assert sum(len(record[4]) for record in small_records) == 21

successful = []
for node, offset, minimum, triples, transversals, block in small_records:
    original = set(seventh_corrected) | set(block)
    for transversal_index, core in enumerate(transversals):
        correction = correction_from_core(original, core, maximum_extra=2)
        if correction is not None:
            successful.append(
                (node, offset, minimum, transversal_index, core, correction, block)
            )

assert len(successful) == 1
node, offset, minimum, transversal_index, core, correction, eighth_block = successful[0]
assert (node, offset, minimum, transversal_index) == (("P", 1), 31, 5, 4)
assert correction[0] == 7
assert correction[2] == (
    (0, 2), (1, 3), (23, 108), (24, 49), (28, 110), (28, 113), (30, 110)
)
assert correction[3] == (
    (0, 110), (1, 113), (23, 2), (24, 110), (28, 3), (28, 108), (30, 49)
)

eighth_corrected = correction[4]
assert len(eighth_corrected) == 64
assert first_collinear(eighth_corrected) is None
ninth_x = next_x + 4
ninth_y = next_y + offset
raw_ninth = []
for ninth_node, ninth_offset in product(NODES, range(-RADIUS, RADIUS + 1)):
    kind, variant = ninth_node
    block = {
        (ninth_x + x, ninth_y + ninth_offset + y)
        for x, y in VARIANTS[kind][variant]
    }
    if first_collinear(set(eighth_corrected) | block) is None:
        raw_ninth.append((ninth_node, ninth_offset))
assert raw_ninth == []

print({
    "raw_eighth_attempts": len(NODES) * (2 * RADIUS + 1),
    "minimum_transversal_histogram_through_six": dict(histogram),
    "minimum_transversals_for_sizes_four_and_five": 21,
    "degree_preserving_corrected_eighth_transitions": len(successful),
    "corrected_transition": {
        "eighth_block": node,
        "offset": offset,
        "minimum_transversal_size": minimum,
        "minimum_transversal_index": transversal_index,
        "minimum_transversal": core,
        "degree_corrector_size": correction[0],
        "deleted": correction[2],
        "added": correction[3],
        "two_step_vertical_drift": 5,
    },
    "corrected_eighth_state_points": len(eighth_corrected),
    "raw_ninth_attempts": len(NODES) * (2 * RADIUS + 1),
    "raw_ninth_extensions": 0,
    "remaining_gap": "a two-edge corrected path exists, but there is no raw ninth step or corrected-state cycle",
    "evidence_level": "exact_repeated_boundary_corrector_transition",
    "status": "passed",
})
