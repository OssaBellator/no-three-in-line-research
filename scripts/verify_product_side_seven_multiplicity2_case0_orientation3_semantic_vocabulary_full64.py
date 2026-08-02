#!/usr/bin/env python3
"""Verify the complete 64-reference semantic vocabulary census."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_FINAL = (
    "FINAL references=64 vocabulary=49 equal_selector_masks=30 "
    "pair_size_counts=5:4,6:36,7:16,8:7,9:1 mask_classes=30 "
    "extension_sum=169 covered_union=92 overlap=77 bottom_checks=1703520 "
    "digest=8868513888596877870 PASS"
)


def field(line: str, name: str) -> int:
    prefix = f"{name}="
    for token in line.split():
        if token.startswith(prefix):
            return int(token[len(prefix):])
    raise AssertionError((name, line))


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_multiplicity2_case0_orientation3_semantic_vocabulary_full64.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "semantic-full64-vocabulary"
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
    assert len(summaries) == 64
    assert [field(line, "top_index") for line in summaries] == list(range(64))
    assert lines[-1] == EXPECTED_FINAL
    print(lines[-1])
    print("PX1076--PX1080 complete 64-reference semantic vocabulary: PASS")


if __name__ == "__main__":
    main()
