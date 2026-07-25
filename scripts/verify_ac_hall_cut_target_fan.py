#!/usr/bin/env python3
"""Finite checks for AC3ji--AC3jm."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import ceil, floor
from random import Random


def verify_hall_centres(counts: Counter[str]) -> None:
    # Exhaust every defect subset meeting the AC3iz lower bound through side 7.
    for n in range(3, 8):
        for m in range(1, n + 1):
            s = n - m + 1
            cut = [(row, column) for row in range(m) for column in range(s)]
            lower = m * s - min(m, s) - 1
            for mask in range(1 << len(cut)):
                if mask.bit_count() < lower:
                    continue
                defects = [cut[i] for i in range(len(cut)) if mask >> i & 1]
                row_degree = [0] * m
                column_degree = [0] * s
                for row, column in defects:
                    row_degree[row] += 1
                    column_degree[column] += 1
                maximum = max(row_degree + column_degree)
                assert maximum >= floor(n / 2)
                if min(m, s) == 1:
                    assert maximum >= n - 2
                else:
                    assert maximum >= max(m, s) - 1
                counts["Hall-cut defect subsets"] += 1


def verify_role_and_owner_pigeonholes(counts: Counter[str]) -> None:
    rng = Random(1)
    for n in range(3, 30):
        target_count = floor(n / 2)
        for role_count in range(1, 9):
            for owner_capacity in range(1, 6):
                for threshold in range(1, 8):
                    for _ in range(100):
                        roles = [rng.randrange(role_count) for _ in range(target_count)]
                        selected_role = max(range(role_count), key=roles.count)
                        selected_targets = [i for i, role in enumerate(roles) if role == selected_role]
                        u = len(selected_targets)
                        assert u >= ceil(target_count / role_count)

                        owners = []
                        owner_loads: list[int] = []
                        for _target in selected_targets:
                            available = [i for i, load in enumerate(owner_loads) if load < owner_capacity]
                            if available and rng.random() < 0.65:
                                owner = rng.choice(available)
                                owner_loads[owner] += 1
                            else:
                                owner = len(owner_loads)
                                owner_loads.append(1)
                            owners.append(owner)

                        assert len(set(owners)) >= ceil(u / owner_capacity)
                        if max(owner_loads) <= threshold:
                            assert len(owner_loads) >= ceil(u / threshold)
                        else:
                            assert max(owner_loads) > threshold
                        counts["role-owner target systems"] += 1


def verify_cross_centre_residuals(counts: Counter[str]) -> None:
    variables = range(4)
    residual_options = [frozenset()]
    residual_options.extend(
        frozenset(choice)
        for size in (1, 2)
        for choice in combinations(variables, size)
    )

    for target_count in range(1, 6):
        for family in product(residual_options, repeat=target_count):
            empty_count = sum(not residual for residual in family)
            nonempty = [residual for residual in family if residual]

            matching = []
            used = set()
            for residual in nonempty:
                if residual.isdisjoint(used):
                    matching.append(residual)
                    used.update(residual)
            assert all(not residual.isdisjoint(used) for residual in nonempty)

            degrees = {
                variable: sum(variable in residual for residual in nonempty)
                for variable in variables
            }
            for threshold in range(1, 5):
                if 2 * empty_count >= target_count:
                    assert empty_count >= ceil(target_count / 2)
                elif max(degrees.values(), default=0) > threshold:
                    assert any(degree > threshold for degree in degrees.values())
                else:
                    assert len(matching) >= ceil(target_count / (4 * threshold))
                counts["cross-centre residual systems"] += 1


def verify_formula_grid(counts: Counter[str]) -> None:
    for n in range(3, 100):
        for m in range(1, n + 1):
            s = n - m + 1
            a = min(m, s)
            b = max(m, s)
            lower = m * s - a - 1
            centre = ceil(lower / a)
            if a == 1:
                assert centre == n - 2
            else:
                assert centre >= b - 1
            assert centre >= floor(n / 2)
            counts["centre formulae"] += 1


def main() -> None:
    counts: Counter[str] = Counter()
    verify_hall_centres(counts)
    verify_role_and_owner_pigeonholes(counts)
    verify_cross_centre_residuals(counts)
    verify_formula_grid(counts)

    print("AC3ji--AC3jm Hall-cut target-fan verification passed")
    for name in sorted(counts):
        print(f"  {name}: {counts[name]:,}")


if __name__ == "__main__":
    main()
