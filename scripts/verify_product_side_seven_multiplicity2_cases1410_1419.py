#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1410--1419."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1410: "FINAL case=1410 signature=257,6,516,2064,2176,12288,96 top_orders=57100,106140 top_nodes=341445,467360 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=187822,281869,152568,332266 rejection_total=954525 digest=17584218828418708989 PASS",
    1411: "FINAL case=1411 signature=257,6,516,2064,2176,12288,4160 top_orders=29902,84038 top_nodes=249035,511132 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=86949,222603,85107,225870 rejection_total=620529 digest=2957650116471118414 PASS",
    1412: "FINAL case=1412 signature=257,6,1028,24,17,96,4160 top_orders=2424,4056 top_nodes=7476,11992 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=4916,14582,6496,8112 rejection_total=34106 digest=2222917410722152829 PASS",
    1413: "FINAL case=1413 signature=257,6,1028,24,17,96,12288 top_orders=10968,4200 top_nodes=32043,13835 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=25069,14423,26176,8592 rejection_total=74260 digest=4273257825716142296 PASS",
    1414: "FINAL case=1414 signature=257,6,1028,24,17,4128,4160 top_orders=13008,21408 top_nodes=36729,59854 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=29333,56505,36143,43578 rejection_total=165559 digest=14893605509215099704 PASS",
    1415: "FINAL case=1415 signature=257,6,1028,24,17,4128,8256 top_orders=8964,18468 top_nodes=26347,52650 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=19791,48635,23045,37422 rejection_total=128893 digest=5331428447541144751 PASS",
    1416: "FINAL case=1416 signature=257,6,1028,24,17,8224,96 top_orders=4224,10848 top_nodes=12373,30425 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=8795,25879,10141,21738 rejection_total=66553 digest=493467968458165697 PASS",
    1417: "FINAL case=1417 signature=257,6,1028,24,17,8224,4128 top_orders=9672,20514 top_nodes=28003,57768 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=20683,55910,24641,42314 rejection_total=143548 digest=17855131710443158887 PASS",
    1418: "FINAL case=1418 signature=257,6,1028,24,17,8224,8256 top_orders=13008,21408 top_nodes=36729,59854 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=29333,56505,36143,43578 rejection_total=165559 digest=14861941076081487932 PASS",
    1419: "FINAL case=1419 signature=257,6,1028,24,17,8224,12288 top_orders=25182,30312 top_nodes=71897,88906 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=70308,89501,65219,69614 rejection_total=294642 digest=11557078296270044135 PASS",
}
FINAL_RE = re.compile(
    r"^FINAL case=(\d+).* top_orders=(\d+),(\d+) top_nodes=(\d+),(\d+) "
    r"infeasible_selectors=(\d+) constructive_selectors=(\d+) "
    r"rejection_nodes=(\d+),(\d+),(\d+),(\d+) rejection_total=(\d+) "
    r"digest=(\d+) PASS$"
)


def main() -> None:
    root = Path(__file__).resolve().parent
    source = root / "measure_product_side_seven_single_case_all_selectors.cpp"
    with tempfile.TemporaryDirectory() as temporary_directory:
        executable = Path(temporary_directory) / "classify-case"
        subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            check=True,
        )
        top_orders = [0, 0]
        top_nodes = [0, 0]
        rejection_nodes = [0, 0, 0, 0]
        infeasible = constructive = 0
        for case in range(1410, 1420):
            completed = subprocess.run(
                [str(executable), str(case), "2"],
                check=True,
                capture_output=True,
                text=True,
            )
            assert not any(
                line.startswith("FEASIBLE ")
                for line in completed.stdout.splitlines()
            )
            final = completed.stdout.strip().splitlines()[-1]
            assert final == EXPECTED[case]
            match = FINAL_RE.fullmatch(final)
            assert match is not None
            values = [int(value) for value in match.groups()]
            top_orders[0] += values[1]
            top_orders[1] += values[2]
            top_nodes[0] += values[3]
            top_nodes[1] += values[4]
            infeasible += values[5]
            constructive += values[6]
            for orientation in range(4):
                rejection_nodes[orientation] += values[7 + orientation]
            assert sum(values[7:11]) == values[11]
            print(final)

    assert top_orders == [174_452, 321_392]
    assert top_nodes == [842_077, 1_353_776]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [482_999, 866_412, 465_679, 833_084]
    assert sum(rejection_nodes) == 2_648_174
    print(
        "PX1204--PX1207 cases1410--1419: "
        "top_orders=174452,321392 top_nodes=842077,1353776 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=482999,866412,465679,833084 "
        "rejection_total=2648174 PASS"
    )


if __name__ == "__main__":
    main()
