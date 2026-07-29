#!/usr/bin/env python3
"""Finite audit for AC5au--AC5ay."""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product


def sequential_distribution(rows, pstar):
    """Exact law of the canonical sequential uniform injection."""
    out = defaultdict(Fraction)

    def rec(i, used, word, probability):
        if i == len(rows):
            out[tuple(word)] += probability
            return
        choices = [u for u in range(pstar) if u in rows[i] and u not in used]
        assert choices
        weight = probability / len(choices)
        for u in choices:
            rec(i + 1, used | {u}, word + [u], weight)

    rec(0, set(), [], Fraction(1))
    assert sum(out.values(), Fraction()) == 1
    return out


def audit_spread():
    graphs = 0
    cylinders = 0
    for pstar in range(2, 6):
        for t in range(1, min(3, pstar - 1) + 1):
            for delta in range(0, pstar - t):
                sigma = pstar - delta - t
                if sigma <= 0:
                    continue
                masks = []
                for bits in range(1 << pstar):
                    row = {u for u in range(pstar) if bits >> u & 1}
                    if len(row) >= pstar - delta:
                        masks.append(row)
                row_products = product(masks, repeat=t)
                limit = 5000 if pstar == 5 else None
                for index, rows in enumerate(row_products):
                    if limit is not None and index >= limit:
                        break
                    law = sequential_distribution(rows, pstar)
                    events = defaultdict(Fraction)
                    for word, probability in law.items():
                        for r in range(1, min(3, t) + 1):
                            for chosen_rows in combinations(range(t), r):
                                key = tuple((i, word[i]) for i in chosen_rows)
                                events[key] += probability
                    for event, probability in events.items():
                        r = len(event)
                        assert probability <= Fraction(1, sigma**r)
                        cylinders += 1
                    graphs += 1
    return graphs, cylinders


def audit_inventory_formula():
    cases = 0
    for n, pstar, kappa, ell, t, theta, m, new_count in product(
        range(2, 7), range(2, 8), range(1, 5), range(2, 7), range(1, 5),
        range(0, 7), range(0, 5), range(0, 6)
    ):
        pair_shadow = theta + 3 * m * new_count
        anchored = 8 * n * pair_shadow
        rank_two = 4 * ell * t * pstar
        rank_three = 8 * ell * t * t * pstar * pstar
        direct = (
            Fraction(anchored * kappa * kappa, pstar * pstar)
            + Fraction(rank_two * kappa * kappa, pstar * pstar)
            + Fraction(rank_three * kappa**3, pstar**3)
        )
        displayed = (
            Fraction(8 * kappa * kappa * n * pair_shadow, pstar * pstar)
            + Fraction(4 * kappa * kappa * ell * t, pstar)
            + Fraction(8 * kappa**3 * ell * t * t, pstar)
        )
        assert direct == displayed
        cases += 1
    return cases


def audit_overload_alternative():
    cases = 0
    for components in product(range(6), repeat=5):
        for t in range(1, 6):
            weighted = list(components) + [t]
            total = sum(weighted)
            for pstar in range(1, 12):
                if total >= pstar:
                    assert 6 * max(weighted) >= pstar
                    cases += 1
    return cases


def main():
    graphs, cylinders = audit_spread()
    inventory_cases = audit_inventory_formula()
    overload_cases = audit_overload_alternative()
    print("AC restricted-menu closed-form audit passed")
    print(f"  admissibility graphs: {graphs}")
    print(f"  cylinder inequalities: {cylinders}")
    print(f"  inventory substitutions: {inventory_cases}")
    print(f"  overload alternatives: {overload_cases}")


if __name__ == "__main__":
    main()
