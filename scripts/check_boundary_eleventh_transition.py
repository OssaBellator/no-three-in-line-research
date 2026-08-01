#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent

with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    outputs = {}
    for stem in ("check_boundary_eleventh_spectrum", "check_boundary_eleventh_corrections"):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

spectrum = outputs["check_boundary_eleventh_spectrum"]
expected_histogram = "hist 4:12 5:35 6:76 7:135 8:261 9:21 10:41 11:79 12:99 13:170 14:103 small=519 sets=9300"
assert expected_histogram in spectrum.stderr
minimum_four = [line for line in spectrum.stdout.splitlines() if " min 4 " in line]
assert len(minimum_four) == 12
assert sum(int(line.rsplit(" ", 1)[1]) for line in minimum_four) == 94

corrections = outputs["check_boundary_eleventh_corrections"]
assert "successes=12" in corrections.stderr
assert corrections.stdout.count(" budget ") == 12
assert "P1 31 budget 5" in corrections.stdout
assert "D (0,79) (6,34) (23,2) (40,196) (43,195)" in corrections.stdout
assert "A (0,196) (6,2) (23,195) (40,34) (43,79)" in corrections.stdout

BLOCKS = {
    "P": {"size": 4, "permutations": ((0, 1, 3, 2), (2, 3, 1, 0))},
    "Q": {"size": 7, "permutations": ((5, 6, 2, 1, 4, 0, 3), (3, 0, 4, 5, 2, 6, 1))},
}
TENTH = frozenset({
    (0,79),(0,110),(1,61),(1,113),(2,1),(2,98),(3,3),(3,100),(4,33),(4,77),(5,1),(5,35),
    (6,33),(6,34),(7,32),(7,35),(8,34),(8,105),(9,59),(9,60),(10,58),(10,61),(11,59),(11,60),
    (12,2),(12,105),(13,46),(13,77),(14,47),(14,48),(15,46),(15,49),(16,75),(16,76),(17,74),(17,99),
    (18,75),(18,76),(19,0),(19,74),(20,106),(20,107),(21,0),(21,108),(22,106),(22,107),(23,2),(23,58),
    (24,82),(24,110),(25,80),(25,81),(26,47),(26,48),(27,80),(27,81),(28,3),(28,108),(29,111),(29,112),
    (30,49),(30,113),(31,111),(31,112),(32,79),(32,98),(33,99),(33,101),(34,32),(34,101),(35,82),(35,100),
    (36,163),(36,164),(37,162),(37,165),(38,163),(38,164),(39,162),(39,165),
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

def block_at(x_origin, y_origin, node, offset):
    kind, variant = node
    return frozenset((x_origin + x, y_origin + offset + y) for x, y in VARIANTS[kind][variant])

def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])

def first_collinear(points):
    for triple in combinations(sorted(points), 3):
        if collinear(*triple):
            return triple
    return None

ELEVENTH_BLOCK = block_at(40, 162, ("P", 1), 31)
DELETED = {(0,79),(6,34),(23,2),(40,196),(43,195)}
ADDED = {(0,196),(6,2),(23,195),(40,34),(43,79)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
ELEVENTH = frozenset((set(TENTH) | set(ELEVENTH_BLOCK)) - DELETED | ADDED)
assert len(ELEVENTH) == 88 and first_collinear(ELEVENTH) is None

raw_twelfth = []
for node in NODES:
    for offset in range(-64, 65):
        block = block_at(44, 193, node, offset)
        if first_collinear(set(ELEVENTH) | set(block)) is None:
            raw_twelfth.append((node, offset))
assert raw_twelfth == []

print({
    "eleventh_attempts_radius_64": len(NODES) * 129,
    "minimum_transversal_histogram": {4:12,5:35,6:76,7:135,8:261,9:21,10:41,11:79,12:99,13:170,14:103},
    "minimum_four_attempts": len(minimum_four),
    "minimum_four_cores": 94,
    "minimum_four_attempts_with_correction_budget_at_most_seven": 12,
    "canonical_transition": {"block": ("P",1), "offset":31, "correction_size":5},
    "corrected_eleventh_state_points": len(ELEVENTH),
    "raw_twelfth_attempts_radius_64": len(NODES) * 129,
    "raw_twelfth_extensions": 0,
    "remaining_gap": "the corrected radius-64 path reaches eleven blocks but has no raw twelfth transition or verified cycle",
    "evidence_level": "exact_corrected_eleventh_transition",
    "status": "passed",
})
