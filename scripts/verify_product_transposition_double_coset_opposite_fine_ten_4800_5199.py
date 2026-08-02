#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 4800 through 5199 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        4800: (3_251_516, 483_718),
        4900: (2_122_630, 151_134),
        5000: (2_520_838, 205_642),
        5100: (4_523_858, 250_094),
    },
    "ff": {
        4800: (2_034_679, 99_810),
        4900: (1_714_119, 77_663),
        5000: (3_814_344, 503_447),
        5100: (4_017_219, 276_969),
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
            for first_pair in (4800, 4900, 5000, 5100):
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

    assert totals == {"fc": 12_418_842, "ff": 11_580_361}
    assert maxima == {"fc": 483_718, "ff": 503_447}
    print(
        "PX1191--PX1193 side-ten opposite-pair fine-row thirteenth prefix: "
        "fc_nodes=12418842 ff_nodes=11580361 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
