#!/usr/bin/env python3

"""Finite audit for BDA5ca--BDA5ce."""

from __future__ import annotations

import math
import random


def main() -> None:
    rng = random.Random(280726)
    cycles = 0
    charged_mass = 0
    epochs = 0

    for _ in range(4000):
        length_bound = rng.randint(2, 9)
        jump_threshold = rng.randint(2, 12)
        source_capacity: dict[tuple[int, int, int], int] = {}
        selected: list[tuple[int, int, tuple[int, int, int], int]] = []

        for _ in range(rng.randint(1, 25)):
            word_length = rng.randint(2, length_bound)
            while True:
                increments = [
                    rng.randint(-20, 20) for _ in range(word_length - 1)
                ]
                increments.append(-sum(increments))
                negative = [
                    index for index, value in enumerate(increments) if value < 0
                ]
                positive = [
                    index for index, value in enumerate(increments) if value > 0
                ]
                if negative and positive:
                    break

            restoration_index = min(negative, key=lambda index: increments[index])
            jump = -increments[restoration_index]
            if jump < jump_threshold:
                continue

            source_index = max(positive, key=lambda index: increments[index])
            source_increment = increments[source_index]
            assert source_increment >= math.ceil(jump / (word_length - 1))

            edge = (word_length, source_index, source_increment % 5)
            source_capacity[edge] = source_capacity.get(edge, 0) + source_increment
            selected.append((jump, word_length, edge, source_increment))
            cycles += 1
            charged_mass += source_increment

        total_capacity = sum(source_capacity.values())
        if selected:
            assert len(selected) <= (
                (length_bound - 1) * total_capacity // jump_threshold
            )

            bins: dict[int, int] = {}
            for jump, _, _, _ in selected:
                scale = jump.bit_length() - 1
                bins[scale] = bins.get(scale, 0) + 1
            for scale, count in bins.items():
                minimum_charge = math.ceil((2**scale) / (length_bound - 1))
                assert count <= total_capacity // minimum_charge

        epochs += 1

    print(f"epochs={epochs}")
    print(f"cycles={cycles}")
    print(f"charged_mass={charged_mass}")


if __name__ == "__main__":
    main()
