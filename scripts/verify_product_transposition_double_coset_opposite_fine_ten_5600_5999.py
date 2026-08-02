#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 5600 through 5999 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        5600: (4_273_810, 329_264),
        5700: (4_940_017, 569_902),
        5800: (3_618_878, 794_719),
        5900: (7_097_190, 715_911),
    },
    "ff": {
        5600: (2_277_537, 477_189),
        5700: (2_355_426, 188_842),
        5800: (2_987_768, 357_401),
        5900: (2_477_012, 472_540),
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
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        totals = {"fc": 0, "ff": 0}
        maxima = {"fc": 0, "ff": 0}
        for orientation in ("fc", "ff"):
            for first_pair in (5600, 5700, 5800, 5900):
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

    assert totals == {"fc": 19_929_895, "ff": 10_097_743}
    assert maxima == {"fc": 794_719, "ff": 477_189}
    print(
        "PX1208--PX1210 side-ten opposite-pair fine-row fifteenth prefix: "
        "fc_nodes=19929895 ff_nodes=10097743 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
