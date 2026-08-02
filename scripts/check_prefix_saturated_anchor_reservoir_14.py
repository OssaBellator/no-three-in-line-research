#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
source = HERE / "check_prefix_saturated_anchor_reservoir_14.cpp"
with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_prefix_saturated_anchor_reservoir_14"
    subprocess.run(["c++", "-O3", "-std=c++17", str(source), "-o", str(binary)], check=True)
    completed = subprocess.run([str(binary)], check=True, capture_output=True, text=True)

expected = "OK compositions=8192 max_coordinate=100 components=1 component_sizes 14 pairing 5 6 7 8 9 10 11 12 13 0 1 2 3 4"
assert completed.stdout.strip() == expected

print({
    "saturated_source_grid_size": 14,
    "saturated_source_cells": 28,
    "row_degree": 2,
    "column_degree": 2,
    "source_no_three_in_line": True,
    "disjoint_anchor_pairs": 14,
    "pairing_shift": 5,
    "unary_run_compositions_checked": 8192,
    "cross_run_collinear_triples": 0,
    "maximum_coordinate": 100,
    "incidence_component_sizes": (14,),
    "componentwise_nesting": False,
    "remaining_gap": "the global fourteen-pair witness is one incidence cycle and does not provide a nested or uniform all-size family",
    "evidence_level": "explicit_fourteen_pair_saturated_anchor_reservoir",
    "status": "passed",
})
