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
    for stem in (
        "check_boundary_fourteenth_spectrum",
        "check_boundary_fourteenth_corrections",
        "check_boundary_fifteenth_spectrum",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

fourteenth = outputs["check_boundary_fourteenth_spectrum"]
assert "hist 3:3 4:13 5:62 6:123 7:173 8:151 9:36 10:61 11:130 12:131 13:98 14:51 small=201 sets=3139" in fourteenth.stderr
best = [line for line in fourteenth.stdout.splitlines() if " min 3 " in line or " min 4 " in line]
assert len(best) == 16
assert sum(int(line.rsplit(" ", 1)[1]) for line in best) == 125

corrections = outputs["check_boundary_fourteenth_corrections"]
assert "attempts=16 successes=16 core_successes=125 budgets 3:2 4:23 5:54 6:38 7:8" in corrections.stderr
assert "P2 63 min 3 cores 9 successful_cores 9 budget 3" in corrections.stdout
assert "D (32,79) (44,258) (52,377)" in corrections.stdout
assert "A (32,258) (44,377) (52,79)" in corrections.stdout

fifteenth = outputs["check_boundary_fifteenth_spectrum"]
assert "hist 4:10 5:36 6:100 7:193 8:186 9:28 10:81 11:106 12:151 13:110 14:31 small=146 sets=3073" in fifteenth.stderr

THIRTEENTH = frozenset({
    (0,110),(0,196),(1,61),(1,113),(2,98),(2,257),(3,3),(3,100),
    (4,33),(4,77),(5,1),(5,35),(6,2),(6,33),(7,32),(7,35),
    (8,34),(8,105),(9,59),(9,60),(10,58),(10,61),(11,59),(11,60),
    (12,2),(12,105),(13,46),(13,77),(14,47),(14,258),(15,46),(15,49),
    (16,75),(16,76),(17,74),(17,99),(18,76),(18,316),(19,0),(19,74),
    (20,106),(20,107),(21,0),(21,108),(22,106),(22,107),(23,58),(23,195),
    (24,82),(24,110),(25,80),(25,81),(26,47),(26,48),(27,80),(27,81),
    (28,3),(28,108),(29,111),(29,112),(30,49),(30,113),(31,111),(31,112),
    (32,79),(32,98),(33,99),(33,101),(34,32),(34,101),(35,82),(35,100),
    (36,163),(36,164),(37,162),(37,165),(38,163),(38,164),(39,162),(39,165),
    (40,34),(40,315),(41,194),(41,195),(42,193),(42,196),(43,79),(43,194),
    (44,258),(44,260),(45,257),(45,259),(46,1),(46,259),(47,48),(47,260),
    (48,313),(48,315),(49,314),(49,316),(50,193),(50,314),(51,75),(51,313),
})
P2 = ((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3))
BLOCK = {(52+x, 376+y) for x, y in P2}
DELETED = {(32,79),(44,258),(52,377)}
ADDED = {(32,258),(44,377),(52,79)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
FOURTEENTH = frozenset((set(THIRTEENTH) | BLOCK) - DELETED | ADDED)
assert len(FOURTEENTH) == 112

def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

assert all(not collinear(*triple) for triple in combinations(FOURTEENTH, 3))
print({
    "fourteenth_attempts_radius_64": 1032,
    "minimum_transversal_histogram": {3:3,4:13,5:62,6:123,7:173,8:151,9:36,10:61,11:130,12:131,13:98,14:51},
    "minimum_three_or_four_attempts": 16,
    "minimum_cores": 125,
    "correctable_minimum_cores_budget_at_most_seven": 125,
    "all_low_transversal_attempts_correctable": True,
    "all_minimum_cores_correctable": True,
    "successful_core_budget_histogram": {3:2,4:23,5:54,6:38,7:8},
    "canonical_transition": {"block":"P2","offset":63,"correction_size":3},
    "corrected_fourteenth_state_points": 112,
    "raw_fifteenth_attempts_radius_64": 1032,
    "raw_fifteenth_extensions": 0,
    "status": "passed",
})
