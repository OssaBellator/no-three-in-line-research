#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 6400 through 6799 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        6400: (1_307_940, 50_519),
        6500: (1_849_486, 73_456),
        6600: (1_991_015, 89_440),
        6700: (2_663_691, 80_905),
    },
    "ff": {
        6400: (2_081_486, 99_345),
        6500: (2_784_407, 161_219),
        6600: (4_660_688, 566_774),
        6700: (5_073_185, 330_134),
    },
}
LINE = re.compile(
    r"^NONE n=10 o=(fc|ff) distance=5 maps=200 first=(\d+) "
    r"pairs=100 total=(\d+) avg=(\d+) max=(\d+)$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "search_product_transposition_double_coset_ten.cpp"
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double-coset-search"
        subprocess.run(["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)], check=True)
        totals = {"fc": 0, "ff": 0}
        maxima = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (6400, 6500, 6600, 6700):
                completed = subprocess.run(
                    [str(executable), orientation, "5", str(first_pair), "100"],
                    check=True,
                    capture_output=True,
                    text=True,
                )
                output = completed.stdout.strip()
                assert not output.startswith("FOUND"), output
                match = LINE.fullmatch(output)
                assert match is not None, output
                total = int(match.group(3))
                average = int(match.group(4))
                maximum = int(match.group(5))
                assert (total, maximum) == EXPECTED[orientation][first_pair]
                assert average == total // 100
                totals[orientation] += total
                maxima[orientation] = max(maxima[orientation], maximum)
                print(output)

    assert totals == {"fc": 7_812_132, "ff": 14_599_766}
    assert maxima == {"fc": 89_440, "ff": 566_774}
    print(
        "PX1222--PX1224 side-ten opposite-pair fine-row seventeenth prefix: "
        "fc_nodes=7812132 ff_nodes=14599766 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
