#!/usr/bin/env python3
"""Verify AC3aj--AC3ak cross-centre target routing."""

from __future__ import annotations

from itertools import combinations, product


Literal = tuple[int, int]
Check = tuple[Literal, ...]
Assignment = tuple[int, ...]
Scope = frozenset[int]


def maximal_matching(scopes: tuple[Scope, ...]) -> tuple[int, ...]:
    matching: list[int] = []
    occupied: set[int] = set()
    for index in sorted(
        range(len(scopes)),
        key=lambda item: (len(scopes[item]), tuple(scopes[item]), item),
    ):
        if scopes[index] and occupied.isdisjoint(scopes[index]):
            matching.append(index)
            occupied.update(scopes[index])
    return tuple(matching)


def ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def verify_unsafe_scopes(scopes: tuple[Scope | None, ...]) -> None:
    unsafe = tuple(scope for scope in scopes if scope is not None)
    units = tuple(scope for scope in unsafe if not scope)
    positive = tuple(scope for scope in unsafe if scope)
    matching_indices = maximal_matching(positive)
    matching = tuple(positive[index] for index in matching_indices)
    transversal = set().union(*matching) if matching else set()
    assert all(transversal & scope for scope in positive)
    assert len(transversal) <= 2 * len(matching)

    variables = set().union(*positive) if positive else set()
    degrees = {
        variable: sum(variable in scope for scope in positive)
        for variable in variables
    }
    positive_count = len(positive)
    cover_sum = sum(degrees[variable] for variable in transversal)
    assert positive_count <= cover_sum
    maximum_degree = max(degrees.values(), default=0)
    assert cover_sum <= 2 * len(matching) * maximum_degree

    for threshold in range(1, max(2, len(scopes) + 1)):
        if maximum_degree > threshold:
            assert any(
                degree > threshold for degree in degrees.values()
            )
        elif positive_count:
            assert len(matching) >= ceil_div(
                positive_count, 2 * threshold
            )
        else:
            assert len(units) == len(unsafe)

        if 2 * len(units) < len(unsafe) and maximum_degree <= threshold:
            assert len(matching) >= ceil_div(
                len(unsafe), 4 * threshold
            )


def verify_abstract_blockers() -> int:
    residual_variables = 3
    scope_options: tuple[Scope | None, ...] = (
        None,
        frozenset(),
        *(frozenset((variable,)) for variable in range(residual_variables)),
        *(
            frozenset(pair)
            for pair in combinations(range(residual_variables), 2)
        ),
    )
    checked = 0
    for target_count in range(1, 6):
        for scopes in product(scope_options, repeat=target_count):
            verify_unsafe_scopes(scopes)
            checked += 1
    return checked


def check_scope(check: Check) -> Scope:
    return frozenset(variable for variable, _ in check)


def check_label(check: Check, variable: int) -> int:
    return next(label for candidate, label in check if candidate == variable)


def violated(check: Check, assignment: Assignment) -> bool:
    return all(assignment[variable] == label for variable, label in check)


def canonical_checks(sizes: tuple[int, ...]) -> tuple[Check, ...]:
    checks: list[Check] = []
    for rank in (1, 2, 3):
        for scope in combinations(range(len(sizes)), rank):
            for labels in product(*(range(sizes[v]) for v in scope)):
                checks.append(tuple(zip(scope, labels)))
    return tuple(checks)


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
            candidate == variable or assignment[candidate] == label
            for candidate, label in check
        )
    )


def family_bank(universe: tuple[Check, ...]) -> tuple[tuple[Check, ...], ...]:
    families = [(), universe]
    for modulus in range(2, 11):
        for residue in range(modulus):
            families.append(tuple(
                check
                for index, check in enumerate(universe)
                if (index * index + 3 * index + 7) % modulus == residue
            ))
    return tuple(families)


def effective_residual(
    check: Check,
    variable: int,
    sizes: tuple[int, ...],
) -> Scope:
    return frozenset(
        candidate
        for candidate in check_scope(check) - {variable}
        if sizes[candidate] >= 2
    )


def verify_canonical_buckets() -> tuple[int, int]:
    sizes = (4, 2, 1)
    universe = canonical_checks(sizes)
    assignments = tuple(product(*(range(size) for size in sizes)))
    checked = 0
    paid = 0
    for family_id, family in enumerate(family_bank(universe)):
        weights = tuple(
            1 + (5 * index + 7 * family_id) % 13
            for index in range(len(family))
        )
        hard_pattern = tuple(
            check
            for index, check in enumerate(family)
            if (index + 2 * family_id) % 5 == 0
        )
        for assignment in assignments:
            hard = tuple(
                check
                for check in hard_pattern
                if not violated(check, assignment)
            )
            variable = 0
            destroyed = sum(
                weight
                for check, weight in zip(family, weights)
                if variable in check_scope(check)
                and violated(check, assignment)
            )
            safe_creations: list[int] = []
            selected: list[Scope | None] = []
            safe_bucket_sets: list[set[int]] = []
            for target in range(sizes[variable]):
                if target == assignment[variable]:
                    continue
                hard_bucket = activated_bucket(
                    hard, assignment, variable, target
                )
                soft_bucket = activated_bucket(
                    family, assignment, variable, target
                )
                if hard_bucket:
                    effective = tuple(
                        effective_residual(
                            hard[index], variable, sizes
                        )
                        for index in hard_bucket
                    )
                    if any(not scope for scope in effective):
                        selected.append(frozenset())
                    else:
                        assert effective
                        selected.append(effective[0])
                        assert all(
                            check_label(hard[index], residual_variable)
                            == assignment[residual_variable]
                            for index, scope in zip(hard_bucket, effective)
                            for residual_variable in scope
                        )
                    continue

                selected.append(None)
                creation = sum(weights[index] for index in soft_bucket)
                safe_creations.append(creation)
                safe_bucket_sets.append(set(soft_bucket))

            verify_unsafe_scopes(tuple(selected))
            assert all(
                left.isdisjoint(right)
                for left, right in combinations(safe_bucket_sets, 2)
            )
            if safe_creations and all(
                creation >= destroyed for creation in safe_creations
            ):
                assert sum(safe_creations) >= (
                    len(safe_creations) * destroyed
                )
                paid += 1
            checked += 1
    return checked, paid


def main() -> None:
    abstract = verify_abstract_blockers()
    canonical, paid = verify_canonical_buckets()
    print(
        "AC cross-centre routing verified:",
        f"{abstract} abstract target records,",
        f"{canonical} canonical states,",
        f"{paid} paid safe-target profiles",
    )


if __name__ == "__main__":
    main()
