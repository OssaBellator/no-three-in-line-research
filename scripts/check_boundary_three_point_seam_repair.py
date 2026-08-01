#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations, product

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
RADIUS = 32


def points_from_permutations(permutations):
    return frozenset((x, permutation[x]) for permutation in permutations for x in range(len(permutation)))


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
    variants = []
    for transform in transforms:
        variant = frozenset(transform(x, y) for x, y in points)
        if variant not in variants:
            variants.append(variant)
    return tuple(variants)


VARIANTS = {
    name: dihedral_variants(points_from_permutations(data["permutations"]), data["size"])
    for name, data in BLOCKS.items()
}
NODES = tuple((block_type, variant) for block_type in ("P", "Q") for variant in range(4))

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


def bad_cross_triples(old_points, new_points):
    triples = set()
    for a, b in combinations(old_points, 2):
        for c in new_points:
            if collinear(a, b, c):
                triples.add(tuple(sorted((a, b, c))))
    for a, b in combinations(new_points, 2):
        for c in old_points:
            if collinear(a, b, c):
                triples.add(tuple(sorted((a, b, c))))
    return tuple(sorted(triples))


def hitting_set_at_most(triples, limit):
    family = tuple(frozenset(triple) for triple in triples)

    @lru_cache(None)
    def search(remaining, budget):
        if not remaining:
            return ()
        if budget == 0:
            return None
        sets = [set(item) for item in remaining]
        frequencies = {}
        for item in sets:
            for point in item:
                frequencies[point] = frequencies.get(point, 0) + 1
        branch = max(sets, key=lambda item: sum(frequencies[point] for point in item))
        for point in sorted(branch, key=lambda item: (-frequencies[item], item)):
            next_remaining = tuple(
                sorted(
                    (frozenset(item) for item in sets if point not in item),
                    key=lambda item: tuple(sorted(item)),
                )
            )
            tail = search(next_remaining, budget - 1)
            if tail is not None:
                return (point,) + tail
        return None

    canonical = tuple(sorted(family, key=lambda item: tuple(sorted(item))))
    return search(canonical, limit)


five_states = []
for word, offsets in product(FIVE_WORD_PATTERNS, OFFSET_PATTERNS):
    points, x_end, y_origin = place(word, offsets)
    if first_collinear(points) is None:
        five_states.append((word, offsets, points, x_end, y_origin))

assert len(five_states) == 8

attempts = 0
repairable_with_two = []
repairable_with_three = []
for state_index, (_, _, old_points, x_end, y_origin) in enumerate(five_states):
    for target, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
        attempts += 1
        block_type, variant = target
        new_points = frozenset(
            (x_end + x, y_origin + offset + y)
            for x, y in VARIANTS[block_type][variant]
        )
        triples = bad_cross_triples(old_points, new_points)
        assert triples
        witness_two = hitting_set_at_most(triples, 2)
        if witness_two is not None:
            repairable_with_two.append((state_index, target, offset, witness_two))
            continue
        witness_three = hitting_set_at_most(triples, 3)
        if witness_three is not None:
            repaired = (old_points | new_points) - set(witness_three)
            assert first_collinear(repaired) is None
            assert all(point in old_points for point in witness_three)
            repairable_with_three.append(
                {
                    "state_index": state_index,
                    "target": target,
                    "offset": offset,
                    "deleted_points": tuple(sorted(witness_three)),
                    "bad_triples_before_repair": len(triples),
                    "deleted_columns": len({point[0] for point in witness_three}),
                    "deleted_rows": len({point[1] for point in witness_three}),
                }
            )

assert attempts == 4160
assert repairable_with_two == []
assert len(repairable_with_three) == 4
assert {entry["bad_triples_before_repair"] for entry in repairable_with_three} == {10}
assert {entry["deleted_columns"] for entry in repairable_with_three} == {3}
assert {entry["deleted_rows"] for entry in repairable_with_three} == {2}

print({
    "offset_radius": RADIUS,
    "five_block_survivors": len(five_states),
    "sixth_block_attempts": attempts,
    "extensions_repairable_with_at_most_two_deletions": len(repairable_with_two),
    "extensions_repairable_with_exactly_three_deletions": len(repairable_with_three),
    "three_deletion_certificates": repairable_with_three,
    "minimum_point_deletions": 3,
    "remaining_gap": "the three deletions create row and column deficits that need a separate saturation repair",
    "evidence_level": "exact_coordinate_repair_catalogue",
    "status": "passed",
})
