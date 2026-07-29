#!/usr/bin/env python3

from __future__ import annotations

import itertools
import math
import random


def degree_data(matrix: list[list[int]]) -> tuple[int, int]:
    left = [sum(row) for row in matrix]
    right = [
        sum(matrix[row][column] for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    ]
    return min(left), max(right)


def main() -> None:
    rng = random.Random(1515)
    systems = 0
    tensor_incidences = 0
    conditioned_checks = 0

    for _ in range(6000):
        factors: list[tuple[list[list[int]], int, int]] = []
        for _ in range(rng.randint(1, 3)):
            left_size = rng.randint(1, 3)
            right_size = rng.randint(1, 3)
            matrix = [
                [rng.randint(0, 1) for _ in range(right_size)]
                for _ in range(left_size)
            ]
            for row in range(left_size):
                if not any(matrix[row]):
                    matrix[row][rng.randrange(right_size)] = 1
            minimum, maximum = degree_data(matrix)
            factors.append((matrix, minimum, maximum))

        expected_minimum = math.prod(item[1] for item in factors)
        expected_maximum = math.prod(item[2] for item in factors)

        left_tuples = list(
            itertools.product(*[range(len(item[0])) for item in factors])
        )
        right_tuples = list(
            itertools.product(*[range(len(item[0][0])) for item in factors])
        )

        left_degrees = [
            sum(
                all(
                    factors[index][0][left[index]][right[index]]
                    for index in range(len(factors))
                )
                for right in right_tuples
            )
            for left in left_tuples
        ]
        right_degrees = [
            sum(
                all(
                    factors[index][0][left[index]][right[index]]
                    for index in range(len(factors))
                )
                for left in left_tuples
            )
            for right in right_tuples
        ]

        assert min(left_degrees) == expected_minimum
        assert max(right_degrees) == expected_maximum

        reference = 1.0
        lower_product = 1.0
        upper_product = 1.0
        for _, minimum, maximum in factors:
            local_reference = max(1.0, (minimum + maximum) / 2.0)
            eta = max(0.0, 1.0 - minimum / local_reference)
            zeta = max(0.0, maximum / local_reference - 1.0)
            reference *= local_reference
            lower_product *= 1.0 - eta
            upper_product *= 1.0 + zeta

        assert expected_minimum + 1e-9 >= reference * lower_product
        assert expected_maximum <= reference * upper_product + 1e-9

        loss = rng.random() * 0.25 * reference * lower_product
        true_imbalance = max(
            0.0, 1.0 - (expected_minimum - loss) / expected_maximum
        )
        bound = max(
            0.0,
            1.0 - (reference * lower_product - loss) / (reference * upper_product),
        )
        assert true_imbalance <= bound + 1e-9

        systems += 1
        tensor_incidences += len(left_tuples) * len(right_tuples)
        conditioned_checks += 1

    print(f"systems={systems}")
    print(f"tensor_incidences={tensor_incidences}")
    print(f"conditioned_checks={conditioned_checks}")


if __name__ == "__main__":
    main()
