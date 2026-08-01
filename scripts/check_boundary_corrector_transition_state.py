#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, product
from math import gcd
from runpy import run_path

previous = run_path("scripts/check_boundary_six_point_corrector.py")
BLOCKS = previous["BLOCKS"]
RADIUS = previous["RADIUS"]
VARIANTS = previous["VARIANTS"]
NODES = previous["NODES"]
five_states = previous["five_states"]
witnesses = previous["witnesses"]
collinear = previous["collinear"]
first_collinear = previous["first_collinear"]
bad_cross_triples = previous["bad_cross_triples"]
hitting_set_at_most = previous["hitting_set_at_most"]


def all_hitting_sets(triples, size):
    universe = sorted(set().union(*(set(triple) for triple in triples)))
    family = tuple(set(triple) for triple in triples)
    return tuple(subset for subset in combinations(universe, size) if all(set(subset).intersection(item) for item in family))


def line(a, b):
    A = b[1] - a[1]
    B = a[0] - b[0]
    C = -(A * a[0] + B * a[1])
    divisor = gcd(gcd(abs(A), abs(B)), abs(C))
    if divisor:
        A, B, C = A // divisor, B // divisor, C // divisor
    if A < 0 or (A == 0 and B < 0):
        A, B, C = -A, -B, -C
    return A, B, C


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


def correction_from_core(original, core, maximum_extra=2):
    available = sorted(set(original) - set(core))
    for extra_count in range(maximum_extra + 1):
        for index, extra in enumerate(combinations(available, extra_count), 1):
            deleted = set(core) | set(extra)
            column_counts = Counter(x for x, _ in deleted)
            row_counts = Counter(y for _, y in deleted)
            columns = [column for column, count in column_counts.items() for _ in range(count)]
            rows = [row for row, count in row_counts.items() for _ in range(count)]
            additions = one_legal_refill(set(original) - deleted, columns, rows)
            if additions is not None:
                corrected = frozenset((set(original) - deleted) | set(additions))
                return len(deleted), index, tuple(sorted(deleted)), additions, corrected
    return None


corrected_states = []
for state_index, target, offset, deleted, additions, corrected in witnesses:
    _, _, _, x_end, y_origin = five_states[state_index]
    corrected_states.append(
        (state_index, target, offset, corrected,
         x_end + BLOCKS[target[0]]["size"], y_origin + offset)
    )

attempts = 0
minimum_four_attempts = []
for corrected_index, (_, _, _, corrected, next_x, current_y) in enumerate(corrected_states):
    for node, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
        attempts += 1
        kind, variant = node
        new_block = frozenset((next_x + x, current_y + offset + y) for x, y in VARIANTS[kind][variant])
        triples = bad_cross_triples(corrected, new_block)
        assert triples
        if hitting_set_at_most(triples, 4) is not None:
            assert hitting_set_at_most(triples, 3) is None
            hitting_sets = all_hitting_sets(triples, 4)
            minimum_four_attempts.append((corrected_index, node, offset, hitting_sets, new_block))

assert attempts == 2080
assert len(minimum_four_attempts) == 6
assert sum(len(record[3]) for record in minimum_four_attempts) == 82

canonical_records = []
for corrected_index, node, offset, hitting_sets, new_block in minimum_four_attempts:
    core = min(hitting_sets)
    original = set(corrected_states[corrected_index][3]) | set(new_block)
    canonical_records.append((corrected_index, node, offset, core, correction_from_core(original, core)))

successful = [record for record in canonical_records if record[4] is not None]
assert len(successful) == 1
corrected_index, seventh_node, seventh_offset, core, correction = successful[0]
assert (corrected_index, seventh_node, seventh_offset) == (3, ("P", 1), -26)
assert correction[:2] == (6, 142)
assert correction[2] == ((0, 58), (1, 77), (8, 61), (13, 49), (23, 105), (24, 79))
assert correction[3] == ((0, 79), (1, 61), (8, 105), (13, 77), (23, 58), (24, 49))

seventh_corrected = correction[4]
next_x = corrected_states[corrected_index][4] + BLOCKS[seventh_node[0]]["size"]
next_y = corrected_states[corrected_index][5] + seventh_offset
raw_eighth = []
for node, offset in product(NODES, range(-RADIUS, RADIUS + 1)):
    kind, variant = node
    block = {(next_x + x, next_y + offset + y) for x, y in VARIANTS[kind][variant]}
    if first_collinear(set(seventh_corrected) | block) is None:
        raw_eighth.append((node, offset))
assert raw_eighth == []

print({
    "corrected_six_block_states": len(corrected_states),
    "raw_seventh_block_attempts": attempts,
    "attempts_with_minimum_line_transversal_four": len(minimum_four_attempts),
    "minimum_four_transversals_total": 82,
    "canonical_transversals_with_degree_corrector_size_at_most_six": len(successful),
    "canonical_corrected_transition": {
        "source_corrected_state": corrected_index,
        "seventh_block": seventh_node,
        "offset": seventh_offset,
        "minimum_transversal": core,
        "degree_corrector_size": correction[0],
        "extra_deletion_pair_index": correction[1],
        "deleted": correction[2],
        "added": correction[3],
    },
    "raw_eighth_block_attempts": len(NODES) * (2 * RADIUS + 1),
    "raw_eighth_block_extensions": 0,
    "remaining_gap": "one canonical corrected seventh transition exists, but it has no raw eighth extension and no periodic corrected-state cycle is established",
    "evidence_level": "exact_corrector_aware_boundary_transition_census",
    "status": "passed",
})
