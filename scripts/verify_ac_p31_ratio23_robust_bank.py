#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations, product
from pathlib import Path
import json

import verify_ac_prime_seed_census as base

P = 31
N = P - 1
ANCHOR_CHANNEL = 1
SWITCH_CHANNEL = 23
SWITCH_ROWS = (15, 16)
CANDIDATE = (15, 15)

ALL_PERMUTATIONS = list(permutations(range(7)))
PERM_TERMS = {}
for permutation in ALL_PERMUTATIONS:
    position_ids = tuple(index * 7 + permutation[index] for index in range(7))
    PERM_TERMS[permutation] = (
        position_ids,
        tuple((position_ids[i], position_ids[j]) for i, j in combinations(range(7), 2)),
        tuple(
            tuple(sorted((position_ids[i], position_ids[j], position_ids[k])))
            for i, j, k in combinations(range(7), 3)
        ),
    )


def physical_seed():
    anchor = set(base.hyperbola(P, ANCHOR_CHANNEL))
    switch = set(base.hyperbola(P, SWITCH_CHANNEL))
    switch_by_column = dict(switch)
    first, second = SWITCH_ROWS
    removed = {
        (first, switch_by_column[first]),
        (second, switch_by_column[second]),
    }
    inserted = {
        (first, switch_by_column[second]),
        (second, switch_by_column[first]),
    }
    pairs = base.secant_pairs(tuple(sorted(anchor)), CANDIDATE)
    return anchor, switch, removed, inserted, pairs


def orientation_tables(anchor, switch, removed, inserted, selected):
    columns = [point[0] for point in selected]
    rows = [point[1] for point in selected]
    switched = (switch - removed) | inserted
    switched_by_column = dict(switched)

    forbidden = {(index, index) for index in range(7)}
    for index, column in enumerate(columns):
        other_row = switched_by_column[column]
        if other_row in rows:
            forbidden.add((index, rows.index(other_row)))

    points = [None] * 49
    for i in range(7):
        for j in range(7):
            if (i, j) not in forbidden:
                points[i * 7 + j] = (columns[i], rows[j])

    current = anchor | switch
    fixed = (current - set(selected) - removed) | inserted
    assert len(current) == 60
    assert len(fixed) == 53
    assert switched <= fixed | set(selected)

    fixed_list = list(fixed)
    base_potential = base.direct_potential(fixed)
    unary = [0] * 49
    for position_id, point in enumerate(points):
        if point is not None:
            unary[position_id] = sum(
                base.collinear(point, first, second)
                for first, second in combinations(fixed_list, 2)
            )

    pair_cost = [[0] * 49 for _ in range(49)]
    valid_positions = [index for index, point in enumerate(points) if point is not None]
    for first_id, second_id in combinations(valid_positions, 2):
        first_row, first_column = divmod(first_id, 7)
        second_row, second_column = divmod(second_id, 7)
        if first_row == second_row or first_column == second_column:
            continue
        cost = sum(
            base.collinear(points[first_id], points[second_id], fixed_point)
            for fixed_point in fixed_list
        )
        pair_cost[first_id][second_id] = cost
        pair_cost[second_id][first_id] = cost

    triple_cost = set()
    for position_ids in combinations(valid_positions, 3):
        row_ids = {position_id // 7 for position_id in position_ids}
        column_ids = {position_id % 7 for position_id in position_ids}
        if len(row_ids) < 3 or len(column_ids) < 3:
            continue
        if base.collinear(*(points[position_id] for position_id in position_ids)):
            triple_cost.add(position_ids)

    return (
        columns,
        rows,
        forbidden,
        points,
        fixed,
        base_potential,
        unary,
        pair_cost,
        triple_cost,
    )


def bank_value(permutation, base_potential, unary, pair_cost, triple_cost):
    position_ids, pair_ids, triple_ids = PERM_TERMS[permutation]
    value = base_potential
    value += sum(unary[position_id] for position_id in position_ids)
    value += sum(pair_cost[first_id][second_id] for first_id, second_id in pair_ids)
    value += sum(triple_id in triple_cost for triple_id in triple_ids)
    return value


def ac1_audit(anchor, switch, removed, inserted, selected, expected):
    (
        columns,
        rows,
        forbidden,
        points,
        fixed,
        _,
        _,
        _,
        _,
    ) = orientation_tables(anchor, switch, removed, inserted, selected)
    current = anchor | switch
    base_state = current - set(selected) - removed

    items = [
        ("anchor", divmod(position_id, 7), point)
        for position_id, point in enumerate(points)
        if point is not None
    ] + [("fixed", None, point) for point in fixed]

    counts = Counter({1: 0, 2: 0, 3: 0})
    degrees = {1: Counter(), 2: Counter(), 3: Counter()}
    for triple in combinations(items, 3):
        triple_points = [entry[2] for entry in triple]
        if len(set(triple_points)) < 3 or not base.collinear(*triple_points):
            continue
        addresses = [entry[1] for entry in triple if entry[0] == "anchor"]
        rank = len(addresses)
        if rank == 0:
            continue
        if len({i for i, _ in addresses}) != rank:
            continue
        if len({j for _, j in addresses}) != rank:
            continue
        counts[rank] += 1
        for address in addresses:
            degrees[rank][address] += 1

    base_potential = base.direct_potential(base_state)
    fixed_potential = base.direct_potential(fixed)
    d_star = base.direct_potential(current) - base_potential
    f_star = fixed_potential - base_potential
    gap = d_star - f_star
    assert (base_potential, fixed_potential, d_star, f_star, gap) == (
        expected["base_potential"],
        expected["fixed_potential"],
        expected["D_star"],
        expected["F_star"],
        expected["gap"],
    )
    assert counts == Counter(
        {
            1: expected["certificate_counts"]["rank_1"],
            2: expected["certificate_counts"]["rank_2"],
            3: expected["certificate_counts"]["rank_3"],
        }
    )

    normalized = {1: counts[1] / 7, 2: counts[2] / 42, 3: counts[3] / 210}
    heavy_rank = max(normalized, key=normalized.get)
    assert heavy_rank == expected["heavy_rank"] == 1
    heavy_address, heavy_degree = degrees[heavy_rank].most_common(1)[0]
    heavy_point = points[heavy_address[0] * 7 + heavy_address[1]]
    assert list(heavy_address) == expected["heavy_anchor_address"]
    assert list(heavy_point) == expected["heavy_anchor_cell"]
    assert heavy_degree == expected["heavy_anchor_degree"]
    assert normalized[heavy_rank] >= gap / 384


def heavy_line_filter_audit(anchor, switch, removed, inserted, selected, expected):
    (
        columns,
        rows,
        forbidden,
        points,
        fixed,
        fixed_potential,
        unary,
        pair_cost,
        triple_cost,
    ) = orientation_tables(anchor, switch, removed, inserted, selected)

    heavy_address = tuple(expected["heavy_anchor_address"])
    heavy_point = points[heavy_address[0] * 7 + heavy_address[1]]
    direction_classes = {}
    for fixed_point in fixed:
        direction = base.primitive(
            fixed_point[0] - heavy_point[0], fixed_point[1] - heavy_point[1]
        )
        direction_classes.setdefault(direction, []).append(fixed_point)

    actual_classes = []
    for direction, fixed_points in sorted(direction_classes.items()):
        if len(fixed_points) < 2:
            continue
        actual_classes.append(
            {
                "direction": list(direction),
                "fixed_points": sorted(map(list, fixed_points)),
                "certificate_pairs": len(fixed_points) * (len(fixed_points) - 1) // 2,
            }
        )
    expected_classes = sorted(
        expected["heavy_line_classes"], key=lambda record: tuple(record["direction"])
    )
    assert actual_classes == expected_classes
    assert sum(record["certificate_pairs"] for record in actual_classes) == expected[
        "heavy_anchor_degree"
    ]

    allowed = [
        permutation
        for permutation in ALL_PERMUTATIONS
        if all((index, permutation[index]) not in forbidden for index in range(7))
    ]
    actual_filters = []
    for threshold in (3, 4, 5):
        bad_positions = set()
        for position_id, point in enumerate(points):
            if point is None:
                continue
            line_loads = Counter(
                base.primitive(fixed_point[0] - point[0], fixed_point[1] - point[1])
                for fixed_point in fixed
            )
            if any(load >= threshold for load in line_loads.values()):
                bad_positions.add(divmod(position_id, 7))

        values = []
        for permutation in allowed:
            if any(
                (index, permutation[index]) in bad_positions for index in range(7)
            ):
                continue
            values.append(
                bank_value(
                    permutation, fixed_potential, unary, pair_cost, triple_cost
                )
            )
        actual_filters.append(
            {
                "minimum_fixed_points": threshold,
                "bad_positions": len(bad_positions),
                "remaining_states": len(values),
                "minimum_potential": min(values),
                "potential_sum": sum(values),
            }
        )
    assert actual_filters == expected["fixed_line_filters"]


def main():
    record = json.loads(Path("data/ac-p31-ratio23-robust-bank.json").read_text())
    anchor, switch, removed, inserted, pairs = physical_seed()

    assert record["p"] == P and record["n"] == N
    assert record["anchor_channel"] == ANCHOR_CHANNEL
    assert record["switch_channel"] == SWITCH_CHANNEL
    assert record["channel_ratio"] == SWITCH_CHANNEL
    assert sorted(map(list, removed)) == sorted(record["removed_cells"])
    assert sorted(map(list, inserted)) == sorted(record["inserted_cells"])
    assert len(pairs) == 8
    assert [[list(first), list(second)] for first, second in pairs] == record[
        "full_secant_pairs"
    ]

    current_potential = base.direct_potential(anchor | switch)
    assert current_potential == record["current_potential"] == 82

    allowed_cache = {}
    total_states = 0
    total_potential_sum = 0
    improving_states = 0
    global_best = None
    group_records = []

    for omitted_pair_index in range(8):
        selected_pairs = [
            pair for index, pair in enumerate(pairs) if index != omitted_pair_index
        ]
        group_states = 0
        group_sum = 0
        group_minimum = None
        group_minimum_states = 0

        for orientation_bits in product((0, 1), repeat=7):
            selected = [pair[bit] for pair, bit in zip(selected_pairs, orientation_bits)]
            if len({x for x, _ in selected}) < 7:
                continue
            if len({y for _, y in selected}) < 7:
                continue

            (
                columns,
                rows,
                forbidden,
                points,
                fixed,
                fixed_potential,
                unary,
                pair_cost,
                triple_cost,
            ) = orientation_tables(anchor, switch, removed, inserted, selected)

            forbidden_key = frozenset(forbidden)
            allowed = allowed_cache.setdefault(
                forbidden_key,
                [
                    permutation
                    for permutation in ALL_PERMUTATIONS
                    if all(
                        (index, permutation[index]) not in forbidden
                        for index in range(7)
                    )
                ],
            )

            for permutation in allowed:
                value = bank_value(
                    permutation, fixed_potential, unary, pair_cost, triple_cost
                )
                group_states += 1
                total_states += 1
                group_sum += value
                total_potential_sum += value
                improving_states += value < current_potential

                if group_minimum is None or value < group_minimum:
                    group_minimum = value
                    group_minimum_states = 1
                elif value == group_minimum:
                    group_minimum_states += 1

                candidate = (value, omitted_pair_index, orientation_bits, permutation)
                if global_best is None or candidate < global_best:
                    global_best = candidate

        group_records.append(
            {
                "omitted_pair_index": omitted_pair_index,
                "states": group_states,
                "minimum_potential": group_minimum,
                "minimum_states": group_minimum_states,
                "potential_sum": group_sum,
            }
        )

    assert group_records == record["omitted_pair_groups"]
    assert total_states == record["total_states"] == 1376614
    assert total_potential_sum == record["total_potential_sum"] == 175975875
    assert improving_states == record["improving_states"] == 0
    assert global_best[0] == record["global_minimum_potential"] == 87
    assert global_best[0] - current_potential == record["global_gap"] == 5

    value, omitted_pair_index, orientation_bits, permutation = global_best
    selected_pairs = [
        pair for index, pair in enumerate(pairs) if index != omitted_pair_index
    ]
    selected = [pair[bit] for pair, bit in zip(selected_pairs, orientation_bits)]
    columns = [point[0] for point in selected]
    rows = [point[1] for point in selected]
    replacement = {(columns[index], rows[permutation[index]]) for index in range(7)}
    fixed = ((anchor | switch) - set(selected) - removed) | inserted
    assert len(fixed | replacement) == 60
    assert base.direct_potential(fixed | replacement) == value == 87

    best_record = record["best_record"]
    assert omitted_pair_index == best_record["omitted_pair_index"]
    assert list(orientation_bits) == best_record["orientation_bits"]
    assert list(permutation) == best_record["permutation"]
    assert [list(point) for point in selected] == best_record["selected_endpoints"]
    assert sorted(map(list, replacement)) == sorted(best_record["replacement_cells"])

    ac1_audit(anchor, switch, removed, inserted, selected, record["best_record_ac1"])
    heavy_line_filter_audit(
        anchor, switch, removed, inserted, selected, record["best_record_ac1"]
    )

    rotate = lambda point: (P - point[0], P - point[1])
    candidate_two = tuple(record["conjugate_candidate"])
    assert rotate(CANDIDATE) == candidate_two
    assert {rotate(point) for point in anchor} == anchor
    assert {rotate(point) for point in switch} == switch
    assert {rotate(point) for point in removed} == removed
    assert {rotate(point) for point in inserted} == inserted
    pairs_two = base.secant_pairs(tuple(sorted(anchor)), candidate_two)
    assert {
        tuple(sorted((rotate(first), rotate(second)))) for first, second in pairs
    } == set(pairs_two)

    print("AC p=31 ratio-23 robust-bank audit")
    print("full_secant_pairs: 8")
    print("selection_orientation_classes: 8 x 128")
    print("occurrence_addressed_states: 1376614")
    print("group_minima: 90, 89, 89, 87, 87, 91, 91, 89")
    print("current_global_minimum: 82, 87")
    print("improving_states: 0")
    print("best_record_ac1_counts: 208, 122, 13")
    print("best_record_heavy_anchor: (5, 19), degree 14")
    print("heavy_line_certificate_split: 6, 6, 1, 1")
    print("high_line_filter_remaining_states: 42, 167, 1044")
    print("high_line_filter_minima: 87, 87, 87")
    print("candidate_180_degree_conjugacy: verified")


if __name__ == "__main__":
    main()
