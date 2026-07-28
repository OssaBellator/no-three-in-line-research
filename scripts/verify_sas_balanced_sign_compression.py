#!/usr/bin/env python3
import random


def maximum_matching_size(adjacency, right_count):
    states = {0: 0}
    for neighbours in adjacency:
        updated = dict(states)
        for mask, value in states.items():
            for right in neighbours:
                if not ((mask >> right) & 1):
                    new_mask = mask | (1 << right)
                    updated[new_mask] = max(updated.get(new_mask, 0), value + 1)
        states = updated
    return max(states.values(), default=0)


def main() -> None:
    rng = random.Random(1107)
    systems = 9_000
    coordinates = 0
    positive_units = 0
    negative_units = 0
    legal_pairs = 0
    fully_compressed = 0
    imbalance_obstructions = 0
    hall_obstructions = 0

    for _ in range(systems):
        dimension = rng.randint(1, 5)
        for _ in range(dimension):
            positive = rng.randint(0, 7)
            negative = rng.randint(0, 7)
            adjacency = []
            for _ in range(positive):
                adjacency.append({j for j in range(negative) if rng.random() < 0.55})

            matching = maximum_matching_size(adjacency, negative)
            deficiency = min(positive, negative) - matching
            residual = positive + negative - 2 * matching
            assert residual == abs(positive - negative) + 2 * deficiency

            coordinates += 1
            positive_units += positive
            negative_units += negative
            legal_pairs += matching
            if residual == 0:
                fully_compressed += 1
            elif positive != negative:
                imbalance_obstructions += 1
            else:
                hall_obstructions += 1
                assert deficiency > 0

    print(f"systems={systems}")
    print(f"coordinates={coordinates}")
    print(f"positive_units={positive_units}")
    print(f"negative_units={negative_units}")
    print(f"legal_pairs={legal_pairs}")
    print(f"fully_compressed_coordinates={fully_compressed}")
    print(f"imbalance_obstructions={imbalance_obstructions}")
    print(f"hall_obstructions={hall_obstructions}")


if __name__ == "__main__":
    main()
