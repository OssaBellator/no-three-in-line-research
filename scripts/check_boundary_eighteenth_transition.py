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
        "check_boundary_eighteenth_corrections",
        "check_boundary_nineteenth_spectrum",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(
            ["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)],
            check=True,
        )
        outputs[stem] = subprocess.run(
            [str(binary)],
            check=True,
            capture_output=True,
            text=True,
        )

corrections = outputs["check_boundary_eighteenth_corrections"].stdout.splitlines()
assert corrections == [
    "P0/-39 core1 first none_through_6 tested 4:24 5:16560 6:6782040",
    "P0/-39 core2 first 6 tested 4:24 5:16560 6:562887",
    "D (2,257) (31,111) (58,347) (69,216) (71,213) (71,215)",
    "A (2,213) (31,257) (58,216) (69,215) (71,111) (71,347)",
    "P0/-39 core3 first none_through_6 tested 4:12 5:8340 6:3440430",
    "P2/-40 core1 first none_through_6 tested 4:24 5:16560 6:6782040",
    "P2/-40 core2 first none_through_6 tested 4:24 5:16560 6:6782040",
    "P2/-40 core3 first none_through_6 tested 4:12 5:8340 6:3440430",
    "P2/-26 core1 first none_through_6 tested 4:12 5:8340 6:3440430",
]

spectrum = outputs["check_boundary_nineteenth_spectrum"]
assert spectrum.stderr.splitlines() == [
    "state=144",
    "hist 4:2 5:9 6:47 7:175 8:283 9:3 10:16 11:63 12:121 13:176 14:137 small=58 sets=495",
]
low = [line for line in spectrum.stdout.splitlines() if " min 4 " in line]
assert low == [
    "P1 -33 min 4 triples 10 cores 1",
    "P2 -64 min 4 triples 9 cores 5",
]

def points_from_source(path):
    text = path.read_text()
    match = re.search(r"vector<Pt> T=\{(.*?)\};\s*sort", text, re.S)
    assert match
    return {
        (int(x), int(y))
        for x, y in re.findall(r"\{(-?\d+),(-?\d+)\}", match.group(1))
    }

SEVENTEENTH = points_from_source(HERE / "check_boundary_eighteenth_spectrum.cpp")
NINETEENTH_BASE = points_from_source(HERE / "check_boundary_nineteenth_spectrum.cpp")
assert len(SEVENTEENTH) == 136
assert len(NINETEENTH_BASE) == 144

P0 = ((0,0),(0,2),(1,1),(1,3),(2,1),(2,3),(3,0),(3,2))
BLOCK = {(68+x, 213+y) for x, y in P0}
DELETED = {(2,257),(31,111),(58,347),(69,216),(71,213),(71,215)}
ADDED = {(2,213),(31,257),(58,216),(69,215),(71,111),(71,347)}
assert Counter(x for x, _ in DELETED) == Counter(x for x, _ in ADDED)
assert Counter(y for _, y in DELETED) == Counter(y for _, y in ADDED)
CORRECTED = (SEVENTEENTH | BLOCK) - DELETED | ADDED
assert CORRECTED == NINETEENTH_BASE
assert len(CORRECTED) == 144

def collinear(first, second, third):
    return (
        (second[0]-first[0])*(third[1]-first[1])
        == (second[1]-first[1])*(third[0]-first[0])
    )

assert all(not collinear(*triple) for triple in combinations(CORRECTED, 3))

print({
    "eighteenth_minimum_cores": 7,
    "budgets_exhausted": (4,5,6),
    "cores_correctable_through_budget_six": 1,
    "canonical_attempt": "P0/-39",
    "canonical_core": 2,
    "canonical_correction_size": 6,
    "corrected_eighteenth_state_points": 144,
    "corrected_eighteenth_state_blocks": 18,
    "raw_nineteenth_attempts": 1032,
    "raw_nineteenth_extensions": 0,
    "raw_nineteenth_minimum_transversal_histogram": {
        4:2,5:9,6:47,7:175,8:283,9:3,10:16,11:63,12:121,13:176,14:137,
    },
    "minimum_four_nineteenth_attempts": {"P1/-33": 1, "P2/-64": 5},
    "status": "passed",
})
