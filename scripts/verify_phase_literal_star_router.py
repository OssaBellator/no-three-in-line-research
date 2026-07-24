#!/usr/bin/env python3
"""Verify OP2l--OP2m and OP3c activated phase-bucket routing."""

from __future__ import annotations

from itertools import combinations, product


Literal = tuple[int, int]
Check = tuple[Literal, ...]
Assignment = tuple[int, ...]
Scope = frozenset[int]


def assignments(sizes: tuple[int, ...]) -> tuple[Assignment, ...]:
    return tuple(product(*(range(size) for size in sizes)))


def check_scope(check: Check) -> Scope:
    return frozenset(variable for variable, _ in check)


def check_label(check: Check, variable: int) -> int:
    return next(
        label
        for candidate, label in check
        if candidate == variable
    )


def violated(check: Check, assignment: Assignment) -> bool:
    return all(
        assignment[variable] == label
        for variable, label in check
    )


def potential(
    family: tuple[Check, ...],
    weights: tuple[int, ...],
    assignment: Assignment,
) -> int:
    return sum(
        weight
        for check, weight in zip(family, weights)
        if violated(check, assignment)
    )


def disjoint(family: tuple[Scope, ...]) -> bool:
    return all(
        not (left & right)
        for left, right in combinations(family, 2)
    )


def maximal_matching(family: tuple[Scope, ...]) -> tuple[Scope, ...]:
    matching: list[Scope] = []
    occupied: set[int] = set()
    for scope in sorted(family, key=lambda item: (len(item), tuple(item))):
        if occupied.isdisjoint(scope):
            matching.append(scope)
            occupied.update(scope)
    return tuple(matching)


def matching_number(family: tuple[Scope, ...]) -> int:
    return max(
        (
            len(candidate)
            for mask in range(1 << len(family))
            if disjoint(
                candidate := tuple(
                    scope
                    for index, scope in enumerate(family)
                    if mask & (1 << index)
                )
            )
        ),
        default=0,
    )


def hits_all(transversal: set[int], family: tuple[Scope, ...]) -> bool:
    return all(transversal & scope for scope in family)


def transversal_number(
    variable_count: int,
    family: tuple[Scope, ...],
) -> int:
    variables = range(variable_count)
    for size in range(variable_count + 1):
        for candidate in combinations(variables, size):
            if hits_all(set(candidate), family):
                return size
    raise AssertionError("the full variable set must hit nonempty scopes")


def scope_antichain(family: tuple[Scope, ...]) -> bool:
    return all(
        not (left <= right or right <= left)
        for left, right in combinations(family, 2)
    )


def aligned_check(
    residual: Scope,
    center: int,
    target: int,
    reference: Assignment,
) -> Check:
    return tuple(
        sorted(
            ((center, target),)
            + tuple((variable, reference[variable]) for variable in residual)
        )
    )


def verify_residual_family(
    variable_count: int,
    family: tuple[Scope, ...],
) -> None:
    matching = maximal_matching(family)
    assert disjoint(matching)
    transversal = set().union(*matching) if matching else set()
    assert hits_all(transversal, family)
    assert len(transversal) <= 2 * len(matching)

    maximum = matching_number(family)
    minimum_cover = transversal_number(variable_count, family)
    assert maximum <= minimum_cover <= 2 * maximum

    for threshold in range(1, variable_count + 3):
        if len(matching) >= threshold:
            assert disjoint(matching[:threshold])
        else:
            assert len(transversal) <= 2 * (threshold - 1)

    center = variable_count
    sizes = tuple(3 for _ in range(variable_count + 1))
    reference = tuple(0 for _ in sizes)
    target = 1
    checks = tuple(
        aligned_check(scope, center, target, reference)
        for scope in family
    )
    repaired = list(reference)
    repaired[center] = target
    for variable in transversal:
        repaired[variable] = 1
    repaired_assignment = tuple(repaired)
    assert all(
        not violated(check, repaired_assignment)
        for check in checks
    )

    for mask in range(1 << variable_count):
        changed = {
            variable
            for variable in range(variable_count)
            if mask & (1 << variable)
        }
        candidate = list(reference)
        candidate[center] = target
        for variable in changed:
            candidate[variable] = 1
        satisfies = all(
            not violated(check, tuple(candidate))
            for check in checks
        )
        assert satisfies == hits_all(changed, family)

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
    cover_load = sum(loads[variable] for variable in transversal)
    assert total <= cover_load
    maximum_load = max(loads.values(), default=0)
    assert cover_load <= 2 * len(matching) * maximum_load

    if family:
        degrees = {
            variable: sum(variable in scope for scope in family)
            for variable in range(variable_count)
        }
        max_degree = max(degrees.values())
        assert len(matching) * 2 * max_degree >= len(family)


def verify_matching_transversal_router() -> None:
    for variable_count in range(1, 5):
        universe = tuple(
            (frozenset((variable,)) for variable in range(variable_count))
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
            if scope_antichain(family):
                verify_residual_family(variable_count, family)


def canonical_checks(
    sizes: tuple[int, ...],
) -> tuple[Check, ...]:
    checks: list[Check] = []
    for rank in (2, 3):
        if rank > len(sizes):
            continue
        for scope in combinations(range(len(sizes)), rank):
            for labels in product(*(range(sizes[v]) for v in scope)):
                checks.append(tuple(zip(scope, labels)))
    return tuple(checks)


def family_bank(universe: tuple[Check, ...]) -> tuple[tuple[Check, ...], ...]:
    families = [(), universe]
    for modulus in range(2, 8):
        for residue in range(modulus):
            families.append(
                tuple(
                    check
                    for index, check in enumerate(universe)
                    if (index * index + 5 * index + 3) % modulus
                    == residue
                )
            )
    return tuple(families)


def activated_bucket(
    family: tuple[Check, ...],
    assignment: Assignment,
    variable: int,
    target: int,
) -> tuple[int, ...]:
    return tuple(
        index
        for index, check in enumerate(family)
        if variable in check_scope(check)
        and check_label(check, variable) == target
        and all(
            candidate == variable
            or assignment[candidate] == label
            for candidate, label in check
        )
    )


def replace(
    assignment: Assignment,
    variable: int,
    value: int,
) -> Assignment:
    return (
        assignment[:variable]
        + (value,)
        + assignment[variable + 1 :]
    )


def verify_bucket_router(
    family: tuple[Check, ...],
    assignment: Assignment,
    variable: int,
    target: int,
    bucket: tuple[int, ...],
) -> None:
    residuals = tuple(
        check_scope(family[index]) - {variable}
        for index in bucket
    )
    assert all(1 <= len(scope) <= 2 for scope in residuals)
    assert all(
        check_label(family[index], residual_variable)
        == assignment[residual_variable]
        for index, residual in zip(bucket, residuals)
        for residual_variable in residual
    )

    matching = maximal_matching(residuals)
    transversal = set().union(*matching) if matching else set()
    assert hits_all(transversal, residuals)
    repaired = list(assignment)
    repaired[variable] = target
    for residual_variable in transversal:
        size = 3 if residual_variable == 0 else 2
        repaired[residual_variable] = (
            assignment[residual_variable] + 1
        ) % size
    assert all(
        not violated(family[index], tuple(repaired))
        for index in bucket
    )


def verify_phase_averaging() -> None:
    sizes = (3, 2, 2)
    universe = canonical_checks(sizes)
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

        for assignment in assignments(sizes):
            current_potential = potential(family, weights, assignment)
            for variable, size in enumerate(sizes):
                current = assignment[variable]
                destroyed = sum(
                    weight
                    for check, weight in zip(family, weights)
                    if variable in check_scope(check)
                    and violated(check, assignment)
                )
                creation_total = 0
                drifts: list[int] = []
                unsafe_targets: list[int] = []

                for target in range(size):
                    if target == current:
                        continue
                    bucket = activated_bucket(
                        family,
                        assignment,
                        variable,
                        target,
                    )
                    created = sum(weights[index] for index in bucket)
                    creation_total += created
                    changed = replace(
                        assignment,
                        variable,
                        target,
                    )
                    drift = (
                        potential(family, weights, changed)
                        - current_potential
                    )
                    assert drift == created - destroyed
                    drifts.append(drift)

                    brute_created = sum(
                        weight
                        for check, weight in zip(family, weights)
                        if not violated(check, assignment)
                        and violated(check, changed)
                    )
                    assert brute_created == created
                    verify_bucket_router(
                        family,
                        assignment,
                        variable,
                        target,
                        bucket,
                    )

                    current_hard = tuple(
                        check
                        for check in hard
                        if not violated(check, assignment)
                    )
                    hard_bucket = activated_bucket(
                        current_hard,
                        assignment,
                        variable,
                        target,
                    )
                    brute_unsafe = any(
                        violated(check, changed)
                        for check in current_hard
                    )
                    assert brute_unsafe == bool(hard_bucket)
                    if hard_bucket:
                        unsafe_targets.append(target)

                if size > 1:
                    created_buckets = tuple(
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
                        if target != current
                    )
                    assert sum(created_buckets) == creation_total
                    assert min(created_buckets) * (size - 1) <= (
                        creation_total
                    )
                    if (size - 1) * destroyed > creation_total:
                        assert min(drifts) < 0
                    if all(drift >= 0 for drift in drifts):
                        assert all(
                            created >= destroyed
                            for created in created_buckets
                        )
                        assert creation_total >= (size - 1) * destroyed

                    if len(unsafe_targets) == size - 1:
                        assert len(set(unsafe_targets)) == size - 1


def main() -> None:
    verify_matching_transversal_router()
    verify_phase_averaging()
    print("OP activated literal-star routing: verified")


if __name__ == "__main__":
    main()
