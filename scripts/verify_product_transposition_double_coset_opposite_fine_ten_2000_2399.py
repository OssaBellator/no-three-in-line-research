#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 2000 through 2399 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        2000: (2_159_382, 109_513),
        2100: (2_052_531, 98_292),
        2200: (5_243_099, 521_147),
        2300: (8_662_717, 955_107),
    },
    "ff": {
        2000: (1_835_243, 226_247),
        2100: (2_304_264, 153_011),
        2200: (3_124_937, 873_267),
        2300: (3_284_811, 270_865),
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
            for first_pair in (2000, 2100, 2200, 2300):
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

    assert totals == {"fc": 18_117_729, "ff": 10_549_255}
    assert maxima == {"fc": 955_107, "ff": 873_267}
    print(
        "PX1092--PX1094 side-ten opposite-pair fine-row sixth prefix: "
        "fc_nodes=18117729 ff_nodes=10549255 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
