#!/usr/bin/env python3
"""Exact finite checks for AC3lz--AC3me."""

from __future__ import annotations

from itertools import combinations, product

Check = tuple[tuple[int, ...], tuple[int, ...]]
Context = tuple[int, ...]


def generate_checks(nvars: int, max_rank: int = 3) -> list[Check]:
    checks: list[Check] = []
    for rank in range(1, max_rank + 1):
        for scope in combinations(range(nvars), rank):
            for values in product((0, 1), repeat=rank):
                if all(value == 0 for value in values):
                    continue
                checks.append((scope, values))
    return checks


def violates(check: Check, context: Context) -> bool:
    scope, values = check
    return tuple(context[index] for index in scope) == values


def activated(check: Check, context: Context, target: int) -> bool:
    scope, values = check
    if context[target] != 0 or target not in scope:
        return False
    target_position = scope.index(target)
    if values[target_position] != 1:
        return False
    return all(
        values[position] == context[scope[position]]
        for position in range(len(scope))
        if position != target_position
    )


def host(registry: tuple[Check, ...], context: Context, nvars: int) -> frozenset[int]:
    return frozenset(
        target
        for target in range(nvars)
        if not any(activated(check, context, target) for check in registry)
    )


def reason_map(
    registry: tuple[Check, ...],
    context: Context,
    nvars: int,
    order: dict[Check, int],
) -> dict[int, Check]:
    result: dict[int, Check] = {}
    for target in range(nvars):
        active = [
            check
            for check in registry
            if activated(check, context, target)
        ]
        if active:
            result[target] = min(active, key=order.__getitem__)
    return result


def changed_reason_support(
    left: dict[int, Check],
    right: dict[int, Check],
) -> set[int]:
    return {
        target
        for target in set(left) | set(right)
        if left.get(target) != right.get(target)
    }


def main() -> None:
    nvars = 4
    checks = generate_checks(nvars)
    order = {check: index for index, check in enumerate(checks)}
    contexts = list(product((0, 1), repeat=nvars))

    totals = {
        "canonical_checks": len(checks),
        "contexts": len(contexts),
        "unique_activation_records": 0,
        "deterministic_reconstructions": 0,
        "registry_atom_toggles": 0,
        "registry_reason_toggles": 0,
        "context_bit_transitions": 0,
        "context_host_witnesses": 0,
        "monotone_registry_inclusions": 0,
        "combined_input_transitions": 0,
        "combined_host_witnesses": 0,
        "decoration_formula_checks": 0,
    }

    for check in checks:
        for context in contexts:
            targets = [
                target
                for target in range(nvars)
                if activated(check, context, target)
            ]
            assert len(targets) <= 1
            totals["unique_activation_records"] += 1

    registries_by_size: dict[int, list[tuple[Check, ...]]] = {
        size: [
            tuple(checks[index] for index in indices)
            for indices in combinations(range(len(checks)), size)
        ]
        for size in range(4)
    }

    # Determinism, one-atom registry sensitivity and induced monotonicity.
    for size in range(3):
        for registry in registries_by_size[size]:
            registry_set = set(registry)
            for context in contexts:
                if any(violates(check, context) for check in registry):
                    continue

                left_host = host(registry, context, nvars)
                left_reason = reason_map(registry, context, nvars, order)
                assert left_host == host(registry, context, nvars)
                assert left_reason == reason_map(registry, context, nvars, order)
                totals["deterministic_reconstructions"] += 1

                for check in checks:
                    if check in registry_set or violates(check, context):
                        continue
                    right_registry = registry + (check,)
                    right_host = host(right_registry, context, nvars)
                    right_reason = reason_map(
                        right_registry,
                        context,
                        nvars,
                        order,
                    )

                    assert right_host <= left_host
                    assert len(left_host ^ right_host) <= 1
                    assert len(changed_reason_support(left_reason, right_reason)) <= 1
                    totals["registry_atom_toggles"] += 1
                    totals["registry_reason_toggles"] += 1
                    totals["monotone_registry_inclusions"] += 1

    # Fixed-registry context sensitivity and exact incident-check witnesses.
    for size in range(4):
        for registry in registries_by_size[size]:
            for context in contexts:
                if any(violates(check, context) for check in registry):
                    continue

                left_host = host(registry, context, nvars)
                left_reason = reason_map(registry, context, nvars, order)
                for changed_bit in range(nvars):
                    context2_list = list(context)
                    context2_list[changed_bit] ^= 1
                    context2 = tuple(context2_list)
                    if any(violates(check, context2) for check in registry):
                        continue

                    incident = [
                        check
                        for check in registry
                        if changed_bit in check[0]
                    ]
                    right_host = host(registry, context2, nvars)
                    right_reason = reason_map(
                        registry,
                        context2,
                        nvars,
                        order,
                    )

                    assert len(left_host ^ right_host) <= 2 * len(incident)
                    assert len(
                        changed_reason_support(left_reason, right_reason)
                    ) <= 2 * len(incident)

                    for target in left_host ^ right_host:
                        assert any(
                            activated(check, context, target)
                            != activated(check, context2, target)
                            for check in incident
                        )
                        totals["context_host_witnesses"] += 1
                    totals["context_bit_transitions"] += 1

    # One registry addition combined with one context-bit change.
    for size in range(2):
        for registry in registries_by_size[size]:
            registry_set = set(registry)
            for context in contexts:
                if any(violates(check, context) for check in registry):
                    continue

                for changed_check in checks:
                    if changed_check in registry_set:
                        continue
                    registry2 = registry + (changed_check,)

                    for changed_bit in range(nvars):
                        context2_list = list(context)
                        context2_list[changed_bit] ^= 1
                        context2 = tuple(context2_list)
                        if any(violates(check, context2) for check in registry2):
                            continue

                        left_host = host(registry, context, nvars)
                        right_host = host(registry2, context2, nvars)
                        common_incident = [
                            check
                            for check in registry
                            if changed_bit in check[0]
                        ]

                        assert len(left_host ^ right_host) <= (
                            1 + 2 * len(common_incident)
                        )

                        for target in left_host ^ right_host:
                            registry_cause = activated(
                                changed_check,
                                context2,
                                target,
                            )
                            context_cause = any(
                                activated(check, context, target)
                                != activated(check, context2, target)
                                for check in common_incident
                            )
                            assert registry_cause or context_cause
                            totals["combined_host_witnesses"] += 1
                        totals["combined_input_transitions"] += 1

    for cells in range(1, 101):
        for atoms in range(1, 101):
            for context_literals in range(1, 21):
                bound = 2 * cells * atoms * (context_literals + 1)
                assert bound >= 2 * cells * atoms
                assert bound >= 2 * cells * atoms * context_literals
                totals["decoration_formula_checks"] += 1

    print("AC3lz--AC3me verification passed")
    for key, value in totals.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
