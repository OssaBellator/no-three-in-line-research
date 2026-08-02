#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    outputs = {}
    for stem in (
        "check_prefix_14_low_defect_search",
        "check_prefix_saturated_anchor_reservoir_14_components",
    ):
        source = HERE / f"{stem}.cpp"
        binary = directory / stem
        subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
        outputs[stem] = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

search = outputs["check_prefix_14_low_defect_search"]
assert "depth=14 best=0 seen=884907" in search.stderr
assert search.stdout.splitlines() == [
    "P 8 3 4 11 13 6 1 12 7 0 10 5 2 9",
    "Q 4 11 8 3 7 12 13 0 1 6 2 9 10 5",
]

reservoir = outputs["check_prefix_saturated_anchor_reservoir_14_components"]
assert "compositions=8192 maximum_coordinate=80 components=2,2,2,2,3,3 induced12=4 induced11=2 component_anchor=false" in reservoir.stdout
assert "PAIR 1 0 3 2 5 4 7 6 9 8 11 10 13 12" in reservoir.stdout

print({
    "global_search_states_scored": 884907,
    "legal_source_search_depth": 14,
    "saturated_source_grid_size": 14,
    "saturated_source_cells": 28,
    "source_no_three_in_line": True,
    "disjoint_anchor_pairs": 14,
    "unary_run_compositions_checked": 8192,
    "maximum_coordinate": 80,
    "incidence_component_pair_sizes": (2,2,2,2,3,3),
    "induced_twelve_pair_subsources": 4,
    "induced_eleven_pair_subsources": 2,
    "component_respecting_anchor_pairing": False,
    "remaining_gap": "finite reservoirs reach fourteen pairs, but no uniform all-size source or anchor-compatible recurrence is known",
    "evidence_level": "explicit_fourteen_pair_saturated_anchor_reservoir",
    "status": "passed",
})
