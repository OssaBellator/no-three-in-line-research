#!/usr/bin/env python3
"""Finite checks for CMR1582--CMR1589."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from random import Random
from math import gcd


Permutation = tuple[int, ...]
Edge = tuple[int, int]


def assignment_value(side: int, allowed: set[Edge], score: dict[Edge, Fraction]) -> Fraction:
    best: Fraction | None = None
    for perm in permutations(range(side)):
        if all((x, perm[x]) in allowed for x in range(side)):
            value = sum((score[(x, perm[x])] for x in range(side)), Fraction())
            if best is None or value > best:
                best = value
    assert best is not None
    return best


def verify_random_laws(seed: int = 1589) -> tuple[int, int, int, int]:
    rng = Random(seed)
    laws = 0
    edge_conditionals = 0
    assignments = 0
    certificates = 0

    for side in range(2, 7):
        all_perms = list(permutations(range(side)))
        old = tuple(range(side))
        for _ in range(240):
            bank_size = rng.randint(1, min(len(all_perms), 45))
            bank = rng.sample(all_perms, bank_size)
            weights = [rng.randint(1, 11) for _ in bank]
            total_weight = sum(weights)
            selector_cap = rng.randint(0, 9)

            ret_load: dict[tuple[Permutation, Edge], int] = {}
            sel_load: dict[tuple[Permutation, Edge], int] = {}
            for perm in bank:
                for x, y in enumerate(perm):
                    edge = (x, y)
                    if y == old[x]:
                        ret_load[(perm, edge)] = 0
                        sel_load[(perm, edge)] = 0
                    else:
                        ret_load[(perm, edge)] = rng.randint(0, 5)
                        sel_load[(perm, edge)] = rng.randint(0, 4)

            alpha = Fraction(
                sum(
                    weight
                    * sum(ret_load[(perm, (x, y))] for x, y in enumerate(perm))
                    for perm, weight in zip(bank, weights)
                ),
                total_weight,
            )
            beta = Fraction(
                sum(
                    weight
                    * sum(sel_load[(perm, (x, y))] for x, y in enumerate(perm))
                    for perm, weight in zip(bank, weights)
                ),
                total_weight,
            )

            allowed = {(x, perm[x]) for perm in bank for x in range(side)}
            probability: dict[Edge, Fraction] = {}
            g_ret: dict[Edge, Fraction] = {}
            g_sel: dict[Edge, Fraction] = {}

            for x in range(side):
                for y in range(side):
                    edge = (x, y)
                    denominator = sum(
                        weight
                        for perm, weight in zip(bank, weights)
                        if perm[x] == y
                    )
                    probability[edge] = Fraction(denominator, total_weight)
                    if denominator:
                        g_ret[edge] = Fraction(
                            sum(
                                weight * ret_load[(perm, edge)]
                                for perm, weight in zip(bank, weights)
                                if perm[x] == y
                            ),
                            denominator,
                        )
                        g_sel[edge] = Fraction(
                            sum(
                                weight * sel_load[(perm, edge)]
                                for perm, weight in zip(bank, weights)
                                if perm[x] == y
                            ),
                            denominator,
                        )
                        edge_conditionals += 1
                    else:
                        g_ret[edge] = Fraction()
                        g_sel[edge] = Fraction()

            for x in range(side):
                assert sum((probability[(x, y)] for y in range(side)), Fraction()) == 1
            for y in range(side):
                assert sum((probability[(x, y)] for x in range(side)), Fraction()) == 1

            exact_ret = sum(
                (probability[e] * g_ret[e] for e in probability), Fraction()
            )
            exact_sel = sum(
                (probability[e] * g_sel[e] for e in probability), Fraction()
            )
            assert exact_ret == alpha
            assert exact_sel == beta

            combined = {
                edge: g_ret[edge] + selector_cap * g_sel[edge] for edge in allowed
            }
            scalar = alpha + selector_cap * beta
            exact_scalar = sum(
                (
                    probability[e]
                    * (g_ret[e] + selector_cap * g_sel[e])
                    for e in probability
                ),
                Fraction(),
            )
            assert scalar == exact_scalar

            primal = assignment_value(side, allowed, combined)
            assert scalar <= primal
            assignments += 1

            row_dual = sum(
                max(combined.get((x, y), Fraction()) for y in range(side))
                for x in range(side)
            )
            column_dual = sum(
                max(combined.get((x, y), Fraction()) for x in range(side))
                for y in range(side)
            )
            assert primal <= row_dual
            assert primal <= column_dual

            u = [Fraction(rng.randint(0, 20), 7) for _ in range(side)]
            v = [Fraction(rng.randint(0, 20), 7) for _ in range(side)]
            dominated = {
                edge: min(combined[edge], u[edge[0]] + v[edge[1]])
                for edge in allowed
            }
            dominated_primal = assignment_value(side, allowed, dominated)
            dual_value = sum(u, Fraction()) + sum(v, Fraction())
            assert dominated_primal <= dual_value

            denominator = 1
            for value in [*dominated.values(), *u, *v]:
                denominator = denominator * value.denominator // gcd(
                    denominator, value.denominator
                )
            integer_score = {
                edge: dominated[edge] * denominator for edge in allowed
            }
            assert all(value.denominator == 1 for value in integer_score.values())
            assert all(
                int(u[x] * denominator) + int(v[y] * denominator)
                >= int(integer_score[(x, y)])
                for x, y in allowed
            )
            certificates += 1

            class_count = rng.randint(1, 6)
            edge_class = {edge: rng.randrange(class_count) for edge in allowed}
            ret_cap = [Fraction(rng.randint(0, 9), 3) for _ in range(class_count)]
            sel_cap = [Fraction(rng.randint(0, 9), 3) for _ in range(class_count)]
            coarse_score = {
                edge: max(g_ret[edge], ret_cap[edge_class[edge]])
                + selector_cap * max(g_sel[edge], sel_cap[edge_class[edge]])
                for edge in allowed
            }
            assert all(coarse_score[e] >= combined[e] for e in allowed)
            assert primal <= assignment_value(side, allowed, coarse_score)

            laws += 1

    return laws, edge_conditionals, assignments, certificates


def verify_shared_improvement() -> int:
    side = 2
    allowed = {(0, 0), (0, 1), (1, 0), (1, 1)}
    g_ret = {
        (0, 0): Fraction(1),
        (1, 1): Fraction(1),
        (0, 1): Fraction(),
        (1, 0): Fraction(),
    }
    g_sel = {
        (0, 0): Fraction(),
        (1, 1): Fraction(),
        (0, 1): Fraction(1),
        (1, 0): Fraction(1),
    }
    separate = assignment_value(side, allowed, g_ret) + assignment_value(
        side, allowed, g_sel
    )
    combined = {edge: g_ret[edge] + g_sel[edge] for edge in allowed}
    shared = assignment_value(side, allowed, combined)
    assert separate == 4
    assert shared == 2
    assert shared < separate
    return 1


def verify_two_row_certificates() -> int:
    checked = 0
    for denominator in range(1, 80):
        for a in range(denominator + 1):
            for b in range(denominator + 1):
                for cap in range(10):
                    alpha = Fraction(a, denominator)
                    beta = Fraction(b, denominator)
                    strict = alpha + beta * cap < 1
                    integer = a + b * cap < denominator
                    assert strict == integer
                    checked += 1
    return checked


def main() -> None:
    laws, conditionals, assignments, certificates = verify_random_laws()
    shared = verify_shared_improvement()
    two_row = verify_two_row_certificates()
    print(
        "verified return-selector assignment scalarization: "
        f"{laws} rational response laws, {conditionals} conditional owner loads, "
        f"{assignments} exact assignment bounds, {certificates} rational/integer dual checks, "
        f"{shared} strict shared-versus-separate witness, and {two_row} two-row certificates"
    )


if __name__ == "__main__":
    main()
