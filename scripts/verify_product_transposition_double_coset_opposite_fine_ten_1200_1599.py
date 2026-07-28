#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 1200 through 1599 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        1200: (1_227_566, 49_897),
        1300: (2_062_659, 170_613),
        1400: (1_340_627, 52_920),
        1500: (2_415_553, 105_685),
    },
    "ff": {
        1200: (5_682_907, 909_040),
        1300: (4_321_785, 228_366),
        1400: (2_649_324, 105_192),
        1500: (2_571_980, 116_732),
    },
}
LINE = re.compile(
    r"^NONE n=10 o=(fc|ff) distance=5 maps=200 first=(\d+) "
    r"pairs=100 total=(\d+) avg=(\d+) max=(\d+)$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "search_product_transposition_double_coset_ten.cpp"
    assert source.exists(), source

    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "double-coset-search"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        totals = {"fc": 0, "ff": 0}
        maxima = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (1200, 1300, 1400, 1500):
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
                assert match.group(1) == orientation
                assert int(match.group(2)) == first_pair
                total = int(match.group(3))
                average = int(match.group(4))
                maximum = int(match.group(5))
                assert (total, maximum) == EXPECTED[orientation][first_pair]
                assert average == total // 100
                totals[orientation] += total
                maxima[orientation] = max(maxima[orientation], maximum)
                print(output)

    assert totals == {"fc": 7_046_405, "ff": 15_225_996}
    assert maxima == {"fc": 170_613, "ff": 909_040}
    print(
        "PX1069--PX1071 side-ten opposite-pair fine-row fourth prefix: "
        "fc_nodes=7046405 ff_nodes=15225996 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
