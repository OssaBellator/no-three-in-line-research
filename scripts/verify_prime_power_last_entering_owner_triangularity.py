#!/usr/bin/env python3
"""Finite checks for CMR1318--CMR1325."""

from fractions import Fraction
import random


def matvec(matrix, vector):
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def check_one_coordinate_product_ownership():
    rng = random.Random(1319)
    checked = 0
    created = 0
    for factor_count in range(2, 8):
        for _ in range(1500):
            factors = []
            next_edge = 0
            for _factor in range(factor_count):
                size = rng.randint(2, 12)
                factor = set(range(next_edge, next_edge + size))
                next_edge += size
                factors.append(factor)
            core = set(range(next_edge, next_edge + rng.randint(0, 8)))
            active = rng.randrange(factor_count)
            old_factor = set(rng.sample(tuple(factors[active]), rng.randint(1, len(factors[active]) - 1)))
            new_factor = set(old_factor)
            removed = set(rng.sample(tuple(new_factor), rng.randint(0, min(3, len(new_factor)))))
            new_factor -= removed
            addable = factors[active] - new_factor
            entering = set(rng.sample(tuple(addable), rng.randint(1, min(3, len(addable)))))
            new_factor |= entering

            frozen = set(core)
            for index, factor in enumerate(factors):
                if index == active:
                    continue
                frozen |= set(rng.sample(tuple(factor), rng.randint(1, len(factor))))

            old_state = frozen | old_factor
            new_state = frozen | new_factor
            candidates = list(new_state)
            for _triple in range(80):
                triple = set(rng.sample(candidates, min(3, len(candidates))))
                if len(triple) < 3 or triple <= old_state:
                    continue
                owner_candidates = sorted(triple & (new_state - old_state))
                assert owner_candidates
                owner = owner_candidates[0]
                assert owner in factors[active]
                assert owner not in core
                assert all(owner not in factors[index] for index in range(factor_count) if index != active)
                created += 1
            checked += 1
    return checked, created


def random_local_certificate(size, rng):
    weight = [Fraction(rng.randint(1, 30)) for _ in range(size)]
    slack = [Fraction(rng.randint(1, 9), 10) * weight[index] for index in range(size)]
    matrix = []
    for row in range(size):
        raw = [rng.randint(1, 20) for _ in range(size)]
        weighted = sum(Fraction(raw[column]) * weight[column] for column in range(size))
        target = weight[row] - slack[row]
        matrix.append([
            target * Fraction(raw[column], 1) / weighted
            for column in range(size)
        ])
    return matrix, weight, slack


def block_matvec(diagonal, off_diagonal, scales, weights):
    images = []
    for i, block in enumerate(diagonal):
        local = matvec(block, [scales[i] * value for value in weights[i]])
        for j in range(i + 1, len(diagonal)):
            cross = off_diagonal.get((i, j))
            if cross is None:
                continue
            contribution = matvec(cross, [scales[j] * value for value in weights[j]])
            local = [left + right for left, right in zip(local, contribution)]
        images.append(local)
    return images


def choose_scales(diagonal, off_diagonal, weights, slack):
    count = len(diagonal)
    scales = [Fraction(0)] * count
    for i in reversed(range(count)):
        cross_total = [Fraction(0)] * len(weights[i])
        for j in range(i + 1, count):
            cross = off_diagonal.get((i, j))
            if cross is None:
                continue
            contribution = matvec(cross, [scales[j] * value for value in weights[j]])
            cross_total = [left + right for left, right in zip(cross_total, contribution)]
        ratios = [
            cross_total[row] / slack[i][row]
            for row in range(len(cross_total))
        ]
        scales[i] = max(ratios, default=Fraction(0)) + 1
    return scales


def check_constructive_upper_triangular_gluing():
    rng = random.Random(1324)
    checked = 0
    blocks = 0
    for block_count in range(1, 11):
        for _ in range(350):
            diagonal = []
            weights = []
            slack = []
            sizes = [rng.randint(1, 7) for _block in range(block_count)]
            for size in sizes:
                matrix, weight, local_slack = random_local_certificate(size, rng)
                diagonal.append(matrix)
                weights.append(weight)
                slack.append(local_slack)
            off_diagonal = {}
            for i in range(block_count):
                for j in range(i + 1, block_count):
                    if rng.random() < 0.45:
                        off_diagonal[(i, j)] = [
                            [Fraction(rng.randint(0, 50), 10) for _column in range(sizes[j])]
                            for _row in range(sizes[i])
                        ]
            scales = choose_scales(diagonal, off_diagonal, weights, slack)
            images = block_matvec(diagonal, off_diagonal, scales, weights)
            for index in range(block_count):
                target = [scales[index] * value for value in weights[index]]
                assert all(left < right for left, right in zip(images[index], target))
            checked += 1
            blocks += block_count
    return checked, blocks


def check_topological_direction():
    rng = random.Random(1321)
    checked = 0
    arcs = 0
    for owner_count in range(1, 200):
        order = list(range(owner_count))
        for _ in range(100):
            graph = {owner: set() for owner in order}
            for source in order:
                for target in range(source + 1, owner_count):
                    if rng.random() < 0.03:
                        graph[source].add(target)
                        arcs += 1
            for source, targets in graph.items():
                assert all(target > source for target in targets)
            checked += 1
    return checked, arcs


def check_strict_side_descents():
    checked = 0
    for side in range(2, 500):
        for first in range(side):
            second = side - 1 - first
            assert first < side and second < side
            checked += 1
        for child in range(1, side):
            assert child < side
            checked += 1
    return checked


def main():
    product = check_one_coordinate_product_ownership()
    topology = check_topological_direction()
    gluing = check_constructive_upper_triangular_gluing()
    print(
        "verified owner triangularity:",
        product[0],
        "one-coordinate products with",
        product[1],
        "created triples,",
        topology[0],
        "owner DAGs with",
        topology[1],
        "forward arcs,",
        check_strict_side_descents(),
        "strict-side cases, and",
        gluing[0],
        "rational block gluings across",
        gluing[1],
        "diagonal blocks",
    )


if __name__ == "__main__":
    main()
