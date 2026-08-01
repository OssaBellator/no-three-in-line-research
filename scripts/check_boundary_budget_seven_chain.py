#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import gcd

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
RADIUS = 32
SEVENTH_CORRECTED = frozenset({
    (0, 2), (0, 79), (1, 3), (1, 61), (2, 1), (2, 2), (3, 0), (3, 3),
    (4, 33), (4, 77), (5, 32), (5, 35), (6, 33), (6, 34), (7, 32), (7, 35),
    (8, 34), (8, 105), (9, 59), (9, 60), (10, 58), (10, 61), (11, 59), (11, 60),
    (12, 47), (12, 48), (13, 46), (13, 77), (14, 47), (14, 48), (15, 46), (15, 49),
    (16, 75), (16, 76), (17, 1), (17, 74), (18, 75), (18, 76), (19, 0), (19, 74),
    (20, 106), (20, 107), (21, 105), (21, 108), (22, 106), (22, 107), (23, 58), (23, 108),
    (24, 49), (24, 82), (25, 80), (25, 81), (26, 79), (26, 82), (27, 80), (27, 81),
})

def point_set(permutations):
    return frozenset((x, permutation[x]) for permutation in permutations for x in range(len(permutation)))

def variants(points, size):
    transforms = (
        lambda x, y: (x, y), lambda x, y: (y, size - 1 - x),
        lambda x, y: (size - 1 - x, size - 1 - y), lambda x, y: (size - 1 - y, x),
        lambda x, y: (size - 1 - x, y), lambda x, y: (x, size - 1 - y),
        lambda x, y: (y, x), lambda x, y: (size - 1 - y, size - 1 - x),
    )
    out = []
    for transform in transforms:
        image = frozenset(transform(x, y) for x, y in points)
        if image not in out:
            out.append(image)
    return tuple(out)

VARIANTS = {name: variants(point_set(data["permutations"]), data["size"]) for name, data in BLOCKS.items()}
NODES = tuple((kind, variant) for kind in ("P", "Q") for variant in range(4))

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def first_collinear(points):
    for triple in combinations(sorted(points), 3):
        if collinear(*triple):
            return triple
    return None

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
        branch = max(sets, key=lambda item: sum(frequency[p] for p in item))
        for point in sorted(branch, key=lambda p: (-frequency[p], p)):
            nxt = tuple(sorted((frozenset(item) for item in sets if point not in item), key=lambda item: tuple(sorted(item))))
            tail = search(nxt, budget - 1)
            if tail is not None:
                return (point,) + tail
        return None
    return search(tuple(sorted(family, key=lambda item: tuple(sorted(item)))), limit)

def all_hitting_sets(triples, size):
    universe = sorted(set().union(*(set(triple) for triple in triples)))
    index = {point: i for i, point in enumerate(universe)}
    masks = [sum(1 << index[p] for p in triple) for triple in triples]
    out = []
    for indices in combinations(range(len(universe)), size):
        mask = sum(1 << i for i in indices)
        if all(mask & item for item in masks):
            out.append(tuple(universe[i] for i in indices))
    return tuple(out)

def norm_direction(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    divisor = gcd(abs(dx), abs(dy))
    dx, dy = dx // divisor, dy // divisor
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy

def one_legal_refill(original, deleted):
    deleted = set(deleted)
    base = set(original) - deleted
    column_counts = Counter(x for x, _ in deleted)
    row_counts = Counter(y for _, y in deleted)
    columns = sorted([x for x, count in column_counts.items() for _ in range(count)], key=lambda x: (-column_counts[x], x))
    candidates = set()
    for x in set(columns):
        for y in row_counts:
            point = (x, y)
            if point in base:
                continue
            directions = set()
            for old in base:
                direction = norm_direction(point, old)
                if direction in directions:
                    break
                directions.add(direction)
            else:
                candidates.add(point)
    chosen = []
    def search(index):
        if index == len(columns):
            return tuple(sorted(chosen))
        column = columns[index]
        previous_row = chosen[-1][1] if index and columns[index - 1] == column else None
        for row in sorted(row_counts):
            if not row_counts[row] or (previous_row is not None and row <= previous_row):
                continue
            point = (column, row)
            if point not in candidates or point in chosen:
                continue
            if any(collinear(old, selected, point) for selected in chosen for old in base):
                continue
            if any(collinear(a, b, point) for a, b in combinations(chosen, 2)):
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

def has_correction(original, core, maximum_size):
    available = sorted(set(original) - set(core))
    for extra_count in range(maximum_size - len(core) + 1):
        for extra in combinations(available, extra_count):
            deleted = tuple(sorted(set(core) | set(extra)))
            additions = one_legal_refill(original, deleted)
            if additions is not None:
                return deleted, additions
    return None

def block_at(x_origin, y_origin, node, offset):
    kind, variant = node
    return frozenset((x_origin + x, y_origin + offset + y) for x, y in VARIANTS[kind][variant])

def promising_attempts(state, x_origin, y_origin):
    records = []
    for node, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
        block = block_at(x_origin, y_origin, node, offset)
        triples = bad_cross_triples(state, block)
        if hitting_set_at_most(triples, 4) is not None:
            minimum = 4
        elif hitting_set_at_most(triples, 5) is not None:
            minimum = 5
        else:
            continue
        records.append((node, offset, minimum, all_hitting_sets(triples, minimum), block))
    return tuple(records)

assert first_collinear(SEVENTH_CORRECTED) is None
step8 = promising_attempts(SEVENTH_CORRECTED, 28, 79)
assert [(node, offset, minimum, len(cores)) for node, offset, minimum, cores, _ in step8] == [
    (("P", 0), 21, 5, 1), (("P", 1), 30, 4, 1), (("P", 1), 31, 5, 9),
    (("P", 2), 22, 5, 3), (("P", 3), -31, 5, 1), (("P", 3), 29, 5, 3), (("P", 3), 32, 5, 3),
]
assert sum(len(record[3]) for record in step8) == 21
step8_record = next(record for record in step8 if record[0] == ("P", 1) and record[1] == 31)
step8_core = ((23, 108), (24, 49), (28, 110), (28, 113), (30, 110))
assert step8_core in step8_record[3]
step8_deleted = ((0, 2), (1, 3), (23, 108), (24, 49), (28, 110), (28, 113), (30, 110))
step8_added = ((0, 110), (1, 113), (23, 2), (24, 110), (28, 3), (28, 108), (30, 49))
assert one_legal_refill(set(SEVENTH_CORRECTED) | set(step8_record[4]), step8_deleted) == step8_added
EIGHTH_CORRECTED = frozenset((set(SEVENTH_CORRECTED) | set(step8_record[4])) - set(step8_deleted) | set(step8_added))
assert first_collinear(EIGHTH_CORRECTED) is None and len(EIGHTH_CORRECTED) == 64

step9 = promising_attempts(EIGHTH_CORRECTED, 32, 110)
assert len(step9) == 16
assert Counter(record[2] for record in step9) == Counter({5: 12, 4: 4})
assert sum(len(record[3]) for record in step9) == 120
step9_record = next(record for record in step9 if record[0] == ("P", 0) and record[1] == -12)
step9_core = ((12, 48), (26, 82), (34, 99), (35, 98))
assert step9_record[3] == (step9_core,)
step9_deleted = ((5, 32), (12, 48), (17, 1), (21, 105), (26, 82), (34, 99), (35, 98))
step9_added = ((5, 1), (12, 105), (17, 99), (21, 98), (26, 48), (34, 32), (35, 82))
assert one_legal_refill(set(EIGHTH_CORRECTED) | set(step9_record[4]), step9_deleted) == step9_added
NINTH_CORRECTED = frozenset((set(EIGHTH_CORRECTED) | set(step9_record[4])) - set(step9_deleted) | set(step9_added))
assert first_collinear(NINTH_CORRECTED) is None and len(NINTH_CORRECTED) == 72

step10 = promising_attempts(NINTH_CORRECTED, 36, 98)
assert [(node, offset, minimum, len(cores)) for node, offset, minimum, cores, _ in step10] == [
    (("P", 2), -32, 5, 1), (("P", 3), -32, 5, 1),
]
assert all(has_correction(set(NINTH_CORRECTED) | set(block), cores[0], 7) is None for _, _, _, cores, block in step10)

print({
    "starting_corrected_blocks": 7,
    "eighth_attempts": len(NODES) * (2 * RADIUS + 1),
    "eighth_promising_attempts": len(step8),
    "eighth_minimum_transversals": sum(len(record[3]) for record in step8),
    "eighth_correction_size": len(step8_deleted),
    "ninth_promising_attempts": len(step9),
    "ninth_minimum_transversals": sum(len(record[3]) for record in step9),
    "ninth_correction_size": len(step9_deleted),
    "tenth_promising_attempts": len(step10),
    "tenth_minimum_transversals": sum(len(record[3]) for record in step10),
    "tenth_corrections_with_budget_seven": 0,
    "corrected_chain_length": 9,
    "remaining_gap": "the exact budget-seven corrected chain reaches nine blocks but has no budget-seven tenth transition in radius 32",
    "evidence_level": "exact_budget_seven_corrected_boundary_chain",
    "status": "passed",
})
