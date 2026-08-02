#!/usr/bin/env python3
from itertools import permutations

N = 4
RESOURCE = 0
CONFLICTS = (
    ((0, 0), (1, 1)),
    ((0, 0), (1, 2)),
    ((0, 0), (1, 3)),
    ((0, 1), (1, 0)),
    ((0, 3), (2, 0)),
    ((0, 3), (3, 1)),
)

fibres = {(RESOURCE, right): set() for right in range(N)}
for first, second in CONFLICTS:
    centre, partner = (first, second) if first[0] == RESOURCE else (second, first)
    fibres[centre].add(partner)

records = []
for centre in sorted(fibres):
    removed_right = centre[1]
    left = tuple(range(1, N))
    right = tuple(value for value in range(N) if value != removed_right)
    partners = fibres[centre]
    partial_matching = (
        len({cell[0] for cell in partners}) == len(partners)
        and len({cell[1] for cell in partners}) == len(partners)
    )
    degrees = [sum(cell[0] == vertex for cell in partners) for vertex in left]
    degrees += [sum(cell[1] == vertex for cell in partners) for vertex in right]
    matchings = [
        image
        for image in permutations(right)
        if all((l, r) not in partners for l, r in zip(left, image))
    ]
    records.append((centre, len(partners), max(degrees, default=0), partial_matching, len(matchings)))

assert records == [
    ((0, 0), 3, 3, False, 0),
    ((0, 1), 1, 1, True, 4),
    ((0, 2), 0, 0, True, 6),
    ((0, 3), 2, 1, True, 3),
]
GOOD_CENTRES = tuple(record[0] for record in records if record[3])
BAD_CENTRES = tuple(record[0] for record in records if not record[3])
assert len(GOOD_CENTRES) == 3 and len(BAD_CENTRES) == 1

MIXED_DEGREE_TOTAL = 28

def pruned_pool_threshold(bad_centres: int) -> tuple[int, int]:
    return MIXED_DEGREE_TOTAL + bad_centres, MIXED_DEGREE_TOTAL

assert pruned_pool_threshold(1) == (29, 28)
assert 10 * len(GOOD_CENTRES) >= MIXED_DEGREE_TOTAL
assert 9 * len(GOOD_CENTRES) < MIXED_DEGREE_TOTAL

print({
    "source_fixture_centres": len(records),
    "centre_records": records,
    "matching_shaped_centres": GOOD_CENTRES,
    "bad_centres": BAD_CENTRES,
    "good_centre_fraction": "3/4",
    "mixed_degree_total_without_pruning": MIXED_DEGREE_TOTAL,
    "centred_side_threshold_with_b_bad_centres": "28+b",
    "opposite_side_threshold": 28,
    "fixture_motifs_needed_for_28_good_centres": 10,
    "remaining_gap": "the asymptotic source must bound bad centres and verify degree at most two for source and host-defect restrictions after pruning",
    "evidence_level": "exact_source_star_centre_pruning_interface",
    "status": "passed",
})
