#!/usr/bin/env python3
"""Verify OP2g canonical nogood subsumption and unit propagation."""

from __future__ import annotations

from itertools import combinations, product

Check = tuple[tuple[int, int], ...]
Domains = tuple[frozenset[int], ...]


def solutions(domains: Domains, checks: tuple[Check, ...]) -> set[tuple[int, ...]]:
    if any(not domain for domain in domains):
        return set()
    return {
        assignment
        for assignment in product(*(sorted(domain) for domain in domains))
        if all(
            any(assignment[variable] != label for variable, label in check)
            for check in checks
        )
    }


def reduce_instance(
    input_domains: Domains,
    input_checks: tuple[Check, ...],
) -> tuple[Domains, tuple[Check, ...]] | None:
    domains = [set(domain) for domain in input_domains]
    checks = set(input_checks)

    while True:
        if any(not domain for domain in domains):
            return None

        normalized: set[Check] = set()
        for check in checks:
            if any(label not in domains[variable] for variable, label in check):
                continue
            residual = tuple(
                (variable, label)
                for variable, label in check
                if domains[variable] != {label}
            )
            if not residual:
                return None
            normalized.add(residual)

        minimal = {
            check
            for check in normalized
            if not any(
                other != check and set(other).issubset(check)
                for other in normalized
            )
        }
        units = {check for check in minimal if len(check) == 1}
        if not units:
            return (
                tuple(frozenset(domain) for domain in domains),
                tuple(sorted(minimal)),
            )

        for ((variable, label),) in units:
            domains[variable].discard(label)
        checks = minimal - units


def possible_checks(variable_count: int = 3) -> tuple[Check, ...]:
    result: list[Check] = []
    for arity in range(1, variable_count + 1):
        for scope in combinations(range(variable_count), arity):
            for labels in product(range(2), repeat=arity):
                result.append(tuple(zip(scope, labels)))
    return tuple(result)


def verify() -> None:
    checks = possible_checks()
    domain_options = (
        frozenset({0}),
        frozenset({1}),
        frozenset({0, 1}),
    )
    for domains in product(domain_options, repeat=3):
        for family_size in range(4):
            for family in combinations(checks, family_size):
                original = solutions(domains, family)
                reduced = reduce_instance(domains, family)
                if reduced is None:
                    assert not original
                    continue

                reduced_domains, reduced_checks = reduced
                assert solutions(reduced_domains, reduced_checks) == original
                assert all(len(check) >= 2 for check in reduced_checks)
                assert all(
                    label in reduced_domains[variable]
                    and len(reduced_domains[variable]) >= 2
                    for check in reduced_checks
                    for variable, label in check
                )
                assert not any(
                    set(left).issubset(right)
                    for index, left in enumerate(reduced_checks)
                    for other_index, right in enumerate(reduced_checks)
                    if index != other_index
                )

    duplicate = (((0, 0), (1, 1)),) * 2
    reduced = reduce_instance(
        (frozenset({0, 1}),) * 3,
        duplicate,
    )
    assert reduced is not None
    assert len(reduced[1]) == 1


def main() -> None:
    verify()
    print("phase-core preprocessing: exhaustive binary regressions passed")


if __name__ == "__main__":
    main()
