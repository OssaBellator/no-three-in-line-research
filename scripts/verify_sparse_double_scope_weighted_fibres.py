#!/usr/bin/env python3
"""Finite checks for SAS5at--SAS5ax weighted double-scope fibres."""

from fractions import Fraction
from itertools import combinations
from random import Random


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
        selected = sorted(loads, reverse=True)[:m]
        selected_total = sum(selected, Fraction(0))
        if k:
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
            # Every chosen defect sees the same d-2 safe donors, so the first m give an injection.
            assignment = {z: safe[z] for z in range(m)}
            assert len(assignment) == m
            assert len(set(assignment.values())) == m
            checks += 1
    return checks


def whole_fibre_repair_checks():
    rng = Random(77)
    checks = 0
    # Columns x,y,z,q.  Records in one fibre may use different row triples but the same columns.
    for _ in range(25000):
        label_x = rng.randint(0, 2)
        label_y = rng.randint(0, 2)
        ell = rng.randint(0, 2)
        wrong = (ell + rng.randint(1, 2)) % 3
        labels = {"x": label_x, "y": label_y, "z": wrong, "q": ell}
        required = {"x": label_x, "y": label_y, "z": ell}
        multiplicity = rng.randint(1, 8)
        assert all(not all(labels[c] == required[c] for c in ("x", "y", "z")) for _ in range(multiplicity))
        labels["z"], labels["q"] = labels["q"], labels["z"]
        assert all(all(labels[c] == required[c] for c in ("x", "y", "z")) for _ in range(multiplicity))
        checks += 1
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
        # Build a graph while respecting the target degree bound.
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
    repair = whole_fibre_repair_checks()
    compat = compatibility_checks()
    print("double-scope weighted fibres: PASS")
    print(f"  top-fibre weight systems checked: {top}")
    print(f"  donor matching systems checked: {matching}")
    print(f"  whole-fibre repair systems checked: {repair}")
    print(f"  weighted compatibility systems checked: {compat}")


if __name__ == "__main__":
    main()
