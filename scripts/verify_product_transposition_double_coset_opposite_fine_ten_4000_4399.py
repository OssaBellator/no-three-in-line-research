#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 4000 through 4399 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        4000: (3_575_001, 221_153),
        4100: (3_440_083, 618_518),
        4200: (5_245_873, 667_002),
        4300: (5_704_438, 860_978),
    },
    "ff": {
        4000: (2_341_449, 235_532),
        4100: (1_595_971, 99_407),
        4200: (2_603_319, 276_463),
        4300: (2_787_182, 390_524),
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
            for first_pair in (4000, 4100, 4200, 4300):
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

    assert totals == {"fc": 17_965_395, "ff": 9_327_921}
    assert maxima == {"fc": 860_978, "ff": 390_524}
    print(
        "PX1177--PX1179 side-ten opposite-pair fine-row eleventh prefix: "
        "fc_nodes=17965395 ff_nodes=9327921 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
