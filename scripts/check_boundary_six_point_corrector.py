#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import combinations, product

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
RADIUS = 32
FIVE_WORD_PATTERNS = (
    (("P", 1), ("P", 1), ("P", 3), ("P", 1), ("P", 1)),
    (("P", 3), ("P", 3), ("P", 1), ("P", 3), ("P", 3)),
)
OFFSET_PATTERNS = ((-32, -26, 12, -28), (-28, 12, -26, -32), (28, -12, 26, 32), (32, 26, -12, 28))


def point_set(permutations):
    return frozenset((x, permutation[x]) for permutation in permutations for x in range(len(permutation)))


def variants(points, size):
    transforms = (
        lambda x, y: (x, y), lambda x, y: (y, size - 1 - x),
        lambda x, y: (size - 1 - x, size - 1 - y), lambda x, y: (size - 1 - y, x),
        lambda x, y: (size - 1 - x, y), lambda x, y: (x, size - 1 - y),
        lambda x, y: (y, x), lambda x, y: (size - 1 - y, size - 1 - x),
    )
    result = []
    for transform in transforms:
        image = frozenset(transform(x, y) for x, y in points)
        if image not in result:
            result.append(image)
    return tuple(result)


VARIANTS = {name: variants(point_set(data["permutations"]), data["size"]) for name, data in BLOCKS.items()}
NODES = tuple((kind, variant) for kind in ("P", "Q") for variant in range(4))


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def first_collinear(points):
    for triple in combinations(sorted(points), 3):
        if collinear(*triple):
            return triple
    return None


def place(word, offsets):
    x_origin = y_origin = 0
    points = set()
    for index, (kind, variant) in enumerate(word):
        points.update((x_origin + x, y_origin + y) for x, y in VARIANTS[kind][variant])
        x_origin += BLOCKS[kind]["size"]
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
        frequency = Counter(point for item in sets for point in item)
        branch = max(sets, key=lambda item: sum(frequency[point] for point in item))
        for point in sorted(branch, key=lambda item: (-frequency[item], item)):
            next_remaining = tuple(sorted((frozenset(item) for item in sets if point not in item), key=lambda item: tuple(sorted(item))))
            tail = search(next_remaining, budget - 1)
            if tail is not None:
                return (point,) + tail
        return None

    return search(tuple(sorted(family, key=lambda item: tuple(sorted(item)))), limit)


def line(a, b):
    return b[1] - a[1], a[0] - b[0], -((b[1] - a[1]) * a[0] + (a[0] - b[0]) * a[1])


def on_line(point, equation):
    return equation[0] * point[0] + equation[1] * point[1] + equation[2] == 0


def one_legal_refill(base, columns, rows):
    base = tuple(base)
    inherited_lines = tuple(line(a, b) for a, b in combinations(base, 2))
    column_counts = Counter(columns)
    row_counts = Counter(rows)
    ordered_columns = sorted(columns, key=lambda column: (-column_counts[column], column))
    chosen = []

    def search(index):
        if index == len(ordered_columns):
            return tuple(sorted(chosen))
        column = ordered_columns[index]
        previous_row = chosen[-1][1] if index and ordered_columns[index - 1] == column else None
        for row in sorted(row_counts):
            if not row_counts[row] or (previous_row is not None and row <= previous_row):
                continue
            point = (column, row)
            if point in base or point in chosen or any(on_line(point, equation) for equation in inherited_lines):
                continue
            if any(collinear(a, b, point) for a, b in combinations(chosen, 2)):
                continue
            if any(collinear(old, selected, point) for selected in chosen for old in base):
                continue
            row_counts[row] -= 1
            chosen.append(point)
            result = search(index + 1)
            if result is not None:
                return result
            chosen.pop()
            row_counts[row] += 1
        return None

    return search(0)


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
        new_points = frozenset((x_end + x, y_origin + offset + y) for x, y in VARIANTS[kind][variant])
        triples = bad_cross_triples(old_points, new_points)
        if not triples or hitting_set_at_most(triples, 2) is not None:
            continue
        witness = hitting_set_at_most(triples, 3)
        if witness is not None and all(point in old_points for point in witness):
            original = old_points | new_points
            if first_collinear(original - set(witness)) is None:
                sharp_repairs.append((state_index, target, offset, tuple(sorted(witness)), original))
assert len(sharp_repairs) == 4

witnesses = []
examined_cases = []
for state_index, target, offset, deleted_three, original in sharp_repairs:
    repaired = original - set(deleted_three)
    witness = None
    examined = 0
    for extra_deleted in combinations(sorted(repaired), 3):
        examined += 1
        deleted = set(deleted_three) | set(extra_deleted)
        column_counts = Counter(x for x, _ in deleted)
        row_counts = Counter(y for _, y in deleted)
        columns = [column for column, count in column_counts.items() for _ in range(count)]
        rows = [row for row, count in row_counts.items() for _ in range(count)]
        additions = one_legal_refill(original - deleted, columns, rows)
        if additions is not None:
            candidate = (original - deleted) | set(additions)
            assert len(candidate) == len(original)
            assert first_collinear(candidate) is None
            assert Counter(x for x, _ in deleted) == Counter(x for x, _ in additions)
            assert Counter(y for _, y in deleted) == Counter(y for _, y in additions)
            witness = (tuple(sorted(deleted)), additions, candidate)
            break
    assert witness is not None
    examined_cases.append(examined)
    witnesses.append((state_index, target, offset, *witness))

assert examined_cases == [1863, 1864, 57, 56]
assert len(witnesses) == 4

seventh_extensions = []
for state_index, target, offset, deleted, additions, corrected in witnesses:
    _, _, _, x_end, y_origin = five_states[state_index]
    sixth_y_origin = y_origin + offset
    next_x_origin = x_end + BLOCKS[target[0]]["size"]
    local = []
    for next_node, next_offset in product(NODES, range(-RADIUS, RADIUS + 1)):
        kind, variant = next_node
        next_block = {(next_x_origin + x, sixth_y_origin + next_offset + y) for x, y in VARIANTS[kind][variant]}
        if first_collinear(set(corrected) | next_block) is None:
            local.append((next_node, next_offset))
    seventh_extensions.append(tuple(local))
assert seventh_extensions == [(), (), (), ()]

print({
    "sharp_three_deletion_repairs": len(sharp_repairs),
    "minimum_degree_preserving_refill_size": 6,
    "six_point_correctors": [
        {"state_index": state_index, "target": target, "offset": offset, "deleted": deleted, "added": additions}
        for state_index, target, offset, deleted, additions, _ in witnesses
    ],
    "extra_deletion_cases_examined_before_lexicographic_witness": examined_cases,
    "raw_seventh_block_attempts": len(witnesses) * len(NODES) * (2 * RADIUS + 1),
    "raw_seventh_block_extensions_within_radius_32": 0,
    "remaining_gap": "the exact six-point seam corrector does not compose with an uncorrected seventh block inside the audited radius",
    "evidence_level": "exact_degree_preserving_boundary_corrector",
    "status": "passed",
})
