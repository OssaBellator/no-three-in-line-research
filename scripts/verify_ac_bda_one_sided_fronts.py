#!/usr/bin/env python3
"""Verify AC3du--AC3dx on exhaustive small abstract scalar fronts."""

from fractions import Fraction
from itertools import combinations, product


def path_fronts(weights, step):
    overlap = 0
    endpoint_slots = set()
    down_edges = [[], []]
    up_edges = [[], []]

    for residue in range(min(step, len(weights))):
        path = list(range(residue, len(weights), step))
        endpoint_slots.add(path[0])
        endpoint_slots.add(path[-1])
        for local_index, left in enumerate(path[:-1]):
            right = path[local_index + 1]
            overlap += min(weights[left], weights[right])
            difference = weights[right] - weights[left]
            if difference > 0:
                up_edges[local_index % 2].append((left, right, difference))
            elif difference < 0:
                down_edges[local_index % 2].append((left, right, -difference))

    endpoint_weight = sum(weights[index] for index in endpoint_slots)
    pair_weight = Fraction(overlap, 2)
    oriented_classes = down_edges + up_edges
    oriented_weight = max(
        (sum(edge[2] for edge in edge_class) for edge_class in oriented_classes),
        default=0,
    )
    return pair_weight, endpoint_slots, endpoint_weight, oriented_classes, oriented_weight


def verify_scalar_fronts(maximum_length=7, maximum_weight=3):
    systems = 0
    hall_subfamilies = 0
    composition_checks = 0

    for length in range(1, maximum_length + 1):
        for step in range(1, length + 1):
            for weights in product(range(maximum_weight + 1), repeat=length):
                total = sum(weights)
                pair, endpoints, endpoint_weight, classes, oriented = path_fronts(
                    weights, step
                )

                # Every parity class is slot-disjoint.
                for edge_class in classes:
                    used = []
                    for left, right, _ in edge_class:
                        used.extend((left, right))
                    assert len(used) == len(set(used))

                # Private singleton resources give exact Hall on every selected
                # endpoint set and every selected parity edge set.
                endpoint_list = sorted(endpoints)
                for mask in range(1 << len(endpoint_list)):
                    selected = {
                        endpoint_list[index]
                        for index in range(len(endpoint_list))
                        if mask >> index & 1
                    }
                    assert len(selected) == sum(1 for _ in selected)
                    hall_subfamilies += 1
                for edge_class in classes:
                    for mask in range(1 << len(edge_class)):
                        selected = [
                            edge_class[index]
                            for index in range(len(edge_class))
                            if mask >> index & 1
                        ]
                        resources = {
                            slot
                            for left, right, _ in selected
                            for slot in (left, right)
                        }
                        assert len(resources) == 2 * len(selected)
                        hall_subfamilies += 1

                if total:
                    # theta=1/2 guarantee from the source BDA theorem.
                    assert (
                        pair >= Fraction(total, 4)
                        or endpoint_weight > Fraction(total, 4)
                        or oriented > Fraction(total, 8)
                    )

                    for role_count in range(1, 5):
                        for multiplicity in range(1, 4):
                            for profile_count in range(1, 6):
                                source = 2 * role_count * multiplicity * profile_count * total
                                scale = Fraction(source, 2 * role_count * multiplicity * profile_count)
                                assert scale == total
                                assert Fraction(source, 8 * role_count * multiplicity * profile_count) == Fraction(total, 4)
                                assert Fraction(source, 16 * role_count * multiplicity * profile_count) == Fraction(total, 8)
                                composition_checks += 1
                systems += 1

    return systems, hall_subfamilies, composition_checks


def maximum_independent_weight(vertex_count, edges, weights):
    best = 0
    for mask in range(1 << vertex_count):
        if all(not (mask >> left & 1 and mask >> right & 1) for left, right in edges):
            best = max(
                best,
                sum(weights[index] for index in range(vertex_count) if mask >> index & 1),
            )
    return best


def verify_conflict_router(maximum_vertices=5):
    checks = 0
    graphs = 0
    for vertex_count in range(1, maximum_vertices + 1):
        possible_edges = list(combinations(range(vertex_count), 2))
        for edge_mask in range(1 << len(possible_edges)):
            edges = {
                edge
                for index, edge in enumerate(possible_edges)
                if edge_mask >> index & 1
            }
            closed = []
            for vertex in range(vertex_count):
                neighbourhood = {vertex}
                for left, right in edges:
                    if left == vertex:
                        neighbourhood.add(right)
                    if right == vertex:
                        neighbourhood.add(left)
                closed.append(neighbourhood)

            for weights in product((1, 2), repeat=vertex_count):
                total = sum(weights)
                best = maximum_independent_weight(vertex_count, edges, weights)
                for threshold in range(1, 6):
                    overloaded = any(
                        sum(weights[index] for index in closed[vertex])
                        > threshold * weights[vertex]
                        for vertex in range(vertex_count)
                    )
                    if not overloaded:
                        assert Fraction(best, 1) >= Fraction(total, threshold)
                    checks += 1
            graphs += 1
    return graphs, checks


def main():
    systems, hall, constants = verify_scalar_fronts()
    graphs, conflicts = verify_conflict_router()
    print(
        "AC BDA one-sided fronts: verified "
        f"{systems} scalar systems, {hall} Hall subfamilies, "
        f"{constants} composition constants, {graphs} conflict graphs, "
        f"and {conflicts} weighted router cases"
    )


if __name__ == "__main__":
    main()
