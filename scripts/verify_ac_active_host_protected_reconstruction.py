#!/usr/bin/env python3
"""Exact finite audit for AC3ml--AC3mq."""

from collections import Counter
from itertools import combinations, product


def subsets(items):
    items = tuple(items)
    for rank in range(len(items) + 1):
        for combo in combinations(items, rank):
            yield frozenset(combo)


def active(atom, context):
    _, dependencies, pattern = atom
    return tuple(context[index] for index in dependencies) == pattern


def active_host(base_support, registry, context):
    blocked = {atom[0] for atom in registry if active(atom, context)}
    return frozenset(set(base_support) - blocked)


def target_cells(atoms):
    return {atom[0] for atom in atoms}


def run_active_host_audit(counts):
    cells = tuple(range(3))
    variables = tuple(range(2))
    atoms = []
    for target in cells:
        for rank in (1, 2):
            for dependencies in combinations(variables, rank):
                for pattern in product((0, 1), repeat=rank):
                    atoms.append((target, dependencies, pattern))

    bases = list(subsets(cells))
    contexts = list(product((0, 1), repeat=len(variables)))
    registries = (
        [frozenset()]
        + [frozenset([atom]) for atom in atoms]
        + [frozenset(pair) for pair in combinations(atoms, 2)]
    )

    # Determinism, one-atom Lipschitz, and registry monotonicity.
    for base in bases:
        for context in contexts:
            for registry in registries:
                first = active_host(base, registry, context)
                second = active_host(base, registry, context)
                assert first == second
                counts["active deterministic states"] += 1

                for atom in atoms:
                    changed = registry ^ frozenset([atom])
                    other = active_host(base, changed, context)
                    assert len(first ^ other) <= 1
                    if atom not in registry:
                        assert other <= first
                    else:
                        assert first <= other
                    counts["active registry toggles"] += 1

    # Context changes affect only targets of incident common atoms.
    for base in bases:
        for registry in registries:
            for context in contexts:
                for other_context in contexts:
                    changed_variables = {
                        index
                        for index in variables
                        if context[index] != other_context[index]
                    }
                    incident_targets = {
                        atom[0]
                        for atom in registry
                        if set(atom[1]) & changed_variables
                    }
                    difference = (
                        active_host(base, registry, context)
                        ^ active_host(base, registry, other_context)
                    )
                    assert difference <= incident_targets
                    counts["active context pairs"] += 1

    # Base-support monotonicity.
    for registry in registries[:50]:
        for context in contexts:
            for base in bases:
                for larger_base in bases:
                    if base <= larger_base:
                        assert (
                            active_host(base, registry, context)
                            <= active_host(larger_base, registry, context)
                        )
                        counts["active base inclusions"] += 1

    # Combined exact cause inclusion for one registry toggle.
    small_registries = [frozenset()] + [
        frozenset([atom]) for atom in atoms
    ]
    for base in bases:
        for other_base in bases:
            for registry in small_registries:
                for atom in atoms:
                    other_registry = registry ^ frozenset([atom])
                    registry_difference = registry ^ other_registry
                    for context in contexts:
                        for other_context in contexts:
                            changed_variables = {
                                index
                                for index in variables
                                if context[index] != other_context[index]
                            }
                            common_incident = {
                                common_atom
                                for common_atom in registry & other_registry
                                if set(common_atom[1]) & changed_variables
                            }
                            cause_cells = (
                                (base ^ other_base)
                                | target_cells(registry_difference)
                                | target_cells(common_incident)
                            )
                            host_difference = (
                                active_host(base, registry, context)
                                ^ active_host(
                                    other_base,
                                    other_registry,
                                    other_context,
                                )
                            )
                            assert host_difference <= cause_cells
                            counts["combined active changes"] += 1


def protected_registry(state, mode, atoms):
    return frozenset(
        atom_id
        for atom_id, scope, required_mode in atoms
        if required_mode == mode and scope <= state
    )


def run_protected_audit(counts):
    cells = tuple(range(4))
    scopes = [
        frozenset(combo)
        for rank in (1, 2, 3)
        for combo in combinations(cells, rank)
    ]
    atoms = [
        (atom_id, scope, required_mode)
        for atom_id, scope in enumerate(scopes)
        for required_mode in (0, 1)
    ]
    states = list(subsets(cells))

    for state in states:
        for other_state in states:
            changed_cells = state ^ other_state
            for mode in (0, 1):
                first = protected_registry(state, mode, atoms)
                second = protected_registry(other_state, mode, atoms)
                changed_atoms = first ^ second
                incident_atoms = {
                    atom_id
                    for atom_id, scope, required_mode in atoms
                    if required_mode == mode and scope & changed_cells
                }
                assert changed_atoms <= incident_atoms
                maximum_incidence = max(
                    sum(
                        1
                        for _, scope, required_mode in atoms
                        if required_mode == mode and cell in scope
                    )
                    for cell in cells
                )
                assert len(changed_atoms) <= (
                    maximum_incidence * len(changed_cells)
                )
                counts["protected state pairs"] += 1

    # Context changes have no unexplained atom changes.
    atom_ids = {atom_id for atom_id, _, _ in atoms}
    for state in states:
        difference = (
            protected_registry(state, 0, atoms)
            ^ protected_registry(state, 1, atoms)
        )
        assert difference <= atom_ids
        counts["protected context changes"] += 1


def main():
    counts = Counter()
    run_active_host_audit(counts)
    run_protected_audit(counts)

    print("AC3ml--AC3mq finite audit passed")
    for label in sorted(counts):
        print(f"{label}: {counts[label]:,}")


if __name__ == "__main__":
    main()
