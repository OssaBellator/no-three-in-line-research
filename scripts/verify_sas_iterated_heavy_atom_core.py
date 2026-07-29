#!/usr/bin/env python3

from __future__ import annotations

import random


def maximum_weight_independent_set(
    vertex_count: int,
    conflicts: set[tuple[int, int]],
    weights: list[int],
) -> int:
    best = 0
    for mask in range(1 << vertex_count):
        total = 0
        valid = True
        for first in range(vertex_count):
            if not (mask >> first) & 1:
                continue
            total += weights[first]
            for second in range(first):
                if (mask >> second) & 1 and (first, second) in conflicts:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            best = max(best, total)
    return best


def main() -> None:
    rng = random.Random(1616)
    systems = 0
    heavy_extensions = 0
    depth_r_fans = 0
    maximum_depth = 0

    for _ in range(5000):
        square_count = rng.randint(1, 5)
        support_rank = rng.randint(1, 4)
        atom_count = rng.randint(support_rank, 7)
        square_weights = [rng.randint(1, 8) for _ in range(square_count)]

        candidates: list[tuple[int, frozenset[int], int]] = []
        for square in range(square_count):
            for _ in range(rng.randint(1, 3)):
                support_size = rng.randint(1, support_rank)
                support = frozenset(rng.sample(range(atom_count), support_size))
                candidates.append((square, support, square_weights[square]))
        candidates = candidates[:15]

        threshold = rng.randint(8, 25)
        core: set[int] = set()
        active = list(range(len(candidates)))

        while True:
            loads: dict[int, int] = {}
            for index in active:
                _, support, weight = candidates[index]
                for atom in support - core:
                    loads[atom] = loads.get(atom, 0) + weight

            heavy = [atom for atom, load in loads.items() if load > threshold]
            if heavy:
                atom = min(heavy)
                core.add(atom)
                heavy_extensions += 1
                active = [
                    index for index in active if atom in candidates[index][1]
                ]
                assert active
                assert len(core) <= support_rank
                continue

            conflicts: set[tuple[int, int]] = set()
            for first_position, first_index in enumerate(active):
                first_square, first_support, _ = candidates[first_index]
                for second_position in range(first_position):
                    second_index = active[second_position]
                    second_square, second_support, _ = candidates[second_index]
                    if (
                        first_square == second_square
                        or (first_support - core) & (second_support - core)
                    ):
                        conflicts.add((first_position, second_position))

            weights = [candidates[index][2] for index in active]
            exact = maximum_weight_independent_set(
                len(active), conflicts, weights
            )

            multiplicity: dict[int, int] = {}
            for index in active:
                square = candidates[index][0]
                multiplicity[square] = multiplicity.get(square, 0) + 1

            bound = 0.0
            for index in active:
                square, _, weight = candidates[index]
                denominator = (
                    multiplicity[square] * weight
                    + (support_rank - len(core)) * threshold
                )
                bound += weight * weight / denominator
            assert exact + 1e-9 >= bound

            if len(core) == support_rank:
                expected = sum(square_weights[square] for square in multiplicity)
                assert exact == expected
                depth_r_fans += 1

            maximum_depth = max(maximum_depth, len(core))
            systems += 1
            break

    print(f"systems={systems}")
    print(f"heavy_extensions={heavy_extensions}")
    print(f"depth_r_fans={depth_r_fans}")
    print(f"maximum_depth={maximum_depth}")


if __name__ == "__main__":
    main()
