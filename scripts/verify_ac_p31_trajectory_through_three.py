#!/usr/bin/env python3
from __future__ import annotations

from itertools import combinations
from pathlib import Path
import json

N = 30


def collinear(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def potential(red: list[int], blue: list[int]) -> int:
    points = [(row + 1, red[row]) for row in range(N)]
    points += [(row + 1, blue[row]) for row in range(N)]
    return sum(collinear(*triple) for triple in combinations(points, 3))


def assert_state(red: list[int], blue: list[int]) -> None:
    assert sorted(red) == list(range(1, N + 1))
    assert sorted(blue) == list(range(1, N + 1))
    assert all(red[row] != blue[row] for row in range(N))


def apply_move(red: list[int], blue: list[int], word: str) -> None:
    layer, address = word.split(":")
    first, second = (int(value) - 1 for value in address.split(","))
    active = red if layer == "r" else blue
    other = blue if layer == "r" else red
    assert active[second] != other[first]
    assert active[first] != other[second]
    active[first], active[second] = active[second], active[first]


def replay_segment(
    red: list[int], blue: list[int], moves: list[str], expected: list[int]
) -> None:
    assert len(expected) == len(moves) + 1
    assert potential(red, blue) == expected[0]
    for index, word in enumerate(moves):
        apply_move(red, blue, word)
        assert_state(red, blue)
        assert potential(red, blue) == expected[index + 1]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    frontier = json.loads((root / "data/ac-p31-explicit-switch-frontier.json").read_text())
    tails = [
        json.loads((root / "data/ac-p31-tail-six-to-five.json").read_text()),
        json.loads((root / "data/ac-p31-tail-five-to-four.json").read_text()),
        json.loads((root / "data/ac-p31-tail-four-to-three.json").read_text()),
    ]

    red = [value for _, value in frontier["installed_red"]]
    blue = [value for _, value in frontier["installed_blue"]]
    assert_state(red, blue)
    assert potential(red, blue) == frontier["installed_potential"] == 75

    switch_count = 0
    for segment in frontier["segments"]:
        replay_segment(red, blue, segment["moves"], segment["potentials"])
        switch_count += len(segment["moves"])

    assert switch_count == frontier["total_switches"] == 154
    assert red == [value for _, value in frontier["final_red"]]
    assert blue == [value for _, value in frontier["final_blue"]]
    assert potential(red, blue) == 6

    for tail in tails:
        assert red == tail["start_red"]
        assert blue == tail["start_blue"]
        replay_segment(red, blue, tail["moves"], tail["potentials"])
        switch_count += len(tail["moves"])
        assert red == tail["end_red"]
        assert blue == tail["end_blue"]
        assert potential(red, blue) == tail["end_potential"]

    assert switch_count == 253
    assert potential(red, blue) == 3

    print("AC p31 combined trajectory audit")
    print(f"switches: {switch_count}")
    print("initial_potential: 75")
    print("terminal_potential: 3")
    print("recovered_tail_switches: 99")


if __name__ == "__main__":
    main()
