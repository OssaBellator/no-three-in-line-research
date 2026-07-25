#!/usr/bin/env python3
"""Finite checks for PX428--PX436 paired rectangle-label packets."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import random


def collinear(
    first: tuple[int, int],
    second: tuple[int, int],
    anchor: tuple[int, int],
) -> bool:
    return (
        (first[0] - anchor[0]) * (second[1] - anchor[1])
        == (second[0] - anchor[0]) * (first[1] - anchor[1])
    )


def check_typed_product_identity() -> None:
    rng = random.Random(428)
    for order in range(3, 30):
        row0 = rng.sample(range(-100, 101), order)
        row1 = rng.sample(range(200, 500), order)
        columns = rng.sample(range(-300, 301), order)

        for _ in range(1000):
            u, s = rng.sample(range(order), 2)
            v, w = rng.sample(range(order), 2)
            epsilon = rng.randrange(2)
            delta = rng.randrange(2)
            anchor = (rng.randint(-500, 500), rng.randint(-500, 500))
            rows = (row0, row1)

            first = (rows[epsilon][u], columns[v])
            second = (rows[delta][s], columns[w])
            left = (rows[epsilon][u] - anchor[0]) * (columns[w] - anchor[1])
            right = (rows[delta][s] - anchor[0]) * (columns[v] - anchor[1])
            assert collinear(first, second, anchor) == (left == right)


def check_packet_partial_matching() -> None:
    rng = random.Random(429)
    for order in range(2, 30):
        for _ in range(200):
            rows = rng.sample(range(-100, 101), order)
            columns = rng.sample(range(-150, 151), order)
            anchor = (rng.randint(-200, 200), rng.randint(-200, 200))
            levels: dict[int, list[tuple[int, int]]] = defaultdict(list)
            for source in range(order):
                for target in range(order):
                    product = (
                        (rows[source] - anchor[0])
                        * (columns[target] - anchor[1])
                    )
                    if product:
                        levels[product].append((source, target))

            for arcs in levels.values():
                source_degree = Counter(source for source, _ in arcs)
                target_degree = Counter(target for _, target in arcs)
                assert max(source_degree.values(), default=0) <= 1
                assert max(target_degree.values(), default=0) <= 1


def check_correction_aggregation() -> None:
    rng = random.Random(431)
    for order in range(3, 20):
        for _ in range(300):
            defects: list[tuple[int, int, int, int]] = []
            for u, s in combinations(range(order), 2):
                for epsilon in range(2):
                    for delta in range(2):
                        multiplicity = rng.randint(0, 5)
                        defects.extend((u, s, epsilon, delta) for _ in range(multiplicity))

            weights = Counter((u, s) for u, s, _, _ in defects)
            assert sum(weights.values()) == len(defects)

            # A source matching gives disjoint commuting corrections and exact
            # destruction equal to its selected edge weight.
            vertices = list(range(order))
            rng.shuffle(vertices)
            correction_matching = [
                tuple(sorted((vertices[i], vertices[i + 1])))
                for i in range(0, order - 1, 2)
            ]
            used = {vertex for edge in correction_matching for vertex in edge}
            assert len(used) == 2 * len(correction_matching)
            destruction = sum(weights[edge] for edge in correction_matching)
            direct = sum(
                1
                for u, s, _, _ in defects
                if tuple(sorted((u, s))) in correction_matching
            )
            assert destruction == direct


def check_four_point_first_order_shapes() -> None:
    # Four new points in two paired columns.  Two within-column pairs have no
    # fixed third point; four cross-column pairs remain.
    points = ((0, 0), (1, 0), (2, 1), (3, 1))
    pairs = list(combinations(range(4), 2))
    within = [pair for pair in pairs if points[pair[0]][1] == points[pair[1]][1]]
    cross = [pair for pair in pairs if points[pair[0]][1] != points[pair[1]][1]]
    assert len(within) == 2
    assert len(cross) == 4

    for triple in combinations(points, 3):
        assert not collinear(triple[0], triple[1], triple[2])


def check_strict_sign_constants() -> None:
    rng = random.Random(435)
    for _ in range(5000):
        block_order = rng.randint(2, 100)
        threshold_r = rng.randint(1, 100)
        threshold_t = rng.randint(1, 100)
        line_cap_k = rng.randint(1, 50)
        loaded_cap_l = rng.randint(0, 50)
        residual = (2 * threshold_r - 1) * (block_order // 2) * (
            4 * line_cap_k * threshold_t + 4 * loaded_cap_l
        )
        mass = residual + rng.randint(1, 1000)
        matching_weight = mass / (2 * threshold_r - 1)
        first_order = (block_order / 2) * (
            4 * line_cap_k * threshold_t + 4 * loaded_cap_l
        )
        assert matching_weight > first_order


def main() -> None:
    check_typed_product_identity()
    check_packet_partial_matching()
    check_correction_aggregation()
    check_four_point_first_order_shapes()
    check_strict_sign_constants()
    print("PX428--PX436 paired-label packet verifier: PASS")


if __name__ == "__main__":
    main()
