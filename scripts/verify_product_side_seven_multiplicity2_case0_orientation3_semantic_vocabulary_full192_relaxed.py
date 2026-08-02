#!/usr/bin/env python3
"""Verify the relaxed complete 192-reference semantic vocabulary census."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_FINAL = (
    "FINAL references=192 vocabulary=150 baseline128_vocabulary=102 "
    "new_distinct_keys=48 reused_baseline128_references=15 "
    "equal_selector_masks=60 new_equal_selector_masks=20 "
    "pair_size_counts=5:11,6:64,7:45,8:56,9:16 "
    "new_pair_size_counts=5:4,6:19,7:10,8:22,9:9 "
    "selector0_cover_sizes=7:189,12:3 selector1_cover_sizes=7:192 "
    "new_selector0_cover_sizes=7:64 new_selector1_cover_sizes=7:64 "
    "mask_classes=57 extension_sum=443 new_extension_sum=127 "
    "covered_union=204 new_covered_union=40 overlap=239 "
    "bottom_checks=4465440 new_bottom_checks=1280160 "
    "digest=10342663634156701870 PASS"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_orientation3_"
        "semantic_vocabulary_full192_relaxed.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-full192-relaxed"
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
    print("PX1153--PX1157 relaxed 192-reference semantic vocabulary: PASS")


if __name__ == "__main__":
    main()
