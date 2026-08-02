#!/usr/bin/env python3
from collections import Counter
from itertools import combinations
from pathlib import Path
import subprocess
import tempfile

HERE=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    directory=Path(directory)
    outputs={}
    for stem in ("check_boundary_twelfth_spectrum","check_boundary_twelfth_corrections"):
        source=HERE/f"{stem}.cpp"; binary=directory/stem
        subprocess.run(["c++","-O3","-std=c++17",str(source),"-o",str(binary)],check=True)
        outputs[stem]=subprocess.run([str(binary)],check=True,capture_output=True,text=True)

spectrum=outputs["check_boundary_twelfth_spectrum"]
expected="hist 3:1 4:4 5:8 6:101 7:173 8:239 9:8 10:25 11:75 12:146 13:158 14:94 small=526 sets=18187"
assert expected in spectrum.stderr
small=[line for line in spectrum.stdout.splitlines() if " min 3 " in line or " min 4 " in line]
assert small==[
    "P1 63 min 4 triples 6 sets 15",
    "P1 64 min 4 triples 9 sets 1",
    "P2 64 min 3 triples 4 sets 9",
    "P3 61 min 4 triples 6 sets 9",
    "P3 64 min 4 triples 5 sets 27",
]
assert sum(int(line.rsplit(" ",1)[1]) for line in small)==61

corrections=outputs["check_boundary_twelfth_corrections"]
assert "attempts=5 cores=61 successes=5" in corrections.stderr
assert corrections.stdout.count(" budget ")==5
assert "P2 64 min 3 budget 5" in corrections.stdout
assert "D (2,1) (14,48) (32,98) (46,257) (47,258)" in corrections.stdout
assert "A (2,257) (14,258) (32,98) (46,1) (47,48)" in corrections.stdout

ELEVENTH=frozenset({
(0,110),(0,196),(1,61),(1,113),(2,1),(2,98),(3,3),(3,100),(4,33),(4,77),(5,1),(5,35),(6,2),(6,33),(7,32),(7,35),(8,34),(8,105),(9,59),(9,60),(10,58),(10,61),(11,59),(11,60),(12,2),(12,105),(13,46),(13,77),(14,47),(14,48),(15,46),(15,49),(16,75),(16,76),(17,74),(17,99),(18,75),(18,76),(19,0),(19,74),(20,106),(20,107),(21,0),(21,108),(22,106),(22,107),(23,58),(23,195),(24,82),(24,110),(25,80),(25,81),(26,47),(26,48),(27,80),(27,81),(28,3),(28,108),(29,111),(29,112),(30,49),(30,113),(31,111),(31,112),(32,79),(32,98),(33,99),(33,101),(34,32),(34,101),(35,82),(35,100),(36,163),(36,164),(37,162),(37,165),(38,163),(38,164),(39,162),(39,165),(40,34),(40,193),(41,194),(41,195),(42,193),(42,196),(43,79),(43,194)
})
TWELFTH_BLOCK={(44,258),(44,260),(45,257),(45,259),(46,257),(46,259),(47,258),(47,260)}
DELETED={(2,1),(14,48),(32,98),(46,257),(47,258)}
ADDED={(2,257),(14,258),(32,98),(46,1),(47,48)}
assert Counter(x for x,_ in DELETED)==Counter(x for x,_ in ADDED)
assert Counter(y for _,y in DELETED)==Counter(y for _,y in ADDED)
TWELFTH=frozenset((set(ELEVENTH)|TWELFTH_BLOCK)-DELETED|ADDED)

def collinear(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0])
assert len(TWELFTH)==96
assert all(not collinear(*triple) for triple in combinations(TWELFTH,3))

NODES={
"P0":((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2)),
"P1":((0,0),(0,3),(1,1),(1,2),(2,0),(2,3),(3,1),(3,2)),
"P2":((0,1),(0,3),(1,0),(1,2),(2,0),(2,2),(3,1),(3,3)),
"P3":((0,1),(0,2),(1,0),(1,3),(2,1),(2,2),(3,0),(3,3)),
"Q0":((0,3),(0,5),(1,0),(1,6),(2,2),(2,4),(3,1),(3,5),(4,2),(4,4),(5,0),(5,6),(6,1),(6,3)),
"Q1":((0,1),(0,5),(1,0),(1,3),(2,2),(2,4),(3,0),(3,6),(4,2),(4,4),(5,3),(5,6),(6,1),(6,5)),
"Q2":((0,1),(0,3),(1,0),(1,6),(2,2),(2,4),(3,1),(3,5),(4,2),(4,4),(5,0),(5,6),(6,3),(6,5)),
"Q3":((0,1),(0,5),(1,3),(1,6),(2,2),(2,4),(3,0),(3,6),(4,2),(4,4),(5,0),(5,3),(6,1),(6,5)),
}
raw=[]
for name,points in NODES.items():
    for offset in range(-64,65):
        block={(48+x,257+offset+y) for x,y in points}
        if all(not collinear(*triple) for triple in combinations(TWELFTH|block,3)):
            raw.append((name,offset))
assert raw==[]

print({
    "twelfth_attempts_radius_64":1032,
    "minimum_transversal_histogram":{3:1,4:4,5:8,6:101,7:173,8:239,9:8,10:25,11:75,12:146,13:158,14:94},
    "minimum_three_or_four_attempts":5,
    "minimum_cores":61,
    "attempts_with_correction_budget_at_most_seven":5,
    "canonical_transition":{"block":"P2","offset":64,"minimum_transversal":3,"correction_size":5},
    "corrected_twelfth_state_points":96,
    "raw_thirteenth_attempts_radius_64":1032,
    "raw_thirteenth_extensions":0,
    "remaining_gap":"the corrected radius-64 path reaches twelve blocks but has no raw thirteenth transition or verified recurrence",
    "evidence_level":"exact_corrected_twelfth_transition",
    "status":"passed",
})
