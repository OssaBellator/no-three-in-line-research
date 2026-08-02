#!/usr/bin/env python3
"""Verify the semantic two-selector cover core at case zero, orientation three."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = """selector=0 delete_column=0 candidate_mask=11530 retained=6 clean_extensions=4 checked_extensions=4 top_nodes=21 tested_bottoms=20160 valid=1
selector=0 delete_column=1 candidate_mask=11528 retained=5 clean_extensions=11 checked_extensions=1 top_nodes=403 tested_bottoms=1 valid=0
selector=0 delete_column=3 candidate_mask=11522 retained=5 clean_extensions=7 checked_extensions=3 top_nodes=408 tested_bottoms=10111 valid=0
selector=0 delete_column=8 candidate_mask=11274 retained=5 clean_extensions=8 checked_extensions=2 top_nodes=33 tested_bottoms=5041 valid=0
selector=0 delete_column=10 candidate_mask=10506 retained=5 clean_extensions=12 checked_extensions=1 top_nodes=44 tested_bottoms=121 valid=0
selector=0 delete_column=11 candidate_mask=9482 retained=5 clean_extensions=5 checked_extensions=5 top_nodes=33 tested_bottoms=20311 valid=0
selector=0 delete_column=13 candidate_mask=3338 retained=5 clean_extensions=12 checked_extensions=1 top_nodes=44 tested_bottoms=153 valid=0
selector=0 syntactic_mask=11531 syntactic_size=7 semantic_mask=11530 semantic_size=6
selector=1 delete_column=0 candidate_mask=9502 retained=7 clean_extensions=5 checked_extensions=5 top_nodes=20 tested_bottoms=25200 valid=1
selector=1 delete_column=1 candidate_mask=9500 retained=6 clean_extensions=5 checked_extensions=5 top_nodes=29 tested_bottoms=25200 valid=1
selector=1 delete_column=2 candidate_mask=9496 retained=5 clean_extensions=5 checked_extensions=5 top_nodes=259 tested_bottoms=25200 valid=1
selector=1 delete_column=3 candidate_mask=9488 retained=4 clean_extensions=72 checked_extensions=1 top_nodes=1534 tested_bottoms=1 valid=0
selector=1 delete_column=4 candidate_mask=9480 retained=4 clean_extensions=25 checked_extensions=1 top_nodes=1336 tested_bottoms=1 valid=0
selector=1 delete_column=8 candidate_mask=9240 retained=4 clean_extensions=10 checked_extensions=2 top_nodes=463 tested_bottoms=5041 valid=0
selector=1 delete_column=10 candidate_mask=8472 retained=4 clean_extensions=18 checked_extensions=1 top_nodes=137 tested_bottoms=121 valid=0
selector=1 delete_column=13 candidate_mask=1304 retained=4 clean_extensions=20 checked_extensions=1 top_nodes=143 tested_bottoms=153 valid=0
selector=1 syntactic_mask=9503 syntactic_size=8 semantic_mask=9496 semantic_size=5
FINAL case=0 orientation=3 top_index=35 selector0_mask=11530 selector1_mask=9496 pair_mask=11546 pair_size=7 clean_extensions=4 top_nodes=15 tested_bottoms=40320 digest=2649867520580673397 PASS"""


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / (
        "measure_product_side_seven_multiplicity2_case0_"
        "orientation3_semantic_cover_core.cpp"
    )
    assert source.exists(), source
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-cover-core"
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
    print("PX1010--PX1012 semantic cover core: PASS")


if __name__ == "__main__":
    main()
