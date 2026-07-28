#!/usr/bin/env python3
"""Finite audit for SAS5hd--SAS5hh."""

import random

SEED = 20260728


def conflict_graph(candidates):
    adjacency = [set() for _ in candidates]
    for i in range(len(candidates)):
        square_i, atoms_i, _weight_i = candidates[i]
        for j in range(i + 1, len(candidates)):
            square_j, atoms_j, _weight_j = candidates[j]
            if square_i == square_j or atoms_i & atoms_j:
                adjacency[i].add(j)
                adjacency[j].add(i)
    return adjacency


def maximum_independent_weight(candidates, adjacency):
    n = len(candidates)
    best = 0
    for mask in range(1 << n):
        valid = True
        for i in range(n):
            if not (mask >> i & 1):
                continue
            if any(mask >> j & 1 for j in adjacency[i]):
                valid = False
                break
        if valid:
            best = max(
                best,
                sum(
                    candidates[i][2]
                    for i in range(n)
                    if mask >> i & 1
                ),
            )
    return best


def main():
    rng = random.Random(SEED)
    counters = {
        "candidate_systems": 0,
        "candidates": 0,
        "failure_systems": 0,
        "missing_slots": 0,
    }

    for _ in range(8_000):
        square_count = rng.randint(1, 4)
        menu_size = rng.randint(1, 3)
        atom_count = rng.randint(2, 8)
        atom_cap = rng.randint(1, min(3, atom_count))
        atoms = list(range(atom_count))
        square_weights = [rng.randint(1, 7) for _ in range(square_count)]

        candidates = []
        for square in range(square_count):
            for _orientation in range(menu_size):
                support = frozenset(
                    rng.sample(atoms, rng.randint(1, atom_cap))
                )
                candidates.append((square, support, square_weights[square]))

        incidence = {
            atom: sum(atom in support for _square, support, _weight in candidates)
            for atom in atoms
        }
        Lambda = max(incidence.values())
        adjacency = conflict_graph(candidates)
        maximum_degree = max((len(row) for row in adjacency), default=0)
        degree_bound = (menu_size - 1) + atom_cap * (Lambda - 1)
        assert maximum_degree <= degree_bound

        optimum = maximum_independent_weight(candidates, adjacency)
        total_square_weight = sum(square_weights)
        guaranteed = (
            menu_size * total_square_weight
            / (menu_size + atom_cap * (Lambda - 1))
        )
        assert optimum + 1e-12 >= guaranteed

        counters["candidate_systems"] += 1
        counters["candidates"] += len(candidates)

        # Missing-orientation failure-reason concentration.
        reason_count = rng.randint(1, 6)
        reason_weight = [0] * reason_count
        missing_incidence = 0
        for square in range(square_count):
            legal = rng.randint(0, menu_size)
            missing = menu_size - legal
            for _ in range(missing):
                reason = rng.randrange(reason_count)
                reason_weight[reason] += square_weights[square]
                missing_incidence += square_weights[square]
                counters["missing_slots"] += 1
        if missing_incidence:
            assert max(reason_weight) * reason_count >= missing_incidence
            counters["failure_systems"] += 1

    print("SAS orientation-legality batching audit passed")
    for key in sorted(counters):
        print(f"  {key.replace('_', ' ')}: {counters[key]}")


if __name__ == "__main__":
    main()
