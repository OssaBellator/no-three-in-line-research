#!/usr/bin/env python3
"""Verify the first 16 uncovered-top semantic expansion references."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = """REFERENCE top_index=192 pair_mask=1434 pair_size=6 new_key=1 clean_extensions=2 top_nodes=11
REFERENCE top_index=193 pair_mask=10136 pair_size=7 new_key=1 clean_extensions=1 top_nodes=21
REFERENCE top_index=194 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=50
REFERENCE top_index=195 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=36
REFERENCE top_index=196 pair_mask=9624 pair_size=6 new_key=1 clean_extensions=1 top_nodes=51
REFERENCE top_index=197 pair_mask=1434 pair_size=6 new_key=0 clean_extensions=2 top_nodes=11
REFERENCE top_index=198 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=50
REFERENCE top_index=199 pair_mask=10136 pair_size=7 new_key=1 clean_extensions=1 top_nodes=21
REFERENCE top_index=200 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=50
REFERENCE top_index=201 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=57
REFERENCE top_index=202 pair_mask=9624 pair_size=6 new_key=1 clean_extensions=1 top_nodes=51
REFERENCE top_index=203 pair_mask=1432 pair_size=5 new_key=1 clean_extensions=2 top_nodes=19
REFERENCE top_index=204 pair_mask=6040 pair_size=7 new_key=1 clean_extensions=1 top_nodes=25
REFERENCE top_index=205 pair_mask=6040 pair_size=7 new_key=1 clean_extensions=1 top_nodes=16
REFERENCE top_index=206 pair_mask=5528 pair_size=6 new_key=1 clean_extensions=2 top_nodes=51
REFERENCE top_index=207 pair_mask=1944 pair_size=6 new_key=1 clean_extensions=1 top_nodes=57
FINAL baseline_references=192 baseline_vocabulary=150 baseline_union=204 expansion_references=16 selected_indices=192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207 new_reference_keys=15 new_distinct_keys=15 expanded_vocabulary=165 extension_sum=20 union_growth=17 expanded_union=221 remaining_uncovered=34891 pair_size_counts=5:1,6:11,7:4 bottom_checks=201600 digest=16150749401146711547 PASS"""


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_orientation3_"
        "semantic_uncovered16.cpp"
    )
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-uncovered16"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        completed = subprocess.run(
            [str(executable)],
            check=True,
            capture_output=True,
            text=True,
        )

    assert completed.stdout.strip() == EXPECTED
    print(EXPECTED)
    print("PX1194--PX1196 uncovered-top semantic expansion 16: PASS")


if __name__ == "__main__":
    main()
