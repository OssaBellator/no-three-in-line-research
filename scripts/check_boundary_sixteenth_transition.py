#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import re
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    outputs = {}
    for stem in (
        "check_boundary_sixteenth_spectrum",
        "check_boundary_sixteenth_canonical_corrections",
        "check_boundary_seventeenth_spectrum",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

sixteenth = outputs["check_boundary_sixteenth_spectrum"]
assert "hist 4:9 5:21 6:88 7:166 8:238 9:8 10:38 11:83 12:157 13:151 14:73 small=118 sets=1578" in sixteenth.stderr
best = [line for line in sixteenth.stdout.splitlines() if " min 4 " in line]
expected = {
    ("P0", -38): 7,
    ("P1", -37): 15,
    ("P1", -27): 3,
    ("P1", -26): 1,
    ("P2", -37): 5,
    ("P2", -27): 5,
    ("P2", -25): 1,
    ("P2", -4): 1,
    ("P3", -25): 1,
}
observed = {}
for line in best:
    fields = line.split()
    observed[(fields[0], int(fields[1]))] = int(fields[-1])
assert observed == expected
assert sum(observed.values()) == 39

corrections = outputs["check_boundary_sixteenth_canonical_corrections"]
assert "attempts=1 totalcores=15 successes=1 core_successes=15 budgets 4:1 5:7 6:5 7:2" in corrections.stderr
assert "P1 -37 min 4 cores 15 successful_cores 15 budget 4" in corrections.stdout
assert "D (22,106) (39,165) (48,315) (62,312)" in corrections.stdout
assert "A (22,315) (39,312) (48,165) (62,106)" in corrections.stdout

source_text = (HERE / "check_boundary_sixteenth_spectrum.cpp").read_text()
match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", source_text, re.S)
assert match
FIFTEENTH = {
    (int(x), int(y))
    for x, y in re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))
}
assert len(FIFTEENTH) == 120
P1 = ((0,0),(0,3),(1,1),(1,2),(2,0),(2,3),(3,1),(3,2))
BLOCK = {(60+x, 309+y) for x, y in P1}
DELETED = {(22,106),(39,165),(48,315),(62,312)}
ADDED = {(22,315),(39,312),(48,165),(62,106)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
SIXTEENTH = (FIFTEENTH | BLOCK) - DELETED | ADDED
assert len(SIXTEENTH) == 128

def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

assert all(not collinear(*triple) for triple in combinations(SIXTEENTH, 3))

seventeenth = outputs["check_boundary_seventeenth_spectrum"]
assert "hist 3:1 4:2 5:17 6:56 7:192 8:248 9:1 10:18 11:65 12:182 13:162 14:88 small=76 sets=1467" in seventeenth.stderr
assert "P2 -57 min 3 triples 5 cores 3" in seventeenth.stdout
assert not any(" min 0 " in line for line in seventeenth.stdout.splitlines())

print({
    "sixteenth_attempts_radius_64": 1032,
    "sixteenth_minimum_transversal_histogram": {4:9,5:21,6:88,7:166,8:238,9:8,10:38,11:83,12:157,13:151,14:73},
    "minimum_four_attempts": len(expected),
    "minimum_four_cores": sum(expected.values()),
    "canonical_attempt": {"block":"P1","offset":-37,"minimum_cores":15},
    "canonical_core_budget_histogram": {4:1,5:7,6:5,7:2},
    "all_canonical_minimum_cores_correctable_through_budget_seven": True,
    "certified_transition": {"block":"P1","offset":-37,"correction_size":4},
    "corrected_sixteenth_state_points": len(SIXTEENTH),
    "seventeenth_attempts_radius_64": 1032,
    "seventeenth_minimum_transversal_histogram": {3:1,4:2,5:17,6:56,7:192,8:248,9:1,10:18,11:65,12:182,13:162,14:88},
    "raw_seventeenth_extensions": 0,
    "unique_minimum_three_attempt": "P2/-57",
    "status": "passed",
})
