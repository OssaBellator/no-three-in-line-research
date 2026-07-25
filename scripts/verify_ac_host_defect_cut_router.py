#!/usr/bin/env python3
"""Exact finite checks for AC3iz--AC3jc."""

from __future__ import annotations

from itertools import combinations, permutations
from math import ceil


def check_sharp_cut_bound():
    systems = 0
    minima = {}
    for n in range(2, 7):
        best = None
        for m in range(1, n + 1):
            for X_tuple in combinations(range(n), m):
                X = set(X_tuple)
                neighbour_size = 0 if m == 1 else m - 1
                for Y_tuple in combinations(range(n), neighbour_size):
                    Y = set(Y_tuple)
                    Z = set(range(n)) - Y
                    assert len(Z) == n - m + 1
                    cut = {(a, b) for a in X for b in Z}
                    for projected_columns in permutations(range(n)):
                        projected_cut = {
                            (a, projected_columns[a])
                            for a in X
                            if projected_columns[a] in Z
                        }
                        pivot_count = 1 if cut - projected_cut else 0
                        host_missing = len(cut) - len(projected_cut) - pivot_count
                        formula = (
                            m * (n - m + 1)
                            - min(m, n - m + 1)
                            - 1
                        )
                        assert host_missing >= formula
                        if n >= 3:
                            assert formula >= n - 2
                        best = host_missing if best is None else min(best, host_missing)
                        systems += 1
        minima[n] = best
        assert best == n - 2
    return systems, minima


def check_weighted_concentration():
    systems = 0
    for n in range(3, 21):
        cells = n * n
        for total in range(1, 121):
            incidences = (n - 2) * total
            q, r = divmod(incidences, cells)
            loads = [q + (i < r) for i in range(cells)]
            assert sum(loads) == incidences
            assert max(loads) >= ceil(incidences / cells)
            systems += 1
    return systems


def check_reason_router():
    systems = 0
    for n in range(3, 16):
        for total in range(1, 80):
            incidence = (n - 2) * total
            for roles in range(1, 9):
                q, r = divmod(incidence, roles)
                role_loads = [q + (i < r) for i in range(roles)]
                assert max(role_loads) >= ceil(incidence / roles)
                for beta_num in range(1, 8):
                    cap_num = beta_num * total
                    selected = max(role_loads)
                    needed = ceil(8 * selected / cap_num)
                    assert needed * cap_num >= 8 * selected
                    systems += 1
    return systems


def check_formula_grid():
    checks = 0
    for n in range(3, 101):
        for m in range(1, n + 1):
            s = n - m + 1
            value = m * s - min(m, s) - 1
            assert value >= n - 2
            checks += 1
    return checks


def main():
    cut_systems, minima = check_sharp_cut_bound()
    weighted = check_weighted_concentration()
    reasons = check_reason_router()
    formula = check_formula_grid()
    print("AC3iz--AC3jc exact checks passed")
    print(f"Hall-cut placement systems: {cut_systems}")
    print(f"sharp minima: {minima}")
    print(f"weighted concentration systems: {weighted}")
    print(f"reason-router systems: {reasons}")
    print(f"formula-grid checks: {formula}")


if __name__ == "__main__":
    main()
