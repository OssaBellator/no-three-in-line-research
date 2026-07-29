#!/usr/bin/env python3
from __future__ import annotations
from itertools import combinations, permutations
from pathlib import Path
import json

P = 19
ANCHOR_CHANNEL = 7
SWITCH_CHANNEL = 1


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
        for triple in combinations(sorted(set(points)), 3)
    )


def main():
    record = json.loads(
        Path("data/ac-explicit-p19-an-seed.json").read_text()
    )
    assert record["p"] == P and record["n"] == P - 1

    anchor_layer = hyperbola(ANCHOR_CHANNEL)
    switch_layer = hyperbola(SWITCH_CHANNEL)
    assert len(anchor_layer) == P - 1
    assert len(switch_layer) == P - 1
    assert anchor_layer.isdisjoint(switch_layer)

    removed = {tuple(point) for point in record["switch"]["removed"]}
    inserted = {tuple(point) for point in record["switch"]["inserted"]}
    candidate = tuple(record["switch"]["candidate"])
    assert removed == {(6, 16), (16, 6)}
    assert inserted == {(6, 6), (16, 16)}
    assert removed <= switch_layer
    switched_layer = (switch_layer - removed) | inserted
    assert len({x for x, _ in switched_layer}) == P - 1
    assert len({y for _, y in switched_layer}) == P - 1
    assert switched_layer.isdisjoint(anchor_layer)

    pairs = [
        (tuple(pair[0]), tuple(pair[1]))
        for pair in record["secant_pairs"]
    ]
    assert len(pairs) == 7
    assert len({point for pair in pairs for point in pair}) == 14
    assert all(
        first in anchor_layer
        and second in anchor_layer
        and collinear(candidate, first, second)
        for first, second in pairs
    )

    selected = [first for first, _ in pairs]
    columns = [point[0] for point in selected]
    rows = [point[1] for point in selected]
    assert columns == record["source_columns"]
    assert rows == record["target_rows"]
    assert len(set(columns)) == len(set(rows)) == 7

    forbidden = {(i, i) for i in range(7)}
    switched_by_column = dict(switched_layer)
    for i, column in enumerate(columns):
        other_row = switched_by_column[column]
        if other_row in rows:
            forbidden.add((i, rows.index(other_row)))
    assert sorted(map(list, forbidden)) == record["forbidden_positions"]
    assert all(
        sum(1 for i, _ in forbidden if i == row) <= 2
        for row in range(7)
    )
    assert all(
        sum(1 for _, j in forbidden if j == column) <= 2
        for column in range(7)
    )

    bank = [
        permutation
        for permutation in permutations(range(7))
        if all((i, permutation[i]) not in forbidden for i in range(7))
    ]
    assert len(bank) == record["allowed_matching_count"] == 1300
    assert len(bank) * 128 >= 5040

    current = anchor_layer | switch_layer
    selected_set = set(selected)
    base_x = current - (selected_set | removed)
    post_switch_z = base_x | inserted
    anchor_cells = {
        (i, j): (columns[i], rows[j])
        for i in range(7)
        for j in range(7)
        if (i, j) not in forbidden
    }
    assert not (set(anchor_cells.values()) & post_switch_z)

    certificate_counts = {1: 0, 2: 0, 3: 0}
    items = [
        ("anchor", address, point)
        for address, point in anchor_cells.items()
    ] + [
        ("fixed", None, point) for point in post_switch_z
    ]
    for triple in combinations(items, 3):
        points = [entry[2] for entry in triple]
        if len(set(points)) < 3 or not collinear(*points):
            continue
        addresses = [
            entry[1] for entry in triple if entry[0] == "anchor"
        ]
        rank = len(addresses)
        if rank == 0:
            continue
        if len({i for i, _ in addresses}) != rank:
            continue
        if len({j for _, j in addresses}) != rank:
            continue
        certificate_counts[rank] += 1
    assert certificate_counts == {1: 149, 2: 138, 3: 33}
    assert record["certificate_counts"] == {
        "rank_1": 149, "rank_2": 138, "rank_3": 33
    }

    current_potential = potential(current)
    base_potential = potential(base_x)
    post_switch_potential = potential(post_switch_z)
    assert (
        current_potential,
        base_potential,
        post_switch_potential,
    ) == (66, 15, 29)
    assert record["potentials"] == {
        "current": 66, "base_X": 15, "post_switch_Z": 29
    }

    evaluated = []
    for permutation in bank:
        matching = {
            (columns[i], rows[permutation[i]]) for i in range(7)
        }
        assert len(matching) == 7
        assert matching.isdisjoint(post_switch_z)
        successor = post_switch_z | matching
        evaluated.append((potential(successor), permutation, matching))
    evaluated.sort(key=lambda value: (value[0], value[1]))
    best_potential, best_permutation, best_matching = evaluated[0]
    assert best_permutation == tuple(record["best_permutation"])
    assert sorted(map(list, best_matching)) == sorted(
        record["best_replacement_cells"]
    )
    assert best_potential == record["best_potential"] == 41
    improving_count = sum(
        value < current_potential for value, _, _ in evaluated
    )
    assert improving_count == record["improving_matching_count"] == 1025
    assert current_potential - best_potential == 25

    average_collateral = sum(
        value - post_switch_potential for value, _, _ in evaluated
    ) / len(evaluated)

    print("AC explicit p=19 AN seed audit")
    print(f"anchor_layer_points: {len(anchor_layer)}")
    print(f"switch_layer_points: {len(switch_layer)}")
    print(f"secant_pairs: {len(pairs)}")
    print(f"forbidden_positions: {len(forbidden)}")
    print(f"allowed_matching_states: {len(bank)}")
    print(f"rank_1_certificates: {certificate_counts[1]}")
    print(f"rank_2_certificates: {certificate_counts[2]}")
    print(f"rank_3_certificates: {certificate_counts[3]}")
    print(f"current_potential: {current_potential}")
    print(f"post_switch_potential: {post_switch_potential}")
    print(f"best_potential: {best_potential}")
    print(f"potential_decrease: {current_potential - best_potential}")
    print(f"improving_matching_states: {improving_count}")
    print(f"average_anchor_collateral: {average_collateral:.12f}")


if __name__ == "__main__":
    main()
