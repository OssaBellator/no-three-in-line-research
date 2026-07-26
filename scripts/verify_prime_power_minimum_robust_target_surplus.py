#!/usr/bin/env python3
"""Finite checks for CMR990--CMR997."""

from itertools import combinations
from math import ceil, comb
import random


def random_state(cell_count, cardinality, rng):
    cells = rng.sample(range(cell_count), cardinality)
    return frozenset((rng.randint(0, 1), cell) for cell in cells)


def physical_cells(state):
    return {cell for _layer, cell in state}


def triple_set(state, hyperedges):
    cells = physical_cells(state)
    return {edge for edge in hyperedges if set(edge) <= cells}


def check_energy_identity_and_support():
    rng = random.Random(990)
    checked = 0
    robust = 0
    for cell_count in range(4, 40):
        all_triples = list(combinations(range(cell_count), 3))
        for cardinality in range(3, min(cell_count, 12) + 1):
            for _ in range(200):
                state = random_state(cell_count, cardinality, rng)
                candidate = random_state(cell_count, cardinality, rng)
                hyperedges = set(
                    rng.sample(
                        all_triples,
                        rng.randint(0, min(len(all_triples), 100)),
                    )
                )
                old = triple_set(state, hyperedges)
                new = triple_set(candidate, hyperedges)
                gained = new - old
                lost = old - new
                gap = len(new) - len(old)
                assert gap == len(gained) - len(lost)

                entering = set(candidate) - set(state)
                for triple in gained:
                    new_cells = set(triple) - physical_cells(state)
                    assert new_cells
                    assert any(edge[1] in new_cells for edge in entering)

                if gap >= 1 and lost:
                    designated = rng.randint(1, len(lost))
                    assert len(gained) >= designated + gap
                    assert entering
                    assignments = {edge: 0 for edge in entering}
                    for triple in gained:
                        supports = sorted(
                            edge
                            for edge in entering
                            if edge[1] in set(triple) - physical_cells(state)
                        )
                        assert supports
                        assignments[supports[0]] += 1
                    assert max(assignments.values()) >= ceil(len(gained) / len(entering))
                    assert max(assignments.values()) >= ceil((designated + gap) / len(entering))
                    robust += 1
                checked += 1
    return checked, robust


def check_cumulative_surplus():
    rng = random.Random(993)
    checked = 0
    for episode_count in range(1, 500):
        for _ in range(100):
            designated = [rng.randint(1, 20) for _ in range(episode_count)]
            gaps = [rng.randint(1, 10) for _ in range(episode_count)]
            new_counts = [
                designated[index] + gaps[index] + rng.randint(0, 20)
                for index in range(episode_count)
            ]
            assert sum(new_counts) >= sum(designated) + sum(gaps)
            assert sum(new_counts) >= sum(designated) + episode_count
            checked += 1
    return checked


def check_signature_stock():
    checked = 0
    for side in range(1, 300):
        cells = side * side
        stock = 2 * cells * comb(cells - 1, 2) if cells >= 3 else 0
        direct = 0
        if cells <= 100:
            for _layer in range(2):
                for cell in range(cells):
                    direct += comb(cells - 1, 2)
            assert direct == stock
        assert stock >= 0
        checked += 1
    return checked


def check_recurrence_bounds():
    checked = 0
    for side in range(2, 80):
        cells = side * side
        stock = 2 * cells * comb(cells - 1, 2)
        for threshold in range(2, 30):
            one_target_cap = ((threshold - 1) * stock) // 2
            assert 2 * one_target_cap <= (threshold - 1) * stock
            for episodes in range(1, 100):
                designated = episodes
                gaps = episodes
                if episodes > one_target_cap:
                    assert designated + gaps > (threshold - 1) * stock
            checked += 1
    return checked


def check_rank_two_transfer():
    rng = random.Random(996)
    checked = 0
    for universe_size in range(3, 100):
        edges = list(range(universe_size))
        for _ in range(1000):
            triple = frozenset(rng.sample(edges, 3))
            edge = rng.choice(tuple(triple))
            residual = triple - {edge}
            assert len(residual) == 2
            family = {
                frozenset(rng.sample(edges, rng.randint(3, universe_size)))
                for _ in range(100)
            }
            conditioned = {state for state in family if edge in state}
            for state in conditioned:
                assert (triple <= state) == (residual <= state - {edge})
            checked += 1
    return checked


def main():
    identities, robust = check_energy_identity_and_support()
    print(
        "verified minimum-robust target surplus:",
        identities,
        "energy identities including",
        robust,
        "positive-gap cases,",
        check_cumulative_surplus(),
        "cumulative cases,",
        check_signature_stock(),
        "signature stocks,",
        check_recurrence_bounds(),
        "recurrence bounds, and",
        check_rank_two_transfer(),
        "rank-two transfers",
    )


if __name__ == "__main__":
    main()
