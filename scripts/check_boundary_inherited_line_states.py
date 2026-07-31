#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations, product
from math import gcd

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
OFFSET_RADIUS = 24


def points_from_permutations(permutations):
    return frozenset(
        (x, permutation[x])
        for permutation in permutations
        for x in range(len(permutation))
    )


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
    name: dihedral_variants(
        points_from_permutations(data["permutations"]),
        data["size"],
    )
    for name, data in BLOCKS.items()
}


def first_collinear(points):
    for a, b, c in combinations(sorted(points), 3):
        if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
            return a, b, c
    return None


def first_new_collinear(existing, new_points):
    new_set = set(new_points)
    for a, b, c in combinations(sorted(existing | new_points), 3):
        if not ({a, b, c} & new_set):
            continue
        if (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0]):
            return a, b, c
    return None


def normalized_line(a, b, origin):
    x1, y1 = a[0] - origin[0], a[1] - origin[1]
    x2, y2 = b[0] - origin[0], b[1] - origin[1]
    coefficients = [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]
    divisor = 0
    for value in coefficients:
        divisor = gcd(divisor, abs(value))
    coefficients = [value // divisor for value in coefficients]
    for value in coefficients:
        if value:
            if value < 0:
                coefficients = [-entry for entry in coefficients]
            break
    return tuple(coefficients)


def inherited_signature(points, origin):
    return frozenset(
        normalized_line(a, b, origin)
        for a, b in combinations(sorted(points), 2)
    )


edges = []
for left_type, right_type in product(("P", "Q"), repeat=2):
    for left_variant in range(len(VARIANTS[left_type])):
        for right_variant in range(len(VARIANTS[right_type])):
            left = VARIANTS[left_type][left_variant]
            width = BLOCKS[left_type]["size"]
            for offset in range(-OFFSET_RADIUS, OFFSET_RADIUS + 1):
                right = frozenset(
                    (width + x, offset + y)
                    for x, y in VARIANTS[right_type][right_variant]
                )
                if first_collinear(left | right) is None:
                    edges.append(
                        (
                            (left_type, left_variant),
                            (right_type, right_variant),
                            offset,
                        )
                    )
assert len(edges) == 282

adjacency = defaultdict(list)
for source, target, offset in edges:
    adjacency[source].append((target, offset))

states = []
for node in sorted(adjacency):
    points = VARIANTS[node[0]][node[1]]
    states.append(
        {
            "node": node,
            "origin": (0, 0),
            "points": points,
            "path": (node,),
            "offsets": (),
        }
    )

path_counts = [len(states)]
signature_ranges = []
for block_count in range(1, 5):
    sizes = [
        len(inherited_signature(state["points"], state["origin"]))
        for state in states
    ]
    signature_ranges.append((min(sizes), max(sizes)))
    if block_count == 4:
        break
    next_states = []
    for state in states:
        source = state["node"]
        x_origin, y_origin = state["origin"]
        next_x = x_origin + BLOCKS[source[0]]["size"]
        for target, offset in adjacency[source]:
            next_y = y_origin + offset
            new_points = frozenset(
                (next_x + x, next_y + y)
                for x, y in VARIANTS[target[0]][target[1]]
            )
            if first_new_collinear(state["points"], new_points) is not None:
                continue
            next_states.append(
                {
                    "node": target,
                    "origin": (next_x, next_y),
                    "points": state["points"] | new_points,
                    "path": state["path"] + (target,),
                    "offsets": state["offsets"] + (offset,),
                }
            )
    states = next_states
    path_counts.append(len(states))

assert path_counts == [8, 282, 74, 4]
assert signature_ranges == [(28, 91), (120, 378), (276, 435), (496, 496)]

survivors = tuple(
    (state["path"], state["offsets"])
    for state in states
)
assert survivors == (
    (
        (("P", 1), ("P", 1), ("P", 1), ("P", 1)),
        (-24, 10, -24),
    ),
    (
        (("P", 1), ("P", 1), ("P", 1), ("P", 1)),
        (24, -10, 24),
    ),
    (
        (("P", 3), ("P", 3), ("P", 3), ("P", 3)),
        (-24, 10, -24),
    ),
    (
        (("P", 3), ("P", 3), ("P", 3), ("P", 3)),
        (24, -10, 24),
    ),
)

extension_attempts = 0
failure_slopes = Counter()
first_failure = None
for state in states:
    source = state["node"]
    next_x = state["origin"][0] + BLOCKS[source[0]]["size"]
    for target, offset in adjacency[source]:
        extension_attempts += 1
        next_y = state["origin"][1] + offset
        new_points = frozenset(
            (next_x + x, next_y + y)
            for x, y in VARIANTS[target[0]][target[1]]
        )
        witness = first_new_collinear(state["points"], new_points)
        assert witness is not None
        if first_failure is None:
            first_failure = {
                "path": state["path"],
                "offsets": state["offsets"],
                "target": target,
                "offset": offset,
                "triple": witness,
            }
        dx = witness[1][0] - witness[0][0]
        dy = witness[1][1] - witness[0][1]
        divisor = gcd(abs(dx), abs(dy)) or 1
        failure_slopes[(dy // divisor, dx // divisor)] += 1

assert extension_attempts == 306
assert failure_slopes.most_common(1)[0] == ((-1, 1), 53)

print(
    {
        "offset_radius": OFFSET_RADIUS,
        "adjacent_legal_edges": len(edges),
        "globally_legal_path_counts_by_blocks": path_counts + [0],
        "inherited_line_signature_ranges": signature_ranges,
        "four_block_survivors": survivors,
        "five_block_extension_attempts": extension_attempts,
        "five_block_survivors": 0,
        "first_extension_failure": first_failure,
        "most_common_extension_failure_slope": failure_slopes.most_common(1)[0],
        "conclusion": "within offset radius 24, exact inherited-line state certifies that no five-block word exists",
        "evidence_level": "independently_enumerated_candidate_obstruction",
        "status": "passed",
    }
)
