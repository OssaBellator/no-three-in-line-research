#!/usr/bin/env python3
"""Finite audit for SRR2ac--SRR2ag.

The script samples small threshold graphs and conditioned edge deletions. The
Markdown note contains the arbitrary-size proof.
"""

from fractions import Fraction
from math import floor
import random


def deficiency(edges, left_size, right_size):
    answer = 0
    for mask in range(1 << left_size):
        X = [left for left in range(left_size) if (mask >> left) & 1]
        neighbourhood = {
            right
            for left in X
            for right in range(right_size)
            if (left, right) in edges
        }
        answer = max(answer, len(X) - len(neighbourhood))
    return max(0, answer)


def main():
    rng = random.Random(2718)
    graphs = conditioned_graphs = 0

    for left_size in range(1, 7):
        for right_size in range(1, 8):
            for _ in range(400):
                density = rng.uniform(0.2, 0.9)
                edges = {
                    (left, right)
                    for left in range(left_size)
                    for right in range(right_size)
                    if rng.random() < density
                }
                if not edges:
                    continue

                left_degree = min(
                    sum((left, right) in edges for right in range(right_size))
                    for left in range(left_size)
                )
                right_load = max(
                    sum((left, right) in edges for left in range(left_size))
                    for right in range(right_size)
                )
                if right_load == 0:
                    continue

                reference = max(1, round((left_degree + right_load) / 2))
                eta = Fraction(max(0, reference - left_degree), reference)
                zeta = Fraction(max(0, right_load - reference), reference)

                epsilon = max(
                    Fraction(0),
                    Fraction(right_load - left_degree, right_load),
                )
                reference_bound = min(
                    Fraction(1),
                    (eta + zeta) / (1 + zeta),
                )
                assert epsilon <= reference_bound
                assert deficiency(edges, left_size, right_size) <= floor(
                    left_size * epsilon
                )

                kept = {edge for edge in edges if rng.random() > 0.2}
                deleted_per_left = max(
                    sum(
                        (left, right) in edges and (left, right) not in kept
                        for right in range(right_size)
                    )
                    for left in range(left_size)
                )
                conditioned_left = min(
                    sum((left, right) in kept for right in range(right_size))
                    for left in range(left_size)
                )
                conditioned_right = max(
                    [
                        sum((left, right) in kept for left in range(left_size))
                        for right in range(right_size)
                    ]
                    or [0]
                )

                if conditioned_right > 0:
                    beta = Fraction(deleted_per_left, reference)
                    conditioned_epsilon = max(
                        Fraction(0),
                        Fraction(
                            conditioned_right - conditioned_left,
                            conditioned_right,
                        ),
                    )
                    conditioned_bound = min(
                        Fraction(1),
                        (eta + beta + zeta) / (1 + zeta),
                    )
                    assert conditioned_epsilon <= conditioned_bound
                    assert deficiency(
                        kept, left_size, right_size
                    ) <= floor(left_size * conditioned_epsilon)
                    conditioned_graphs += 1

                graphs += 1

    print(f"{graphs:,} near-biregular threshold graphs")
    print(f"{conditioned_graphs:,} conditioned threshold graphs")


if __name__ == "__main__":
    main()
