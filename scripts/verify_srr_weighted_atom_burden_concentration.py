#!/usr/bin/env python3
from fractions import Fraction
import random


def maximum_weight_independent_set(weights, adjacency):
    vertex_count = len(weights)
    best = 0
    for mask in range(1 << vertex_count):
        legal = True
        for i in range(vertex_count):
            if not ((mask >> i) & 1):
                continue
            for j in adjacency[i]:
                if j > i and ((mask >> j) & 1):
                    legal = False
                    break
            if not legal:
                break
        if legal:
            best = max(best, sum(weights[i] for i in range(vertex_count) if (mask >> i) & 1))
    return best


def main() -> None:
    rng = random.Random(1106)
    systems = 3_000
    candidates = 0
    witnessed_edges = 0
    atom_classes = 0
    weighted_conflict_burden = 0
    heavy_atom_witnesses = 0
    brute_force_checks = 0

    for _ in range(systems):
        vertex_count = rng.randint(2, 9)
        atom_count = rng.randint(1, 7)
        weights = [rng.randint(1, 8) for _ in range(vertex_count)]
        supports = [set(rng.sample(range(atom_count), rng.randint(1, min(atom_count, 3)))) for _ in range(vertex_count)]
        adjacency = [set() for _ in range(vertex_count)]
        witnesses = {}

        for i in range(vertex_count):
            for j in range(i + 1, vertex_count):
                common = sorted(supports[i] & supports[j])
                if common and rng.random() < 0.55:
                    atom = rng.choice(common)
                    adjacency[i].add(j)
                    adjacency[j].add(i)
                    witnesses[(i, j)] = atom

        total_weight = sum(weights)
        burden = sum(weights[i] * len(adjacency[i]) for i in range(vertex_count))
        lower_bound = Fraction(total_weight * total_weight, total_weight + burden)
        optimum = maximum_weight_independent_set(weights, adjacency)
        assert optimum >= lower_bound

        atom_burdens = [0 for _ in range(atom_count)]
        for (i, j), atom in witnesses.items():
            atom_burdens[atom] += weights[i] + weights[j]
        assert burden == sum(atom_burdens)
        if burden > 0:
            atom = max(range(atom_count), key=lambda a: atom_burdens[a])
            assert atom_burdens[atom] * atom_count >= burden
            heavy_atom_witnesses += 1

        candidates += vertex_count
        witnessed_edges += len(witnesses)
        atom_classes += atom_count
        weighted_conflict_burden += burden
        brute_force_checks += 1

    print(f"systems={systems}")
    print(f"candidates={candidates}")
    print(f"witnessed_edges={witnessed_edges}")
    print(f"atom_classes={atom_classes}")
    print(f"weighted_conflict_burden={weighted_conflict_burden}")
    print(f"heavy_atom_witnesses={heavy_atom_witnesses}")
    print(f"brute_force_checks={brute_force_checks}")


if __name__ == "__main__":
    main()
