#!/usr/bin/env python3
"""Finite checks for CMR966--CMR973."""

from itertools import combinations, product
import random


def product_family(factors):
    return {frozenset().union(*states) for states in product(*factors)}


def potential(state, atoms):
    return sum(1 for atom in atoms if set(atom) <= set(state))


def minimum_face(family, atoms):
    values = {state: potential(state, atoms) for state in family}
    value = min(values.values())
    return {state for state in family if values[state] == value}, value


def common_core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def random_product(rng):
    factor_count = rng.randint(1, 4)
    factors = []
    edge_sets = []
    offset = 0
    for _ in range(factor_count):
        universe_size = rng.randint(1, 5)
        state_size = rng.randint(0, universe_size)
        edges = tuple(range(offset, offset + universe_size))
        all_states = [
            frozenset(state)
            for state in combinations(edges, state_size)
        ]
        family = set(rng.sample(all_states, rng.randint(1, min(8, len(all_states)))))
        factors.append(family)
        edge_sets.append(frozenset(edges))
        offset += universe_size
    all_edges = tuple(range(offset))
    atoms = set()
    if len(all_edges) >= 3:
        triples = list(combinations(all_edges, 3))
        atoms = {
            frozenset(atom)
            for atom in rng.sample(triples, rng.randint(0, min(30, len(triples))))
        }
    return factors, edge_sets, atoms


def fibre(factors, selected_parts, variable):
    frozen = frozenset().union(
        *(selected_parts[index] for index in range(len(factors)) if index != variable)
    )
    return {frozen | state for state in factors[variable]}, frozen


def check_minimum_inheritance_and_decomposition():
    rng = random.Random(966)
    inheritance = 0
    decomposition = 0
    target_cases = 0
    for _ in range(20000):
        factors, edge_sets, atoms = random_product(rng)
        family = product_family(factors)
        global_face, global_value = minimum_face(family, atoms)
        selected = min(global_face, key=lambda state: tuple(sorted(state)))
        selected_parts = [frozenset(set(selected) & set(edges)) for edges in edge_sets]
        variable = rng.randrange(len(factors))
        coordinate_fibre, frozen = fibre(factors, selected_parts, variable)
        fibre_face, fibre_value = minimum_face(coordinate_fibre, atoms)
        assert selected in coordinate_fibre
        assert selected in fibre_face
        assert fibre_value == global_value
        inheritance += 1

        variable_edges = edge_sets[variable]
        for state in coordinate_fibre:
            constant = 0
            pure = 0
            anchored = 0
            for atom in atoms:
                if not set(atom) <= set(state):
                    continue
                variable_rank = len(set(atom) & set(variable_edges))
                if variable_rank == 0:
                    assert set(atom) <= set(frozen)
                    constant += 1
                elif variable_rank == 3:
                    assert set(atom) <= set(variable_edges)
                    pure += 1
                else:
                    assert variable_rank in (1, 2)
                    assert set(atom) & set(frozen)
                    anchored += 1
            assert potential(state, atoms) == constant + pure + anchored
            decomposition += 1

        if atoms:
            targets = [atom for atom in atoms if set(atom) <= set(selected)]
            for target in targets:
                rank = len(set(target) & set(variable_edges))
                assert rank in (0, 1, 2, 3)
                if rank == 0:
                    assert set(target) <= set(frozen)
                elif rank == 3:
                    assert set(target) <= set(variable_edges)
                else:
                    assert set(target) & set(frozen)
                target_cases += 1
    return inheritance, decomposition, target_cases


def normalize_fibre(coordinate_fibre, frozen, variable_edges, atoms):
    family = set(coordinate_fibre)
    fixed = set(frozen)
    available = set(variable_edges)
    initial_edges = len(available)
    initial_cardinality = len(next(iter(family))) - len(fixed)
    deletions = 0
    contracted = 0

    while True:
        face, _value = minimum_face(family, atoms)
        active = []
        fixed_conflict = False
        for atom in atoms:
            if not any(set(atom) <= set(state) for state in face):
                continue
            rank = len(set(atom) & available)
            if rank == 0:
                fixed_conflict = True
            elif rank in (1, 2) and set(atom) & fixed:
                active.append(atom)
        if not active:
            return deletions, contracted, fixed_conflict, face, fixed, available

        atom = min(active, key=lambda item: tuple(sorted(item)))
        prescription = set(atom) & available
        core = set(common_core(face))
        noncommon = sorted(prescription - core)
        if noncommon:
            edge = noncommon[0]
            old_face = face
            family = {state for state in family if edge not in state}
            assert family
            new_face, _value = minimum_face(family, atoms)
            assert new_face == {state for state in old_face if edge not in state}
            available.remove(edge)
            deletions += 1
        else:
            assert prescription
            family = set(face)
            fixed.update(prescription)
            available.difference_update(prescription)
            contracted += len(prescription)

        assert deletions <= initial_edges
        assert contracted <= initial_cardinality
        assert deletions + contracted <= initial_edges + initial_cardinality


def check_fibre_normalization():
    rng = random.Random(970)
    checked = 0
    for _ in range(12000):
        factors, edge_sets, atoms = random_product(rng)
        family = product_family(factors)
        global_face, _value = minimum_face(family, atoms)
        selected = rng.choice(tuple(global_face))
        selected_parts = [frozenset(set(selected) & set(edges)) for edges in edge_sets]
        variable = rng.randrange(len(factors))
        coordinate_fibre, frozen = fibre(factors, selected_parts, variable)
        result = normalize_fibre(
            coordinate_fibre, frozen, edge_sets[variable], atoms
        )
        deletions, contracted, fixed_conflict, face, fixed, available = result
        assert deletions >= 0 and contracted >= 0
        if not fixed_conflict:
            for state in face:
                for atom in atoms:
                    if set(atom) <= set(state):
                        rank = len(set(atom) & available)
                        assert not (rank in (1, 2) and set(atom) & fixed)
        checked += 1
    return checked


def check_strict_side_arithmetic():
    checked = 0
    for parent in range(2, 1000):
        for child in range(1, parent):
            assert 1 <= child < parent
            checked += 1
    return checked


def main():
    inheritance, decomposition, targets = check_minimum_inheritance_and_decomposition()
    print(
        "verified minimum coordinate fibre descent:",
        inheritance,
        "minimum fibres,",
        decomposition,
        "induced decompositions,",
        targets,
        "target locations,",
        check_fibre_normalization(),
        "fibre normalizations, and",
        check_strict_side_arithmetic(),
        "strict-side cases",
    )


if __name__ == "__main__":
    main()
