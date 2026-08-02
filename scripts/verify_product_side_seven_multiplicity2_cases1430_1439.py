#!/usr/bin/env python3
"""Verify the selector-aware classification of multiplicity-two cases 1430--1439."""
from __future__ import annotations

import re
import subprocess
import tempfile
from pathlib import Path

EXPECTED = {
    1430: "FINAL case=1430 signature=257,6,1028,24,129,8224,8256 top_orders=20004,15852 top_nodes=59076,49027 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=49896,39549,52402,35786 rejection_total=177633 digest=9022283284995776830 PASS",
    1431: "FINAL case=1431 signature=257,6,1028,24,129,8224,12288 top_orders=20912,12032 top_nodes=71528,55502 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=55942,31651,53471,30795 rejection_total=171859 digest=13086807189344959278 PASS",
    1432: "FINAL case=1432 signature=257,6,1028,24,129,8256,4128 top_orders=15400,13496 top_nodes=52019,46127 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=35410,33685,38446,29267 rejection_total=136808 digest=18158334224973120649 PASS",
    1433: "FINAL case=1433 signature=257,6,1028,24,129,8256,4160 top_orders=14028,12816 top_nodes=47068,42072 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=32348,31689,36291,28298 rejection_total=128626 digest=18429921265688731684 PASS",
    1434: "FINAL case=1434 signature=257,6,1028,24,129,12288,96 top_orders=24224,39136 top_nodes=81410,122048 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=64152,98470,63071,94398 rejection_total=320091 digest=14206178255592492007 PASS",
    1435: "FINAL case=1435 signature=257,6,1028,24,129,12288,4160 top_orders=24076,65672 top_nodes=83464,210634 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=65813,170776,63360,172309 rejection_total=472258 digest=9947680513117902040 PASS",
    1436: "FINAL case=1436 signature=257,6,1028,24,2049,96,4160 top_orders=11124,2412 top_nodes=32552,8562 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=23418,6364,28993,5017 rejection_total=63792 digest=7034531801571772175 PASS",
    1437: "FINAL case=1437 signature=257,6,1028,24,2049,96,12288 top_orders=23296,1296 top_nodes=76557,9652 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=52770,3274,56705,2858 rejection_total=115607 digest=14608730979352190165 PASS",
    1438: "FINAL case=1438 signature=257,6,1028,24,2049,4128,4160 top_orders=20004,15852 top_nodes=59126,49017 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=49914,39375,52461,36280 rejection_total=178030 digest=17007583894268159062 PASS",
    1439: "FINAL case=1439 signature=257,6,1028,24,2049,4128,8256 top_orders=15400,13496 top_nodes=52215,46201 infeasible_selectors=2 constructive_selectors=0 rejection_nodes=35155,33429,38351,29324 rejection_total=136259 digest=10584922255083157802 PASS",
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
        subprocess.run(["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)], check=True)
        top_orders = [0, 0]
        top_nodes = [0, 0]
        rejection_nodes = [0, 0, 0, 0]
        infeasible = constructive = 0
        for case in range(1430, 1440):
            completed = subprocess.run([str(executable), str(case), "2"], check=True, capture_output=True, text=True)
            assert not any(line.startswith("FEASIBLE ") for line in completed.stdout.splitlines())
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

    assert top_orders == [188_468, 192_060]
    assert top_nodes == [615_015, 638_842]
    assert infeasible == 20 and constructive == 0
    assert rejection_nodes == [464_818, 488_262, 483_551, 464_332]
    assert sum(rejection_nodes) == 1_900_963
    print(
        "PX1218--PX1221 cases1430--1439: "
        "top_orders=188468,192060 top_nodes=615015,638842 "
        "infeasible_selectors=20 constructive_selectors=0 "
        "rejection_nodes=464818,488262,483551,464332 "
        "rejection_total=1900963 PASS"
    )


if __name__ == "__main__":
    main()
