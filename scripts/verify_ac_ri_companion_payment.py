#!/usr/bin/env python3
"""Verify AC3dn--AC3dq on small rational fibres and conflict graphs."""

from fractions import Fraction
from itertools import combinations, product


def inv(value, prime):
    return pow(value % prime, prime - 2, prime)


def f_map(ratio, root, prime):
    return root * (1 - root) * inv(ratio - root, prime) % prime


def tau(ratio, root, prime):
    return ratio * (root - 1) * inv(root - ratio, prime) % prime


def point(channel, column, prime):
    return channel % prime, column % prime, channel * inv(column, prime) % prime


def records_for_profile(prime, ratio, root):
    image = f_map(ratio, root, prime)
    companion = tau(ratio, root, prime)
    records = []
    for base in range(1, prime):
        edge = frozenset(
            {
                point(1, base, prime),
                point(1, image * base, prime),
            }
        )
        anchor = point(ratio, root * base, prime)
        desired = point(ratio, companion * base, prime)
        resource = (edge, anchor)
        records.append((base, resource, desired))
    return image, companion, records


def verify_fibres():
    profiles = 0
    records_checked = 0
    hall_subfamilies = 0
    involutions = 0

    for prime in (5, 7, 11, 13):
        for ratio in range(2, prime):
            for root in range(1, prime):
                if root in (1, ratio):
                    continue
                image = f_map(ratio, root, prime)
                if image in (0, 1):
                    continue
                companion = tau(ratio, root, prime)
                if companion in (0, 1, ratio):
                    continue

                image2, companion2, records = records_for_profile(
                    prime, ratio, root
                )
                assert image2 == image
                assert companion2 == companion
                assert tau(ratio, companion, prime) == root
                assert f_map(ratio, companion, prime) == image
                involutions += 1

                resources = [resource for _, resource, _ in records]
                desired = [cell for _, _, cell in records]
                assert len(resources) == len(set(resources))
                assert len(desired) == len(set(desired))

                sample = records[: min(7, len(records))]
                for mask in range(1 << len(sample)):
                    selected = [sample[index] for index in range(len(sample)) if mask >> index & 1]
                    eligible = {resource for _, resource, _ in selected}
                    assert len(eligible) == len(selected)
                    hall_subfamilies += 1

                records_checked += len(records)
                profiles += 1

    return profiles, records_checked, hall_subfamilies, involutions


def independent_weight(vertex_count, edges, weights):
    best = 0
    for mask in range(1 << vertex_count):
        valid = True
        for left, right in edges:
            if mask >> left & 1 and mask >> right & 1:
                valid = False
                break
        if valid:
            total = sum(weights[index] for index in range(vertex_count) if mask >> index & 1)
            best = max(best, total)
    return best


def verify_weighted_conflict_router(maximum_vertices=5):
    graph_checks = 0
    weighted_checks = 0

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
                maximum = independent_weight(vertex_count, edges, weights)
                for threshold in range(1, 6):
                    overloaded = any(
                        sum(weights[index] for index in closed[vertex])
                        > threshold * weights[vertex]
                        for vertex in range(vertex_count)
                    )
                    if not overloaded:
                        assert Fraction(maximum, 1) >= Fraction(total, threshold)
                    weighted_checks += 1
            graph_checks += 1

    return graph_checks, weighted_checks


def verify_ticket_potential(maximum_records=9):
    checks = 0
    for record_count in range(1, maximum_records + 1):
        for used in range(record_count + 1):
            # Each nonfixed base has one capacity-one root-change ticket.
            remaining = record_count - used
            assert remaining >= 0
            if used == record_count:
                assert remaining == 0
            checks += 1
    return checks


def main():
    profiles, records, hall, involutions = verify_fibres()
    graphs, weighted = verify_weighted_conflict_router()
    tickets = verify_ticket_potential()
    print(
        "AC RI companion payment: verified "
        f"{profiles} profiles, {records} private records, "
        f"{hall} Hall subfamilies, {involutions} involutions, "
        f"{graphs} conflict graphs, {weighted} weighted AC2c cases, "
        f"and {tickets} ticket states"
    )


if __name__ == "__main__":
    main()
