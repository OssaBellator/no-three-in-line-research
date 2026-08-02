#!/usr/bin/env python3
"""Verify the deduplicated case-zero orientation-three semantic vocabulary."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_TOP_INDICES = [0, 1, 6, 7, 9, 50, 51, 56, 57, 60, 61, 63]
EXPECTED_FINAL = (
    "FINAL references=12 vocabulary=5 mask6936_keys=4 mask6920_keys=1 "
    "extension_sum=40 covered_union=14 overlap=26 bottom_checks=403200 "
    "digest=11777308162869991640 PASS"
)


def parse_field(line: str, name: str) -> int:
    marker = f" {name}="
    start = line.index(marker) + len(marker)
    return int(line[start:].split()[0])


def main() -> None:
    root = Path(__file__).resolve().parent
    source = (
        root
        / "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary.cpp"
    )
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "measure-semantic-vocabulary"
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
    assert len(summaries) == 12
    assert lines[-1] == EXPECTED_FINAL
    print(lines[-1])
    print("PX1030--PX1032 semantic vocabulary coverage: PASS")


if __name__ == "__main__":
    main()
