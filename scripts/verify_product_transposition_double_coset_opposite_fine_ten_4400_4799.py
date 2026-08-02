#!/usr/bin/env python3
"""Verify opposite-pair fine-row pair indices 4400 through 4799 at side ten."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    "fc": {
        4400: (8_355_467, 1_877_339),
        4500: (13_288_964, 648_369),
        4600: (6_337_608, 917_874),
        4700: (5_578_776, 803_776),
    },
    "ff": {
        4400: (2_218_298, 327_084),
        4500: (2_420_162, 311_771),
        4600: (2_169_979, 118_690),
        4700: (2_168_742, 165_140),
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
            for first_pair in (4400, 4500, 4600, 4700):
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

    assert totals == {"fc": 33_560_815, "ff": 8_977_181}
    assert maxima == {"fc": 1_877_339, "ff": 327_084}
    print(
        "PX1184--PX1186 side-ten opposite-pair fine-row twelfth prefix: "
        "fc_nodes=33560815 ff_nodes=8977181 geometries=800 PASS"
    )


if __name__ == "__main__":
    main()
