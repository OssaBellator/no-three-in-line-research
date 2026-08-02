#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1400--1409."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1400: "FINAL case=1400 signature=257,6,516,2064,2176,96,4160 top_orders=115966,16012 top_nodes=392567,75993 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=314721,44232,336589,48718 rejection_total=744260 digest=3729959886903785438 PASS",
    1401: "FINAL case=1401 signature=257,6,516,2064,2176,96,12288 top_orders=88364,4992 top_nodes=483110,79586 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=231446,12479,244457,16269 rejection_total=504651 digest=17491553376708229085 PASS",
    1402: "FINAL case=1402 signature=257,6,516,2064,2176,4128,4160 top_orders=62336,39954 top_nodes=242907,177766 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=175727,100508,173591,122011 rejection_total=571837 digest=16249811963486277739 PASS",
    1403: "FINAL case=1403 signature=257,6,516,2064,2176,4128,8256 top_orders=47031,32363 top_nodes=278798,192698 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=128039,82750,126769,89824 rejection_total=427382 digest=15807777010410543117 PASS",
    1404: "FINAL case=1404 signature=257,6,516,2064,2176,8224,96 top_orders=91364,70080 top_nodes=315008,232789 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=283388,190514,260744,210135 rejection_total=944781 digest=8335780563140783661 PASS",
    1405: "FINAL case=1405 signature=257,6,516,2064,2176,8224,4128 top_orders=57024,34670 top_nodes=336904,209659 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=157302,94235,162850,103773 rejection_total=518160 digest=594254067995011962 PASS",
    1406: "FINAL case=1406 signature=257,6,516,2064,2176,8224,8256 top_orders=62336,39954 top_nodes=242907,177766 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=175727,100508,173591,122011 rejection_total=571837 digest=7413084282017054975 PASS",
    1407: "FINAL case=1407 signature=257,6,516,2064,2176,8224,12288 top_orders=37652,15832 top_nodes=298482,227248 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=100375,41233,108826,44484 rejection_total=294918 digest=1367388716652260009 PASS",
    1408: "FINAL case=1408 signature=257,6,516,2064,2176,8256,4128 top_orders=47031,32363 top_nodes=280072,192100 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=128052,82767,126764,89825 rejection_total=427408 digest=9586278848783989832 PASS",
    1409: "FINAL case=1409 signature=257,6,516,2064,2176,8256,4160 top_orders=57024,34670 top_nodes=336904,209659 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=157302,94235,162850,103773 rejection_total=518160 digest=2832897585058173214 PASS",
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
        for case in range(1400, 1410):
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

    assert top_orders == [666_128, 320_890]
    assert top_nodes == [3_207_659, 1_775_264]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [1_852_079, 843_461, 1_877_031, 950_823]
    assert sum(rejection_nodes) == 5_523_394
    print(
        "PX1197--PX1200 cases1400--1409: "
        "top_orders=666128,320890 top_nodes=3207659,1775264 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=1852079,843461,1877031,950823 "
        "rejection_total=5523394 PASS"
    )


if __name__ == "__main__":
    main()
