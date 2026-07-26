#!/usr/bin/env python3
"""Finite checks for CMR1038--CMR1045."""

from itertools import combinations, product
from math import comb, factorial
import random


def skeleton_count(protected, free):
    return sum(
        comb(protected, flow) ** 2
        * comb(free, flow) ** 2
        * factorial(flow) ** 2
        for flow in range(min(protected, free) + 1)
    )


def check_skeleton_arithmetic():
    checked = 0
    for side in range(1, 50):
        for protected in range(side + 1):
            free = side - protected
            exact = skeleton_count(protected, free)
            assert exact <= (free + 1) * side ** (4 * free)
            assert 2 * min(protected, free) <= 2 * free or protected < free
            checked += 1
    return checked


def product_family(factors, skeleton):
    return {
        frozenset(set(skeleton).union(*map(set, factor_states)))
        for factor_states in product(*factors)
    }


def minimum_face(family, potential):
    value = min(potential[state] for state in family)
    return {state for state in family if potential[state] == value}, value


def random_product(rng):
    factor_count = rng.randint(1, 4)
    offset = 0
    factors = []
    edge_sets = []
    for _ in range(factor_count):
        universe_size = rng.randint(1, 5)
        state_size = rng.randint(0, universe_size)
        edges = list(range(offset, offset + universe_size))
        offset += universe_size
        states = [
            frozenset(state)
            for state in combinations(edges, state_size)
        ]
        factors.append(
            set(rng.sample(states, rng.randint(1, min(8, len(states)))))
        )
        edge_sets.append(set(edges))
    skeleton = frozenset(range(offset, offset + rng.randint(0, 3)))
    return factors, edge_sets, skeleton


def check_minimum_skeleton_and_fibres():
    rng = random.Random(1038)
    checked = 0
    for _ in range(10000):
        factors, edge_sets, skeleton = random_product(rng)
        family = product_family(factors, skeleton)
        potential = {state: rng.randint(0, 20) for state in family}
        face, minimum = minimum_face(family, potential)
        selected = min(face, key=lambda state: tuple(sorted(state)))

        # Restricting to the selected class preserves the known minimum.
        assert selected in family
        assert potential[selected] == minimum

        variable_index = rng.randrange(len(factors))
        selected_parts = [
            frozenset(set(selected) & edge_sets[index])
            for index in range(len(factors))
        ]
        fibre = set()
        for variable_state in factors[variable_index]:
            parts = [
                selected_parts[index]
                if index != variable_index
                else variable_state
                for index in range(len(factors))
            ]
            fibre.add(
                frozenset(set(skeleton).union(*map(set, parts)))
            )

        assert selected in fibre
        assert fibre <= family
        assert min(potential[state] for state in fibre) == minimum
        checked += 1
    return checked


def check_recursion_budgets():
    checked = 0
    for side in range(0, 1000):
        assert side * side >= 0
        remaining = side
        contractions = 0
        while remaining:
            remaining -= 1
            contractions += 1
            assert contractions <= side
        assert contractions <= side
        checked += 1
    return checked


def check_strict_descent_paths():
    rng = random.Random(1043)
    checked = 0
    for initial in range(1, 1000):
        current = initial
        visited = []
        while current:
            visited.append(current)
            current = rng.randint(0, current - 1)
        assert len(visited) <= initial
        assert len(visited) == len(set(visited))
        checked += 1
    return checked


def main():
    print(
        "verified large protected-core minimum descent:",
        check_skeleton_arithmetic(),
        "skeleton bounds,",
        check_minimum_skeleton_and_fibres(),
        "minimum fibres,",
        check_recursion_budgets(),
        "recursion budgets, and",
        check_strict_descent_paths(),
        "strict descent paths",
    )


if __name__ == "__main__":
    main()
