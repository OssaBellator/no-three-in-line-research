#!/usr/bin/env python3
"""Verify top-column support of 64-top orientation-three covers."""
from __future__ import annotations

import collections
import subprocess
import tempfile
from pathlib import Path

EXPECTED_FINAL = (
    "FINAL multiplicity=2 case=0 orientation=3 top_orders=64 "
    "selector_covers=128 cover_entries=896 triple_dictionary=55 "
    "cover_dictionary=93 digest=5859277578097176413 PASS"
)
EXPECTED_SUPPORT_SIZES = {7: 1, 8: 9, 9: 33, 10: 79, 11: 6}
EXPECTED_UNIQUE_MASKS = 37
EXPECTED_COMMON_MASK = 6975
EXPECTED_COMMON_MASK_COUNT = 28
EXPECTED_MINIMUM_LINE = (
    "top_index=35 selector=0 available_triples=730 greedy_cover=7 "
    "top_support=7 support_mask=11531 support_dictionary=28 "
    "triple_dictionary=45 cover_dictionary=52 digest=4661741805201626164"
)


def parse_field(line: str, name: str) -> int:
    marker = f" {name}="
    start = line.index(marker) + len(marker)
    return int(line[start:].split()[0])


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_bottom_triple_cover.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "measure-cover-support"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        completed = subprocess.run(
            [str(executable), "2", "0", "3", "64"],
            check=True,
            capture_output=True,
            text=True,
        )

    lines = completed.stdout.strip().splitlines()
    obligation_lines = [line for line in lines if line.startswith("top_index=")]
    assert len(obligation_lines) == 128
    support_sizes = collections.Counter(
        parse_field(line, "top_support") for line in obligation_lines
    )
    support_masks = collections.Counter(
        parse_field(line, "support_mask") for line in obligation_lines
    )
    assert dict(sorted(support_sizes.items())) == EXPECTED_SUPPORT_SIZES
    assert len(support_masks) == EXPECTED_UNIQUE_MASKS
    assert support_masks[EXPECTED_COMMON_MASK] == EXPECTED_COMMON_MASK_COUNT
    assert EXPECTED_MINIMUM_LINE in obligation_lines
    assert lines[-1] == EXPECTED_FINAL
    print(lines[-1])
    print("PX1007--PX1009 orientation-three cover top support: PASS")


if __name__ == "__main__":
    main()
