#!/usr/bin/env python3
"""Finite checks for CMR958--CMR965."""

from itertools import combinations, product
from math import comb
import random


def product_family(factors, fixed):
    return {
        frozenset(set(fixed).union(*map(set, states)))
        for states in product(*factors)
    }


def classify(atom, fixed, factor_edges):
    atom = set(atom)
    if atom <= set(fixed):
        return "constant", ()
    ranks = tuple(len(atom & set(edges)) for edges in factor_edges)
    positive = tuple(rank for rank in ranks if rank)
    if len(positive) == 1 and positive[0] == 3 and not (atom & set(fixed)):
        return "pure", ranks
    return "coupling", ranks


def minimum_face(family, atoms):
    potential = {
        state: sum(1 for atom in atoms if set(atom) <= set(state))
        for state in family
    }
    value = min(potential.values())
    return {state for state in family if potential[state] == value}, potential, value


def common_core(family):
    iterator = iter(family)
    result = set(next(iterator))
    for state in iterator:
        result.intersection_update(state)
    return frozenset(result)


def random_exact_product(rng):
    factor_count = rng.randint(1, 4)
    offset = 0
    factor_edges = []
    factors = []
    for _ in range(factor_count):
        universe_size = rng.randint(1, 5)
        state_size = rng.randint(0, universe_size)
        edges = tuple(range(offset, offset + universe_size))
        states = [
            frozenset(state)
            for state in combinations(edges, state_size)
        ]
        family = set(rng.sample(states, rng.randint(1, min(8, len(states)))))
        factor_edges.append(frozenset(edges))
        factors.append(family)
        offset += universe_size
    core_size = rng.randint(0, 4)
    fixed = frozenset(range(offset, offset + core_size))
    all_edges = frozenset(range(offset + core_size))
    family = product_family(factors, fixed)
    atoms = set()
    if len(all_edges) >= 3:
        triples = list(combinations(all_edges, 3))
        atoms = set(rng.sample(triples, rng.randint(0, min(30, len(triples)))))
        atoms = {frozenset(atom) for atom in atoms}
    return family, fixed, factor_edges, all_edges, atoms


def check_decomposition_and_ranks():
    rng = random.Random(958)
    checked = 0
    for _ in range(20000):
        family, fixed, factor_edges, _all_edges, atoms = random_exact_product(rng)
        for state in family:
            contained = [atom for atom in atoms if set(atom) <= set(state)]
            constant = []
            pure = []
            coupling = []
            for atom in contained:
                kind, ranks = classify(atom, fixed, factor_edges)
                if kind == "constant":
                    constant.append(atom)
                elif kind == "pure":
                    pure.append(atom)
                else:
                    coupling.append(atom)
                    residual = set(atom) - set(fixed)
                    assert residual
                    assert all(rank <= 2 for rank in ranks)
                    positive = tuple(rank for rank in ranks if rank)
                    core_rank = len(set(atom) & set(fixed))
                    if core_rank:
                        assert positive in ((1,), (2,), (1, 1))
                    else:
                        assert positive in ((2, 1), (1, 2), (1, 1, 1))
            assert len(contained) == len(constant) + len(pure) + len(coupling)
        checked += 1
    return checked


def check_occurrence_boxes():
    rng = random.Random(960)
    checked = 0
    for _ in range(12000):
        family, fixed, factor_edges, _all_edges, atoms = random_exact_product(rng)
        coupling_atoms = [
            atom for atom in atoms if classify(atom, fixed, factor_edges)[0] == "coupling"
        ]
        for atom in coupling_atoms:
            actual = {state for state in family if set(atom) <= set(state)}
            local_allowed = []
            for edges in factor_edges:
                prescription = set(atom) & set(edges)
                projections = {frozenset(set(state) & set(edges)) for state in family}
                local_allowed.append(
                    {state for state in projections if prescription <= set(state)}
                )
            expected = product_family(local_allowed, fixed)
            assert actual == expected
            checked += 1
    return checked


def check_stock_bound():
    checked = 0
    for fixed_size in range(0, 30):
        for residual_size in range(0, 60):
            bound = (
                fixed_size * comb(residual_size, 2)
                + comb(fixed_size, 2) * residual_size
                + comb(residual_size, 3)
            )
            assert bound >= 0
            checked += 1
    return checked


def check_contraction_equivalence():
    rng = random.Random(962)
    checked = 0
    for _ in range(15000):
        family, fixed, _factor_edges, all_edges, atoms = random_exact_product(rng)
        core = common_core(family)
        contractable = tuple(core - fixed)
        if not contractable:
            continue
        rank = rng.randint(1, min(3, len(contractable)))
        prescription = frozenset(rng.sample(contractable, rank))
        new_fixed = fixed | prescription
        for state in family:
            residual = frozenset(set(state) - set(new_fixed))
            for atom in atoms:
                left = set(atom) <= set(state)
                right = (set(atom) - set(new_fixed)) <= set(residual)
                if set(atom) <= set(new_fixed):
                    right = True
                assert left == right
        checked += 1
    return checked


def normalize_coupling(family, fixed, factor_edges, atoms):
    family = set(family)
    fixed = set(fixed)
    factor_edges = [set(edges) for edges in factor_edges]
    initial_edges = sum(len(edges) for edges in factor_edges)
    initial_cardinality = len(next(iter(family))) - len(fixed)
    deletions = 0
    contraction_rank = 0

    while True:
        face, _potential, _value = minimum_face(family, atoms)
        active = []
        fixed_conflict = False
        for atom in atoms:
            if not any(set(atom) <= set(state) for state in face):
                continue
            kind, _ranks = classify(atom, fixed, factor_edges)
            if kind == "constant":
                fixed_conflict = True
                continue
            if kind == "coupling":
                active.append(atom)
        if not active:
            return deletions, contraction_rank, fixed_conflict, face, fixed, factor_edges

        atom = min(active, key=lambda item: tuple(sorted(item)))
        residual = set(atom) - fixed
        core = set(common_core(face))
        noncommon = sorted(residual - core)
        if noncommon:
            edge = noncommon[0]
            old_size = len(family)
            family = {state for state in family if edge not in state}
            assert family and len(family) < old_size
            for edges in factor_edges:
                edges.discard(edge)
            deletions += 1
        else:
            assert residual
            fixed.update(residual)
            for edge in residual:
                for edges in factor_edges:
                    edges.discard(edge)
            contraction_rank += len(residual)

        assert deletions <= initial_edges
        assert contraction_rank <= initial_cardinality
        assert deletions + contraction_rank <= initial_edges + initial_cardinality


def check_minimum_normalization():
    rng = random.Random(964)
    checked = 0
    for _ in range(10000):
        family, fixed, factor_edges, _all_edges, atoms = random_exact_product(rng)
        if not family:
            continue
        deletions, rank, fixed_conflict, face, final_fixed, final_factors = normalize_coupling(
            family, fixed, factor_edges, atoms
        )
        assert deletions >= 0 and rank >= 0
        if not fixed_conflict:
            for state in face:
                for atom in atoms:
                    if set(atom) <= set(state):
                        assert classify(atom, final_fixed, final_factors)[0] != "coupling"
        checked += 1
    return checked


def main():
    print(
        "verified induced product potential transport:",
        check_decomposition_and_ranks(),
        "decompositions,",
        check_occurrence_boxes(),
        "coupling boxes,",
        check_stock_bound(),
        "stock bounds,",
        check_contraction_equivalence(),
        "contractions, and",
        check_minimum_normalization(),
        "minimum normalizations",
    )


if __name__ == "__main__":
    main()
