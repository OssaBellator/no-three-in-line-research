#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from itertools import combinations
from pathlib import Path
import gc
import json

import verify_ac_prime_seed_census as base

P = 31
N = P - 1


def enumerate_seed_addresses():
    layers = {channel: base.hyperbola(P, channel) for channel in range(1, P)}
    layer_sets = {channel: set(points) for channel, points in layers.items()}
    records = []
    for anchor_channel in range(1, P):
        anchor = layers[anchor_channel]
        anchor_set = layer_sets[anchor_channel]
        for switch_channel in range(1, P):
            if switch_channel == anchor_channel:
                continue
            switch_by_column = dict(layers[switch_channel])
            for first, second in combinations(range(1, P), 2):
                inserted = (
                    (first, switch_by_column[second]),
                    (second, switch_by_column[first]),
                )
                if inserted[0] in anchor_set or inserted[1] in anchor_set:
                    continue
                for candidate in inserted:
                    pairs = base.secant_pairs(anchor, candidate)
                    if len(pairs) >= 7:
                        records.append(
                            (
                                anchor_channel,
                                switch_channel,
                                first,
                                second,
                                candidate,
                                pairs,
                            )
                        )
    return records


def evaluate(record):
    anchor_channel, switch_channel, first, second, candidate, pairs = record
    expected = {
        "p": P,
        "anchor_channel": anchor_channel,
        "switch_channel": switch_channel,
        "switch_rows": [first, second],
        "candidate": list(candidate),
    }
    result = base.evaluate_bank(expected)
    return {
        "anchor_channel": anchor_channel,
        "switch_channel": switch_channel,
        "ratio": switch_channel * pow(anchor_channel, -1, P) % P,
        "switch_rows": [first, second],
        "candidate": list(candidate),
        "pair_count": len(pairs),
        "bank_size": result["bank_size"],
        "current_potential": result["current_potential"],
        "best_potential": result["best_potential"],
        "improving_states": result["improving_states"],
        "potential_sum": result["potential_sum"],
    }


def transform_point(point, action):
    x, y = point
    if action == 0:
        return x, y
    if action == 1:
        return N + 1 - x, y
    if action == 2:
        return x, N + 1 - y
    if action == 3:
        return N + 1 - x, N + 1 - y
    if action == 4:
        return y, x
    if action == 5:
        return N + 1 - y, N + 1 - x
    if action == 6:
        return y, N + 1 - x
    if action == 7:
        return N + 1 - y, x
    raise ValueError(action)


def geometric_record(record, action=0):
    anchor_channel, switch_channel, first, second, candidate, pairs = record
    anchor = tuple(
        sorted(transform_point(point, action) for point in base.hyperbola(P, anchor_channel))
    )
    switch = tuple(
        sorted(transform_point(point, action) for point in base.hyperbola(P, switch_channel))
    )
    switch_by_column = dict(base.hyperbola(P, switch_channel))
    removed = (
        (first, switch_by_column[first]),
        (second, switch_by_column[second]),
    )
    inserted = (
        (first, switch_by_column[second]),
        (second, switch_by_column[first]),
    )
    transformed_pairs = tuple(
        sorted(
            tuple(
                sorted(
                    (
                        transform_point(pair[0], action),
                        transform_point(pair[1], action),
                    )
                )
            )
            for pair in pairs
        )
    )
    return (
        anchor,
        switch,
        tuple(sorted(transform_point(point, action) for point in removed)),
        tuple(sorted(transform_point(point, action) for point in inserted)),
        transform_point(candidate, action),
        transformed_pairs,
    )


def main():
    expected = json.loads(Path("data/ac-p31-seed-orbit-census.json").read_text())
    seeds = enumerate_seed_addresses()
    assert len(seeds) == expected["raw_seed_addresses"] == 216

    evaluated = []
    for seed in seeds:
        evaluated.append(evaluate(seed))
        gc.collect()

    improving = sum(record["improving_states"] > 0 for record in evaluated)
    neutral = sum(
        record["best_potential"] == record["current_potential"] for record in evaluated
    )
    assert improving == expected["improving_seed_addresses"] == 140
    assert len(evaluated) - improving == expected["nonimproving_seed_addresses"] == 76
    assert neutral == expected["neutral_best_equals_current"] == 10
    assert (
        sum(record["best_potential"] > record["current_potential"] for record in evaluated)
        == expected["strictly_worse"]
        == 66
    )
    deltas = [
        record["best_potential"] - record["current_potential"] for record in evaluated
    ]
    assert [min(deltas), max(deltas)] == expected["best_minus_current_range"]

    bank_sizes = Counter(record["bank_size"] for record in evaluated)
    assert {str(key): value for key, value in sorted(bank_sizes.items())} == expected[
        "bank_size_distribution"
    ]

    ratio_counts = {}
    for ratio in range(2, P):
        selected = [record for record in evaluated if record["ratio"] == ratio]
        if not selected:
            continue
        ratio_counts[str(ratio)] = {
            "improving": sum(record["improving_states"] > 0 for record in selected),
            "nonimproving": sum(record["improving_states"] == 0 for record in selected),
        }
    assert ratio_counts == expected["ratio_counts"]
    assert [
        int(ratio)
        for ratio, counts in ratio_counts.items()
        if counts["nonimproving"] == 0
    ] == expected["uniformly_improving_ratios"]
    assert [
        int(ratio)
        for ratio, counts in ratio_counts.items()
        if counts["improving"] == 0
    ] == expected["uniformly_nonimproving_ratios"] == [23]

    lookup = {geometric_record(seed): index for index, seed in enumerate(seeds)}
    seen = set()
    orbit_records = []
    for index, seed in enumerate(seeds):
        if index in seen:
            continue
        members = sorted(
            {
                lookup[geometric_record(seed, action)]
                for action in range(8)
            }
        )
        assert len(members) == 4
        seen.update(members)
        representative = min(members, key=lambda member: geometric_record(seeds[member]))
        orbit_records.append(
            {
                "seed_indices": members,
                "improving_members": sum(
                    evaluated[member]["improving_states"] > 0 for member in members
                ),
                "equivariant_representative_index": representative,
                "equivariant_improving": (
                    evaluated[representative]["improving_states"] > 0
                ),
            }
        )

    assert len(seen) == len(seeds)
    orbit_summary = expected["orbits"]
    assert len(orbit_records) == orbit_summary["count"] == 54
    assert Counter(len(record["seed_indices"]) for record in orbit_records) == Counter({4: 54})
    assert sum(record["improving_members"] == 4 for record in orbit_records) == orbit_summary[
        "all_improving"
    ] == 30
    assert sum(record["improving_members"] == 0 for record in orbit_records) == orbit_summary[
        "all_nonimproving"
    ] == 14
    assert sum(record["improving_members"] == 2 for record in orbit_records) == orbit_summary[
        "mixed"
    ] == 10
    assert sum(record["equivariant_improving"] for record in orbit_records) == orbit_summary[
        "equivariant_improving"
    ] == 37
    assert (
        len(orbit_records)
        - sum(record["equivariant_improving"] for record in orbit_records)
        == orbit_summary["equivariant_nonimproving"]
        == 17
    )

    print("AC p=31 seed-orbit census")
    print("raw_seed_addresses: 216")
    print("improving_nonimproving: 140, 76")
    print("neutral_strictly_worse: 10, 66")
    print("best_minus_current_range: -33, 31")
    print("square_symmetry_orbits: 54")
    print("orbit_types_all_improving_all_nonimproving_mixed: 30, 14, 10")
    print("equivariant_selector_improving_nonimproving: 37, 17")
    print("uniformly_nonimproving_ratio: 23")
    print("ratio_2_improving_nonimproving: 2, 6")


if __name__ == "__main__":
    main()
