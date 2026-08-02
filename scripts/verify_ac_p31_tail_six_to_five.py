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


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    frontier = json.loads((root / "data/ac-p31-explicit-switch-frontier.json").read_text())
    record = json.loads((root / "data/ac-p31-tail-six-to-five.json").read_text())

    red = list(record["start_red"])
    blue = list(record["start_blue"])
    assert red == [value for _, value in frontier["final_red"]]
    assert blue == [value for _, value in frontier["final_blue"]]
    assert_state(red, blue)
    assert potential(red, blue) == record["start_potential"] == 6

    observed = [6]
    for word in record["moves"]:
        apply_move(red, blue, word)
        assert_state(red, blue)
        observed.append(potential(red, blue))

    assert observed == record["potentials"]
    assert max(observed) == record["exact_barrier"] == 10
    assert red == record["end_red"]
    assert blue == record["end_blue"]
    assert potential(red, blue) == record["end_potential"] == 5

    assert record["lower_barrier_components"] == [
        {"barrier": 6, "states": 1},
        {"barrier": 7, "states": 9},
        {"barrier": 8, "states": 33},
        {"barrier": 9, "states": 860},
    ]

    print("AC p31 six-to-five tail audit")
    print(f"switches: {len(record['moves'])}")
    print(f"maximum_potential: {max(observed)}")
    print(f"terminal_potential: {observed[-1]}")
    print("barrier_9_component_states: 860")


if __name__ == "__main__":
    main()
