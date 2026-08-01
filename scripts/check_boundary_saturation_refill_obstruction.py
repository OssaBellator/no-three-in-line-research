#!/usr/bin/env python3
from itertools import combinations, permutations, product

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
FIVE_WORD_PATTERNS = (
    (("P", 1), ("P", 1), ("P", 3), ("P", 1), ("P", 1)),
    (("P", 3), ("P", 3), ("P", 1), ("P", 3), ("P", 3)),
)
OFFSET_PATTERNS = (
    (-32, -26, 12, -28),
    (-28, 12, -26, -32),
    (28, -12, 26, 32),
    (32, 26, -12, 28),
)
# Exact sharp repairs extracted by scripts/check_boundary_three_point_seam_repair.py.
REPAIRS = (
    (0, ("P", 1), -31, ((5, -31), (16, -74), (18, -74))),
    (3, ("P", 1), 31, ((5, 34), (16, 77), (18, 77))),
    (4, ("P", 3), -31, ((4, -31), (17, -74), (19, -74))),
    (7, ("P", 3), 31, ((4, 34), (17, 77), (19, 77))),
)


def points_from_permutations(permutations_):
    return frozenset((x, permutation[x]) for permutation in permutations_ for x in range(len(permutation)))


def dihedral_variants(points, size):
    transforms = (
        lambda x, y: (x, y),
        lambda x, y: (y, size - 1 - x),
        lambda x, y: (size - 1 - x, size - 1 - y),
        lambda x, y: (size - 1 - y, x),
        lambda x, y: (size - 1 - x, y),
        lambda x, y: (x, size - 1 - y),
        lambda x, y: (y, x),
        lambda x, y: (size - 1 - y, size - 1 - x),
    )
    out = []
    for transform in transforms:
        variant = frozenset(transform(x, y) for x, y in points)
        if variant not in out:
            out.append(variant)
    return tuple(out)


VARIANTS = {
    name: dihedral_variants(points_from_permutations(data["permutations"]), data["size"])
    for name, data in BLOCKS.items()
}


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def first_collinear(points):
    for triple in combinations(sorted(points), 3):
        if collinear(*triple):
            return triple
    return None


def place(word, offsets):
    x_origin = 0
    y_origin = 0
    points = set()
    for index, node in enumerate(word):
        block_type, variant = node
        points.update((x_origin + x, y_origin + y) for x, y in VARIANTS[block_type][variant])
        x_origin += BLOCKS[block_type]["size"]
        if index < len(offsets):
            y_origin += offsets[index]
    return frozenset(points), x_origin, y_origin


five_states = []
for word, offsets in product(FIVE_WORD_PATTERNS, OFFSET_PATTERNS):
    points, x_end, y_origin = place(word, offsets)
    assert first_collinear(points) is None
    five_states.append((points, x_end, y_origin))
assert len(five_states) == 8

records = []
for state_index, target, offset, deleted in REPAIRS:
    old_points, x_end, y_origin = five_states[state_index]
    block_type, variant = target
    new_points = frozenset(
        (x_end + x, y_origin + offset + y)
        for x, y in VARIANTS[block_type][variant]
    )
    repaired = (old_points | new_points) - set(deleted)
    assert all(point in old_points for point in deleted)
    assert first_collinear(repaired) is None

    deleted_columns = tuple(sorted(point[0] for point in deleted))
    deleted_rows = tuple(sorted(point[1] for point in deleted))
    refill_candidates = sorted(
        {
            tuple(sorted(zip(deleted_columns, row_order)))
            for row_order in permutations(deleted_rows)
        }
    )
    assert len(refill_candidates) == 3

    failures = []
    legal_refills = []
    for refill in refill_candidates:
        assert set(refill).isdisjoint(repaired)
        witness = first_collinear(repaired | set(refill))
        if witness is None:
            legal_refills.append(refill)
        else:
            failures.append({"refill": refill, "triple": witness})
    assert legal_refills == []
    assert len(failures) == 3
    records.append(
        {
            "state_index": state_index,
            "target": target,
            "offset": offset,
            "deleted_points": deleted,
            "deficient_columns": deleted_columns,
            "deficient_rows": deleted_rows,
            "saturation_refills_checked": len(refill_candidates),
            "legal_saturation_refills": 0,
            "first_failure": failures[0],
        }
    )

assert sum(record["saturation_refills_checked"] for record in records) == 12

print({
    "sharp_three_deletion_repairs": len(records),
    "exact_row_column_refills_checked": 12,
    "legal_exact_refills": 0,
    "repair_records": records,
    "conclusion": "restoring exactly the deleted row and column degrees reintroduces a collinear triple in every case",
    "remaining_gap": "a valid boundary repair must alter a wider resource neighbourhood or replace rather than merely refill the deleted cells",
    "evidence_level": "exact_saturation_refill_obstruction",
    "status": "passed",
})
