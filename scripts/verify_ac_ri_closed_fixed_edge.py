#!/usr/bin/env python3
"""Verify AC3bf--AC3bj on exhaustive small completion and cyclic I6 models."""

from itertools import combinations, permutations, product
from math import factorial


def inverse_permutation(perm):
    inverse = [0] * len(perm)
    for index, value in enumerate(perm):
        inverse[value] = index
    return tuple(inverse)


def decompose_completion(current, target, selected):
    inverse = inverse_permutation(current)
    sigma = {x: inverse[target[x]] for x in selected}
    unseen = set(selected)
    cycles = []
    paths = []

    while unseen:
        start = min(unseen)
        order = []
        position = {}
        x = start
        while x in selected and x not in position:
            position[x] = len(order)
            order.append(x)
            unseen.discard(x)
            x = sigma[x]

        if x in position:
            cut = position[x]
            assert cut == 0
            cycles.append(tuple(order))
        else:
            assert x not in selected
            paths.append((tuple(order), x))

    return sigma, cycles, paths


def closed_target(current, target, selected):
    sigma, cycles, paths = decompose_completion(current, target, selected)
    mapping = {x: target[x] for x in selected}
    outside = set()
    for path, endpoint in paths:
        mapping[endpoint] = current[path[0]]
        outside.add(endpoint)
    return sigma, cycles, paths, outside, mapping


def verify_fixed_roots_and_closure(maximum_n=6):
    fixed_checks = 0
    closure_checks = 0
    lifted_checks = 0

    for n in range(2, maximum_n + 1):
        all_perms = list(permutations(range(n)))
        # Full enumeration through n=5; a structured sample at n=6.
        if n == maximum_n:
            all_perms = all_perms[:40]
        for current in all_perms:
            inverse = inverse_permutation(current)
            for target in all_perms:
                if n == maximum_n and target not in all_perms[:40]:
                    continue
                for mask in range(1, 1 << n):
                    selected = {x for x in range(n) if mask & (1 << x)}
                    sigma, cycles, paths, outside, mapping = closed_target(
                        current, target, selected
                    )

                    for x in selected:
                        if current[x] == target[x]:
                            assert sigma[x] == x
                            fixed_checks += 1

                    columns = selected | outside
                    assert set(mapping) == columns
                    assert len(set(mapping.values())) == len(mapping)
                    assert {mapping[x] for x in columns} == {
                        current[x] for x in columns
                    }
                    closure_checks += 1

                    # Any permutation of the target rows on X lifts through
                    # the same closure. This contains every I6 state as a subset.
                    target_rows = [target[x] for x in sorted(selected)]
                    for row_order in list(permutations(target_rows))[:24]:
                        lifted = dict(mapping)
                        for x, row in zip(sorted(selected), row_order, strict=True):
                            lifted[x] = row
                        assert set(lifted) == columns
                        assert len(set(lifted.values())) == len(lifted)
                        assert {lifted[x] for x in columns} == {
                            current[x] for x in columns
                        }
                        lifted_checks += 1

    return fixed_checks, closure_checks, lifted_checks


def subgroup_elements(group_order, subgroup_order):
    assert group_order % subgroup_order == 0
    step = group_order // subgroup_order
    return tuple((step * j) % group_order for j in range(subgroup_order))


def i6_states(group_order, subgroup_order, representatives):
    subgroup = subgroup_elements(group_order, subgroup_order)
    states = []
    m = len(representatives)
    for perm in permutations(range(m)):
        for shifts in product(subgroup, repeat=m):
            mapping = {}
            for alpha, source_rep in enumerate(representatives):
                target_rep = representatives[perm[alpha]]
                shift = shifts[alpha]
                for g in subgroup:
                    column = (source_rep + g) % group_order
                    row = (-target_rep - shift - g) % group_order
                    mapping[column] = row
            assert len(mapping) == m * subgroup_order
            states.append((perm, shifts, mapping))
    return subgroup, states


def coset_index(value, quotient_index):
    return value % quotient_index


def verify_i6(maximum_group_order=12):
    state_checks = 0
    survival_checks = 0
    cylinder_checks = 0

    for group_order in range(4, maximum_group_order + 1):
        for subgroup_order in range(2, group_order + 1):
            if group_order % subgroup_order:
                continue
            quotient_index = group_order // subgroup_order
            if quotient_index < 1:
                continue
            max_m = min(4, quotient_index)
            for m in range(1, max_m + 1):
                representatives = tuple(range(m))
                subgroup, states = i6_states(
                    group_order, subgroup_order, representatives
                )
                columns = {
                    (rep + g) % group_order
                    for rep in representatives
                    for g in subgroup
                }
                target_rows = {(-x) % group_order for x in columns}
                for _, _, mapping in states:
                    assert set(mapping) == columns
                    assert set(mapping.values()) == target_rows
                    assert len(set(mapping.values())) == len(mapping)
                    state_checks += 1

                total_states = len(states)
                expected_single = total_states // (m * subgroup_order)
                for alpha, rep in enumerate(representatives):
                    for g in subgroup:
                        column = (rep + g) % group_order
                        current_row = (-column) % group_order
                        count = sum(
                            mapping[column] == current_row
                            for _, _, mapping in states
                        )
                        assert count == expected_single
                        survival_checks += 1

                # Prescribe one cell in each of r distinct source cosets from
                # a concrete base state and count all states containing it.
                sample_states = states[: min(8, len(states))]
                for _, _, base_mapping in sample_states:
                    for rank in range(1, min(3, m) + 1):
                        for source_indices in combinations(range(m), rank):
                            prescribed = []
                            target_cosets = set()
                            for alpha in source_indices:
                                rep = representatives[alpha]
                                g = subgroup[(alpha + rank) % subgroup_order]
                                column = (rep + g) % group_order
                                row = base_mapping[column]
                                prescribed.append((column, row))
                                target_cosets.add(coset_index((-row) % group_order, quotient_index))
                            if len(target_cosets) != rank:
                                continue
                            count = sum(
                                all(mapping[column] == row for column, row in prescribed)
                                for _, _, mapping in states
                            )
                            expected = (
                                factorial(m - rank)
                                * subgroup_order ** (m - rank)
                            )
                            assert count == expected
                            cylinder_checks += 1

    return state_checks, survival_checks, cylinder_checks


def repaired_blocker(active, blocker):
    intersections = [
        column
        for column in range(len(active))
        if active[column] == blocker[column]
    ]
    t = len(intersections)
    if t == 0:
        return blocker, "zero"
    if t == 1:
        c0 = intersections[0]
        c1 = next(column for column in range(len(active)) if column != c0)
        repaired = list(blocker)
        repaired[c0], repaired[c1] = blocker[c1], blocker[c0]
        return tuple(repaired), "singleton"

    repaired = list(blocker)
    rows = [blocker[column] for column in intersections]
    rotated = rows[1:] + rows[:1]
    for column, row in zip(intersections, rotated, strict=True):
        repaired[column] = row
    return tuple(repaired), "multiple"


def verify_blocker_repairs(maximum_n=6):
    checks = {"zero": 0, "singleton": 0, "multiple": 0}
    for n in range(2, maximum_n + 1):
        perms = list(permutations(range(n)))
        if n == maximum_n:
            perms = perms[:80]
        for active in perms:
            for blocker in perms:
                repaired, kind = repaired_blocker(active, blocker)
                assert sorted(repaired) == list(range(n))
                assert all(repaired[c] != active[c] for c in range(n))
                checks[kind] += 1
    return checks


def verify_failure_router(maximum=16):
    checks = 0
    for gain in range(1, maximum + 1):
        for fixed in range(gain):
            residual = gain - fixed
            for terms in product(range(residual + 1), repeat=4):
                if sum(terms) < residual:
                    continue
                assert max(terms) * 4 >= residual
                checks += 1
    return checks


def main():
    fixed, closure, lifted = verify_fixed_roots_and_closure()
    states, survival, cylinders = verify_i6()
    blocker = verify_blocker_repairs()
    routers = verify_failure_router()
    print(
        "AC RI closed fixed edge: verified "
        f"{fixed} fixed roots, {closure} closure systems, "
        f"{lifted} lifted target states, {states} I6 states, "
        f"{survival} single-cell survival counts, "
        f"{cylinders} distinct-coset cylinders, "
        f"{sum(blocker.values())} blocker repairs "
        f"({blocker['zero']}/{blocker['singleton']}/{blocker['multiple']}), "
        f"and {routers} failed-bank routers"
    )


if __name__ == "__main__":
    main()
