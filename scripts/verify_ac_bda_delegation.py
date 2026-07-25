#!/usr/bin/env python3
"""Exhaust AC3an--AC3aq arithmetic and weighted delegation checks."""

from itertools import product
from math import gcd


def primitive_directions(bound):
    return [
        (x, y)
        for x in range(1, bound + 1)
        for y in range(-bound, bound + 1)
        if gcd(x, abs(y)) == 1
    ]


def determinant(left, right):
    return left[0] * right[1] - left[1] * right[0]


def path_edges(weights, step):
    return [
        (index, index + step, min(weights[index], weights[index + step]))
        for index in range(len(weights) - step)
    ]


def parity_classes(weights, step):
    classes = ([], [])
    for left, right, weight in path_edges(weights, step):
        residue = left % step
        path_index = (left - residue) // step
        classes[path_index % 2].append((left, right, weight))
    return classes


def verify_profiles(maximum_q=7, maximum_bound=4):
    profile_checks = 0
    pigeonhole_checks = 0

    for bound in range(1, maximum_bound + 1):
        directions = primitive_directions(bound)
        count = len(directions)
        assert count <= bound * (2 * bound + 1)

        for maximum_q_now in range(2, maximum_q + 1):
            actual = sum(
                q * count * count for q in range(2, maximum_q_now + 1)
            )
            formula = count * count * sum(range(2, maximum_q_now + 1))
            crude = (
                bound
                * bound
                * (2 * bound + 1) ** 2
                * maximum_q_now
                * (maximum_q_now + 1)
                // 2
            )
            assert actual == formula
            assert actual <= crude
            profile_checks += 1

    for class_count in range(1, 7):
        for weights in product(range(4), repeat=class_count):
            total = sum(weights)
            if total:
                assert max(weights) * class_count >= total
                pigeonhole_checks += 1

    return profile_checks, pigeonhole_checks


def verify_slotization(maximum_q=10, bound=4):
    directions = primitive_directions(bound)
    congruence_checks = 0
    aggregation_checks = 0

    for q in range(2, maximum_q + 1):
        for left, right in product(directions, repeat=2):
            delta = determinant(left, right)
            if delta == 0:
                continue
            common = gcd(abs(delta), q)
            step = q // common

            for residue in range(q):
                solutions = [
                    h
                    for h in range(1, 4 * q + 1)
                    if (h * delta - residue) % q == 0
                ]
                if not solutions:
                    assert residue % common != 0
                    congruence_checks += 1
                    continue

                assert residue % common == 0
                assert len({h % step for h in solutions}) == 1
                smallest = min(solutions)
                largest = max(solutions)
                slot_count = 1 + (largest - smallest) // step
                slots = [smallest + index * step for index in range(slot_count)]
                assert all(h in slots for h in solutions)

                records = []
                for anchor in range(3):
                    for h in solutions:
                        weight = 1 + (anchor + h) % 3
                        records.append((anchor, h, weight))

                aggregated = {
                    (anchor, index): 0
                    for anchor in range(3)
                    for index in range(slot_count)
                }
                for anchor, h, weight in records:
                    index = (h - smallest) // step
                    aggregated[(anchor, index)] += weight

                assert sum(aggregated.values()) == sum(
                    weight for _, _, weight in records
                )
                congruence_checks += 1
                aggregation_checks += 1

    return congruence_checks, aggregation_checks


def verify_weighted_paths(maximum_length=8, maximum_beta=3):
    overlap_checks = 0
    parity_checks = 0
    anchor_checks = 0

    for length in range(1, maximum_length + 1):
        for step in range(1, maximum_length + 1):
            for beta in range(1, maximum_beta + 1):
                for weights in product(range(beta + 1), repeat=length):
                    total = sum(weights)
                    edges = path_edges(weights, step) if step < length else []
                    overlap = sum(weight for _, _, weight in edges)
                    lower = max(0, 2 * total - beta * (length + step))
                    assert overlap >= lower
                    overlap_checks += 1

                    classes = parity_classes(weights, step) if step < length else ([], [])
                    assert sum(
                        weight
                        for class_edges in classes
                        for _, _, weight in class_edges
                    ) == overlap
                    for class_edges in classes:
                        used = []
                        for left, right, _ in class_edges:
                            used.extend((left, right))
                        assert len(used) == len(set(used))
                    assert max(
                        sum(weight for _, _, weight in class_edges)
                        for class_edges in classes
                    ) * 2 >= overlap
                    parity_checks += 1

    # Additivity across two anchors is the only extra step used in AC3ap.
    for length in range(1, 6):
        for step in range(1, 6):
            for beta in range(1, 3):
                vectors = list(product(range(beta + 1), repeat=length))
                for first in vectors:
                    for second in vectors:
                        total = sum(first) + sum(second)
                        overlap = 0
                        if step < length:
                            overlap += sum(
                                min(first[index], first[index + step])
                                for index in range(length - step)
                            )
                            overlap += sum(
                                min(second[index], second[index + step])
                                for index in range(length - step)
                            )
                        lower = max(
                            0,
                            2 * total - 2 * beta * (length + step),
                        )
                        assert overlap >= lower
                        anchor_checks += 1

    return overlap_checks, parity_checks, anchor_checks


def main():
    profile, pigeonhole = verify_profiles()
    congruence, aggregation = verify_slotization()
    overlap, parity, anchors = verify_weighted_paths()
    print(
        "AC BDA delegation: verified "
        f"{profile} profile counts, {pigeonhole} profile routers, "
        f"{congruence} scalar congruences, {aggregation} aggregations, "
        f"{overlap} weighted paths, {parity} parity classes, "
        f"and {anchors} two-anchor sums"
    )


if __name__ == "__main__":
    main()
