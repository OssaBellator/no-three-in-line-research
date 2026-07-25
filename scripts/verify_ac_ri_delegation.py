#!/usr/bin/env python3
"""Exhaust AC3at--AC3ax scale, coset, completion, and loss checks."""

from fractions import Fraction
from itertools import combinations, permutations, product


def verify_scale_router(max_records=5, max_scales=3):
    partition_checks = 0
    scale_checks = 0

    for record_count in range(1, max_records + 1):
        for states in product(range(-1, max_scales), repeat=record_count):
            for weights in product(range(3), repeat=record_count):
                total = sum(weights)
                if total == 0:
                    continue
                mismatch = sum(
                    weight
                    for state, weight in zip(states, weights, strict=True)
                    if state == -1
                )
                coherent = total - mismatch
                assert 2 * mismatch >= total or 2 * coherent >= total
                partition_checks += 1

                if 2 * mismatch >= total:
                    continue

                classes = {}
                for state, weight in zip(states, weights, strict=True):
                    if state >= 0 and weight:
                        classes[state] = classes.get(state, 0) + weight
                assert sum(classes.values()) == coherent
                assert classes
                class_count = len(classes)
                heaviest = max(classes.values())
                assert heaviest * class_count >= coherent

                for bound in range(1, max_scales + 1):
                    if class_count <= bound:
                        assert 2 * heaviest * bound > total
                    else:
                        assert class_count > bound

                for cap in range(1, 5):
                    if heaviest <= cap:
                        assert class_count * cap >= coherent
                scale_checks += 1

    return partition_checks, scale_checks


def prime_factors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime):
    phi = prime - 1
    factors = prime_factors(phi)
    for candidate in range(2, prime):
        if all(pow(candidate, phi // factor, prime) != 1 for factor in factors):
            return candidate
    raise AssertionError("primitive root not found")


def divisors(value):
    return [divisor for divisor in range(1, value + 1) if value % divisor == 0]


def subgroup(prime, order):
    generator = primitive_root(prime)
    step = (prime - 1) // order
    return {pow(generator, step * index, prime) for index in range(order)}


def coset(scalar, group, prime):
    return frozenset((scalar * element) % prime for element in group)


def multiply_sets(left, right, prime):
    return frozenset((x * y) % prime for x in left for y in right)


def quotient_cosets(prime, group):
    seen = set()
    result = []
    for scalar in range(1, prime):
        current = coset(scalar, group, prime)
        if current not in seen:
            seen.add(current)
            result.append(current)
    return result


def verify_physical_cosets(primes=(5, 7, 11, 13, 17)):
    identity_checks = 0
    block_checks = 0

    for prime in primes:
        for order in divisors(prime - 1):
            group = subgroup(prime, order)
            classes = quotient_cosets(prime, group)
            for source in classes:
                for image in classes:
                    for scale in classes:
                        source_scale = multiply_sets(source, scale, prime)
                        image_scale = multiply_sets(image, scale, prime)
                        source_rep = next(iter(source))
                        image_rep = next(iter(image))
                        scale_rep = next(iter(scale))
                        assert source_scale == coset(
                            source_rep * scale_rep, group, prime
                        )
                        assert image_scale == coset(
                            image_rep * scale_rep, group, prime
                        )
                        assert len(source_scale) == order
                        identity_checks += 1

            for count in range(1, min(4, len(classes)) + 1):
                for selected in combinations(classes, count):
                    for scale in classes:
                        physical = [multiply_sets(item, scale, prime) for item in selected]
                        assert len(set(physical)) == count
                        block = set().union(*physical)
                        assert len(block) == count * order
                        for a in range(1, prime):
                            rows = {(a * pow(x, -1, prime)) % prime for x in block}
                            assert len(rows) == len(block)
                            block_checks += 1

    return identity_checks, block_checks


def inverse_permutation(mapping):
    inverse = [None] * len(mapping)
    for column, row in enumerate(mapping):
        inverse[row] = column
    return inverse


def completion_components(current, target, selected):
    selected = set(selected)
    inverse_current = inverse_permutation(current)
    successor = {x: inverse_current[target[x]] for x in selected}
    indegree = {x: 0 for x in selected}
    for x, y in successor.items():
        if y in selected:
            indegree[y] += 1

    paths = []
    cycles = []
    used = set()

    for start in sorted(x for x in selected if indegree[x] == 0):
        path = []
        vertex = start
        while vertex in selected and vertex not in used:
            used.add(vertex)
            path.append(vertex)
            vertex = successor[vertex]
        assert vertex not in selected
        paths.append((path, vertex))

    for start in sorted(selected - used):
        cycle = []
        vertex = start
        while vertex not in used:
            used.add(vertex)
            cycle.append(vertex)
            vertex = successor[vertex]
        assert vertex == start
        cycles.append(cycle)

    assert used == selected
    return cycles, paths, successor


def verify_completion_debt(maximum_n=5):
    component_checks = 0
    weighted_checks = 0

    for n in range(1, maximum_n + 1):
        all_permutations = list(permutations(range(n)))
        for current in all_permutations:
            for target in all_permutations:
                for mask in range(1, 1 << n):
                    selected = [x for x in range(n) if mask & (1 << x)]
                    cycles, paths, successor = completion_components(
                        current, target, selected
                    )

                    covered = [x for cycle in cycles for x in cycle]
                    covered += [x for path, _ in paths for x in path]
                    assert sorted(covered) == sorted(selected)
                    outside = [outside for _, outside in paths]
                    assert len(outside) == len(set(outside))

                    for cycle in cycles:
                        assert {target[x] for x in cycle} == {
                            current[x] for x in cycle
                        }
                        for x in cycle:
                            assert successor[x] in cycle

                    for path, outside_column in paths:
                        assert outside_column not in selected
                        for left, right in zip(path, path[1:], strict=False):
                            assert target[left] == current[right]
                        assert target[path[-1]] == current[outside_column]
                        closed_rows = {target[x] for x in path}
                        closed_rows.add(current[path[0]])
                        current_rows = {current[x] for x in path}
                        current_rows.add(current[outside_column])
                        assert closed_rows == current_rows

                    weights = {x: 1 + ((x + target[x]) % 3) for x in selected}
                    total = sum(weights.values())
                    cycle_weight = sum(
                        weights[x] for cycle in cycles for x in cycle
                    )
                    if 2 * cycle_weight < total:
                        assert paths
                        path_weights = [
                            sum(weights[x] for x in path) for path, _ in paths
                        ]
                        heaviest = max(path_weights)
                        assert 2 * len(paths) * heaviest > total
                        atom_cap = max(weights.values())
                        heavy_path = paths[path_weights.index(heaviest)][0]
                        assert 2 * len(paths) * atom_cap * len(heavy_path) > total
                    component_checks += 1
                    weighted_checks += 1

    return component_checks, weighted_checks


def verify_blocker_occupancy(maximum_n=5):
    occupancy_checks = 0

    for n in range(2, maximum_n + 1):
        all_permutations = list(permutations(range(n)))
        for target in all_permutations:
            for blocker in all_permutations:
                blocked = [column for column in range(n) if target[column] == blocker[column]]
                count = len(blocked)

                if count == 0:
                    updated = blocker
                elif count == 1:
                    c0 = blocked[0]
                    c1 = next(column for column in range(n) if column != c0)
                    updated = list(blocker)
                    updated[c0], updated[c1] = blocker[c1], blocker[c0]
                    updated = tuple(updated)
                else:
                    updated = list(blocker)
                    rows = [blocker[column] for column in blocked]
                    rotated = rows[1:] + rows[:1]
                    for column, row in zip(blocked, rotated, strict=True):
                        updated[column] = row
                    updated = tuple(updated)

                assert sorted(updated) == list(range(n))
                assert all(updated[column] != target[column] for column in range(n))
                occupancy_checks += 1

    return occupancy_checks


def verify_profile_and_composition(maximum_weight=48):
    profile_checks = 0
    composition_checks = 0

    for class_count in range(1, 8):
        for weights in product(range(4), repeat=class_count):
            total = sum(weights)
            if total:
                assert max(weights) * class_count >= total
                profile_checks += 1

    for total in range(1, maximum_weight + 1):
        for roles in range(1, 5):
            for multiplicity in range(1, 5):
                for scales in range(1, 5):
                    for profiles in range(1, 5):
                        role_weight = Fraction(total, 2 * roles * multiplicity)
                        coherent_weight = role_weight / 2
                        scale_weight = coherent_weight / scales
                        profile_weight = scale_weight / profiles
                        expected = Fraction(
                            total,
                            4 * roles * multiplicity * scales * profiles,
                        )
                        assert profile_weight == expected
                        composition_checks += 1

    return profile_checks, composition_checks


def main():
    partitions, scales = verify_scale_router()
    cosets, blocks = verify_physical_cosets()
    components, weighted = verify_completion_debt()
    occupancy = verify_blocker_occupancy()
    profiles, composition = verify_profile_and_composition()
    print(
        "AC RI delegation: verified "
        f"{partitions} coherence partitions, {scales} scale routers, "
        f"{cosets} coset identities, {blocks} physical blocks, "
        f"{components} completion decompositions, {weighted} weighted routers, "
        f"{occupancy} blocker occupancy states, {profiles} profile routers, "
        f"and {composition} quantitative compositions"
    )


if __name__ == "__main__":
    main()
