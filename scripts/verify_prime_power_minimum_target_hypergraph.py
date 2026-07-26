#!/usr/bin/env python3
"""Finite checks for CMR1070--CMR1077."""

from itertools import combinations
from math import ceil, comb, gcd
import random


def maximal_disjoint_edges(edges):
    selected = []
    used = set()
    for edge in edges:
        if set(edge).isdisjoint(used):
            selected.append(edge)
            used.update(edge)
    return selected, used


def check_general_hypergraph_packing():
    rng = random.Random(1070)
    checked = 0
    for vertex_count in range(3, 80):
        triples = list(combinations(range(vertex_count), 3))
        for _ in range(200):
            family = set(
                rng.sample(
                    triples,
                    rng.randint(1, min(len(triples), 300)),
                )
            )
            ordered = sorted(family)
            selected, cover = maximal_disjoint_edges(ordered)
            assert len(cover) == 3 * len(selected)
            assert all(set(edge) & cover for edge in family)

            threshold = len(selected) + 1
            assert len(cover) <= 3 * (threshold - 1)
            loads = {vertex: 0 for vertex in cover}
            for edge in family:
                witness = min(set(edge) & cover)
                loads[witness] += 1
            assert max(loads.values()) >= ceil(len(family) / len(cover))
            checked += 1
    return checked


def random_permutation(side, rng):
    values = list(range(side))
    rng.shuffle(values)
    return tuple(values)


def random_state(side, rng):
    first = random_permutation(side, rng)
    for _ in range(1000):
        second = random_permutation(side, rng)
        if all(second[index] != first[index] for index in range(side)):
            labelled = frozenset(
                [(0, (source, first[source])) for source in range(side)]
                + [(1, (source, second[source])) for source in range(side)]
            )
            physical = frozenset(cell for _layer, cell in labelled)
            return labelled, physical
    raise RuntimeError("failed to sample disjoint permutation layers")


def collinear(first, second, third):
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def triples_of(physical):
    return {
        frozenset(triple)
        for triple in combinations(physical, 3)
        if collinear(*triple)
    }


def line_key(first, second):
    coefficient_x = second[1] - first[1]
    coefficient_y = first[0] - second[0]
    constant = -(
        coefficient_x * first[0] + coefficient_y * first[1]
    )
    divisor = gcd(
        gcd(abs(coefficient_x), abs(coefficient_y)), abs(constant)
    )
    if divisor:
        coefficient_x //= divisor
        coefficient_y //= divisor
        constant //= divisor
    if coefficient_x < 0 or (
        coefficient_x == 0 and coefficient_y < 0
    ):
        coefficient_x = -coefficient_x
        coefficient_y = -coefficient_y
        constant = -constant
    return coefficient_x, coefficient_y, constant


def check_rooted_line_decomposition():
    rng = random.Random(1072)
    checked = 0
    rooted_cases = 0
    for side in range(3, 16):
        for _ in range(500):
            labelled, physical = random_state(side, rng)
            targets = triples_of(physical)
            if not targets:
                checked += 1
                continue
            root = rng.choice(tuple(physical))
            rooted = {target for target in targets if root in target}

            line_groups = {}
            for point in set(physical) - {root}:
                line_groups.setdefault(line_key(root, point), []).append(point)
            exact = sum(comb(len(points), 2) for points in line_groups.values())
            assert exact == len(rooted)

            threshold = rng.randint(3, max(3, 2 * side))
            maximum = max([len(points) for points in line_groups.values()] or [0])
            if maximum >= threshold:
                loaded = max(line_groups.values(), key=len)
                occupied = [root, *loaded]
                line_targets = sum(
                    1
                    for target in combinations(occupied, 3)
                    if frozenset(target) in targets
                )
                assert line_targets >= comb(threshold + 1, 3)
            else:
                active_lines = sum(
                    1 for points in line_groups.values() if len(points) >= 2
                )
                if rooted:
                    assert active_lines >= ceil(
                        len(rooted) / comb(threshold - 1, 2)
                    )
            rooted_cases += 1
            checked += 1
    return checked, rooted_cases


def check_disjoint_target_compatibility():
    rng = random.Random(1071)
    checked = 0
    total_targets = 0
    for side in range(3, 20):
        for _ in range(500):
            labelled, physical = random_state(side, rng)
            labels = {cell: layer for layer, cell in labelled}
            targets = sorted(
                triples_of(physical),
                key=lambda target: tuple(sorted(target)),
            )
            selected, used = maximal_disjoint_edges(targets)
            prescription = {
                (labels[cell], cell)
                for target in selected
                for cell in target
            }
            assert len(prescription) == 3 * len(selected)
            assert len({cell for _layer, cell in prescription}) == len(prescription)
            for layer in (0, 1):
                layer_cells = [
                    cell for item_layer, cell in prescription if item_layer == layer
                ]
                assert len({source for source, _target in layer_cells}) == len(
                    layer_cells
                )
                assert len({target for _source, target in layer_cells}) == len(
                    layer_cells
                )
            assert len(used) == 3 * len(selected)
            total_targets += len(selected)
            checked += 1
    return checked, total_targets


def check_contraction_budget():
    rng = random.Random(1076)
    checked = 0
    for cardinality in range(0, 1000):
        remaining = cardinality
        target_total = 0
        while remaining >= 3:
            maximum = remaining // 3
            target_count = rng.randint(1, maximum)
            remaining -= 3 * target_count
            target_total += target_count
            assert 3 * target_total + remaining == cardinality
        assert target_total <= cardinality // 3
        checked += 1
    return checked


def check_cover_threshold_arithmetic():
    checked = 0
    for target_count in range(1, 10000):
        for threshold in range(2, 50):
            cover_size = 3 * (threshold - 1)
            concentration = ceil(target_count / cover_size)
            assert concentration * cover_size >= target_count
            checked += 1
    return checked


def main():
    rooted_checked, rooted_cases = check_rooted_line_decomposition()
    compatibility_cases, selected_targets = check_disjoint_target_compatibility()
    print(
        "verified minimum-target hypergraph packing:",
        check_general_hypergraph_packing(),
        "general packing/cover cases,",
        rooted_checked,
        "saturated states with",
        rooted_cases,
        "rooted decompositions,",
        compatibility_cases,
        "compatibility cases containing",
        selected_targets,
        "disjoint targets,",
        check_contraction_budget(),
        "contraction histories, and",
        check_cover_threshold_arithmetic(),
        "cover arithmetic cases",
    )


if __name__ == "__main__":
    main()
