#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from math import gcd

BLOCKS = {
    "P": {
        "size": 4,
        "permutations": ((0, 1, 3, 2), (2, 3, 1, 0)),
    },
    "Q": {
        "size": 7,
        "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1)),
    },
}


def points_from_permutations(perms):
    return frozenset(
        (x, perm[x])
        for perm in perms
        for x in range(len(perm))
    )


def degree_profile(points, size):
    rows = Counter(x for x, _ in points)
    cols = Counter(y for _, y in points)
    return tuple(rows[i] for i in range(size)), tuple(cols[i] for i in range(size))


def first_collinear(points):
    for a, b, c in combinations(sorted(points), 3):
        if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
            return (a, b, c)
    return None


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


def ports(points, size):
    left = tuple(sorted(y for x, y in points if x == 0))
    right = tuple(sorted(y for x, y in points if x == size - 1))
    return left, right


def diagonal_seam(left, right, left_size):
    shifted = frozenset((left_size + x, left_size + y) for x, y in right)
    union = frozenset(left | shifted)
    return first_collinear(union)


point_sets = {}
variants = {}
for name, data in BLOCKS.items():
    size = data["size"]
    points = points_from_permutations(data["permutations"])
    rows, cols = degree_profile(points, size)
    assert len(points) == 2 * size
    assert rows == (2,) * size
    assert cols == (2,) * size
    assert first_collinear(points) is None
    point_sets[name] = points
    variants[name] = dihedral_variants(points, size)

assert len(variants["P"]) == 4
assert len(variants["Q"]) == 4

seam_attempts = 0
legal_seams = []
witnesses = {}
slope_histogram = Counter()
for left_name in ("P", "Q"):
    for right_name in ("P", "Q"):
        left_size = BLOCKS[left_name]["size"]
        for left_index, left in enumerate(variants[left_name]):
            for right_index, right in enumerate(variants[right_name]):
                seam_attempts += 1
                witness = diagonal_seam(left, right, left_size)
                if witness is None:
                    legal_seams.append((left_name, left_index, right_name, right_index))
                    continue
                witnesses.setdefault(
                    f"{left_name}->{right_name}",
                    {
                        "left_variant": left_index,
                        "right_variant": right_index,
                        "triple": witness,
                    },
                )
                dx = witness[1][0] - witness[0][0]
                dy = witness[1][1] - witness[0][1]
                divisor = gcd(abs(dx), abs(dy)) or 1
                slope_histogram[(dy // divisor, dx // divisor)] += 1

assert seam_attempts == 64
assert legal_seams == []
assert set(witnesses) == {"P->P", "P->Q", "Q->P", "Q->Q"}
assert sum(slope_histogram.values()) == seam_attempts
assert slope_histogram[(1, 1)] == 29

print({
    "blocks": {
        name: {
            "size": BLOCKS[name]["size"],
            "points": sorted(point_sets[name]),
            "dihedral_variants": len(variants[name]),
            "ports": [ports(v, BLOCKS[name]["size"]) for v in variants[name]],
        }
        for name in ("P", "Q")
    },
    "seam_attempts": seam_attempts,
    "legal_seams": len(legal_seams),
    "first_failure_witnesses": witnesses,
    "most_common_failure_slope": slope_histogram.most_common(1)[0],
    "evidence_level": "independently_enumerated_candidate",
    "status": "passed",
})
