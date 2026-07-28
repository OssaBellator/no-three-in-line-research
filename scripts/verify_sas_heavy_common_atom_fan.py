#!/usr/bin/env python3
"""Finite audit for SAS5hs--SAS5hw.

The script checks small weighted common-atom candidate systems. The Markdown
note contains the arbitrary-size proof.
"""

from fractions import Fraction
import random


def main():
    rng = random.Random(808)
    systems = heavy = light = 0

    for _ in range(12000):
        square_count = rng.randint(1, 6)
        square_weight = [rng.randint(1, 5) for _ in range(square_count)]

        candidates = []
        candidates_by_square = []
        for square in range(square_count):
            menu_size = rng.randint(1, 3)
            indices = []
            for _ in range(menu_size):
                residual = {
                    atom
                    for atom in range(1, 7)
                    if rng.random() < 0.28
                }
                if len(residual) > 3:
                    residual = set(sorted(residual)[:3])
                indices.append(len(candidates))
                candidates.append((square, residual))
            candidates_by_square.append(indices)

        residual_load = {
            atom: sum(
                square_weight[square]
                for square, residual in candidates
                if atom in residual
            )
            for atom in range(1, 7)
        }
        maximum_load = max(residual_load.values(), default=0)
        threshold = rng.randint(0, max(1, maximum_load + 2))

        if maximum_load > threshold:
            assert any(load > threshold for load in residual_load.values())
            heavy += 1
        else:
            vertex_count = len(candidates)
            conflicts = [[False] * vertex_count for _ in range(vertex_count)]
            for left in range(vertex_count):
                square_left, residual_left = candidates[left]
                for right in range(left + 1, vertex_count):
                    square_right, residual_right = candidates[right]
                    if (
                        square_left == square_right
                        or residual_left & residual_right
                    ):
                        conflicts[left][right] = True
                        conflicts[right][left] = True

            optimum = 0
            for mask in range(1 << vertex_count):
                independent = True
                for left in range(vertex_count):
                    if not ((mask >> left) & 1):
                        continue
                    for right in range(left + 1, vertex_count):
                        if (
                            (mask >> right) & 1
                            and conflicts[left][right]
                        ):
                            independent = False
                            break
                    if not independent:
                        break

                if independent:
                    weight = sum(
                        square_weight[candidates[index][0]]
                        for index in range(vertex_count)
                        if (mask >> index) & 1
                    )
                    optimum = max(optimum, weight)

            bound = Fraction(0)
            residual_support_bound = 3
            for square, indices in enumerate(candidates_by_square):
                menu_size = len(indices)
                weight = square_weight[square]
                bound += Fraction(
                    menu_size * weight * weight,
                    menu_size * weight
                    + residual_support_bound * threshold,
                )

            assert Fraction(optimum, 1) >= bound
            light += 1

        systems += 1

    print(f"{systems:,} common-atom candidate systems")
    print(f"{heavy:,} second-heavy-atom alternatives")
    print(f"{light:,} light-residual compatible fan cases")


if __name__ == "__main__":
    main()
