#!/usr/bin/env python3
"""Verify the deterministic irredundant cover of the 192-reference semantic union."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = (
    "FINAL references=192 vocabulary=150 universe=204 greedy_basis=116 "
    "irredundant_basis=115 "
    "greedy_gains=6,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 "
    "basis_indices=33,34,1,8,38,43,45,62,63,64,65,66,67,122,139,140,116,134,2,4,6,7,9,11,13,42,46,54,56,59,61,79,112,117,120,123,124,126,128,129,132,133,135,137,141,142,143,3,5,10,14,15,19,29,30,31,32,35,39,41,44,47,48,49,50,53,55,58,60,68,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,88,89,90,92,93,94,95,99,101,102,104,105,106,107,108,109,110,111,113,121,127,130,131,138,145,146,147,148,149 "
    "first_references=20,70,84,86,6,8,2,100,101,106,107,112,113,39,41,35,3,5,24,144,72,78,26,146,74,59,17,167,91,163,75,147,49,55,37,166,13,121,127,133,149,52,58,40,165,16,93,30,150,34,82,122,120,90,92,162,164,9,63,11,65,23,69,67,18,36,77,43,38,172,178,179,184,185,27,98,104,170,176,186,188,189,190,191,96,102,108,110,114,116,117,118,119,105,111,169,175,177,181,183,168,174,180,182,33,138,123,29,95,140,94,19,66,68,22 "
    "mask_sizes=5:7,6:27,7:31,8:39,9:11 "
    "extension_sizes=1:44,2:49,3:3,4:17,6:2 "
    "incidence_sum=231 unique_covered=177 maximum_overlap=2 "
    "validation_checks=2832480 digest=12529763722981785837 PASS"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_orientation3_"
        "semantic_set_cover192.cpp"
    )
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-set-cover192"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        completed = subprocess.run(
            [str(executable)], check=True, capture_output=True, text=True
        )
    assert completed.stdout.strip() == EXPECTED
    print(EXPECTED)
    print("PX1163--PX1166 semantic 192-reference irredundant cover: PASS")


if __name__ == "__main__":
    main()
