#!/usr/bin/env python3
"""Verify the next equal-support semantic vocabulary census."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_TOP_INDICES = [3,5,8,10,11,32,33,36,37,38,39,40,41,49,52,55,58,62]
EXPECTED_FINAL = (
    "FINAL references=18 vocabulary=16 "
    "mask_counts=7432:1,7448:1,8984:1,9496:1,11032:7,11544:5 "
    "extension_sum=55 covered_union=47 overlap=8 bottom_checks=554400 "
    "digest=1088196697277134895 PASS"
)


def parse_field(line: str, name: str) -> int:
    marker = f"{name}="
    for token in line.split():
        if token.startswith(marker):
            return int(token[len(marker):])
    raise AssertionError((name, line))


def main() -> None:
    root = Path(__file__).resolve().parent
    source = (
        root
        / "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_next_equal.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-next-equal-vocabulary"
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
    assert [parse_field(line, "top_index") for line in summaries] == EXPECTED_TOP_INDICES
    assert len(summaries) == 18
    assert lines[-1] == EXPECTED_FINAL
    print(lines[-1])
    print("PX1054--PX1057 next equal-support semantic vocabulary: PASS")


if __name__ == "__main__":
    main()
