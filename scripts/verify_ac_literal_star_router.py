#!/usr/bin/env python3
"""Verify AC3ad--AC3af current-context literal-star routing."""

from __future__ import annotations

from itertools import combinations, product


Literal = tuple[int, int]
Check = tuple[Literal, ...]
Assignment = tuple[int, ...]
Scope = frozenset[int]


def check_scope(check: Check) -> Scope:
    return frozenset(variable for variable, _ in check)


def check_label(check: Check, variable: int) -> int:
    return next(label for candidate, label in check if candidate == variable)


def violated(check: Check, assignment: Assignment) -> bool:
    return all(assignment[variable] == label for variable, label in check)


def potential(family, weights, assignment):
    return sum(
        weight
        for check, weight in zip(family, weights)
        if violated(check, assignment)
    )


def activated_bucket(family, assignment, variable, target):
    return tuple(
        index
        for index, check in enumerate(family)
        if variable in check_scope(check)
        and check_label(check, variable) == target
        and all(
            candidate == variable or assignment[candidate] == label
            for candidate, label in check
        )
    )


def replace(assignment, variable, value):
    result = list(assignment)
    result[variable] = value
    return tuple(result)


def effective_residual(check, variable, sizes):
    return frozenset(
        candidate
        for candidate in check_scope(check) - {variable}
        if sizes[candidate] >= 2
    )


def disjoint(family):
    return all(not (left & right) for left, right in combinations(family, 2))


def maximal_matching(family):
    matching = []
    occupied = set()
    for scope in sorted(family, key=lambda item: (len(item), tuple(item))):
        if occupied.isdisjoint(scope):
            matching.append(scope)
            occupied.update(scope)
    return tuple(matching)


def hits_all(transversal, family):
    return all(transversal & scope for scope in family)


def matching_number(family):
    return max(
        (
            len(candidate)
            for mask in range(1 << len(family))
            if disjoint(candidate := tuple(
                scope
                for index, scope in enumerate(family)
                if mask & (1 << index)
            ))
        ),
        default=0,
    )


def transversal_number(variable_count, family):
    for size in range(variable_count + 1):
        for candidate in combinations(range(variable_count), size):
            if hits_all(set(candidate), family):
                return size
    raise AssertionError("full auxiliary set must hit every nonempty scope")


def canonical_checks(sizes):
    checks = []
    for rank in (1, 2, 3):
        if rank > len(sizes):
            continue
        for scope in combinations(range(len(sizes)), rank):
            for labels in product(*(range(sizes[v]) for v in scope)):
                checks.append(tuple(zip(scope, labels)))
    return tuple(checks)


def family_bank(universe):
    families = [(), universe]
    for modulus in range(2, 8):
        for residue in range(modulus):
            families.append(tuple(
                check
                for index, check in enumerate(universe)
                if (index * index + 5 * index + 3) % modulus == residue
            ))
    return tuple(families)


def verify_residual_hypergraphs():
    checked = 0
    for variable_count in range(1, 5):
        universe = tuple(
            frozenset((variable,))
            for variable in range(variable_count)
        ) + tuple(
            frozenset(pair)
            for pair in combinations(range(variable_count), 2)
        )
        for mask in range(1 << len(universe)):
            family = tuple(
                scope
                for index, scope in enumerate(universe)
                if mask & (1 << index)
            )
            matching = maximal_matching(family)
            transversal = set().union(*matching) if matching else set()
            assert disjoint(matching)
            assert hits_all(transversal, family)
            assert len(transversal) <= 2 * len(matching)
            maximum = matching_number(family)
            minimum = transversal_number(variable_count, family)
            assert maximum <= minimum <= 2 * maximum

            weights = tuple(
                1 + (7 * index + 3 * len(scope)) % 11
                for index, scope in enumerate(family)
            )
            loads = {
                variable: sum(
                    weight
                    for scope, weight in zip(family, weights)
                    if variable in scope
                )
                for variable in range(variable_count)
            }
            total = sum(weights)
            cover_load = sum(loads[x] for x in transversal)
            assert total <= cover_load
            maximum_load = max(loads.values(), default=0)
            assert cover_load <= 2 * len(matching) * maximum_load
            for threshold in range(1, 13):
                if maximum_load > threshold:
                    assert any(load > threshold for load in loads.values())
                elif total:
                    assert len(matching) >= (total + 2 * threshold - 1) // (
                        2 * threshold
                    )
            checked += 1
    return checked


def verify_phase_buckets():
    checked = 0
    paid_consequences = 0
    for sizes in ((3, 2, 2), (2, 1, 2)):
        universe = canonical_checks(sizes)
        assignments = tuple(product(*(range(size) for size in sizes)))
        for family_id, family in enumerate(family_bank(universe)):
            weights = tuple(
                1 + (index + 3 * family_id) % 7
                for index in range(len(family))
            )
            hard = tuple(
                check
                for index, check in enumerate(family)
                if (index + family_id) % 4 == 0
            )
            for assignment in assignments:
                current = potential(family, weights, assignment)
                current_hard = tuple(
                    check for check in hard if not violated(check, assignment)
                )
                for variable, size in enumerate(sizes):
                    destroyed = sum(
                        weight
                        for check, weight in zip(family, weights)
                        if variable in check_scope(check)
                        and violated(check, assignment)
                    )
                    creation_total = 0
                    for target in range(size):
                        if target == assignment[variable]:
                            continue
                        bucket = activated_bucket(
                            family, assignment, variable, target
                        )
                        created = sum(weights[index] for index in bucket)
                        creation_total += created
                        changed = replace(assignment, variable, target)
                        assert (
                            potential(family, weights, changed) - current
                            == created - destroyed
                        )
                        hard_bucket = activated_bucket(
                            current_hard, assignment, variable, target
                        )
                        assert bool(hard_bucket) == any(
                            violated(check, changed)
                            for check in current_hard
                        )

                        raw_residuals = tuple(
                            check_scope(family[index]) - {variable}
                            for index in bucket
                        )
                        residuals = tuple(
                            effective_residual(
                                family[index], variable, sizes
                            )
                            for index in bucket
                        )
                        units = tuple(
                            scope for scope in residuals if not scope
                        )
                        positive = tuple(
                            scope for scope in residuals if scope
                        )
                        assert all(len(scope) <= 2 for scope in positive)
                        assert all(
                            check_label(family[index], residual_variable)
                            == assignment[residual_variable]
                            for index, residual in zip(
                                bucket, raw_residuals
                            )
                            for residual_variable in residual
                        )
                        matching = maximal_matching(positive)
                        transversal = (
                            set().union(*matching) if matching else set()
                        )
                        assert hits_all(transversal, positive)
                        repaired = list(changed)
                        for residual_variable in transversal:
                            assert sizes[residual_variable] >= 2
                            repaired[residual_variable] = (
                                assignment[residual_variable] + 1
                            ) % sizes[residual_variable]
                        assert all(
                            not violated(family[index], tuple(repaired))
                            for index, residual in zip(bucket, residuals)
                            if residual
                        )
                        assert len(units) == sum(
                            not residual for residual in residuals
                        )

                        if not hard_bucket and created >= destroyed:
                            unit_weight = sum(
                                weights[index]
                                for index, residual in zip(
                                    bucket, residuals
                                )
                                if not residual
                            )
                            positive_weight = created - unit_weight
                            assert (
                                unit_weight + positive_weight >= destroyed
                            )
                            residual_variables = (
                                set().union(*positive)
                                if positive else set()
                            )
                            loads = {
                                residual_variable: sum(
                                    weights[index]
                                    for index, residual in zip(
                                        bucket, residuals
                                    )
                                    if residual_variable in residual
                                )
                                for residual_variable
                                in residual_variables
                            }
                            maximum_load = max(
                                loads.values(), default=0
                            )
                            if 2 * unit_weight < destroyed:
                                assert 2 * positive_weight > destroyed
                                for threshold in range(1, 13):
                                    if maximum_load <= threshold:
                                        assert len(matching) >= (
                                            destroyed
                                            + 4 * threshold
                                            - 1
                                        ) // (4 * threshold)
                            paid_consequences += 1
                        checked += 1

                    targets = size - 1
                    if targets:
                        created_again = tuple(
                            sum(
                                weights[index]
                                for index in activated_bucket(
                                    family,
                                    assignment,
                                    variable,
                                    target,
                                )
                            )
                            for target in range(size)
                            if target != assignment[variable]
                        )
                        assert sum(created_again) == creation_total
                        assert min(created_again) * targets <= creation_total
    return checked, paid_consequences


def main():
    residual_count = verify_residual_hypergraphs()
    bucket_count, paid_count = verify_phase_buckets()
    print(
        "AC literal-star routing verified:",
        f"{residual_count} residual hypergraphs,",
        f"{bucket_count} phase buckets,",
        f"{paid_count} hard-safe paid consequences",
    )


if __name__ == "__main__":
    main()
