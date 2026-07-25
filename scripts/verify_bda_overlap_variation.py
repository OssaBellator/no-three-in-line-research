#!/usr/bin/env python3
"""Verify BDA5ae--BDA5ah on exhaustive small weighted scalar paths."""

from fractions import Fraction
from itertools import product


def statistics(anchor_weights, step):
    total = sum(sum(weights) for weights in anchor_weights)
    overlap = 0
    variation = 0
    endpoint_multiset = 0
    endpoint_distinct = 0
    pair_parity = [0, 0]
    down_parity = [0, 0]
    up_parity = [0, 0]
    down = 0
    up = 0

    for weights in anchor_weights:
        length = len(weights)
        endpoint_indices = set()
        for residue in range(min(step, length)):
            path = list(range(residue, length, step))
            endpoint_multiset += weights[path[0]] + weights[path[-1]]
            endpoint_indices.add(path[0])
            endpoint_indices.add(path[-1])
            for local_index, left in enumerate(path[:-1]):
                right = path[local_index + 1]
                common = min(weights[left], weights[right])
                difference = weights[right] - weights[left]
                overlap += common
                variation += abs(difference)
                pair_parity[local_index % 2] += common
                if difference > 0:
                    up += difference
                    up_parity[local_index % 2] += difference
                elif difference < 0:
                    down += -difference
                    down_parity[local_index % 2] += -difference
        endpoint_distinct += sum(weights[index] for index in endpoint_indices)

    return {
        "total": total,
        "overlap": overlap,
        "variation": variation,
        "endpoint_multiset": endpoint_multiset,
        "endpoint_distinct": endpoint_distinct,
        "pair_parity": pair_parity,
        "down": down,
        "up": up,
        "down_parity": down_parity,
        "up_parity": up_parity,
    }


def verify_system(anchor_weights, step):
    data = statistics(anchor_weights, step)
    total = data["total"]
    overlap = data["overlap"]
    variation = data["variation"]
    boundary = data["endpoint_multiset"]

    assert 2 * (total - overlap) == boundary + variation
    assert 2 * data["endpoint_distinct"] >= boundary
    assert sum(data["pair_parity"]) == overlap
    assert max(data["pair_parity"]) * 2 >= overlap
    assert data["down"] + data["up"] == variation
    assert sum(data["down_parity"]) == data["down"]
    assert sum(data["up_parity"]) == data["up"]

    for theta in (
        Fraction(0, 1),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(3, 4),
        Fraction(1, 1),
    ):
        if overlap >= theta * total:
            assert max(data["pair_parity"]) >= theta * total / 2
        else:
            endpoint_front = data["endpoint_distinct"] > (1 - theta) * total / 2
            variation_front = variation > (1 - theta) * total
            assert endpoint_front or variation_front
            if variation_front:
                orientation = max(data["down"], data["up"])
                parity = (
                    data["down_parity"]
                    if data["down"] >= data["up"]
                    else data["up_parity"]
                )
                assert orientation * 2 >= variation
                assert max(parity) * 2 >= orientation
                assert max(parity) > (1 - theta) * total / 4

    if total:
        theta = Fraction(1, 2)
        pair = max(data["pair_parity"])
        endpoint = data["endpoint_distinct"]
        best_oriented = max(
            max(data["down_parity"]),
            max(data["up_parity"]),
        )
        assert pair >= total / 4 or endpoint > total / 4 or best_oriented > total / 8


def verify_single_anchor(maximum_length=7, maximum_weight=3):
    systems = 0
    for length in range(1, maximum_length + 1):
        for step in range(1, length + 1):
            for weights in product(range(maximum_weight + 1), repeat=length):
                verify_system([weights], step)
                systems += 1
    return systems


def verify_two_anchors(maximum_length=4, maximum_weight=2):
    systems = 0
    for length in range(1, maximum_length + 1):
        vectors = list(product(range(maximum_weight + 1), repeat=length))
        for step in range(1, length + 1):
            for first in vectors:
                for second in vectors:
                    verify_system([first, second], step)
                    systems += 1
    return systems


def main():
    single = verify_single_anchor()
    multiple = verify_two_anchors()
    print(
        "BDA overlap variation: verified "
        f"{single} one-anchor systems and {multiple} two-anchor systems"
    )


if __name__ == "__main__":
    main()
