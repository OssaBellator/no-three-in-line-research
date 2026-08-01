#!/usr/bin/env python3
from itertools import combinations, permutations

ROWS = range(4)
COLUMNS = range(4)


def decoded_pair(syndrome, choice):
    return ((0, choice), (1, (choice + syndrome + 1) % 4))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def legal(points):
    return all(not collinear(*triple) for triple in combinations(points, 3))


def minimal_blockers(extensions):
    used_cells = sorted(set().union(*(set(extension[2:]) for extension in extensions)))
    for size in range(1, len(used_cells) + 1):
        blockers = []
        for subset in combinations(used_cells, size):
            forbidden = set(subset)
            if all(forbidden.intersection(extension[2:]) for extension in extensions):
                blockers.append(subset)
        if blockers:
            return tuple(blockers)
    raise AssertionError("extensions must have a blocker")


records = {}
for syndrome in range(3):
    for choice in range(4):
        pair = decoded_pair(syndrome, choice)
        used_columns = {column for _, column in pair}
        remaining_columns = tuple(column for column in COLUMNS if column not in used_columns)
        extensions = []
        for assignment in permutations(remaining_columns):
            matching = pair + ((2, assignment[0]), (3, assignment[1]))
            if legal(matching):
                extensions.append(matching)
        assert extensions
        blockers = minimal_blockers(tuple(extensions))
        records[(syndrome, choice)] = {
            "pair": pair,
            "extensions": tuple(extensions),
            "extension_count": len(extensions),
            "minimum_blocker_size": len(blockers[0]),
            "minimum_blockers": blockers,
        }

assert len(records) == 12
assert sum(record["extension_count"] for record in records.values()) == 18
assert sorted(record["extension_count"] for record in records.values()) == [1] * 6 + [2] * 6
assert sorted(record["minimum_blocker_size"] for record in records.values()) == [1] * 6 + [2] * 6
assert all(
    len(record["minimum_blockers"]) == (2 if record["extension_count"] == 1 else 4)
    for record in records.values()
)

fragile = tuple(key for key, record in records.items() if record["minimum_blocker_size"] == 1)
robust = tuple(key for key, record in records.items() if record["minimum_blocker_size"] == 2)
assert len(fragile) == len(robust) == 6

print({
    "decoded_pairs": len(records),
    "total_no_three_in_line_extensions": 18,
    "single_exclusion_fragile_pairs": len(fragile),
    "single_exclusion_robust_pairs": len(robust),
    "fragile_pair_keys": fragile,
    "robust_pair_keys": robust,
    "minimum_blocker_sizes": {
        f"{syndrome}:{choice}": record["minimum_blocker_size"]
        for (syndrome, choice), record in records.items()
    },
    "conclusion": "the complete-grid decoder is not uniformly robust to one host-specific forbidden residual cell",
    "evidence_level": "coordinate_host_robustness_obstruction",
    "status": "passed",
})
