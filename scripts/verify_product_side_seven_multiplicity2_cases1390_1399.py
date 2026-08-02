#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1390--1399."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1390: "FINAL case=1390 signature=257,6,516,2064,144,4128,4160 top_orders=66694,54318 top_nodes=232974,194720 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=179567,146816,186023,149757 rejection_total=662163 digest=4594628904029995916 PASS",
    1391: "FINAL case=1391 signature=257,6,516,2064,144,4128,8256 top_orders=49311,47433 top_nodes=241861,224610 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=128524,128788,132240,123328 rejection_total=512880 digest=5822347682282802730 PASS",
    1392: "FINAL case=1392 signature=257,6,516,2064,144,8224,96 top_orders=72786,70768 top_nodes=237922,226934 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=191704,195191,204306,182125 rejection_total=773326 digest=3809179463797773456 PASS",
    1393: "FINAL case=1393 signature=257,6,516,2064,144,8224,4128 top_orders=68626,57400 top_nodes=333911,272945 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=177078,160065,190594,163598 rejection_total=691335 digest=15167240076065072039 PASS",
    1394: "FINAL case=1394 signature=257,6,516,2064,144,8224,8256 top_orders=66694,54318 top_nodes=232974,194720 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=179567,146816,186023,149757 rejection_total=662163 digest=9838461318309294600 PASS",
    1395: "FINAL case=1395 signature=257,6,516,2064,144,8224,12288 top_orders=58304,35500 top_nodes=332187,264383 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=160274,95767,163577,102977 rejection_total=522595 digest=6505911925465808203 PASS",
    1396: "FINAL case=1396 signature=257,6,516,2064,144,8256,4128 top_orders=49311,47433 top_nodes=242035,223948 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=128533,128783,132225,123316 rejection_total=512857 digest=13009508480959642895 PASS",
    1397: "FINAL case=1397 signature=257,6,516,2064,144,8256,4160 top_orders=68626,57400 top_nodes=333911,272945 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=177078,160065,190594,163598 rejection_total=691335 digest=2640712232549379923 PASS",
    1398: "FINAL case=1398 signature=257,6,516,2064,144,12288,96 top_orders=71224,78048 top_nodes=338933,357116 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=211738,213389,192049,235823 rejection_total=852999 digest=7580872602665828403 PASS",
    1399: "FINAL case=1399 signature=257,6,516,2064,144,12288,4160 top_orders=60330,82980 top_nodes=329072,430679 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=168370,229566,171422,237999 rejection_total=807357 digest=7784300008166380410 PASS",
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
        for case in range(1390, 1400):
            completed = subprocess.run(
                [str(executable), str(case), "2"],
                check=True,
                capture_output=True,
                text=True,
            )
            assert "FEASIBLE " not in completed.stdout
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

    assert top_orders == [631_906, 585_598]
    assert top_nodes == [2_855_780, 2_663_000]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [1_702_433, 1_605_246, 1_749_053, 1_632_278]
    assert sum(rejection_nodes) == 6_689_010
    print(
        "PX1187--PX1190 cases1390--1399: "
        "top_orders=631906,585598 top_nodes=2855780,2663000 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=1702433,1605246,1749053,1632278 "
        "rejection_total=6689010 PASS"
    )


if __name__ == "__main__":
    main()
