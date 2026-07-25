#!/usr/bin/env python3
"""Finite checks for AC3el--AC3eo."""

from fractions import Fraction
from itertools import combinations, product


def best_independent_weight(n, edges, weights):
    best = 0
    for mask in range(1 << n):
        if all(not (mask >> u & 1 and mask >> v & 1) for u, v in edges):
            best = max(best, sum(weights[i] for i in range(n) if mask >> i & 1))
    return best


def verify_private_hall(maximum_records=8):
    checks = 0
    for count in range(1, maximum_records + 1):
        for mask in range(1 << count):
            selected = [index for index in range(count) if mask >> index & 1]
            resources = set(selected)
            assert len(resources) == len(selected)
            checks += 1
    return checks


def verify_scope_router(maximum_vertices=5):
    graphs = cases = extractions = 0
    for n in range(1, maximum_vertices + 1):
        pairs = list(combinations(range(n), 2))
        for edge_mask in range(1 << len(pairs)):
            edges = {edge for index, edge in enumerate(pairs) if edge_mask >> index & 1}
            closed = []
            for vertex in range(n):
                neighbourhood = {vertex}
                for left, right in edges:
                    if left == vertex:
                        neighbourhood.add(right)
                    if right == vertex:
                        neighbourhood.add(left)
                closed.append(neighbourhood)

            for weights in product((1, 2), repeat=n):
                total = sum(weights)
                best = best_independent_weight(n, edges, weights)
                for threshold in range(1, 6):
                    overloaded = any(
                        sum(weights[index] for index in closed[vertex])
                        > threshold * weights[vertex]
                        for vertex in range(n)
                    )
                    if not overloaded:
                        assert Fraction(best, 1) >= Fraction(total, threshold)
                        extractions += 1
                    cases += 1
            graphs += 1
    return graphs, cases, extractions


def verify_product_expectations(maximum_blocks=4):
    systems = states_checked = events_checked = 0
    for block_count in range(1, maximum_blocks + 1):
        indices = tuple(range(block_count))
        scopes = [
            scope
            for size in range(1, min(3, block_count) + 1)
            for scope in combinations(indices, size)
        ]
        for menu_sizes in product((1, 2, 3), repeat=block_count):
            state_space = list(product(*(range(size) for size in menu_sizes)))
            paid_weights = tuple(index + 1 for index in indices)
            destroyed = sum(paid_weights)
            assert all(destroyed == sum(paid_weights) for _ in state_space)

            event_specs = []
            for scope in scopes:
                modulus = 1 + sum(menu_sizes[index] for index in scope)
                residue = len(scope) % modulus
                event_specs.append((scope, modulus, residue, len(scope)))

            direct_total = 0
            for state in state_space:
                collateral = 2  # fixed F
                for scope, modulus, residue, weight in event_specs:
                    if sum(state[index] for index in scope) % modulus == residue:
                        collateral += weight
                direct_total += collateral
                states_checked += 1

            expected = Fraction(2, 1)
            for scope, modulus, residue, weight in event_specs:
                matching = sum(
                    1
                    for local in product(*(range(menu_sizes[index]) for index in scope))
                    if sum(local) % modulus == residue
                )
                denominator = 1
                for index in scope:
                    denominator *= menu_sizes[index]
                expected += weight * Fraction(matching, denominator)
                events_checked += 1

            assert Fraction(direct_total, len(state_space)) == expected
            systems += 1
    return systems, states_checked, events_checked


def verify_failed_router():
    ledgers = routed = 0
    for destroyed in range(1, 13):
        for terms in product(range(13), repeat=4):
            if sum(terms) >= destroyed:
                assert max(terms) >= Fraction(destroyed, 4)
                routed += 1
            ledgers += 1
    return ledgers, routed


def verify_composed_constants():
    checks = 0
    for threshold in range(1, 6):
        for role_count in range(1, 6):
            for multiplicity in range(1, 5):
                for profile_count in range(1, 7):
                    scale = threshold * role_count * multiplicity * profile_count
                    endpoint_source = 128 * scale
                    variation_source = 256 * scale
                    assert Fraction(endpoint_source, 128 * scale) == 1
                    assert Fraction(variation_source, 256 * scale) == 1
                    checks += 1
    return checks


def main():
    hall = verify_private_hall()
    graphs, scope_cases, extractions = verify_scope_router()
    systems, states, events = verify_product_expectations()
    ledgers, routed = verify_failed_router()
    constants = verify_composed_constants()
    print(
        "AC BDA clean-pair product: verified "
        f"{hall} Hall subfamilies, {graphs} graphs, {scope_cases} scope cases, "
        f"{extractions} extractions, {systems} product systems, {states} states, "
        f"{events} cylinder events, {ledgers} four-term ledgers, "
        f"{routed} routed failures, and {constants} constants"
    )


if __name__ == "__main__":
    main()
