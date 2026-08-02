#!/usr/bin/env python3
"""Verify the combined thirty-reference semantic vocabulary census."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_TOP_INDICES = [
    0,1,3,5,6,7,8,9,10,11,
    32,33,36,37,38,39,40,41,49,50,
    51,52,55,56,57,58,60,61,62,63,
]
EXPECTED_FINAL = (
    "FINAL references=30 vocabulary=21 "
    "mask_counts=6920:1,6936:4,7432:1,7448:1,8984:1,9496:1,11032:7,11544:5 "
    "extension_sum=95 covered_union=57 overlap=38 bottom_checks=957600 "
    "digest=14270700727048114206 PASS"
)


def field(line: str, name: str) -> int:
    prefix = f"{name}="
    for token in line.split():
        if token.startswith(prefix):
            return int(token[len(prefix):])
    raise AssertionError((name, line))


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_combined.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-combined-vocabulary"
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

    lines = completed.stdout.strip().splitlines()
    summaries = [line for line in lines if line.startswith("top_index=")]
    assert [field(line, "top_index") for line in summaries] == EXPECTED_TOP_INDICES
    assert lines[-1] == EXPECTED_FINAL
    print(lines[-1])
    print("PX1062--PX1065 combined semantic vocabulary: PASS")


if __name__ == "__main__":
    main()
