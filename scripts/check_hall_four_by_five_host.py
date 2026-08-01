#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations

ROWS = range(4)
HOST_COLUMNS = range(5)
LABELS = range(4)

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def legal(points):
    return all(not collinear(*triple) for triple in combinations(points, 3))

def blocker_number(extensions):
    cells = sorted(set().union(*(set(extension[2:]) for extension in extensions)))
    for size in range(1, len(cells) + 1):
        for subset in combinations(cells, size):
            forbidden = set(subset)
            if all(forbidden.intersection(extension[2:]) for extension in extensions):
                return size
    raise AssertionError("nonempty extension family must have a blocker")

def audit(injection):
    records = {}
    for syndrome in range(3):
        for choice in LABELS:
            pair = (
                (0, injection[choice]),
                (1, injection[(choice + syndrome + 1) % 4]),
            )
            used_columns = {column for _, column in pair}
            remaining = tuple(column for column in HOST_COLUMNS if column not in used_columns)
            extensions = []
            for assignment in permutations(remaining, 2):
                matching = pair + ((2, assignment[0]), (3, assignment[1]))
                if legal(matching):
                    extensions.append(matching)
            assert extensions
            records[(syndrome, choice)] = {
                "extensions": tuple(extensions),
                "extension_count": len(extensions),
                "blocker_number": blocker_number(tuple(extensions)),
            }
    return records

summaries = Counter()
canonical = None
for injection in permutations(HOST_COLUMNS, 4):
    records = audit(injection)
    minimum = min(record["blocker_number"] for record in records.values())
    summaries[minimum] += 1
    if injection == (0, 1, 2, 3):
        canonical = records

assert summaries == Counter({2: 120})
assert canonical is not None
assert sum(record["extension_count"] for record in canonical.values()) == 51
assert Counter(record["extension_count"] for record in canonical.values()) == Counter({3: 4, 4: 4, 6: 3, 5: 1})
assert Counter(record["blocker_number"] for record in canonical.values()) == Counter({2: 7, 3: 5})

print({
    "coordinate_host": "4 rows by 5 columns",
    "label_injections_checked": 120,
    "minimum_blocker_number_for_every_injection": 2,
    "canonical_total_legal_extensions": 51,
    "canonical_extension_count_histogram": dict(sorted(Counter(record["extension_count"] for record in canonical.values()).items())),
    "canonical_blocker_histogram": dict(sorted(Counter(record["blocker_number"] for record in canonical.values()).items())),
    "conclusion": "one extra host column removes all singleton residual blockers",
    "remaining_gap": "the five-column host is not yet identified with an actual prime-patching endpoint host and its source exclusions",
    "evidence_level": "coordinate_level_enlarged_hall_host",
    "status": "passed",
})
