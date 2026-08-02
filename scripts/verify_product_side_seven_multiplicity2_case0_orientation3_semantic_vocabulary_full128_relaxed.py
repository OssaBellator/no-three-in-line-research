#!/usr/bin/env python3
"""Verify the relaxed complete 128-reference semantic vocabulary census."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_FINAL = (
    "FINAL references=128 vocabulary=102 baseline_vocabulary=49 "
    "new_distinct_keys=53 reused_baseline_references=7 "
    "equal_selector_masks=40 new_equal_selector_masks=10 "
    "pair_size_counts=5:7,6:45,7:35,8:34,9:7 "
    "new_pair_size_counts=5:3,6:9,7:19,8:27,9:6 "
    "selector0_cover_sizes=7:125,12:3 selector1_cover_sizes=7:128 "
    "new_selector0_cover_sizes=7:61,12:3 new_selector1_cover_sizes=7:64 "
    "mask_classes=49 extension_sum=316 new_extension_sum=147 "
    "covered_union=164 new_covered_union=72 overlap=152 "
    "bottom_checks=3185280 new_bottom_checks=1481760 "
    "digest=14068988073173727216 PASS"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_orientation3_"
        "semantic_vocabulary_full128_relaxed.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-full128-relaxed"
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

    assert completed.stdout.strip() == EXPECTED_FINAL
    print(EXPECTED_FINAL)
    print("PX1109--PX1113 relaxed 128-reference semantic vocabulary: PASS")


if __name__ == "__main__":
    main()
