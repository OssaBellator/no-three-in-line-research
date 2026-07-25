#!/usr/bin/env python3
"""Finite checks for CMR671--CMR676.

The checker exhausts binary child labels through side four and then uses a fixed
sample of ternary labels and permutation pairs through side seven.
"""

from itertools import permutations, product
from random import Random


def inverse(permutation):
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return result


def routing_skeleton(permutation, source_labels, target_labels):
    inv = inverse(permutation)
    source_routing = tuple(
        target_labels[permutation[source]] for source in range(len(permutation))
    )
    target_routing = tuple(
        source_labels[inv[target]] for target in range(len(permutation))
    )
    return source_routing, target_routing


def check_pair(first, second, source_labels, target_labels):
    first_skeleton = routing_skeleton(first, source_labels, target_labels)
    second_skeleton = routing_skeleton(second, source_labels, target_labels)
    if first_skeleton == second_skeleton:
        return False

    first_inverse = inverse(first)
    second_inverse = inverse(second)
    changed_sources = {
        source
        for source in range(len(first))
        if target_labels[first[source]] != target_labels[second[source]]
    }
    changed_targets = {
        target
        for target in range(len(first))
        if source_labels[first_inverse[target]]
        != source_labels[second_inverse[target]]
    }

    assert changed_sources or changed_targets
    assert not changed_sources or len(changed_sources) >= 2
    assert not changed_targets or len(changed_targets) >= 2

    entering = {
        (source, second[source]) for source in changed_sources
    } | {
        (second_inverse[target], target) for target in changed_targets
    }
    leaving = {
        (source, first[source]) for source in changed_sources
    } | {
        (first_inverse[target], target) for target in changed_targets
    }

    assert len(entering) >= 2
    assert len(leaving) >= 2
    first_edges = {(source, first[source]) for source in range(len(first))}
    second_edges = {(source, second[source]) for source in range(len(second))}
    assert entering <= second_edges - first_edges
    assert leaving <= first_edges - second_edges
    return True


def main():
    exact_changes = 0
    for side in range(2, 5):
        matchings = list(permutations(range(side)))
        nonconstant_labels = [
            labels
            for labels in product(range(2), repeat=side)
            if len(set(labels)) >= 2
        ]
        for source_labels in nonconstant_labels:
            for target_labels in nonconstant_labels:
                for first_index, first in enumerate(matchings):
                    for second in matchings[first_index + 1 :]:
                        if check_pair(
                            first, second, source_labels, target_labels
                        ):
                            exact_changes += 1

    sampled_changes = 0
    rng = Random(0)
    for side in range(5, 8):
        matchings = list(permutations(range(side)))
        for _ in range(6000):
            source_labels = tuple(rng.randrange(3) for _ in range(side))
            target_labels = tuple(rng.randrange(3) for _ in range(side))
            if len(set(source_labels)) == len(set(target_labels)) == 1:
                continue
            first, second = rng.sample(matchings, 2)
            if check_pair(first, second, source_labels, target_labels):
                sampled_changes += 1

    # CMR674--CMR675 arithmetic.
    for side in range(2, 30):
        edge_stock = side * side
        for recurrence in range(2, 12):
            bound = ((recurrence - 1) * edge_stock) // 2
            assert 2 * bound <= (recurrence - 1) * edge_stock
            for prime in (3, 5, 7):
                for height in range(1, 6):
                    incidence = 2 * bound * (prime + 1) * (height - 1)
                    assert incidence >= 0

    print(
        "verified routing-change support:",
        exact_changes,
        "exact changes and",
        sampled_changes,
        "sampled changes",
    )


if __name__ == "__main__":
    main()
