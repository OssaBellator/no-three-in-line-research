#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import json

import verify_ac_p31_ratio23_robust_bank as robust


def channel(point, anchor, switch):
    if point in anchor:
        return 1
    if point in switch:
        return 23
    raise AssertionError(point)


def product_carry(point, channel_value):
    numerator = point[0] * point[1] - channel_value
    assert numerator % 31 == 0
    return numerator // 31


def signature(edge, anchor, switch):
    first, second = edge
    first_channel = channel(first, anchor, switch)
    second_channel = channel(second, anchor, switch)
    first_carry = product_carry(first, first_channel)
    second_carry = product_carry(second, second_channel)
    if first_channel == second_channel:
        return (first_channel, tuple(sorted((first_carry, second_carry))))
    if first_channel == 1:
        return ((1, 23), (first_carry, second_carry))
    return ((1, 23), (second_carry, first_carry))


def main():
    expected = json.loads(Path("data/ac-p31-ratio23-heavy-anchor.json").read_text())
    robust_record = json.loads(Path("data/ac-p31-ratio23-robust-bank.json").read_text())
    anchor, switch, removed, inserted, pairs = robust.physical_seed()

    best = robust_record["best_record"]
    omitted = best["omitted_pair_index"]
    selected_pairs = [pair for index, pair in enumerate(pairs) if index != omitted]
    selected = [
        pair[bit]
        for pair, bit in zip(selected_pairs, best["orientation_bits"])
    ]
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
    ) = robust.orientation_tables(anchor, switch, removed, inserted, selected)

    heavy_address = tuple(robust_record["best_record_ac1"]["heavy_anchor_address"])
    heavy_anchor = points[heavy_address[0] * 7 + heavy_address[1]]
    assert list(heavy_anchor) == expected["heavy_anchor"] == [5, 19]

    occurrences = [
        tuple(sorted((first, second)))
        for first, second in combinations(sorted(fixed), 2)
        if robust.base.collinear(heavy_anchor, first, second)
    ]
    occurrences.sort()
    assert len(occurrences) == expected["occurrences"] == 14

    records = []
    direction_counts = Counter()
    channel_pair_counts = Counter()
    signature_counts = Counter()
    direction_classes = defaultdict(list)
    for edge in occurrences:
        first, second = edge
        first_channel = channel(first, anchor, switch)
        second_channel = channel(second, anchor, switch)
        first_carry = product_carry(first, first_channel)
        second_carry = product_carry(second, second_channel)
        direction = robust.base.primitive(
            second[0] - first[0], second[1] - first[1]
        )
        sig = signature(edge, anchor, switch)
        direction_counts[direction] += 1
        channel_pair_counts[tuple(sorted((first_channel, second_channel)))] += 1
        signature_counts[sig] += 1
        direction_classes[direction].extend(edge)
        records.append(
            {
                "points": [list(first), list(second)],
                "channels": [first_channel, second_channel],
                "product_carries": [first_carry, second_carry],
                "primitive_direction": list(direction),
            }
        )

    assert records == expected["occurrence_records"]
    assert {
        ",".join(map(str, key)): value
        for key, value in sorted(direction_counts.items())
    } == expected["direction_counts"]
    assert {
        ",".join(map(str, key)): value
        for key, value in sorted(channel_pair_counts.items())
    } == expected["channel_pair_counts"]
    assert len(signature_counts) == expected["product_signature_count"] == 11
    assert max(signature_counts.values()) == expected["maximum_signature_multiplicity"] == 4
    assert {
        str(key): value
        for key, value in sorted(signature_counts.items(), key=lambda item: str(item[0]))
    } == expected["signature_multiplicities"]

    components = sorted(
        {
            frozenset(points)
            for points in direction_classes.values()
            if len(set(points)) >= 2
        },
        key=lambda component: min(component),
    )
    component_sizes = sorted((len(component) for component in components), reverse=True)
    assert component_sizes == expected["endpoint_graph_components"] == [4, 4, 2, 2]

    maximum_matchings = []
    best_size = -1
    for mask in range(1 << len(occurrences)):
        chosen = []
        used = set()
        legal = True
        for index, edge in enumerate(occurrences):
            if not (mask >> index) & 1:
                continue
            if edge[0] in used or edge[1] in used:
                legal = False
                break
            used.update(edge)
            chosen.append(edge)
        if not legal:
            continue
        if len(chosen) > best_size:
            best_size = len(chosen)
            maximum_matchings = [chosen]
        elif len(chosen) == best_size:
            maximum_matchings.append(chosen)

    assert best_size == expected["maximum_endpoint_disjoint_size"] == 6
    least_matching = min(maximum_matchings)
    assert [[list(first), list(second)] for first, second in least_matching] == expected[
        "lexicographically_least_maximum_matching"
    ]

    distinct_best = max(
        (
            len({signature(edge, anchor, switch) for edge in matching}),
            tuple(matching),
        )
        for matching in maximum_matchings
    )
    assert distinct_best[0] == expected["maximum_distinct_signature_matching"]["signature_count"] == 6
    assert [[list(first), list(second)] for first, second in distinct_best[1]] == expected[
        "maximum_distinct_signature_matching"
    ]["edges"]

    denominators = sorted({abs(direction[0]) for direction in direction_counts})
    assert denominators == expected["primitive_direction_denominators"] == [1]
    assert expected["owner_route"] == "PROSPECTIVE"
    assert expected["automatic_current_payment"] == 0
    assert heavy_anchor not in anchor | switch

    print("AC p=31 heavy-anchor classification")
    print("occurrences: 14")
    print("direction_counts: 6, 6, 1, 1")
    print("channel_pair_counts: 3, 8, 3")
    print("product_carry_signatures: 11")
    print("maximum_signature_multiplicity: 4")
    print("endpoint_graph_components: 4, 4, 2, 2")
    print("maximum_endpoint_disjoint_size: 6")
    print("maximum_distinct_signatures_in_matching: 6")
    print("primitive_direction_denominators: 1")
    print("owner_route: PROSPECTIVE")


if __name__ == "__main__":
    main()
