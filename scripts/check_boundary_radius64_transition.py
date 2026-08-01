#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "check_boundary_budget_eight.cpp"
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_boundary_budget_eight"
    subprocess.run(["c++", "-O3", "-std=c++17", str(SOURCE), "-o", str(binary)], check=True)
    result = subprocess.run([str(binary)], check=True, capture_output=True, text=True)
    assert "candidate 0 checked 67525 found 0" in result.stdout
    assert "candidate 1 checked 67525 found 0" in result.stdout

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
NINTH = frozenset({
    (0,79),(0,110),(1,61),(1,113),(2,1),(2,2),(3,0),(3,3),(4,33),(4,77),(5,1),(5,35),
    (6,33),(6,34),(7,32),(7,35),(8,34),(8,105),(9,59),(9,60),(10,58),(10,61),(11,59),(11,60),
    (12,47),(12,105),(13,46),(13,77),(14,47),(14,48),(15,46),(15,49),(16,75),(16,76),(17,74),(17,99),
    (18,75),(18,76),(19,0),(19,74),(20,106),(20,107),(21,98),(21,108),(22,106),(22,107),(23,2),(23,58),
    (24,82),(24,110),(25,80),(25,81),(26,48),(26,79),(27,80),(27,81),(28,3),(28,108),(29,111),(29,112),
    (30,49),(30,113),(31,111),(31,112),(32,98),(32,100),(33,99),(33,101),(34,32),(34,101),(35,82),(35,100),
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

def block_at(x_origin, y_origin, node, offset):
    kind, variant = node
    return frozenset((x_origin + x, y_origin + offset + y) for x, y in VARIANTS[kind][variant])

TENTH_BLOCK = block_at(36, 98, ("P", 3), 64)
DELETED = ((2,2),(3,0),(12,47),(21,98),(26,79),(32,100))
ADDED = ((2,98),(3,100),(12,2),(21,0),(26,47),(32,79))
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
TENTH = frozenset((set(NINTH) | set(TENTH_BLOCK)) - set(DELETED) | set(ADDED))
assert len(TENTH) == 80
assert first_collinear(TENTH) is None

raw_eleventh = []
for node in NODES:
    for offset in range(-64, 65):
        block = block_at(40, 162, node, offset)
        if first_collinear(set(TENTH) | set(block)) is None:
            raw_eleventh.append((node, offset))
assert raw_eleventh == []

print({
    "radius_32_tenth_candidates": 2,
    "budget_eight_extra_deletion_triples_per_candidate": 67525,
    "budget_eight_radius_32_corrections": 0,
    "radius_64_tenth_block": ("P", 3),
    "radius_64_tenth_offset": 64,
    "radius_64_tenth_correction_size": 6,
    "corrected_tenth_state_points": len(TENTH),
    "raw_eleventh_attempts_radius_64": len(NODES) * 129,
    "raw_eleventh_extensions_radius_64": 0,
    "remaining_gap": "the widened corrected path reaches ten blocks, but an eleventh correction or periodic component is not established",
    "evidence_level": "exact_radius64_boundary_transition",
    "status": "passed",
})
