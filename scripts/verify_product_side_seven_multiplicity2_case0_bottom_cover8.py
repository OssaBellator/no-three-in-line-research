#!/usr/bin/env python3
"""Verify eight-top greedy bottom covers for multiplicity-two case zero."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    0: (
        "FINAL multiplicity=2 case=0 orientation=0 top_orders=8 "
        "selector_covers=16 cover_entries=187 triple_dictionary=57 "
        "cover_dictionary=16 digest=5267506085810822176 PASS"
    ),
    1: (
        "FINAL multiplicity=2 case=0 orientation=1 top_orders=8 "
        "selector_covers=16 cover_entries=230 triple_dictionary=59 "
        "cover_dictionary=16 digest=2790833927980393128 PASS"
    ),
    2: (
        "FINAL multiplicity=2 case=0 orientation=2 top_orders=8 "
        "selector_covers=16 cover_entries=187 triple_dictionary=60 "
        "cover_dictionary=16 digest=17434165135039401592 PASS"
    ),
    3: (
        "FINAL multiplicity=2 case=0 orientation=3 top_orders=8 "
        "selector_covers=16 cover_entries=112 triple_dictionary=19 "
        "cover_dictionary=10 digest=5620182289796700611 PASS"
    ),
}

EXPECTED_SIZE_COUNTS = {
    0: {7: 1, 12: 15},
    1: {12: 8, 15: 1, 16: 5, 19: 1, 20: 1},
    2: {7: 8, 16: 7, 19: 1},
    3: {7: 16},
}


def parse_cover_sizes(output: str) -> dict[int, int]:
    counts: dict[int, int] = {}
    for line in output.splitlines():
        if not line.startswith("top_index="):
            continue
        marker = " greedy_cover="
        start = line.index(marker) + len(marker)
        size = int(line[start:].split()[0])
        counts[size] = counts.get(size, 0) + 1
    return counts


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_bottom_triple_cover.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "measure-cover"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        for orientation in range(4):
            completed = subprocess.run(
                [str(executable), "2", "0", str(orientation), "8"],
                check=True,
                capture_output=True,
                text=True,
            )
            output = completed.stdout.strip()
            final = output.splitlines()[-1]
            assert final == EXPECTED[orientation], (orientation, final)
            assert parse_cover_sizes(output) == EXPECTED_SIZE_COUNTS[orientation]
            print(final)

    print("PX997--PX999 multiplicity-two case-zero eight-top covers: PASS")


if __name__ == "__main__":
    main()
