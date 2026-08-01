#!/usr/bin/env python3
from itertools import combinations, product
from math import gcd

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
OFFSET_RADIUS = 32
MAX_BLOCKS = 6


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


def normalized_line(a, b):
    x1, y1 = a
    x2, y2 = b
    A = y2 - y1
    B = x1 - x2
    C = -(A * x1 + B * y1)
    divisor = gcd(gcd(abs(A), abs(B)), abs(C)) or 1
    A //= divisor
    B //= divisor
    C //= divisor
    if A < 0 or (A == 0 and B < 0) or (A == 0 and B == 0 and C < 0):
        A, B, C = -A, -B, -C
    return A, B, C


def lies_on(point, line):
    return line[0] * point[0] + line[1] * point[1] + line[2] == 0


def line_signature(points):
    return frozenset(normalized_line(a, b) for a, b in combinations(points, 2))


def shifted_block(node, x_origin, y_origin):
    block_type, variant = node
    return frozenset((x_origin + x, y_origin + y) for x, y in VARIANTS[block_type][variant])


def extend(points, inherited_lines, new_block):
    if not points.isdisjoint(new_block):
        return None

    # One new point on an inherited pair-line creates a triple.
    for point in new_block:
        for line in inherited_lines:
            if lies_on(point, line):
                return None

    # One old point on a pair-line internal to the new block also creates a triple.
    new_internal_lines = tuple(normalized_line(a, b) for a, b in combinations(new_block, 2))
    for line in new_internal_lines:
        for point in points:
            if lies_on(point, line):
                return None

    union = points | new_block
    cross_lines = frozenset(normalized_line(a, b) for a in points for b in new_block)
    return union, inherited_lines | frozenset(new_internal_lines) | cross_lines


states = []
for node in NODES:
    points = shifted_block(node, 0, 0)
    states.append(
        {
            "last": node,
            "x_end": BLOCKS[node[0]]["size"],
            "y_origin": 0,
            "points": points,
            "lines": line_signature(points),
            "word": (node,),
            "offsets": (),
        }
    )

path_counts = [len(states)]
extension_attempts = []
for block_count in range(2, MAX_BLOCKS + 1):
    next_states = []
    attempts = 0
    for state in states:
        for target, offset in product(NODES, range(-OFFSET_RADIUS, OFFSET_RADIUS + 1)):
            attempts += 1
            new_origin = state["y_origin"] + offset
            new_block = shifted_block(target, state["x_end"], new_origin)
            result = extend(state["points"], state["lines"], new_block)
            if result is None:
                continue
            points, lines = result
            next_states.append(
                {
                    "last": target,
                    "x_end": state["x_end"] + BLOCKS[target[0]]["size"],
                    "y_origin": new_origin,
                    "points": points,
                    "lines": lines,
                    "word": state["word"] + (target,),
                    "offsets": state["offsets"] + (offset,),
                }
            )
    if block_count == 5:
        five_states = next_states
    states = next_states
    extension_attempts.append(attempts)
    path_counts.append(len(states))
    if not states:
        break

assert path_counts == [8, 688, 886, 376, 8, 0]
assert extension_attempts == [4160, 357760, 460720, 195520, 4160]
assert len(five_states) == 8
assert all(all(node[0] == "P" for node in state["word"]) for state in five_states)
assert {state["word"] for state in five_states} == {
    (("P", 1), ("P", 1), ("P", 3), ("P", 1), ("P", 1)),
    (("P", 3), ("P", 3), ("P", 1), ("P", 3), ("P", 3)),
}
assert {state["offsets"] for state in five_states} == {
    (-32, -26, 12, -28),
    (-28, 12, -26, -32),
    (28, -12, 26, 32),
    (32, 26, -12, 28),
}
assert all(len(state["lines"]) == 780 for state in five_states)

print({
    "offset_radius": OFFSET_RADIUS,
    "globally_legal_path_counts": path_counts,
    "extension_attempts_by_new_length": extension_attempts,
    "five_block_survivors": len(five_states),
    "five_block_word_types": sorted({state["word"] for state in five_states}),
    "five_block_offset_patterns": sorted({state["offsets"] for state in five_states}),
    "pair_lines_per_five_block_survivor": 780,
    "six_block_survivors": 0,
    "conclusion": "larger offsets postpone but do not remove the inherited-line obstruction",
    "evidence_level": "independently_enumerated_coordinate_obstruction",
    "status": "passed",
})
