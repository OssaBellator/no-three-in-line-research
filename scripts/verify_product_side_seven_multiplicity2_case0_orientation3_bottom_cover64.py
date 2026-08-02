#!/usr/bin/env python3
"""Verify 64-top orientation-three covers for multiplicity-two case zero."""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

EXPECTED_FINAL = (
    "FINAL multiplicity=2 case=0 orientation=3 top_orders=64 "
    "selector_covers=128 cover_entries=896 triple_dictionary=55 "
    "cover_dictionary=93 digest=5859277578097176413 PASS"
)

EXPECTED_CHECKPOINTS = {
    7: (19, 10, 5620182289796700611),
    15: (23, 22, 6505455452320121422),
    31: (41, 45, 18108530045113619216),
    47: (51, 77, 17761038493337610795),
    63: (55, 93, 5859277578097176413),
}


def parse_field(line: str, name: str) -> int:
    marker = f" {name}="
    start = line.index(marker) + len(marker)
    return int(line[start:].split()[0])


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
        completed = subprocess.run(
            [str(executable), "2", "0", "3", "64"],
            check=True,
            capture_output=True,
            text=True,
        )

    lines = completed.stdout.strip().splitlines()
    obligation_lines = [line for line in lines if line.startswith("top_index=")]
    assert len(obligation_lines) == 128
    assert all(parse_field(line, "greedy_cover") == 7 for line in obligation_lines)

    for top_index, expected in EXPECTED_CHECKPOINTS.items():
        line = next(
            line for line in obligation_lines
            if line.startswith(f"top_index={top_index} selector=1 ")
        )
        observed = (
            parse_field(line, "triple_dictionary"),
            parse_field(line, "cover_dictionary"),
            parse_field(line, "digest"),
        )
        assert observed == expected, (top_index, observed, expected)

    assert lines[-1] == EXPECTED_FINAL, lines[-1]
    print(lines[-1])
    print("PX1000--PX1002 multiplicity-two case-zero orientation-three cover64: PASS")


if __name__ == "__main__":
    main()
