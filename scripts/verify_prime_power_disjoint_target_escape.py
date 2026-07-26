#!/usr/bin/env python3
"""Finite checks for CMR1078--CMR1085."""

from itertools import combinations, permutations
from math import ceil
import random


def matching(permutation):
    return {(source, permutation[source]) for source in range(len(permutation))}


def perfect_matching_avoiding(side, forbidden):
    target_to_source = [-1] * side

    def augment(source, seen):
        for target in range(side):
            if (source, target) in forbidden or seen[target]:
                continue
            seen[target] = True
            previous = target_to_source[target]
            if previous < 0 or augment(previous, seen):
                target_to_source[target] = source
                return True
        return False

    for source in range(side):
        if not augment(source, [False] * side):
            return None
    permutation = [-1] * side
    for target, source in enumerate(target_to_source):
        permutation[source] = target
    return tuple(permutation)


def check_exhaustive_small_hall():
    checked = 0
    for side in range(4, 7):
        permutations_list = list(permutations(range(side)))
        for first in permutations_list:
            for second in permutations_list:
                forbidden = matching(first) | matching(second)
                result = perfect_matching_avoiding(side, forbidden)
                assert result is not None
                assert len(set(result)) == side
                assert matching(result).isdisjoint(forbidden)
                checked += 1
    return checked


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return tuple(values)


def random_disjoint_state(side, rng):
    first = random_permutation(side, rng)
    for _ in range(1000):
        second = random_permutation(side, rng)
        if all(first[index] != second[index] for index in range(side)):
            labelled = frozenset(
                [(0, (source, first[source])) for source in range(side)]
                + [(1, (source, second[source])) for source in range(side)]
            )
            physical = frozenset(cell for _layer, cell in labelled)
            return first, second, labelled, physical
    raise RuntimeError("failed to sample disjoint layers")


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def target_triples(physical):
    return [
        frozenset(triple)
        for triple in combinations(physical, 3)
        if collinear(*triple)
    ]


def maximal_disjoint_targets(targets):
    selected = []
    used = set()
    for target in sorted(targets, key=lambda item: tuple(sorted(item))):
        if set(target).isdisjoint(used):
            selected.append(target)
            used.update(target)
    return selected


def check_sampled_target_escape():
    rng = random.Random(1078)
    checked = 0
    bank_targets = 0
    destroyed_targets = 0
    for side in range(4, 25):
        for _ in range(400):
            first, second, labelled, physical = random_disjoint_state(side, rng)
            labels = {cell: layer for layer, cell in labelled}
            targets = maximal_disjoint_targets(target_triples(physical))
            if not targets:
                checked += 1
                continue

            majority_classes = {0: [], 1: []}
            for target in targets:
                counts = {
                    layer: sum(1 for cell in target if labels[cell] == layer)
                    for layer in (0, 1)
                }
                chosen_layer = 0 if counts[0] >= counts[1] else 1
                majority_classes[chosen_layer].append(target)
            layer = 0 if len(majority_classes[0]) >= len(majority_classes[1]) else 1
            chosen_targets = majority_classes[layer]
            assert len(chosen_targets) >= ceil(len(targets) / 2)

            representatives = {
                min(cell for cell in target if labels[cell] == layer)
                for target in chosen_targets
            }
            assert len(representatives) == len(chosen_targets)
            assert len({source for source, _target in representatives}) == len(
                representatives
            )
            assert len({target for _source, target in representatives}) == len(
                representatives
            )

            old_layer = first if layer == 0 else second
            opposite = second if layer == 0 else first
            forbidden = matching(old_layer) | matching(opposite)
            rematching = perfect_matching_avoiding(side, forbidden)
            assert rematching is not None
            new_physical = matching(rematching) | matching(opposite)
            assert matching(rematching).isdisjoint(matching(old_layer))
            assert matching(rematching).isdisjoint(matching(opposite))
            assert representatives.isdisjoint(new_physical)
            for target in chosen_targets:
                assert not set(target) <= new_physical

            bank_targets += len(targets)
            destroyed_targets += len(chosen_targets)
            checked += 1
    return checked, bank_targets, destroyed_targets


def check_scale_arithmetic():
    checked = 0
    for target_count in range(1, 100000):
        destroyed = ceil(target_count / 2)
        assert 2 * destroyed >= target_count
        for gap in range(1, 20):
            new_count = destroyed + gap
            assert new_count >= destroyed + 1
            checked += 1
    return checked


def main():
    sampled, total_targets, destroyed = check_sampled_target_escape()
    print(
        "verified disjoint-target simultaneous escape:",
        check_exhaustive_small_hall(),
        "exhaustive Hall boards,",
        sampled,
        "sampled states containing",
        total_targets,
        "disjoint targets and destroying",
        destroyed,
        "targets, and",
        check_scale_arithmetic(),
        "scale cases",
    )


if __name__ == "__main__":
    main()
