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
        "check_boundary_seventeenth_corrections",
        "check_boundary_eighteenth_spectrum",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

corrections = outputs["check_boundary_seventeenth_corrections"]
assert "m=3 triples=5 cores=3" in corrections.stderr
assert "attempts=1 totalcores=3 successful_cores=3 budgets 5:3" in corrections.stderr
assert "core 1 budget 5" in corrections.stdout
assert "D (0,110) (42,193) (54,378) (64,253) (66,252)" in corrections.stdout
assert "A (0,252) (42,378) (54,253) (64,110) (66,193)" in corrections.stdout
assert "FAIL" not in corrections.stdout

source_text = (HERE / "check_boundary_seventeenth_spectrum.cpp").read_text()
match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", source_text, re.S)
assert match
SIXTEENTH = {
    (int(x), int(y))
    for x, y in re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))
}
assert len(SIXTEENTH) == 128
P2 = ((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3))
BLOCK = {(64+x, 252+y) for x, y in P2}
DELETED = {(0,110),(42,193),(54,378),(64,253),(66,252)}
ADDED = {(0,252),(42,378),(54,253),(64,110),(66,193)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
SEVENTEENTH = (SIXTEENTH | BLOCK) - DELETED | ADDED
assert len(SEVENTEENTH) == 136

def collinear(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

assert all(not collinear(*triple) for triple in combinations(SEVENTEENTH, 3))

eighteenth = outputs["check_boundary_eighteenth_spectrum"]
assert "hist 4:3 5:16 6:70 7:211 8:218 9:2 10:15 11:68 12:152 13:178 14:99 small=89 sets=953" in eighteenth.stderr
minimum_four = [line for line in eighteenth.stdout.splitlines() if " min 4 " in line]
assert minimum_four == [
    "P0 -39 min 4 triples 16 cores 3",
    "P2 -40 min 4 triples 16 cores 3",
    "P2 -26 min 4 triples 12 cores 1",
]

print({
    "unique_minimum_three_seventeenth_attempt": "P2/-57",
    "minimum_cores": 3,
    "all_minimum_cores_correctable": True,
    "minimum_correction_budget_histogram": {5: 3},
    "canonical_correction_size": 5,
    "corrected_seventeenth_state_points": 136,
    "eighteenth_attempts_radius_64": 1032,
    "eighteenth_minimum_transversal_histogram": {4:3,5:16,6:70,7:211,8:218,9:2,10:15,11:68,12:152,13:178,14:99},
    "minimum_four_eighteenth_attempts": 3,
    "minimum_four_eighteenth_cores": 7,
    "raw_eighteenth_extensions": 0,
    "status": "passed",
})
