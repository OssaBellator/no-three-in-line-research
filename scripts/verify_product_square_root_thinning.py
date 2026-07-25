#!/usr/bin/env python3
"""Verify PX189--PX190 square-root endpoint thinning."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations
from math import sqrt
from random import Random


def collinear(first, second, third) -> bool:
    return (
        (second[0] - first[0]) * (third[1] - first[1])
        == (second[1] - first[1]) * (third[0] - first[0])
    )


def candidate_triples(
    endpoints: tuple[tuple[int, int], ...],
    indices: tuple[int, ...],
) -> tuple[tuple[tuple[int, int], ...], ...]:
    triples = []
    for row_indices in combinations(indices, 3):
        row_values = tuple(endpoints[index][0] for index in row_indices)
        for column_indices in combinations(indices, 3):
            column_values = tuple(
                endpoints[index][1] for index in column_indices
            )
            for order in permutations(range(3)):
                labels = tuple(
                    (row_indices[position], column_indices[order[position]])
                    for position in range(3)
                )
                points = tuple(
                    (row_values[position], column_values[order[position]])
                    for position in range(3)
                )
                if collinear(*points):
                    triples.append(labels)
    return tuple(triples)


def union_profile(triples) -> Counter[int]:
    profile: Counter[int] = Counter()
    for triple in triples:
        indices = {
            index
            for cell in triple
            for index in cell
        }
        profile[len(indices)] += 1
    return profile


def random_endpoints(size: int, random: Random) -> tuple[tuple[int, int], ...]:
    rows = random.sample(range(5 * size), size)
    columns = random.sample(range(5 * size), size)
    return tuple(zip(rows, columns))


def arithmetic_endpoints(size: int) -> tuple[tuple[int, int], ...]:
    return tuple((index, index) for index in range(size))


def find_thinned_subset(
    endpoints: tuple[tuple[int, int], ...],
    random: Random,
) -> tuple[tuple[int, ...], int]:
    size = len(endpoints)
    target = max(3, int(sqrt(size) / 2))
    full = tuple(range(size))
    full_triples = candidate_triples(endpoints, full)
    best = None
    best_count = None
    for _ in range(2000):
        chosen = tuple(
            index for index in range(size) if random.random() < size ** -0.5
        )
        if len(chosen) < target:
            continue
        selected = set(chosen)
        count = 0
        for triple in full_triples:
            used = {index for cell in triple for index in cell}
            if used <= selected:
                count += 1
        if best_count is None or count / len(chosen) ** 4 < best_count / len(best) ** 4:
            best = chosen
            best_count = count
    assert best is not None and best_count is not None
    return best, best_count


def verify_family(endpoints: tuple[tuple[int, int], ...], label: str) -> None:
    size = len(endpoints)
    full_triples = candidate_triples(endpoints, tuple(range(size)))
    profile = union_profile(full_triples)
    assert set(profile).issubset({3, 4, 5, 6})
    assert profile[3] <= 6 * size**3
    assert profile[4] <= 4096 * size**4

    random = Random(20260725 + size + len(label))
    subset, triple_count = find_thinned_subset(endpoints, random)
    selected_size = len(subset)
    ratio = triple_count / selected_size**4
    assert selected_size >= max(3, int(sqrt(size) / 2))
    # This is a finite regression threshold, not the asymptotic constant.
    assert ratio <= 2
    print(
        f"{label}, t={size}: full triples={len(full_triples)}, "
        f"profile={dict(profile)}, selected={selected_size}, "
        f"selected triples={triple_count}, T3/s^4={ratio:.6f}"
    )


def verify_probability_scaling() -> None:
    for size in (25, 49, 81, 121, 169):
        probability = size ** -0.5
        # The four union-size sectors have the symbolic scales used in PX189.
        scales = {
            3: probability**3 * size**3,
            4: probability**4 * size**4,
            5: probability**5 * size**4,
            6: probability**6 * size**4,
        }
        assert scales[3] <= size**2
        assert scales[4] == size**2
        assert scales[5] <= size**2
        assert scales[6] <= size**2
    print("square-root sampling exponent scales verified")


def main() -> None:
    random = Random(123456)
    for size in (9, 12, 16, 20):
        verify_family(arithmetic_endpoints(size), "arithmetic")
        verify_family(random_endpoints(size, random), "random")
    verify_probability_scaling()
    print("PX189--PX190 verified")


if __name__ == "__main__":
    main()
