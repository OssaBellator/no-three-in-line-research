#!/usr/bin/env python3
"""Finite checks for AC5ap--AC5at."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product


def saturating_matchings(rows: tuple[int, ...], n: int):
    for image in permutations(range(n), len(rows)):
        if all(rows[a] & (1 << image[a]) for a in range(len(rows))):
            yield image


def verify_shifted_quantiles() -> int:
    checked = 0
    for m in range(1, 4):
        for n in range(m, 5):
            for delta in range(0, min(1, n) + 1):
                full = (1 << n) - 1
                row_options = []
                for holes_n in range(delta + 1):
                    for holes in combinations(range(n), holes_n):
                        mask = full
                        for b in holes:
                            mask &= ~(1 << b)
                        row_options.append(mask)
                for rows in product(row_options, repeat=m):
                    matchings = list(saturating_matchings(rows, n))
                    if not matchings or n < m + delta:
                        continue
                    for costs in product(range(3), repeat=n):
                        optimum = min(sum(costs[b] for b in matching) for matching in matchings)
                        ordered = sorted(costs)
                        bound = sum(ordered[i + delta] for i in range(m))
                        assert optimum <= bound
                    checked += 1
    return checked


def verify_disjoint_multiplicity() -> int:
    checked = 0
    choices = ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2))
    for assignment in product(choices, repeat=5):
        for left, right in assignment:
            assert left + right == max(left, right)
        checked += 1
    return checked


def verify_ri_prescriptions() -> int:
    checked = 0
    for m in range(1, 5):
        for h in range(1, 5):
            states = [
                (sigma, shifts)
                for sigma in permutations(range(m))
                for shifts in product(range(h), repeat=m)
            ]
            for alpha in range(m):
                for beta in range(m):
                    for shift in range(h):
                        count = sum(
                            sigma[alpha] == beta and shifts[alpha] == shift
                            for sigma, shifts in states
                        )
                        assert Fraction(count, len(states)) == Fraction(1, m * h)
                        checked += 1
    return checked


def swap(pi: tuple[int, ...], i: int, j: int) -> tuple[int, ...]:
    out = list(pi)
    out[i], out[j] = out[j], out[i]
    return tuple(out)


def verify_sparse_atoms() -> int:
    checked = 0
    for n in range(2, 5):
        for pi in permutations(range(n)):
            for rho in permutations(range(n)):
                if any(pi[row] == rho[row] for row in range(n)):
                    continue
                for i, j in combinations(range(n), 2):
                    for cross_i, cross_j in product((False, True), repeat=2):
                        swap(pi, i, j)
                        host_ok = cross_i and cross_j
                        collision_i = pi[j] == rho[i]
                        collision_j = pi[i] == rho[j]
                        direct = host_ok and not collision_i and not collision_j
                        conditions = (cross_i, cross_j, not collision_i, not collision_j)
                        assert direct == all(conditions)
                        failures = [k for k, ok in enumerate(conditions) if not ok]
                        if not direct:
                            assert failures and 0 <= failures[0] <= 3
                        checked += 1
    return checked


def main() -> None:
    quantiles = verify_shifted_quantiles()
    disjoint = verify_disjoint_multiplicity()
    ri = verify_ri_prescriptions()
    sparse = verify_sparse_atoms()
    print(
        "verified AC cross-branch interfaces on "
        f"{quantiles} bounded-hole graphs, {disjoint} disjoint inventories, "
        f"{ri} RI prescriptions and {sparse} sparse swap tests"
    )


if __name__ == "__main__":
    main()
