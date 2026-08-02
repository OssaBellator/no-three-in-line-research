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
    for stem in ("check_boundary_thirteenth_spectrum", "check_boundary_thirteenth_corrections"):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++","-O3","-std=c++17",str(source),"-o",str(binary)],check=True)
        outputs[stem] = subprocess.run([str(binary)],check=True,capture_output=True,text=True)

spectrum = outputs["check_boundary_thirteenth_spectrum"]
assert "hist 3:3 4:8 5:25 6:84 7:163 8:240 9:15 10:37 11:123 12:135 13:135 14:64 small=120 sets=1895" in spectrum.stderr
best = [line for line in spectrum.stdout.splitlines() if " min 3 " in line or " min 4 " in line]
assert len(best) == 11
assert sum(int(line.rsplit(" ",1)[1]) for line in best) == 93

corrections = outputs["check_boundary_thirteenth_corrections"]
assert "attempts=11 successes=11 core_successes=93 budgets 4:19 5:45 6:26 7:3" in corrections.stderr
assert "P0 56 min 4 cores 9 successful_cores 9 budget 4" in corrections.stdout
assert "D (18,75) (40,193) (50,316) (51,315)" in corrections.stdout
assert "A (18,316) (40,315) (50,193) (51,75)" in corrections.stdout

TWELFTH = frozenset(((0, 110), (0, 196), (1, 61), (1, 113), (2, 98), (2, 257), (3, 3), (3, 100), (4, 33), (4, 77), (5, 1), (5, 35), (6, 2), (6, 33), (7, 32), (7, 35), (8, 34), (8, 105), (9, 59), (9, 60), (10, 58), (10, 61), (11, 59), (11, 60), (12, 2), (12, 105), (13, 46), (13, 77), (14, 47), (14, 258), (15, 46), (15, 49), (16, 75), (16,  76), (17, 74), (17, 99), (18, 75), (18, 76), (19, 0), (19, 74), (20, 106), (20, 107), (21, 0), (21, 108), (22, 106), (22, 107), (23, 58), (23, 195), (24, 82), (24, 110), (25, 80), (25, 81), (26, 47), (26, 48), (27, 80), (27, 81), (28, 3), (28, 108), (29, 111), (29, 112), (30, 49), (30, 113), (31, 111), (31, 112), (32, 79), (32, 98), (33, 99), (33, 101), (34, 32), (34, 101), (35, 82), (35, 100), (36, 163), (36, 164), (37, 162), (37, 165), (38, 163), (38, 164), (39, 162), (39, 165), (40, 34), (40, 193), (41, 194), (41, 195), (42, 193), (42, 196), (43, 79), (43, 194), (44, 258), (44, 260), (45, 257), (45, 259), (46, 1), (46, 259), (47, 48), (47, 260)))
THIRTEENTH_BLOCK = {(48,313),(48,315),(49,314),(49,316),(50,314),(50,316),(51,313),(51,315)}
DELETED = {(18,75),(40,193),(50,316),(51,315)}
ADDED = {(18,316),(40,315),(50,193),(51,75)}

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) == (b[1]-a[1])*(c[0]-a[0])

assert Counter(x for x,_ in DELETED) == Counter(x for x,_ in ADDED)
assert Counter(y for _,y in DELETED) == Counter(y for _,y in ADDED)
THIRTEENTH = frozenset((set(TWELFTH)|THIRTEENTH_BLOCK)-DELETED|ADDED)
assert len(THIRTEENTH) == 104
assert all(not collinear(*triple) for triple in combinations(THIRTEENTH,3))

NODES = {
"P0":((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2)),
"P1":((0,0),(0,3),(1,1),(1,2),(2,0),(2,3),(3,1),(3,2)),
"P2":((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3)),
"P3":((0,1),(0,2),(1,0),(1,3),(2,1),(2,2),(3,0),(3,3)),
"Q0":((0,3),(0,5),(1,0),(1,6),(2,2),(2,4),(3,1),(3,5),(4,2),(4,4),(5,0),(5,6),(6,1),(6,3)),
"Q1":((0,1),(0,5),(1,0),(1,3),(2,2),(2,4),(3,0),(3,6),(4,2),(4,4),(5,3),(5,6),(6,1),(6,5)),
"Q2":((0,1),(0,3),(1,0),(1,6),(2,2),(2,4),(3,1),(3,5),(4,2),(4,4),(5,0),(5,6),(6,3),(6,5)),
"Q3":((0,1),(0,5),(1,3),(1,6),(2,2),(2,4),(3,0),(3,6),(4,2),(4,4),(5,0),(5,3),(6,1),(6,5)),
}
raw = []
for name, points in NODES.items():
    for offset in range(-64,65):
        block = {(52+x,313+offset+y) for x,y in points}
        if all(not collinear(*triple) for triple in combinations(THIRTEENTH|block,3)):
            raw.append((name,offset))
assert raw == []

print({
    "thirteenth_attempts_radius_64": 1032,
    "minimum_transversal_histogram": {3:3,4:8,5:25,6:84,7:163,8:240,9:15,10:37,11:123,12:135,13:135,14:64},
    "minimum_three_or_four_attempts": 11,
    "minimum_cores": 93,
    "all_best_cores_correctable_with_budget_at_most_seven": True,
    "minimum_correction_budget_histogram": {4:19,5:45,6:26,7:3},
    "canonical_transition": {"block":"P0","offset":56,"correction_size":4},
    "corrected_thirteenth_state_points": 104,
    "raw_fourteenth_attempts_radius_64": 1032,
    "raw_fourteenth_extensions": 0,
    "remaining_gap": "the corrected radius-64 path reaches thirteen blocks but has no raw fourteenth transition or verified recurrence",
    "evidence_level": "exact_corrected_thirteenth_transition",
    "status": "passed",
})
