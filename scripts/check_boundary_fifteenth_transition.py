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
        "check_boundary_fifteenth_spectrum",
        "check_boundary_fifteenth_corrections",
        "check_boundary_sixteenth_spectrum",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

fifteenth = outputs["check_boundary_fifteenth_spectrum"]
assert "hist 4:10 5:36 6:100 7:193 8:186 9:28 10:81 11:106 12:151 13:110 14:31 small=146 sets=3073" in fifteenth.stderr
best = [line for line in fifteenth.stdout.splitlines() if " min 4 " in line]
assert len(best) == 10
assert sum(int(line.rsplit(" ", 1)[1]) for line in best) == 156

corrections = outputs["check_boundary_fifteenth_corrections"]
assert "attempts=10 successes=10 core_successes=156 budgets 4:6 5:70 6:74 7:6" in corrections.stderr
assert "P0 -30 min 4 cores 45 successful_cores 45 budget 4" in corrections.stdout
assert "D (9,59) (19,74) (58,349) (59,346)" in corrections.stdout
assert "A (9,349) (19,346) (58,74) (59,59)" in corrections.stdout

sixteenth = outputs["check_boundary_sixteenth_spectrum"]
assert "hist 4:9 5:21 6:88 7:166 8:238 9:8 10:38 11:83 12:157 13:151 14:73 small=118 sets=1578" in sixteenth.stderr

FOURTEENTH = frozenset({
    (0,110),(0,196),(1,61),(1,113),(2,98),(2,257),(3,3),(3,100),
    (4,33),(4,77),(5,1),(5,35),(6,2),(6,33),(7,32),(7,35),
    (8,34),(8,105),(9,59),(9,60),(10,58),(10,61),(11,59),(11,60),
    (12,2),(12,105),(13,46),(13,77),(14,47),(14,258),(15,46),(15,49),
    (16,75),(16,76),(17,74),(17,99),(18,76),(18,316),(19,0),(19,74),
    (20,106),(20,107),(21,0),(21,108),(22,106),(22,107),(23,58),(23,195),
    (24,82),(24,110),(25,80),(25,81),(26,47),(26,48),(27,80),(27,81),
    (28,3),(28,108),(29,111),(29,112),(30,49),(30,113),(31,111),(31,112),
    (32,98),(32,258),(33,99),(33,101),(34,32),(34,101),(35,82),(35,100),
    (36,163),(36,164),(37,162),(37,165),(38,163),(38,164),(39,162),(39,165),
    (40,34),(40,315),(41,194),(41,195),(42,193),(42,196),(43,79),(43,194),
    (44,260),(44,377),(45,257),(45,259),(46,1),(46,259),(47,48),(47,260),
    (48,313),(48,315),(49,314),(49,316),(50,193),(50,314),(51,75),(51,313),
    (52,79),(52,379),(53,376),(53,378),(54,376),(54,378),(55,377),(55,379),
})
P0 = ((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2))
BLOCK = {(56+x, 346+y) for x, y in P0}
DELETED = {(9,59),(19,74),(58,349),(59,346)}
ADDED = {(9,349),(19,346),(58,74),(59,59)}
assert Counter(x for x,_ in DELETED) == Counter(x for x,_ in ADDED)
assert Counter(y for _,y in DELETED) == Counter(y for _,y in ADDED)
FIFTEENTH = frozenset((set(FOURTEENTH) | BLOCK) - DELETED | ADDED)
assert len(FIFTEENTH) == 120

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

assert all(not collinear(*triple) for triple in combinations(FIFTEENTH, 3))
print({
    "fifteenth_attempts_radius_64": 1032,
    "minimum_four_attempts": 10,
    "minimum_cores": 156,
    "all_minimum_cores_correctable_through_budget_seven": True,
    "minimum_correction_budget_histogram": {4:6,5:70,6:74,7:6},
    "canonical_transition": {"block":"P0","offset":-30,"correction_size":4},
    "corrected_fifteenth_state_points": 120,
    "raw_sixteenth_attempts_radius_64": 1032,
    "raw_sixteenth_extensions": 0,
    "status": "passed",
})
