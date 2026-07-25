#!/usr/bin/env python3
"""Exhaust BDA5z on small capped interlaced slot systems."""

from itertools import product
from math import ceil


def overlap(weights, jump):
    return sum(
        min(weights[index], weights[index + jump])
        for index in range(len(weights) - jump)
    )


def parity_weights(weights, jump):
    totals = [0, 0]
    used = [set(), set()]
    for residue in range(jump):
        path = list(range(residue, len(weights), jump))
        for edge_index in range(len(path) - 1):
            left = path[edge_index]
            right = path[edge_index + 1]
            parity = edge_index % 2
            value = min(weights[left], weights[right])
            totals[parity] += value
            if value:
                assert left not in used[parity]
                assert right not in used[parity]
                used[parity].add(left)
                used[parity].add(right)
    return totals


def verify(maximum_slots=8, cap=2, maximum_jump=4):
    vector_checks = 0
    anchor_checks = 0

    checked_vectors = {}
    for slot_count in range(1, maximum_slots + 1):
        for jump in range(1, min(maximum_jump, slot_count) + 1):
            vectors = []
            for weights in product(range(cap + 1), repeat=slot_count):
                total = sum(weights)
                pair_overlap = overlap(weights, jump)
                lower = max(0, 2 * total - cap * (slot_count + jump))
                assert pair_overlap >= lower

                parity = parity_weights(weights, jump)
                assert sum(parity) == pair_overlap
                assert max(parity) >= ceil(pair_overlap / 2)
                vectors.append((total, pair_overlap))
                vector_checks += 1
            checked_vectors[(slot_count, jump)] = vectors

    # Additive two-anchor check on a bounded prefix of each exhaustive table.
    for (slot_count, jump), vectors in checked_vectors.items():
        sample = vectors[: min(40, len(vectors))]
        for first in sample:
            for second in sample:
                total = first[0] + second[0]
                pair_overlap = first[1] + second[1]
                lower = max(
                    0,
                    2 * total - cap * 2 * (slot_count + jump),
                )
                assert pair_overlap >= lower
                anchor_checks += 1

    return vector_checks, anchor_checks


def main():
    vectors, anchors = verify()
    print(
        "BDA g-step coanchor: verified "
        f"{vectors} weight vectors and {anchors} two-anchor sums"
    )


if __name__ == "__main__":
    main()
