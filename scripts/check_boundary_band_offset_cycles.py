#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, product
from math import gcd

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
OFFSET_RADIUS = 24


def points_from_permutations(perms):
    return frozenset((x, perm[x]) for perm in perms for x in range(len(perm)))


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


VARIANTS = {
    name: dihedral_variants(points_from_permutations(data["permutations"]), data["size"])
    for name, data in BLOCKS.items()
}


def legal_adjacent(left_type, left_variant, right_type, right_variant, offset):
    left = VARIANTS[left_type][left_variant]
    width = BLOCKS[left_type]["size"]
    right = frozenset(
        (width + x, offset + y) for x, y in VARIANTS[right_type][right_variant]
    )
    return first_collinear(left | right) is None


EDGES = []
for left_type, right_type in product(("P", "Q"), repeat=2):
    for left_variant in range(len(VARIANTS[left_type])):
        for right_variant in range(len(VARIANTS[right_type])):
            for offset in range(-OFFSET_RADIUS, OFFSET_RADIUS + 1):
                if legal_adjacent(left_type, left_variant, right_type, right_variant, offset):
                    EDGES.append((left_type, left_variant, right_type, right_variant, offset))

assert len(EDGES) == 282
minimum_offsets = {}
for left_type, right_type in product(("P", "Q"), repeat=2):
    candidates = [
        (abs(offset), offset, left_variant, right_variant)
        for lt, left_variant, rt, right_variant, offset in EDGES
        if lt == left_type and rt == right_type
    ]
    minimum_offsets[f"{left_type}->{right_type}"] = min(candidates)
assert {key: value[0] for key, value in minimum_offsets.items()} == {
    "P->P": 10,
    "P->Q": 16,
    "Q->P": 16,
    "Q->Q": 24,
}

NODES = tuple(sorted({(edge[0], edge[1]) for edge in EDGES} | {(edge[2], edge[3]) for edge in EDGES}))
ADJ = {node: [] for node in NODES}
for left_type, left_variant, right_type, right_variant, offset in EDGES:
    ADJ[(left_type, left_variant)].append(((right_type, right_variant), offset))


def enumerate_zero_drift_cycles(length, mixed_only=False):
    cycles = []

    def search(start, node, path, total_offset):
        if len(path) == length:
            if node == start and total_offset == 0:
                types = {edge[0][0] for edge in path} | {edge[1][0] for edge in path}
                if not mixed_only or types == {"P", "Q"}:
                    cycles.append(tuple(path))
            return
        for target, offset in ADJ[node]:
            search(start, target, path + [(node, target, offset)], total_offset + offset)

    for start in NODES:
        search(start, start, [], 0)
    return tuple(cycles)


def place_periods(cycle, periods=2):
    start = cycle[0][0]
    blocks = [start]
    origins = [(0, 0)]
    current = start
    x_origin = 0
    y_origin = 0
    for _ in range(periods):
        for source, target, offset in cycle:
            assert source == current
            x_origin += BLOCKS[source[0]]["size"]
            y_origin += offset
            blocks.append(target)
            origins.append((x_origin, y_origin))
            current = target
    points = set()
    for (block_type, variant), (x0, y0) in zip(blocks, origins):
        for x, y in VARIANTS[block_type][variant]:
            points.add((x0 + x, y0 + y))
    return frozenset(points)


def failure_audit(cycles):
    legal = 0
    slope_histogram = Counter()
    first_failure = None
    for cycle in cycles:
        witness = first_collinear(place_periods(cycle, periods=2))
        if witness is None:
            legal += 1
            continue
        if first_failure is None:
            first_failure = {"cycle": cycle, "triple": witness}
        dx = witness[1][0] - witness[0][0]
        dy = witness[1][1] - witness[0][1]
        divisor = gcd(abs(dx), abs(dy)) or 1
        slope_histogram[(dy // divisor, dx // divisor)] += 1
    return legal, first_failure, slope_histogram


cycles_2 = enumerate_zero_drift_cycles(2)
cycles_3 = enumerate_zero_drift_cycles(3)
shortest_mixed_cycles = enumerate_zero_drift_cycles(4, mixed_only=True)
assert len(cycles_2) == 242
assert len(cycles_3) == 84
assert len(shortest_mixed_cycles) == 1172

results = {}
for label, cycles in (
    ("length_2", cycles_2),
    ("length_3", cycles_3),
    ("shortest_mixed_length_4", shortest_mixed_cycles),
):
    legal, first_failure, slope_histogram = failure_audit(cycles)
    assert legal == 0
    results[label] = {
        "cycles_checked": len(cycles),
        "globally_legal": legal,
        "first_failure": first_failure,
        "most_common_failure_slope": slope_histogram.most_common(1)[0],
    }

assert results["length_2"]["most_common_failure_slope"] == ((0, 1), 207)
assert results["length_3"]["most_common_failure_slope"] == ((0, 1), 54)
assert results["shortest_mixed_length_4"]["most_common_failure_slope"] == ((0, 1), 553)

print({
    "offset_radius": OFFSET_RADIUS,
    "adjacent_legal_edges": len(EDGES),
    "minimum_absolute_offsets": {key: value[0] for key, value in minimum_offsets.items()},
    "zero_drift_cycle_audits": results,
    "conclusion": "adjacent band-offset legality does not compose through the shortest bounded cycles",
    "evidence_level": "independently_enumerated_candidate_obstruction",
    "status": "passed",
})
