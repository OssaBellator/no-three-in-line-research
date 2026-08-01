#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

ROWS = range(4)
COLUMNS = range(4)


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal(points):
    return all(not collinear(*triple) for triple in combinations(points, 3))


def extensions(pair):
    used_columns = {column for _, column in pair}
    remaining = tuple(column for column in COLUMNS if column not in used_columns)
    out = []
    for assignment in permutations(remaining):
        matching = pair + ((2, assignment[0]), (3, assignment[1]))
        if legal(matching):
            out.append(matching)
    return tuple(out)


pairs = tuple(
    ((0, first), (1, second))
    for first in COLUMNS
    for second in COLUMNS
    if first != second
)
assert len(pairs) == 12
extension_table = {pair: extensions(pair) for pair in pairs}
assert all(extension_table.values())
assert sum(len(value) for value in extension_table.values()) == 18

fragile = tuple(pair for pair in pairs if len(extension_table[pair]) == 1)
robust = tuple(pair for pair in pairs if len(extension_table[pair]) == 2)
assert len(fragile) == len(robust) == 6

# Every complete injective decoder from the twelve quotient choices to the twelve
# ordered distinct grid pairs is a bijection, so it necessarily contains the
# same six fragile geometries. Relabelling cannot increase the minimum blocker.
complete_decoder_minimum_blocker = 1

killed_by_cell = {}
for cell in tuple((2, column) for column in COLUMNS) + tuple((3, column) for column in COLUMNS):
    killed = tuple(
        pair
        for pair, pair_extensions in extension_table.items()
        if all(cell in extension[2:] for extension in pair_extensions)
    )
    killed_by_cell[cell] = killed

killed_histogram = Counter(len(value) for value in killed_by_cell.values())
assert killed_histogram == Counter({1: 4, 2: 4})
assert max(12 - len(value) for value in killed_by_cell.values()) == 11
assert min(12 - len(value) for value in killed_by_cell.values()) == 10

print({
    "ordered_distinct_grid_pairs": len(pairs),
    "fragile_pair_geometries": len(fragile),
    "robust_pair_geometries": len(robust),
    "best_possible_minimum_blocker_for_complete_bijection": complete_decoder_minimum_blocker,
    "single_forbidden_residual_cell_kill_histogram": dict(sorted(killed_histogram.items())),
    "best_surviving_quotient_choices_after_one_fixed_cell_exclusion": 11,
    "worst_surviving_quotient_choices_after_one_fixed_cell_exclusion": 10,
    "killed_pairs_by_cell": {str(cell): value for cell, value in killed_by_cell.items()},
    "conclusion": "no alternative bijection onto the complete twelve-pair grid can make every quotient choice single-exclusion robust",
    "remaining_gap": "a robust decoder must use a larger host, extra residual extensions, or abandon complete bijective coverage of the twelve pair geometries",
    "evidence_level": "exact_decoder_robustness_upper_bound",
    "status": "passed",
})
