#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations, product

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
RADIUS = 32
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


def points_from_permutations(perms):
    return frozenset((x, perm[x]) for perm in perms for x in range(len(perm)))


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
        image = frozenset(transform(x, y) for x, y in points)
        if image not in out:
            out.append(image)
    return tuple(out)


VARIANTS = {
    name: dihedral_variants(points_from_permutations(data["permutations"]), data["size"])
    for name, data in BLOCKS.items()
}
NODES = tuple((kind, variant) for kind in ("P", "Q") for variant in range(4))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def first_collinear(points):
    pts = tuple(sorted(points))
    for triple in combinations(pts, 3):
        if collinear(*triple):
            return triple
    return None


def place(word, offsets):
    x0 = y0 = 0
    points = set()
    for index, (kind, variant) in enumerate(word):
        points.update((x0 + x, y0 + y) for x, y in VARIANTS[kind][variant])
        x0 += BLOCKS[kind]["size"]
        if index < len(offsets):
            y0 += offsets[index]
    return frozenset(points), x0, y0


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
        frequencies = Counter(point for item in sets for point in item)
        branch = max(sets, key=lambda item: sum(frequencies[p] for p in item))
        for point in sorted(branch, key=lambda p: (-frequencies[p], p)):
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

sharp_repairs = []
for state_index, (_, _, old_points, x_end, y_origin) in enumerate(five_states):
    for target, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
        kind, variant = target
        new_points = frozenset(
            (x_end + x, y_origin + offset + y) for x, y in VARIANTS[kind][variant]
        )
        triples = bad_cross_triples(old_points, new_points)
        if not triples or hitting_set_at_most(triples, 2) is not None:
            continue
        witness = hitting_set_at_most(triples, 3)
        if witness is None or not all(point in old_points for point in witness):
            continue
        original = old_points | new_points
        repaired = original - set(witness)
        if first_collinear(repaired) is None:
            sharp_repairs.append((state_index, target, offset, tuple(sorted(witness)), original))
assert len(sharp_repairs) == 4


def candidate_legal(base, additions):
    if len(set(additions)) != len(additions) or any(point in base for point in additions):
        return False
    base_points = tuple(base)
    for point in additions:
        for first, second in combinations(base_points, 2):
            if collinear(first, second, point):
                return False
    for first, second in combinations(additions, 2):
        for point in base_points:
            if collinear(first, second, point):
                return False
    return all(not collinear(*triple) for triple in combinations(additions, 3))


search_cases = 0
matching_candidates = 0
legal = []
repair_stats = []
for repair_index, (_, _, _, deleted_three, original) in enumerate(sharp_repairs):
    repaired = original - set(deleted_three)
    local_cases = 0
    local_matchings = 0
    local_legal = 0
    for extra_deleted in combinations(sorted(repaired), 2):
        deleted = set(deleted_three) | set(extra_deleted)
        column_mult = Counter(x for x, _ in deleted)
        row_mult = Counter(y for _, y in deleted)
        columns = [column for column, count in column_mult.items() for _ in range(count)]
        rows = [row for row, count in row_mult.items() for _ in range(count)]
        local_cases += 1
        seen = set()
        for row_order in permutations(rows):
            additions = tuple((columns[index], row_order[index]) for index in range(5))
            key = tuple(sorted(additions))
            if key in seen or len(set(additions)) < 5:
                continue
            seen.add(key)
            local_matchings += 1
            base = original - deleted
            if candidate_legal(base, additions):
                local_legal += 1
                legal.append((repair_index, extra_deleted, tuple(sorted(additions))))
    search_cases += local_cases
    matching_candidates += local_matchings
    repair_stats.append((local_cases, local_matchings, local_legal))

assert search_cases == 3960
assert matching_candidates == 210092
assert legal == []
assert repair_stats == [(990, 52523, 0)] * 4

print({
    "sharp_three_deletion_repairs": len(sharp_repairs),
    "two_additional_deletion_cases": search_cases,
    "unique_degree_preserving_five_point_refills": matching_candidates,
    "legal_five_point_refills": len(legal),
    "per_repair_counts": repair_stats,
    "conclusion": "two further deleted incidences and exact five-point degree refill still do not complete any sharp seam repair",
    "remaining_gap": "the corrector must leave the five deleted row-column support, change at least three more incidences, or replace the block geometry",
    "evidence_level": "exact_five_point_boundary_repair_obstruction",
    "status": "passed",
})
