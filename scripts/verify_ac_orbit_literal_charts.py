#!/usr/bin/env python3
"""Verify AC3aa--AC3ac canonical orbit-literal charts."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import prod


Assignment = tuple[int, ...]


@dataclass(frozen=True)
class Check:
    scope: tuple[int, ...]
    values: tuple[int, ...]


def assignments(sizes: tuple[int, ...]) -> tuple[Assignment, ...]:
    return tuple(product(*(range(size) for size in sizes)))


def canonical_checks(sizes: tuple[int, ...]) -> tuple[Check, ...]:
    checks: list[Check] = []
    variables = range(len(sizes))
    for rank in range(1, min(3, len(sizes)) + 1):
        for scope in combinations(variables, rank):
            for values in product(*(range(sizes[index]) for index in scope)):
                checks.append(Check(scope, values))
    return tuple(checks)


def violated(check: Check, assignment: Assignment) -> bool:
    return all(
        assignment[variable] == value
        for variable, value in zip(check.scope, check.values)
    )


def violation_vector(
    checks: tuple[Check, ...],
    assignment: Assignment,
) -> tuple[bool, ...]:
    return tuple(violated(check, assignment) for check in checks)


def literal_support(
    sizes: tuple[int, ...],
    checks: tuple[Check, ...],
) -> tuple[frozenset[int], ...]:
    support = [set() for _ in sizes]
    for check in checks:
        for variable, value in zip(check.scope, check.values):
            support[variable].add(value)
    return tuple(frozenset(values) for values in support)


def chart_maps(
    sizes: tuple[int, ...],
    current: Assignment,
    singleton_support: tuple[frozenset[int], ...],
    residual_name: str = "other",
) -> tuple[dict[int, tuple[str, int | None]], ...]:
    maps: list[dict[int, tuple[str, int | None]]] = []
    for variable, size in enumerate(sizes):
        coordinate: dict[int, tuple[str, int | None]] = {}
        for value in range(size):
            if value == current[variable]:
                coordinate[value] = ("current", None)
            elif value in singleton_support[variable]:
                coordinate[value] = ("literal", value)
            else:
                coordinate[value] = (residual_name, None)
        maps.append(coordinate)
    return tuple(maps)


def chart_code(
    assignment: Assignment,
    maps: tuple[dict[int, tuple[str, int | None]], ...],
) -> tuple[tuple[str, int | None], ...]:
    return tuple(
        maps[variable][value]
        for variable, value in enumerate(assignment)
    )


def contexts(
    sizes: tuple[int, ...],
    variable: int,
) -> tuple[tuple[int, ...], ...]:
    other_sizes = sizes[:variable] + sizes[variable + 1 :]
    return tuple(product(*(range(size) for size in other_sizes)))


def insert(
    context: tuple[int, ...],
    variable: int,
    value: int,
) -> Assignment:
    return context[:variable] + (value,) + context[variable:]


def observational_class_count(
    sizes: tuple[int, ...],
    current: Assignment,
    checks: tuple[Check, ...],
    variable: int,
) -> int:
    signatures: set[tuple[tuple[bool, ...], ...]] = set()
    for value in range(sizes[variable]):
        if value == current[variable]:
            continue
        signatures.add(
            tuple(
                violation_vector(
                    checks,
                    insert(context, variable, value),
                )
                for context in contexts(sizes, variable)
            )
        )
    return 1 + len(signatures)


def check_families(
    checks: tuple[Check, ...],
) -> tuple[tuple[Check, ...], ...]:
    if len(checks) <= 12:
        return tuple(
            tuple(
                check
                for index, check in enumerate(checks)
                if mask & (1 << index)
            )
            for mask in range(1 << len(checks))
        )

    families = [(), checks]
    for modulus in range(2, 8):
        for residue in range(modulus):
            families.append(
                tuple(
                    check
                    for index, check in enumerate(checks)
                    if (index * index + 3 * index + 1) % modulus
                    == residue
                )
            )
    return tuple(families)


def verify_exact_literal_charts() -> None:
    for sizes in ((2,), (3,), (2, 2), (3, 2), (2, 2, 2)):
        current = tuple(0 for _ in sizes)
        universe = canonical_checks(sizes)
        for checks in check_families(universe):
            support = literal_support(sizes, checks)
            maps = chart_maps(sizes, current, support)
            behavior_by_code: dict[
                tuple[tuple[str, int | None], ...],
                tuple[bool, ...],
            ] = {}

            for assignment in assignments(sizes):
                code = chart_code(assignment, maps)
                behavior = violation_vector(checks, assignment)
                if code in behavior_by_code:
                    assert behavior_by_code[code] == behavior
                else:
                    behavior_by_code[code] = behavior

            label_counts = tuple(
                len(set(coordinate.values()))
                for coordinate in maps
            )
            assert all(
                label_counts[variable]
                <= len(support[variable] - {current[variable]}) + 2
                for variable in range(len(sizes))
            )
            assert len(behavior_by_code) == prod(label_counts)
            discharge_codes = {
                chart_code(assignment, maps)
                for assignment in assignments(sizes)
                if assignment != current
            }
            assert len(discharge_codes) == prod(label_counts) - 1

            for variable in range(len(sizes)):
                assert (
                    observational_class_count(
                        sizes,
                        current,
                        checks,
                        variable,
                    )
                    <= label_counts[variable]
                )


def soft_loads(
    sizes: tuple[int, ...],
    checks: tuple[Check, ...],
    weights: tuple[int, ...],
) -> tuple[dict[int, int], ...]:
    loads = [dict.fromkeys(range(size), 0) for size in sizes]
    for check, weight in zip(checks, weights):
        for variable, value in zip(check.scope, check.values):
            loads[variable][value] += weight
    return tuple(loads)


def potential(
    checks: tuple[Check, ...],
    weights: tuple[int, ...],
    assignment: Assignment,
) -> int:
    return sum(
        weight
        for check, weight in zip(checks, weights)
        if violated(check, assignment)
    )


def verify_mixed_chart_instance(
    sizes: tuple[int, ...],
    hard: tuple[Check, ...],
    soft: tuple[Check, ...],
    weights: tuple[int, ...],
    threshold: Fraction,
) -> None:
    current = tuple(0 for _ in sizes)
    hard_support = literal_support(sizes, hard)
    loads = soft_loads(sizes, soft, weights)
    singleton_support = tuple(
        frozenset(
            set(hard_support[variable])
            | {
                value
                for value, load in loads[variable].items()
                if Fraction(load) >= threshold
            }
        )
        for variable in range(len(sizes))
    )
    maps = chart_maps(
        sizes,
        current,
        singleton_support,
        residual_name="light",
    )

    all_assignments = assignments(sizes)
    for left, right in combinations(all_assignments, 2):
        if chart_code(left, maps) != chart_code(right, maps):
            continue
        assert violation_vector(hard, left) == violation_vector(hard, right)
        differing = sum(a != b for a, b in zip(left, right))
        assert differing > 0
        assert Fraction(
            abs(
                potential(soft, weights, left)
                - potential(soft, weights, right)
            )
        ) < 2 * differing * threshold

    for variable, size in enumerate(sizes):
        for left_value, right_value in combinations(range(size), 2):
            if maps[variable][left_value] != maps[variable][right_value]:
                continue
            assert maps[variable][left_value][0] == "light"
            assert Fraction(loads[variable][left_value]) < threshold
            assert Fraction(loads[variable][right_value]) < threshold
            for context in contexts(sizes, variable):
                left = insert(context, variable, left_value)
                right = insert(context, variable, right_value)
                difference = abs(
                    potential(soft, weights, left)
                    - potential(soft, weights, right)
                )
                literal_bound = (
                    loads[variable][left_value]
                    + loads[variable][right_value]
                )
                assert difference <= literal_bound
                assert Fraction(difference) < 2 * threshold
                assert (
                    violation_vector(hard, left)
                    == violation_vector(hard, right)
                )

    total_literal_load = sum(
        sum(coordinate.values())
        for coordinate in loads
    )
    weighted_rank = sum(
        len(check.scope) * weight
        for check, weight in zip(soft, weights)
    )
    assert total_literal_load == weighted_rank
    assert weighted_rank <= 3 * sum(weights)
    heavy_count = sum(
        Fraction(load) >= threshold
        for coordinate in loads
        for load in coordinate.values()
    )
    assert heavy_count * threshold <= total_literal_load


def verify_hard_heavy_light_charts() -> None:
    for sizes in ((3, 2), (3, 2, 2)):
        universe = canonical_checks(sizes)
        for seed in range(12):
            hard = tuple(
                check
                for index, check in enumerate(universe)
                if (index + 2 * seed) % 7 == 0
            )
            soft_with_indices = tuple(
                (index, check)
                for index, check in enumerate(universe)
                if (3 * index + seed) % 5 in (1, 2)
            )
            soft = tuple(check for _, check in soft_with_indices)
            weights = tuple(
                1 + (index + 3 * seed) % 5
                for index, _ in soft_with_indices
            )
            for threshold in (
                Fraction(1, 2),
                Fraction(2),
                Fraction(7, 2),
                Fraction(6),
                Fraction(25),
            ):
                verify_mixed_chart_instance(
                    sizes,
                    hard,
                    soft,
                    weights,
                    threshold,
                )


def multiplicative_order(value: int, prime: int) -> int:
    power = 1
    for order in range(1, prime):
        power = power * value % prime
        if power == 1:
            return order
    raise AssertionError("nonzero field element must have finite order")


def verify_o1_exact_phase_lower_bound() -> None:
    for prime in (3, 5, 7, 11, 13, 17, 19):
        for generator in range(1, prime):
            order = multiplicative_order(generator, prime)
            subgroup = tuple(
                pow(generator, exponent, prime)
                for exponent in range(order)
            )
            assert len(set(subgroup)) == order
            layer = 2 % prime or 1
            states: list[frozenset[tuple[int, int]]] = []
            channels: list[int] = []

            for phase in range(order):
                phase_scalar = pow(generator, phase, prime)
                channels.append(
                    layer * pow(phase_scalar, -1, prime) % prime
                )
                states.append(
                    frozenset(
                        (
                            x,
                            layer
                            * pow(phase_scalar * x % prime, -1, prime)
                            % prime,
                        )
                        for x in subgroup
                    )
                )

            assert len(set(channels)) == order
            assert all(len(state) == order for state in states)
            assert all(
                not (states[left] & states[right])
                for left, right in combinations(range(order), 2)
            )
            cells = frozenset().union(*states)
            assert len(cells) == order * order

            phase_of_cell = {
                cell: phase
                for phase, state in enumerate(states)
                for cell in state
            }
            assert len(phase_of_cell) == order * order
            for left, right in combinations(range(order), 2):
                witness = next(iter(states[left]))
                probes = tuple(
                    int(witness in state)
                    for state in states
                )
                assert probes[left] == 1
                assert probes[right] == 0

    # A canonical unary probe for every phase forces the full quotient.
    for size in range(1, 8):
        sizes = (size,)
        current = (0,)
        probes = tuple(Check((0,), (value,)) for value in range(size))
        assert (
            observational_class_count(
                sizes,
                current,
                probes,
                0,
            )
            == size
        )


def main() -> None:
    verify_exact_literal_charts()
    verify_hard_heavy_light_charts()
    verify_o1_exact_phase_lower_bound()
    print("AC canonical orbit-literal charts: verified")


if __name__ == "__main__":
    main()
