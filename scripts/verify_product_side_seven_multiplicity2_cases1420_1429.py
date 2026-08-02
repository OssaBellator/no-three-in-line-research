#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1420--1429."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1420: "FINAL case=1420 signature=257,6,1028,24,17,8256,4128 top_orders=8964,18468 top_nodes=26348,52644 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=19792,48644,23040,37422 rejection_total=128898 digest=4183412894217143445 PASS",
    1421: "FINAL case=1421 signature=257,6,1028,24,17,8256,4160 top_orders=9672,20514 top_nodes=28003,57768 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=20683,55910,24641,42314 rejection_total=143548 digest=13222211643404472107 PASS",
    1422: "FINAL case=1422 signature=257,6,1028,24,17,12288,96 top_orders=23808,36720 top_nodes=67611,103288 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=55949,103228,62332,77256 rejection_total=298765 digest=7484813740925408592 PASS",
    1423: "FINAL case=1423 signature=257,6,1028,24,17,12288,4160 top_orders=38232,81186 top_nodes=108675,227307 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=102940,230576,103849,193924 rejection_total=631289 digest=16594429692102283552 PASS",
    1424: "FINAL case=1424 signature=257,6,1028,24,129,96,4160 top_orders=11124,2412 top_nodes=32544,8544 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=23427,6373,28902,4949 rejection_total=63651 digest=6418617360073411461 PASS",
    1425: "FINAL case=1425 signature=257,6,1028,24,129,96,12288 top_orders=23296,1296 top_nodes=76145,9476 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=53176,3352,56542,2784 rejection_total=115854 digest=769118598104101433 PASS",
    1426: "FINAL case=1426 signature=257,6,1028,24,129,4128,4160 top_orders=20004,15852 top_nodes=59076,49027 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=49896,39549,52402,35786 rejection_total=177633 digest=5604718688552064674 PASS",
    1427: "FINAL case=1427 signature=257,6,1028,24,129,4128,8256 top_orders=15400,13496 top_nodes=51945,46177 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=35413,33691,38453,29266 rejection_total=136823 digest=12021380072371610692 PASS",
    1428: "FINAL case=1428 signature=257,6,1028,24,129,8224,96 top_orders=9732,10524 top_nodes=28652,30784 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=23267,25813,25673,22489 rejection_total=97242 digest=12006458718341313019 PASS",
    1429: "FINAL case=1429 signature=257,6,1028,24,129,8224,4128 top_orders=14028,12816 top_nodes=47068,42072 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=32348,31689,36291,28298 rejection_total=128626 digest=7657698749909335184 PASS",
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
        for case in range(1420, 1430):
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

    assert top_orders == [174_260, 213_284]
    assert top_nodes == [526_067, 627_087]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [416_891, 578_825, 452_125, 474_488]
    assert sum(rejection_nodes) == 1_922_329
    print(
        "PX1211--PX1214 cases1420--1429: "
        "top_orders=174260,213284 top_nodes=526067,627087 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=416891,578825,452125,474488 "
        "rejection_total=1922329 PASS"
    )


if __name__ == "__main__":
    main()
