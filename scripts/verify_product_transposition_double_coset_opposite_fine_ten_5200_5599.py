#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 5200 through 5599 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        5200: (4_853_835, 364_819),
        5300: (6_883_830, 331_606),
        5400: (3_553_773, 271_790),
        5500: (2_690_688, 133_796),
    },
    "ff": {
        5200: (2_602_193, 281_133),
        5300: (2_674_421, 243_337),
        5400: (1_884_284, 99_526),
        5500: (2_343_861, 186_593),
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
            for first_pair in (5200, 5300, 5400, 5500):
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

    assert totals == {"fc": 17_982_126, "ff": 9_504_759}
    assert maxima == {"fc": 364_819, "ff": 281_133}
    print(
        "PX1201--PX1203 side-ten opposite-pair fine-row fourteenth prefix: "
        "fc_nodes=17982126 ff_nodes=9504759 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
