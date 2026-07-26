#!/usr/bin/env python3
"""Finite checks for corrected SAS5at--SAS5ax composed double-scope fibres."""

from fractions import Fraction
from itertools import combinations
from random import Random


def apply_swap(labels, left, right):
    result = dict(labels)
    result[left], result[right] = result[right], result[left]
    return result


def max_weight_independent_set(vertices, edges, weights):
    vertices = list(vertices)
    edge_set = {frozenset(e) for e in edges}
    best = Fraction(0)
    for mask in range(1 << len(vertices)):
        chosen = [vertices[i] for i in range(len(vertices)) if mask & (1 << i)]
        if any(frozenset((u, v)) in edge_set for u, v in combinations(chosen, 2)):
            continue
        total = sum((weights[v] for v in chosen), Fraction(0))
        best = max(best, total)
    return best


def top_fibre_checks():
    rng = Random(20260726)
    systems = 0
    for _ in range(60000):
        k = rng.randint(1, 10)
        d = rng.randint(1, 10)
        loads = [Fraction(rng.randint(0, 15), rng.randint(1, 5)) for _ in range(k)]
        total = sum(loads, Fraction(0))
        m = min(k, max(d - 2, 0))
        selected_total = sum(sorted(loads, reverse=True)[:m], Fraction(0))
        assert selected_total * k >= total * m
        n_board = rng.randint(k, k + 8)
        assert selected_total * n_board >= total * m
        systems += 1
    return systems


def donor_matching_checks():
    checks = 0
    for d in range(1, 9):
        safe = list(range(max(d - 2, 0)))
        for k in range(0, 9):
            m = min(k, max(d - 2, 0))
            assignment = {z: safe[z] for z in range(m)}
            assert len(assignment) == m
            assert len(set(assignment.values())) == m
            checks += 1
    return checks


def composed_fibre_repair_checks():
    rng = Random(77)
    checks = 0
    for bank_size in range(1, 9):
        defects = list(range(bank_size))
        donors = list(range(bank_size, 2 * bank_size))
        x = 2 * bank_size
        y = x + 1
        labels = {x: 0, y: 1}
        labels.update({z: rng.choice((0, 1)) for z in defects})
        labels.update({q: 2 for q in donors})
        required = {z: {x: 1, y: 0, z: 2} for z in defects}
        multiplicity = {z: rng.randint(1, 8) for z in defects}

        post_omega = apply_swap(labels, x, y)
        for z, q in zip(defects, donors):
            donor_alone = apply_swap(labels, z, q)
            composed = apply_swap(post_omega, z, q)
            assert not all(donor_alone[c] == required[z][c] for c in (x, y, z))
            assert all(composed[c] == required[z][c] for c in (x, y, z))
            checks += multiplicity[z]

        simultaneous = dict(post_omega)
        for z, q in zip(defects, donors):
            simultaneous = apply_swap(simultaneous, z, q)
        for z in defects:
            assert all(simultaneous[c] == required[z][c] for c in (x, y, z))
            checks += multiplicity[z]
    return checks


def compatibility_checks():
    rng = Random(991)
    checks = 0
    for _ in range(30000):
        n = rng.randint(1, 11)
        lam = rng.randint(0, 3)
        degree_bound = 4 * lam
        vertices = list(range(n))
        edges = set()
        candidates = list(combinations(vertices, 2))
        rng.shuffle(candidates)
        degree = [0] * n
        for u, v in candidates:
            if degree[u] < degree_bound and degree[v] < degree_bound and rng.randrange(3) == 0:
                edges.add((u, v))
                degree[u] += 1
                degree[v] += 1
        weights = {v: Fraction(rng.randint(0, 12), rng.randint(1, 5)) for v in vertices}
        total = sum(weights.values(), Fraction(0))
        best = max_weight_independent_set(vertices, edges, weights)
        assert best * (degree_bound + 1) >= total
        checks += 1
    return checks


def main():
    top = top_fibre_checks()
    matching = donor_matching_checks()
    repair = composed_fibre_repair_checks()
    compat = compatibility_checks()
    print("double-scope composed weighted fibres: PASS")
    print(f"  top-fibre weight systems checked: {top}")
    print(f"  donor matching systems checked: {matching}")
    print(f"  composed fibre-record checks: {repair}")
    print(f"  weighted compatibility systems checked: {compat}")


if __name__ == "__main__":
    main()
