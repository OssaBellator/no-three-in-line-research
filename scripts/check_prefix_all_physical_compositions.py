#!/usr/bin/env python3
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "check_prefix_all_physical_compositions.cpp"

with tempfile.TemporaryDirectory() as directory:
    binary = Path(directory) / "check_prefix_all_physical_compositions"
    subprocess.run(
        ["c++", "-O3", "-std=c++17", str(SOURCE), "-o", str(binary)],
        check=True,
    )
    result = subprocess.run(
        [str(binary)], check=True, capture_output=True, text=True
    )

assert result.stdout.splitlines() == [
    "matchings=104 cases=208 compositions=1024 audits=212992",
    "distance_hist 4:208",
    "optimal_route_count_hist 144:208",
    "deletion=0 maxcoord 120:52 132:52",
    "deletion=1 maxcoord 84:52 132:52",
]
assert result.stderr == ""

print({
    "minimum_crossing_matchings": 104,
    "deletion_cases_per_matching": 2,
    "physical_matching_deletion_cases": 208,
    "rerouting_distance_histogram": {4: 208},
    "optimal_route_count_histogram": {144: 208},
    "compositions_per_case": 1024,
    "coordinate_audits": 212992,
    "failures": 0,
    "maximum_coordinate_histograms": {
        "delete_0_2": {120: 52, 132: 52},
        "delete_3_5": {84: 52, 132: 52},
    },
    "selector": "lexicographically first optimal radius-four route",
    "remaining_gap": "the audit does not cover all 144 optimal routes per physical case or provide an all-size recurrence",
    "evidence_level": "exact_all_physical_matching_deterministic_route_lift",
    "status": "passed",
})
