#!/usr/bin/env python3
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(points: list[list[int]]) -> list[int]:
    assert all(point[0] == index for index, point in enumerate(points, 1))
    values = [point[1] for point in points]
    assert sorted(values) == list(range(1, 31))
    return values


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def potential(red: list[int], blue: list[int]) -> int:
    points = [(index, value) for index, value in enumerate(red, 1)]
    points += [(index, value) for index, value in enumerate(blue, 1)]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def replay(
    red: list[int],
    blue: list[int],
    moves: list[str],
    potentials: list[int],
) -> int:
    assert len(potentials) == len(moves) + 1
    assert potential(red, blue) == potentials[0]
    for index, word in enumerate(moves):
        layer, row_word = word.split(":")
        first, second = (int(value) - 1 for value in row_word.split(","))
        active = blue if layer == "b" else red
        other = red if layer == "b" else blue
        assert active[second] != other[first]
        assert active[first] != other[second]
        active[first], active[second] = active[second], active[first]
        assert potential(red, blue) == potentials[index + 1]
    return len(moves)


def assert_state(red: list[int], blue: list[int], red_points, blue_points) -> None:
    assert red == rows(red_points)
    assert blue == rows(blue_points)
    assert all(red[index] != blue[index] for index in range(30))


def main() -> None:
    initial = json.loads((ROOT / "data/ac-p31-explicit-switch-frontier.json").read_text())
    recovered = json.loads((ROOT / "data/ac-p31-recovered-tail.json").read_text())
    five_to_four = json.loads((ROOT / "data/ac-p31-five-to-four.json").read_text())
    four_to_three = json.loads((ROOT / "data/ac-p31-four-to-three.json").read_text())

    red = rows(initial["installed_red"])
    blue = rows(initial["installed_blue"])
    assert potential(red, blue) == initial["installed_potential"] == 75

    switches = 0
    for segment in initial["segments"]:
        switches += replay(red, blue, segment["moves"], segment["potentials"])
    assert switches == initial["total_switches"] == 154
    assert_state(red, blue, initial["final_red"], initial["final_blue"])
    assert potential(red, blue) == initial["final_potential"] == 6

    assert_state(red, blue, recovered["start_red"], recovered["start_blue"])
    for segment in recovered["segments"]:
        switches += replay(red, blue, segment["moves"], segment["potentials"])
    assert_state(red, blue, recovered["final_red"], recovered["final_blue"])
    assert potential(red, blue) == recovered["final_potential"] == 5

    assert_state(red, blue, five_to_four["start_red"], five_to_four["start_blue"])
    switches += replay(red, blue, five_to_four["moves"], five_to_four["potentials"])
    assert_state(red, blue, five_to_four["final_red"], five_to_four["final_blue"])
    assert potential(red, blue) == five_to_four["final_potential"] == 4

    assert_state(red, blue, four_to_three["start_red"], four_to_three["start_blue"])
    switches += replay(red, blue, four_to_three["moves"], four_to_three["potentials"])
    assert_state(red, blue, four_to_three["final_red"], four_to_three["final_blue"])
    assert potential(red, blue) == four_to_three["final_potential"] == 3

    assert switches == 154 + 69 + 527 + 35 == 785
    print("AC p31 durable trajectory audit")
    print(f"switches: {switches}")
    print("maximum_potential: 75")
    print("final_potential: 3")
    print("segment_endpoints: 6, 5, 4, 3")


if __name__ == "__main__":
    main()
