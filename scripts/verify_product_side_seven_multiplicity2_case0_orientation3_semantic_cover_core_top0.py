#!/usr/bin/env python3
"""Verify the common-mask semantic cover core at top order zero."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = """selector=0 delete_column=0 candidate_mask=6974 retained=9 clean_extensions=4 checked_extensions=4 top_nodes=13 tested_bottoms=20160 valid=1
selector=0 delete_column=1 candidate_mask=6972 retained=8 clean_extensions=4 checked_extensions=4 top_nodes=14 tested_bottoms=20160 valid=1
selector=0 delete_column=2 candidate_mask=6968 retained=7 clean_extensions=4 checked_extensions=4 top_nodes=16 tested_bottoms=20160 valid=1
selector=0 delete_column=3 candidate_mask=6960 retained=6 clean_extensions=20 checked_extensions=1 top_nodes=176 tested_bottoms=1 valid=0
selector=0 delete_column=4 candidate_mask=6952 retained=6 clean_extensions=6 checked_extensions=5 top_nodes=33 tested_bottoms=20161 valid=0
selector=0 delete_column=5 candidate_mask=6936 retained=6 clean_extensions=4 checked_extensions=4 top_nodes=128 tested_bottoms=20160 valid=1
selector=0 delete_column=8 candidate_mask=6680 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=53 tested_bottoms=10801 valid=0
selector=0 delete_column=9 candidate_mask=6424 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=53 tested_bottoms=10081 valid=0
selector=0 delete_column=11 candidate_mask=4888 retained=5 clean_extensions=10 checked_extensions=5 top_nodes=337 tested_bottoms=20311 valid=0
selector=0 delete_column=12 candidate_mask=2840 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=54 tested_bottoms=10234 valid=0
selector=0 syntactic_mask=6975 syntactic_size=10 semantic_mask=6936 semantic_size=6
selector=1 delete_column=0 candidate_mask=6974 retained=9 clean_extensions=4 checked_extensions=4 top_nodes=13 tested_bottoms=20160 valid=1
selector=1 delete_column=1 candidate_mask=6972 retained=8 clean_extensions=4 checked_extensions=4 top_nodes=14 tested_bottoms=20160 valid=1
selector=1 delete_column=2 candidate_mask=6968 retained=7 clean_extensions=4 checked_extensions=4 top_nodes=16 tested_bottoms=20160 valid=1
selector=1 delete_column=3 candidate_mask=6960 retained=6 clean_extensions=20 checked_extensions=1 top_nodes=176 tested_bottoms=1 valid=0
selector=1 delete_column=4 candidate_mask=6952 retained=6 clean_extensions=6 checked_extensions=5 top_nodes=33 tested_bottoms=20161 valid=0
selector=1 delete_column=5 candidate_mask=6936 retained=6 clean_extensions=4 checked_extensions=4 top_nodes=128 tested_bottoms=20160 valid=1
selector=1 delete_column=8 candidate_mask=6680 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=53 tested_bottoms=10801 valid=0
selector=1 delete_column=9 candidate_mask=6424 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=53 tested_bottoms=10081 valid=0
selector=1 delete_column=11 candidate_mask=4888 retained=5 clean_extensions=10 checked_extensions=5 top_nodes=337 tested_bottoms=20305 valid=0
selector=1 delete_column=12 candidate_mask=2840 retained=5 clean_extensions=12 checked_extensions=3 top_nodes=54 tested_bottoms=10234 valid=0
selector=1 syntactic_mask=6975 syntactic_size=10 semantic_mask=6936 semantic_size=6
FINAL case=0 orientation=3 top_index=0 selector0_mask=6936 selector1_mask=6936 pair_mask=6936 pair_size=6 clean_extensions=4 top_nodes=128 tested_bottoms=40320 digest=7882978161453882300 PASS"""


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_"
        "orientation3_semantic_cover_core_top0.cpp"
    )
    assert source.exists(), source
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-cover-core-top0"
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
    output = completed.stdout.strip()
    assert output == EXPECTED, output
    print(output.splitlines()[-1])
    print("PX1013--PX1015 common semantic cover core: PASS")


if __name__ == "__main__":
    main()
