#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations
from pathlib import Path
import json

P = 19


def hyperbola(channel):
    return {
        (x, channel * pow(x, -1, P) % P)
        for x in range(1, P)
    }


def collinear(a, b, c):
    return (
        (b[0] - a[0]) * (c[1] - a[1])
        == (b[1] - a[1]) * (c[0] - a[0])
    )


def potential(points):
    return sum(
        collinear(*triple)
        for triple in combinations(sorted(points), 3)
    )


def parse_move(text):
    layer, rows = text.split(":")
    first, second = map(int, rows.split(","))
    return layer, first, second


def apply_move(red, blue, text):
    layer_name, first, second = parse_move(text)
    layer = red if layer_name == "r" else blue
    other = blue if layer_name == "r" else red
    by_row = dict(layer)
    removed = {(first, by_row[first]), (second, by_row[second])}
    inserted = {(first, by_row[second]), (second, by_row[first])}
    assert inserted.isdisjoint(other)
    if layer_name == "r":
        red = (red - removed) | inserted
    else:
        blue = (blue - removed) | inserted
    assert len(red) == len(blue) == 18
    assert len(dict(red)) == len(dict(blue)) == 18
    assert red.isdisjoint(blue)
    return red, blue


def main():
    data = json.loads(
        Path("data/ac-p19-switch-trajectory.json").read_text()
    )
    red = (
        hyperbola(7)
        - {(1, 7), (3, 15), (4, 16), (8, 8), (9, 5), (10, 14), (14, 10)}
    ) | {(1, 8), (3, 10), (4, 15), (8, 14), (9, 16), (10, 5), (14, 7)}
    blue = (
        hyperbola(1) - {(6, 16), (16, 6)}
    ) | {(6, 6), (16, 16)}

    strict_potentials = [potential(red | blue)]
    for move in data["monotone_moves"]:
        red, blue = apply_move(red, blue, move)
        strict_potentials.append(potential(red | blue))
    assert strict_potentials == data["monotone_potentials"]

    local = data["local_minimum"]
    assert sorted(map(list, red)) == local["red"]
    assert sorted(map(list, blue)) == local["blue"]
    legal = 0
    improving = 0
    for layer_name, layer, other in (("r", red, blue), ("b", blue, red)):
        by_row = dict(layer)
        for first, second in combinations(range(1, 19), 2):
            removed = {(first, by_row[first]), (second, by_row[second])}
            inserted = {(first, by_row[second]), (second, by_row[first])}
            if not inserted.isdisjoint(other):
                continue
            legal += 1
            successor_layer = (layer - removed) | inserted
            value = potential(successor_layer | other)
            improving += value < 10
    assert legal == local["legal_two_row_switches"] == 270
    assert improving == local["improving_two_row_switches"] == 0

    barrier_potentials = [potential(red | blue)]
    seen = {(tuple(sorted(red)), tuple(sorted(blue)))}
    for move in data["barrier_moves"]:
        red, blue = apply_move(red, blue, move)
        key = tuple(sorted(red)), tuple(sorted(blue))
        assert key not in seen
        seen.add(key)
        barrier_potentials.append(potential(red | blue))
    assert barrier_potentials == data["barrier_potentials"]
    assert max(barrier_potentials) == data["barrier_maximum"] == 40
    assert barrier_potentials[-1] == 5

    final = data["final"]
    assert sorted(map(list, red)) == final["red"]
    assert sorted(map(list, blue)) == final["blue"]
    triples = [
        list(map(list, triple))
        for triple in combinations(sorted(red | blue), 3)
        if collinear(*triple)
    ]
    assert triples == final["triples"]
    assert len(triples) == final["potential"] == 5

    print("AC explicit p=19 switch trajectory audit")
    print(f"strict_descent_moves: {len(data['monotone_moves'])}")
    print(f"strict_potential_sequence: {strict_potentials}")
    print(f"local_legal_switches: {legal}")
    print(f"local_improving_switches: {improving}")
    print(f"loop_erased_barrier_moves: {len(data['barrier_moves'])}")
    print(f"barrier_maximum: {max(barrier_potentials)}")
    print(f"final_potential: {barrier_potentials[-1]}")
    print(f"final_triples: {len(triples)}")


if __name__ == "__main__":
    main()
