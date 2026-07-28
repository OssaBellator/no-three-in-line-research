#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 1600 through 1999 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        1600: (1_983_296, 135_219),
        1700: (2_926_390, 118_965),
        1800: (1_094_675, 32_800),
        1900: (1_056_998, 30_605),
    },
    "ff": {
        1600: (1_728_800, 72_527),
        1700: (1_680_046, 66_093),
        1800: (667_922, 22_250),
        1900: (714_352, 27_231),
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
            for first_pair in (1600, 1700, 1800, 1900):
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

    assert totals == {"fc": 7_061_359, "ff": 4_791_120}
    assert maxima == {"fc": 135_219, "ff": 72_527}
    print(
        "PX1085--PX1087 side-ten opposite-pair fine-row fifth prefix: "
        "fc_nodes=7061359 ff_nodes=4791120 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
