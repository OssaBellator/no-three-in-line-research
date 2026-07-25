#!/usr/bin/env python3
"""Exhaust RI5v--RI5x on small hyperbola completion switches."""

from itertools import combinations, permutations, product
from math import ceil


def inverse(value, prime):
    return pow(value, prime - 2, prime)


def collinear(triple, prime):
    (x1, y1), (x2, y2), (x3, y3) = tuple(triple)
    return ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) % prime == 0


def matching_triples(columns, rows, prime):
    for chosen_columns in combinations(columns, 3):
        for chosen_rows in combinations(rows, 3):
            for assignment in permutations(chosen_rows):
                triple = frozenset(zip(chosen_columns, assignment, strict=True))
                if collinear(triple, prime):
                    yield triple


def build_switch(prime, parameter, components):
    columns = list(range(1, prime))
    target = {x: parameter * inverse(x, prime) % prime for x in columns}
    current = dict(target)

    for component in components:
        ordered = tuple(component)
        for index, column in enumerate(ordered):
            previous = ordered[(index - 1) % len(ordered)]
            current[column] = target[previous]

    assert len(set(current.values())) == len(columns)
    assert len(set(target.values())) == len(columns)
    return columns, current, target


def state_cells(columns, current, target, components, bits):
    component_of = {
        column: index
        for index, component in enumerate(components)
        for column in component
    }
    return {
        (
            column,
            target[column]
            if column in component_of and bits[component_of[column]]
            else current[column],
        )
        for column in columns
    }


def compatible_bits(triple, current, target, components):
    allowed = []
    for component in components:
        component_columns = set(component)
        local = {cell for cell in triple if cell[0] in component_columns}
        current_cells = {(x, current[x]) for x in component}
        target_cells = {(x, target[x]) for x in component}
        states = set()
        if local <= current_cells:
            states.add(0)
        if local <= target_cells:
            states.add(1)
        if not states:
            return None
        allowed.append(states)
    return allowed


def verify_geometry(primes=(5, 7)):
    intersection_checks = 0
    secant_checks = 0

    for prime in primes:
        columns = list(range(1, prime))
        for parameter in columns:
            hyperbola = {
                (x, parameter * inverse(x, prime) % prime)
                for x in columns
            }
            for triple in combinations(hyperbola, 3):
                assert not collinear(frozenset(triple), prime)
                intersection_checks += 1

            seen_lines = {}
            for x, y in combinations(columns, 2):
                point_x = (x, parameter * inverse(x, prime) % prime)
                point_y = (y, parameter * inverse(y, prime) % prime)
                total = (x + y) % prime
                product_value = (x * y) % prime
                for column, row in (point_x, point_y):
                    assert (
                        product_value * row
                        + parameter * column
                        - parameter * total
                    ) % prime == 0
                key = (total, product_value)
                pair = frozenset((x, y))
                assert key not in seen_lines or seen_lines[key] == pair
                seen_lines[key] = pair
                secant_checks += 1

    return intersection_checks, secant_checks


def component_families(columns):
    families = []
    for size in range(2, min(4, len(columns)) + 1):
        for component in combinations(columns, size):
            families.append((tuple(component),))
    if len(columns) >= 4:
        for four in combinations(columns, 4):
            first = tuple(four[:2])
            second = tuple(four[2:])
            families.append((first, second))
    return families


def verify_toggle_profiles(primes=(5, 7)):
    state_checks = 0
    rank_one_checks = 0
    context_groups = {}

    for prime in primes:
        columns = list(range(1, prime))
        rows = columns
        triples = tuple(matching_triples(columns, rows, prime))

        for parameter in columns:
            target_hyperbola = {
                (x, parameter * inverse(x, prime) % prime)
                for x in columns
            }

            for components in component_families(columns):
                columns_now, current, target = build_switch(
                    prime, parameter, components
                )
                current_cells = {(x, current[x]) for x in columns_now}
                target_cells = {(x, target[x]) for x in columns_now}

                controlled = {index: set() for index in range(len(components))}

                for triple in triples:
                    allowed = compatible_bits(
                        triple, current, target, components
                    )
                    if allowed is None:
                        continue
                    prescribed = [
                        (index, next(iter(states)))
                        for index, states in enumerate(allowed)
                        if len(states) == 1
                    ]
                    is_new = not triple <= current_cells

                    if is_new and len(prescribed) == 1:
                        component_index, bit = prescribed[0]
                        assert bit == 1
                        assert len(triple & target_hyperbola) <= 2
                        controlled[component_index].add(triple)
                        rank_one_checks += 1

                        component = components[component_index]
                        exclusive = {
                            (x, target[x])
                            for x in component
                            if target[x] != current[x]
                        }
                        local_target = triple & exclusive
                        assert 1 <= len(local_target) <= 2

                        if len(local_target) == 1:
                            target_cell = next(iter(local_target))
                            context = frozenset(triple - {target_cell})
                            key = (prime, parameter, context)
                            context_groups.setdefault(key, set()).add(
                                target_cell[0]
                            )
                        else:
                            first, second = tuple(local_target)
                            x, y = first[0], second[0]
                            total = (x + y) % prime
                            product_value = (x * y) % prime
                            for column, row in local_target:
                                assert (
                                    product_value * row
                                    + parameter * column
                                    - parameter * total
                                ) % prime == 0

                # Exact rank-one subset additivity.
                for bits in product((0, 1), repeat=len(components)):
                    state = state_cells(
                        columns_now, current, target, components, bits
                    )
                    actual = {
                        triple
                        for index, triples_for_component in controlled.items()
                        if bits[index]
                        for triple in triples_for_component
                        if triple <= state
                    }
                    expected = {
                        triple
                        for index, triples_for_component in controlled.items()
                        if bits[index]
                        for triple in triples_for_component
                    }
                    assert actual == expected
                    assert len(actual) == sum(
                        len(controlled[index])
                        for index, bit in enumerate(bits)
                        if bit
                    )
                    state_checks += 1

    assert all(len(columns) <= 2 for columns in context_groups.values())
    return state_checks, rank_one_checks, len(context_groups)


def verify_routers(maximum_weight=4):
    checks = 0
    for component_count in range(1, 6):
        for collateral in product(
            range(maximum_weight + 1), repeat=component_count
        ):
            for paid in product(
                range(maximum_weight + 1), repeat=component_count
            ):
                total_collateral = sum(collateral)
                total_paid = sum(paid)
                for numerator, denominator in ((1, 2), (1, 1), (2, 1)):
                    bad = [
                        index
                        for index in range(component_count)
                        if denominator * collateral[index]
                        > numerator * paid[index]
                    ]
                    bad_mass = sum(collateral[index] for index in bad)
                    lower = total_collateral - numerator * total_paid / denominator
                    assert bad_mass + 1e-12 >= lower
                    checks += 1

                for profile_count in range(1, 4):
                    class_count = 2 * profile_count
                    if total_collateral:
                        assert ceil(total_collateral / class_count) >= 1
                    checks += 1
    return checks


def main():
    intersections, secants = verify_geometry()
    states, rank_one, contexts = verify_toggle_profiles()
    routers = verify_routers()
    print(
        "RI rank-one active profile: verified "
        f"{intersections} conic triples, {secants} secants, "
        f"{states} toggle states, {rank_one} rank-one triples, "
        f"{contexts} context pairs, and {routers} routers"
    )


if __name__ == "__main__":
    main()
